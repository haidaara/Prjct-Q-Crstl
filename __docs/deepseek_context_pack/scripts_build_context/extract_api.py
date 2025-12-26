#!/usr/bin/env python3
"""
scripts/build_context/extract_api.py

Auto-generate 02_CODE_INDEX.md (deep repo map) from Python source.

Design goals:
- deterministic output (stable ordering)
- signature-level "deep" map (not full bodies)
- best-effort extraction of dict key usage (reads/writes/validates)
"""

from __future__ import annotations

import ast
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional
from collections import defaultdict

# --------- semantic tags (edit if you add new subsystems) ---------
def semantic_tag_for(rel_path: str) -> str:
    p = rel_path.replace("\\", "/")
    if "/tilings/" in p:
        return "[#TILINGS-CORE]"
    if "/obstacle/" in p:
        return "[#OBSTACLES]"
    if "/energy/" in p:
        return "[#ENERGY-CALC]"
    if "/simulation/" in p:
        if "flip" in p:
            return "[#FLIP-ENGINE]"
        if "mc" in p:
            return "[#MC-HEALING]"
        if "growth" in p:
            return "[#GROWTH]"
        return "[#SIMULATION]"
    if p.startswith("validation/"):
        return "[#VALIDATION]"
    if p.startswith("analysis/") or "/viz/" in p:
        return "[#VIZ]"
    if p.startswith("experiments/"):
        return "[#ENTRYPOINTS]"
    if p.startswith("dev_tools/"):
        return "[#DEV-TOOLS]"
    if "/utils/" in p:
        return "[#UTILS]"
    return "[#MISC]"

def unparse(node: ast.AST) -> str:
    try:
        return ast.unparse(node)
    except Exception:
        return ""

def doc_firstline(node: ast.AST) -> str:
    d = ast.get_docstring(node) or ""
    d = d.strip()
    return d.splitlines()[0].strip() if d else ""

def format_arg(a: ast.arg) -> str:
    if a.annotation is not None:
        return f"{a.arg}: {unparse(a.annotation)}"
    return a.arg

def func_signature(fn: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    args = fn.args
    parts: List[str] = []

    pos = list(getattr(args, "posonlyargs", [])) + list(args.args)
    defaults = [None] * (len(pos) - len(args.defaults)) + list(args.defaults)

    for a, d in zip(pos, defaults):
        s = format_arg(a)
        if d is not None:
            s += "=" + unparse(d)
        parts.append(s)

    if args.vararg:
        parts.append("*" + format_arg(args.vararg))
    elif args.kwonlyargs:
        parts.append("*")

    for a, d in zip(args.kwonlyargs, args.kw_defaults):
        s = format_arg(a)
        if d is not None:
            s += "=" + unparse(d)
        parts.append(s)

    if args.kwarg:
        parts.append("**" + format_arg(args.kwarg))

    ret = f" -> {unparse(fn.returns)}" if fn.returns is not None else ""
    return f"({', '.join(parts)}){ret}"

class KeyUsageVisitor(ast.NodeVisitor):
    def __init__(self):
        self.reads=set()
        self.writes=set()
        self.validates=set()

    def visit_Subscript(self, node: ast.Subscript):
        key=None
        sl=node.slice
        if isinstance(sl, ast.Constant) and isinstance(sl.value, str):
            key=sl.value
        elif isinstance(sl, ast.Index) and isinstance(sl.value, ast.Constant) and isinstance(sl.value.value, str):
            key=sl.value.value

        if key:
            if isinstance(node.ctx, ast.Store):
                self.writes.add(key)
            else:
                self.reads.add(key)

        self.generic_visit(node)

    def visit_Call(self, node: ast.Call):
        if isinstance(node.func, ast.Attribute) and node.func.attr in ("get", "setdefault", "pop"):
            if node.args and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str):
                key=node.args[0].value
                self.reads.add(key)
                if node.func.attr == "setdefault":
                    self.writes.add(key)
        self.generic_visit(node)

    def visit_Assert(self, node: ast.Assert):
        keys = re.findall(r"['\"]([A-Za-z0-9_]+)['\"]", unparse(node.test))
        self.validates.update(keys)
        self.generic_visit(node)

    def visit_Raise(self, node: ast.Raise):
        s = unparse(node.exc) if node.exc else ""
        keys = re.findall(r"['\"]([A-Za-z0-9_]+)['\"]", s)
        self.validates.update(keys)
        self.generic_visit(node)

@dataclass
class FuncInfo:
    signature: str
    doc: str = ""

@dataclass
class ClassInfo:
    name: str
    doc: str = ""
    bases: List[str] = field(default_factory=list)
    methods: List[FuncInfo] = field(default_factory=list)

