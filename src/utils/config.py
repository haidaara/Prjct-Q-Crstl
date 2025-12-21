import tomllib
from pathlib import Path
from typing import Dict, Any

class ConfigManager:
    """Central configuration management for reproducible research"""
    
    def __init__(self, config_path: str = "configs/phase2_experiments.toml"):
        self.config_path = Path(config_path)
        self._config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load and merge configuration with includes"""
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
    
        with self.config_path.open("rb") as f:
            cfg = tomllib.load(f)
    
        # FIXED: Implement includes merging
        includes = cfg.get("includes", {})
        base_name = includes.get("base")
        if base_name:
            base_path = self.config_path.parent / base_name
            if base_path.exists():
                with base_path.open("rb") as f:
                    base_cfg = tomllib.load(f)
                # Overlay: current config overrides base
                merged = {**base_cfg, **cfg}
                # Remove includes from final config
                merged.pop("includes", None)
                cfg = merged
            else:
                print(f"⚠️  Base config not found: {base_path}")
    
        return cfg
    
    @property
    def tiling(self) -> Dict[str, Any]:
        return self._config.get("tiling", {})
    
    @property
    def visualization(self) -> Dict[str, Any]:
        return self._config.get("visualization", {})
    
    @property 
    def exports(self) -> Dict[str, Any]:
        return self._config.get("exports", {})

    @property
    def obstacles(self) -> Dict[str, Any]:
        return self._config.get("obstacles", {})
    
    # Add these properties to your existing ConfigManager class:

    @property
    def energy(self) -> Dict[str, Any]:
        """Access energy configuration section"""
        return self._config.get("energy", {})

    @property
    def monte_carlo(self) -> Dict[str, Any]:
            """Access Monte Carlo configuration section"""
            # Fallback to [mc] for backward compatibility
            return self._config.get("monte_carlo", self._config.get("mc", {}))

    @property
    def growth(self) -> Dict[str, Any]:
        """Access growth configuration section"""
        return self._config.get("growth", {})

    @property
    def analysis(self) -> Dict[str, Any]:
        """Access analysis configuration section"""
        return self._config.get("analysis", {})