@dataclass
class ModuleInfo:
    path: str
    tag: str
    purpose: str = ""
    constants: Dict[str, str] = field(default_factory=dict)
    functions: List[FuncInfo] = field(default_factory=list)
    classes: List[ClassInfo] = field(default_factory=list)
    keys: Dict[str, List[str]] = field(default_factory=dict)

def parse_module(path: Path, root: Path) -> ModuleInfo:
    rel = str(path.relative_to(root))
    mi = ModuleInfo(path=rel, tag=semantic_tag_for(rel))
    src = path.read_text(encoding="utf-8", errors="ignore")
    tree = ast.parse(src)

    mi.purpose = doc_firstline(tree)

    # constants (module-level UPPERCASE)
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id.isupper():
                    mi.constants[t.id] = unparse(node.value)
        if isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name) and node.target.id.isupper():
                mi.constants[node.target.id] = unparse(node.value) if node.value else ""

    # functions/classes
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            mi.functions.append(FuncInfo(
                signature=f"{node.name}{func_signature(node)}",
                doc=doc_firstline(node),
            ))
        elif isinstance(node, ast.ClassDef):
            ci = ClassInfo(
                name=node.name,
                doc=doc_firstline(node),
                bases=[unparse(b) for b in node.bases],
            )
            for b in node.body:
                if isinstance(b, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    ci.methods.append(FuncInfo(
                        signature=f"{b.name}{func_signature(b)}",
                        doc=doc_firstline(b),
                    ))
            mi.classes.append(ci)

    # key usage
    v = KeyUsageVisitor()
    v.visit(tree)
    mi.keys = {
        "reads": sorted(v.reads),
        "writes": sorted(v.writes),
        "validates": sorted(v.validates),
    }
    return mi

def render(mi: ModuleInfo) -> str:
    tag = mi.tag
    out = []
    out.append(tag)
    out.append(f"## MODULE: `{mi.path}`")
    out.append(f"PURPOSE: {mi.purpose or '(no module docstring)'}")

    if mi.constants:
        out.append("")
        out.append("### CONSTANTS")
        for k, v in sorted(mi.constants.items()):
            out.append(f"- `{k}` = `{v}`")

    if mi.classes:
        out.append("")
        out.append("### CLASSES")
        for c in sorted(mi.classes, key=lambda x: x.name):
            base = f" (bases: {', '.join(c.bases)})" if c.bases else ""
            out.append(f"- **`{c.name}`**{base}: {c.doc}".rstrip())
            for m in sorted(c.methods, key=lambda x: x.signature):
                out.append(f"  - `{m.signature}`" + (f" — {m.doc}" if m.doc else ""))

    if mi.functions:
        out.append("")
        out.append("### FUNCTIONS")
        for f in sorted(mi.functions, key=lambda x: x.signature):
            out.append(f"- `{f.signature}`" + (f" — {f.doc}" if f.doc else ""))

    out.append("")
    out.append("### DATA_KEYS_USED (best-effort static extraction)")
    out.append(f"- reads: {mi.keys.get('reads', [])}")
    out.append(f"- writes: {mi.keys.get('writes', [])}")
    out.append(f"- validates: {mi.keys.get('validates', [])}")
    out.append(tag.replace("[#", "[/#"))
    return "\n".join(out)

def main():
    repo = Path(__file__).resolve().parents[2]  # adjust if you move this script
    targets = ["src", "experiments", "analysis", "validation", "dev_tools"]

    py_files: List[Path] = []
    for t in targets:
        d = repo / t
        if d.exists():
            py_files += sorted(d.rglob("*.py"))

    modules = []
    for p in py_files:
        if "__pycache__" in str(p):
            continue
        modules.append(parse_module(p, repo))

    grouped = defaultdict(list)
    for m in modules:
        grouped[m.tag].append(m)
    for tag in grouped:
        grouped[tag] = sorted(grouped[tag], key=lambda x: x.path)

    lines = []
    lines.append("# 02_CODE_INDEX.md — Deep API & Repo Map")
    lines.append("")
    lines.append("Generated by scripts/build_context/extract_api.py")
    lines.append("")
    lines.append("## Tag index (semantic anchors)")
    for tag in sorted(grouped.keys()):
        lines.append(f"- {tag}: {len(grouped[tag])} modules")
    lines.append("")
    lines.append("---")
    lines.append("")

    for tag in sorted(grouped.keys()):
        lines.append(f"# {tag}")
        lines.append("")
        for mi in grouped[tag]:
            lines.append(render(mi))
            lines.append("")

    out_path = repo / "02_CODE_INDEX.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[ok] wrote {out_path}")

if __name__ == "__main__":
    main()
