# **A Synoptic Analysis of Aperiodic Order: From Classical Tiling Dynamics to Quantum Geometry**

## **Executive Summary**

This report synthesizes the physics of aperiodic systems, using the Penrose tiling as a canonical example, to construct a comprehensive "learning path" from classical simulation to quantum dynamics. It traces the central concept of the "phason," demonstrating its evolution from a local geometric defect in classical tilings (Part I), to an emergent, entropically-driven diffusive mode in statistical mechanics (Part II), and ultimately to a manipulable quantum degree of freedom that can drive quantum phase transitions and is intrinsically linked to the geometry of quantum information (Part III). The analysis unifies these three distinct physical descriptions, revealing them as multi-scale facets of a single, profound underlying structure.

---

## **Part I: Classical Foundations and Computational Modeling**

### **Section 1.1: The Algorithmic Generation of Aperiodic Order**

The computational generation of aperiodic tilings, such as the Penrose tiling, is dominated by two philosophically distinct but mathematically related approaches. The choice between them depends on whether the goal is to simulate local growth or to analyze global algebraic properties.

#### **1.1.1: The Deflation/Substitution Method: A Local, Recursive Approach**

The deflation method, also known as substitution, is a local, recursive algorithm that builds the tiling based on its inherent self-similarity.1 The process begins with a single tile or small configuration (the "axiom") and proceeds in generations.1 In each step, every tile is replaced by a set of smaller, scaled-down tiles according to a fixed substitution rule.1

References:
- Penrose tiling - Wikipedia, accessed on November 7, 2025, [https://en.wikipedia.org/wiki/Penrose_tiling]  
- Penrose tiling - Rosetta Code, accessed on November 7, 2025, [https://rosettacode.org/wiki/Penrose_tiling]

For the two most common Penrose variants, P2 (kites and darts) and P3 (rhombs), the substitution rules are often defined on their constituent "half-tiles," the acute and obtuse Robinson triangles.3 For instance, in the P2 tiling, a half-kite is replaced by two half-kites and a half-dart, while a half-dart is replaced by a half-kite and a half-dart.4 This process is repeated to a desired computational depth, after which the half-tiles are reassembled into their full tile shapes.3

References:
- Two algorithms for randomly generating aperiodic tilings - Chiark.greenend.org.uk, accessed on November 7, 2025, [https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/aperiodic-tilings/]  
- Penrose tiling quilt - Needlessly complex, accessed on November 7, 2025, [https://mzucker.github.io/2022/11/13/penrose-tiling-quilt.html]  
- Penrose Tiling - University of Utah Math Dept., accessed on November 7, 2025, [https://www.math.utah.edu/~treiberg/PenroseSlides.pdf]

This method is computationally straightforward, often implemented with a simple recursive function that calls the subdivision rule.5 The reverse process, "inflation" or "composition," where tiles are uniquely grouped into larger, coarser-grained super-tiles, is a powerful theoretical tool used to prove the tiling's aperiodicity.5

References:
- Penrose Tiling - University of Utah Math Dept., accessed on November 7, 2025, [https://www.math.utah.edu/~treiberg/PenroseSlides.pdf]  
- Penrose Tiling Explained - Preshing on Programming, accessed on November 7, 2025, [https://preshing.com/20110831/penrose-tiling-explained/]  
- Just C++ - Penrose tiling from python to C++ & Qt - YouTube, accessed on November 7, 2025, [https://www.youtube.com/watch?v=iceyjo0wVT8]  
- Penrose Tiling - Scientific Programming with Python, accessed on November 7, 2025, [https://scipython.com/blog/penrose-tiling-1/]

#### **1.1.2: The Cut-and-Project Method: A Global, Algebraic Approach**

The cut-and-project method is a global, algebraic construction that generates the entire infinite tiling deterministically. First developed by N. G. de Bruijn, this method reveals the Penrose tiling to be a 2D "shadow" of a 5D periodic structure.5

References:
- Penrose Tiling - University of Utah Math Dept., accessed on November 7, 2025, [https://www.math.utah.edu/~treiberg/PenroseSlides.pdf]

The procedure involves projecting the integer points of a 5D hypercubic lattice ($\mathbb{Z}^5$) onto a 2D plane oriented with five-fold symmetry.5 The vertices of the 2D tiling correspond *only* to those 5D lattice points that fall within a specific "acceptance window" or "stripe".5

For the P3 rhombic tiling, this is often implemented as the "Pentagrid" method.10 Here, the 2D plane is overlaid with five families of parallel lines. The intersections of these lines define the vertices and rhombs of the final tiling.5 This global, algebraic approach is computationally robust, and the pynrose Python library, for example, explicitly uses the de Bruijn pentagrid method for P3 generation.13

References:
- Penrose Tiling - University of Utah Math Dept., accessed on November 7, 2025, [https://www.math.utah.edu/~treiberg/PenroseSlides.pdf]  
- Why Penrose Tiles Never Repeat - YouTube, accessed on November 7, 2025, [https://www.youtube.com/watch?v=-eqdj63nEr4]  
- Penrose Tiling - University of Utah Math Dept., accessed on November 7, 2025, [https://www.math.utah.edu/~treiberg/PenroseSlides.pdf]  
- Generating Quasicrystals with the Cut and Project Method - YouTube, accessed on November 7, 2025, [https://www.youtube.com/watch?v=hwMAOFb6yvA]  
- Penrose Rhomb - Tilings Encyclopedia, accessed on November 7, 2025, [https://tilings.math.uni-bielefeld.de/substitution/penrose-rhomb/]  
- pynrose - P3 Penrose Tiling Generator - PyPI, accessed on November 7, 2025, [https://pypi.org/project/pynrose/]

This duality of generation—local/recursive vs. global/algebraic—is the foundational duality of quasicrystal physics. The deflation method provides the conceptual model for *physical growth* and the creation of *local defects*. The cut-and-project method provides the formal, global definition of the tiling's symmetry and the "perpendicular space" in which phason dynamics (see Part II) are theoretically described.14

References:
- Phason modes in quasicrystals - ResearchGate, accessed on November 7, 2025, [https://www.researchgate.net/publication/263270522_Phason_modes_in_quasicrystals]  
- Discussion of phasons in quasicrystals and their dynamics - ResearchGate, accessed on November 7, 2025, [https://www.researchgate.net/publication/228342390_Discussion_of_phasons_in_quasicrystals_and_their_dynamics]

| Method | Core Principle | Computational Nature | Output | Physical Analogy | Theoretical Utility |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **Deflation/Substitution** | Local, recursive self-similarity 1 | Iterative, fractal-like. Depth-limited. | Finite patch with self-similar structure. | Physical growth, self-assembly. | Proof of aperiodicity via inflation.9 |
| **Cut-and-Project** | Global projection from a higher-dim. periodic lattice 5 | Algebraic, deterministic. Calculates vertex positions. | Globally perfect, infinite structure. | Higher-dimensional crystallography. | Defines phasons as translations in perp. space.14 |
|  |  |  |  |  |  |

references: 
- Penrose tiling - Wikipedia, accessed on November 7, 2025, [https://en.wikipedia.org/wiki/Penrose_tiling]  
- Penrose tiling quilt - Needlessly complex, accessed on November 7, 2025, [https://mzucker.github.io/2022/11/13/penrose-tiling-quilt.html]  
- Penrose Tiling - University of Utah Math Dept., accessed on November 7, 2025, [https://www.math.utah.edu/~treiberg/PenroseSlides.pdf]  
- OXFORD MASTERCLASSES IN GEOMETRY 2014. Part 2: Lectures on Penrose Tilings, Prof. Alexander F. Ritter. - People, accessed on November 7, 2025, [https://people.maths.ox.ac.uk/ritter/masterclasses/ritter-lectures-on-penrose-tilings.pdf]  
- Penrose Tiling - University of Utah Math Dept., accessed on November 7, 2025, [https://www.math.utah.edu/~treiberg/PenroseSlides.pdf]  

#### Gpt source:
 - restriction on offset value: https://arxiv.org/html/2402.01257v2?utm




### **Section 1.2: The Phason Flip: A Local Mechanism for Aperiodic Dynamics**

#### **1.2.1: Defining the Phason Flip**

A phason flip is the elementary excitation unique to quasicrystals. It is a discrete, local rearrangement of tiles 16 or, at the atomic level, a local displacement of atoms.17

A critical distinction must be made: a phason flip is *not* a topological defect like a dislocation, nor is it a simple vibration (a phonon). Instead, it is a local shift of a vertex that *respects the tile shapes* (i.e., the P3 tiling remains tiled by thin and fat rhombs) but *breaks the local matching rules* that enforce perfect quasiperiodicity.17 This move transitions the tiling from one valid, low-energy configuration to another.

References:
- Defect-Free Growth of Decagonal Quasicrystals around Obstacles ..., accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/bsbs-rryl]  
- defects in quasicrystals, revisited I− flips, approximants, phason defects - arXiv, accessed on November 7, 2025, [https://arxiv.org/pdf/1303.5563]

#### **1.2.2: The P3 (Rhombus) Flip Algorithm (Conceptual)**

While many simple generation codes do not include a phason flip function 2, the mechanism is well-defined by the tiling's vertex configurations. A phason flip is a local re-tiling of a specific, "flippable" vertex configuration. For example, a vertex of the "Jack" type (formed by a specific arrangement of tiles 18) can be "flipped."

References:
- Penrose tiling - Rosetta Code, accessed on November 7, 2025, [https://rosettacode.org/wiki/Penrose_tiling]  
- Penrose Tiles and Aperiodic Tessellations, accessed on November 7, 2025, [https://e.math.cornell.edu/people/mann/classes/chicago/penrose%20reading.pdf]  
- Penrose Tiling - Scientific Programming with Python, accessed on November 7, 2025, [https://scipython.com/blog/penrose-tiling-1/]

The conceptual algorithm is a local move:

1. **Identify:** Locate a "flippable" local configuration, often a "hexagon" composed of two thick rhombi and one thin rhombus centered on a "Jack" vertex.1  
2. **Move:** The central vertex "jumps" to a new, bistable position.  
3. **Rearrange:** This move reconfigures the three constituent rhombi, changing their relative orientations into an alternative, degenerate arrangement.

References:
- Penrose tiling - Wikipedia, accessed on November 7, 2025, [https://en.wikipedia.org/wiki/Penrose_tiling]  
- Penrose Tiles and Aperiodic Tessellations, accessed on November 7, 2025, [https://e.math.cornell.edu/people/mann/classes/chicago/penrose%20reading.pdf]

This single flip is the "atom" of phason dynamics. As described in 17, a single flip (e.g., $a \rightarrow a'$) locally creates two "mismatches" or "phason singularities".17 These singularities can then "diffuse apart along the row of hexagons by a sequence of local flips".17 This illustrates that the phason flip is not merely a static defect, but the fundamental unit of *change* and *motion* by which the tiling explores its vast configuration space.

References:
- defects in quasicrystals, revisited I− flips, approximants, phason defects - arXiv, accessed on November 7, 2025, [https://arxiv.org/pdf/1303.5563]

### **Section 1.3: Simulating Quasicrystal Growth and Healing**

A primary function of phasonic degrees of freedom is to enable quasicrystal growth and "healing".16 This is a key advantage over periodic crystals, which must resort to high-energy dislocations to accommodate mismatches.

References:
- Defect-Free Growth of Decagonal Quasicrystals around Obstacles ..., accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/bsbs-rryl]

#### **1.3.1: Phason-Mediated Healing and Growth**

Research by Schmiedeberg et al. is central to this understanding. Using a dynamical Phase-Field Crystal (PFC) model, they simulated quasicrystal growth from seeds.19

References:
- (PDF) Growth Modes of Quasicrystals - ResearchGate, accessed on November 7, 2025, [https://www.researchgate.net/publication/262526163_Growth_Modes_of_Quasicrystals]  
- Dislocation-free growth of quasicrystals from two seeds due to additional phasonic degrees of freedom | Phys. Rev. E, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevE.96.012602]  
- Growth Modes of Quasicrystals | Phys. Rev. Lett., accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevLett.112.255501]

This work identified two distinct growth modes: (1) defect-free growth of the stable, ideal quasicrystal, and (2) a mode dominated by phasonic flips, which are incorporated as local defects, leading to a "random tiling-like" ordering.19

References:
- Growth Modes of Quasicrystals | Phys. Rev. Lett., accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevLett.112.255501]

Crucially, when simulating growth from multiple seeds or around obstacles, the phasons provide a unique mechanism for stress relaxation. In a periodic crystal, incommensurate distances lead to high-energy dislocations.20

References:
- Dislocation-free growth of quasicrystals from two seeds due to additional phasonic degrees of freedom | Phys. Rev. E, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevE.96.012602]

In a quasicrystal, this stress is instead relaxed by the creation of a *phasonic strain field*.20 The phasons provide a "softer," lower-energy pathway to accommodate structural mismatch, enabling the growth of dislocation-free quasicrystals.22

References:
- Dislocation-free growth of quasicrystals from two seeds due to additional phasonic degrees of freedom | Phys. Rev. E, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevE.96.012602]  
- Dislocation-free growth of quasicrystals from two seeds due to additional phasonic degrees of freedom - PubMed, accessed on November 7, 2025, [https://pubmed.ncbi.nlm.nih.gov/29347123/]

#### **1.3.2: Monte Carlo (MC) Simulation Methods**

Monte Carlo (MC) methods are a primary tool for modeling this behavior. In this context, the "local move" attempted by the MC algorithm *is* the phason flip.23

References:
- Tuning the stability of a model quasicrystal and its approximants with a periodic substrate, accessed on November 7, 2025, [https://pubs.rsc.org/en/content/articlehtml/2024/sm/d4sm00191e]

For example, in a simulation of decagonal quasicrystals, a "180-degree flip of a pentagon tile" is defined as the elementary MC move, with its acceptance probability dependent on the local energy of the new configuration.24 Other studies explicitly extend MD packages like HOOMD-blue to incorporate "a phason flip in MC".23 These simulations confirm that this "error-and-repair" mechanism allows the quasicrystal to grow with negligible phason strain.25

References:
- Monte Carlo study of the quasicrystal-to-crystal ... - Sci-Hub, accessed on November 7, 2025, [https://2024.sci-hub.box/6404/d3663f3246e3d7fa7fb8a19ae6ead7a8/10.1524@zkri.217.3.109.20646.pdf]  
- Tuning the stability of a model quasicrystal and its approximants with a periodic substrate, accessed on November 7, 2025, [https://pubs.rsc.org/en/content/articlehtml/2024/sm/d4sm00191e]  
- Entropic formation of a thermodynamically stable colloidal quasicrystal with negligible phason strain | PNAS, accessed on November 7, 2025, [https://www.pnas.org/doi/10.1073/pnas.2011799118]

#### **1.3.3: Molecular Dynamics (MD) Simulation Methods**

Molecular Dynamics (MD) provides a more atomistic, first-principles view. In MD, the phason flip is not a pre-programmed "move" but an *emergent* phenomenon. At elevated temperatures, MD simulations observe phason flips as "stochastic particle motion," which can manifest as "single-particle jumps or correlated ringlike multi-particle moves".26

References:
- Self-Assembly of Monatomic Complex Crystals and Quasicrystals with a Double-Well Interaction Potential | Phys. Rev. Lett., accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevLett.98.225505]  
- Dynamics of particle flips in two-dimensional quasicrystals | Phys. Rev. B, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevB.82.134206]

These three simulation scales (PFC, MC, and MD) reveal a complete, hierarchical picture of the healing mechanism. The *atomistic* (MD) particle jumps are the physical basis for the *mesoscopic* (MC) tile flip. The collective, long-range field of these MC flips *is* the *continuum* (PFC) phasonic strain field. This hierarchy explains how quasicrystals heal: local stress initiates a cascade of low-energy phason flips, which diffuse, spreading the stress as a low-gradient phasonic field and preventing the formation of a high-energy dislocation.

### **Section 1.4: The Computational Researcher's Toolkit: Software and Metrics**

The simulation and analysis of these systems rely on a specialized toolkit of software and order parameters.

#### **1.4.1: The Simulation and Analysis Ecosystem**

A core open-source package for this work is **HOOMD-blue**, a high-performance particle simulation toolkit that runs on both CPUs and GPUs.28 It is a product of the Glotzer lab 30 and is explicitly used in quasicrystal research for MD simulations 16 and can be extended with custom plugins to perform MC phason flips.23

References:
- HOOMD-blue 5.4.0 documentation, accessed on November 7, 2025, [https://hoomd-blue.readthedocs.io/]  
- glotzerlab/hoomd-blue: Molecular dynamics and Monte Carlo soft matter simulation on GPUs. - GitHub, accessed on November 7, 2025, [https://github.com/glotzerlab/hoomd-blue]  
- Defect-Free Growth of Decagonal Quasicrystals around Obstacles ..., accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/bsbs-rryl]  
- Tuning the stability of a model quasicrystal and its approximants with a periodic substrate, accessed on November 7, 2025, [https://pubs.rsc.org/en/content/articlehtml/2024/sm/d4sm00191e]  
- Computational Self-Assembly of a Six-Fold Chiral Quasicrystal - arXiv, accessed on November 7, 2025, [https://arxiv.org/html/2408.01984v1]  
- Software - The Glotzer Group - University of Michigan, accessed on November 7, 2025, [https://glotzerlab.engin.umich.edu/software/]

This is supported by a rich Python ecosystem. For generation, libraries like pynrose (cut-and-project) 13 and penrose (deflation) 32, as well as PyQCstrc.ico 33, are used. For analysis, the **freud** Python package is a primary tool, designed to efficiently analyze data from simulations like those run in HOOMD-blue.34

References:
- pynrose - P3 Penrose Tiling Generator - PyPI, accessed on November 7, 2025, [https://pypi.org/project/pynrose/]  
- Penrose tiling generator - GitHub, accessed on November 7, 2025, [https://github.com/samm00/penrose]  
- Structure of face-centred icosahedral quasicrystals with cluster close ..., accessed on November 7, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11532924/]  
- freud.order.Steinhardt - freud 3.5.0 documentation, accessed on November 7, 2025, [https://freud.readthedocs.io/en/latest/gettingstarted/examples/module_intros/order.Steinhardt.html]  
- Entropic formation of a thermodynamically stable colloidal quasicrystal with negligible phason strain - ResearchGate, accessed on November 7, 2025, [https://www.researchgate.net/publication/349171982_Entropic_formation_of_a_thermodynamically_stable_colloidal_quasicrystal_with_negligible_phason_strain]

#### **1.4.2: Key Order Parameters**

To quantify the state of a simulated quasicrystal, several key metrics are required.

i. Bond Orientational Order (BOO): Steinhardt $Q_l$  
The Steinhardt parameters, $q_l$, are rotationally invariant metrics that quantify the local symmetry of a particle's neighborhood using spherical harmonics.35 $Q_l$ is the system-wide average. The local formula is:

$$q_l(i) = \left( \frac{4\pi}{2l+1} \sum_{m=-l}^{l} |q_{lm}(i)|^2 \right)^{1/2}$$  
35  
For a Penrose tiling, $Q_l$ with $l=10$ (or $l=5$ in 2D analysis) is a primary indicator of local five-fold or ten-fold symmetry, distinguishing the quasicrystal from a liquid (low $Q_l$) or a hexagonal crystal (high $Q_6$). This is implemented in libraries like freud.order.Steinhardt 36 and as a compute in LAMMPS.37

References:
- Steinhardt's parameters — pyscal 2.7.0 documentation, accessed on November 7, 2025, [https://docs.pyscal.org/en/doc_update/methods/steinhardtparameters/traditionalsteinhardtparameters.html]  
- freud.order.Steinhardt - freud 3.5.0 documentation, accessed on November 7, 2025, [https://freud.readthedocs.io/en/latest/gettingstarted/examples/module_intros/order.Steinhardt.html]  
- compute orientorder/atom command - LAMMPS documentation, accessed on November 7, 2025, [https://docs.lammps.org/compute_orientorder_atom.html]

ii. Static Structure Factor $S(q)$  
The static structure factor, $S(q)$, is the Fourier transform of the system's pair-correlation function.38 It is the gold standard for identifying long-range order, as it is the quantity directly measured in X-ray, electron, or neutron diffraction experiments.39 Its formula is:

$$S(q) = \frac{1}{N} \left\langle \sum_{j,k} e^{-i\mathbf{q} \cdot (\mathbf{r}_j - \mathbf{r}_k)} \right\rangle$$  
38  
A liquid produces broad, diffuse rings. A crystal produces discrete, periodic Bragg peaks. A quasicrystal's unique signature is a dense set of sharp, aperiodic Bragg peaks.40

References:
- Structure Factor - LS Instruments, accessed on November 7, 2025, [https://lsinstruments.ch/en/theory/static-light-scattering-sls/structure-factor]  
- Structure factor - Wikipedia, accessed on November 7, 2025, [https://en.wikipedia.org/wiki/Structure_factor]  
- Structure factors of harmonic and anharmonic Fibonacci chains by molecular dynamics simulations | Phys. Rev. B, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevB.75.144203]

iii. Tiling-Specific Metrics: Phason Strain and Defect Density  
Phason strain ($\alpha$) is a metric unique to quasicrystals that quantifies the deviation from ideal quasiperiodicity.16 It is the "frozen-in" remnant of phason flips. Computationally, it is derived from the cut-and-project model. Particle positions $\mathbf{r}$ are projected into their "parallel space" ($r_{\parallel}$, the physical world) and "perpendicular space" ($r_{\perp}$, the abstract dimensions). Phason strain is the slope of the perpendicular space displacement as a function of the parallel space position: $\alpha = \text{slope of } \langle r_{\perp}(r_{\parallel}) \rangle$.42 A high-quality quasicrystal is one with negligible phason strain.25

References:
- Defect-Free Growth of Decagonal Quasicrystals around Obstacles ..., accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/bsbs-rryl]  
- Entropic formation of a thermodynamically stable colloidal quasicrystal with negligible phason strain - PMC, accessed on November 7, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7896337/]  
- Entropic formation of a thermodynamically stable colloidal quasicrystal with negligible phason strain | PNAS, accessed on November 7, 2025, [https://www.pnas.org/doi/10.1073/pnas.2011799118]

Tile Defect Density is a simpler, more direct metric, calculated by counting the number of tiles or vertices that violate the local matching rules ("bad tiles") 9 or, in related models, the density of "monomers" (unmatched vertices).43

References:
- OXFORD MASTERCLASSES IN GEOMETRY 2014. Part 2: Lectures on Penrose Tilings, Prof. Alexander F. Ritter. - People, accessed on November 7, 2025, [https://people.maths.ox.ac.uk/ritter/masterclasses/ritter-lectures-on-penrose-tilings.pdf]  
- Classical Dimers on Penrose Tilings | Phys. Rev. X, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevX.10.011005]

| Parameter | Formal Definition (Conceptual) | Computational Formula (from sources) | What It Measures | Implementation |
| :---- | :---- | :---- | :---- | :---- |
| **Bond Orientational Order ($Q_l$)** | Average local symmetry of particle neighbors 35 | $q_l(i) = \left( \frac{4\pi}{2l+1} \sum_{m} | q_{lm}(i) | ^2 \right)^{1/2}$ 35 |
| **Static Structure Factor ($S(q)$)** | Fourier transform of the pair-correlation function 38 | $S(q) = \frac{1}{N} \langle \sum_{j,k} e^{-i\mathbf{q} \cdot (\mathbf{r}_j - \mathbf{r}_k)} \rangle$ 38 | Global translational order (diffraction) | Custom code 44, LAMMPS 45 |
| **Phason Strain ($\alpha$)** | Gradient of the perpendicular-space displacement field 46 | $\alpha = \text{slope of } \langle r_{\perp}(r_{\parallel}) \rangle$ 42 | Deviation from *ideal* quasiperiodicity | Pattern recognition on particle trajectories 25 |
| **Tile Defect Density** | Density of tiles or vertices violating matching rules 9 | $n_{\text{defects}} / N_{\text{tiles}}$ | Local tiling "errors" or mismatches | Vertex/tile configuration analysis 43 |
|  |  |  |  |  |

- Kai Zhang | Computational Soft Matter - Static Structure Factor S(q) or S(k) - Google Sites, accessed on November 7, 2025, [https://sites.google.com/site/kaizhangstatmech/code/structurefactorsq]  
- Steinhardt's parameters — pyscal 2.7.0 documentation, accessed on November 7, 2025, [https://docs.pyscal.org/en/doc_update/methods/steinhardtparameters/traditionalsteinhardtparameters.html]

---

## **Part II: Statistical Mechanics and Emergent Phason Dynamics**

### **Section 2.1: The Random Tiling Model (RTM) and Configurational Entropy**

The Random Tiling Model (RTM) provides the statistical mechanics framework that explains *why* the phason-driven behaviors observed in Part I occur. The RTM posits that stable quasicrystals are *entropically stabilized* high-temperature phases.48

References:
- Confirmation of the Random Tiling Hypothesis for a Decagonal ..., accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevLett.109.225502]

This is a radical departure from periodic crystals, whose stability is typically energetic (a single, perfect ground state). A quasicrystal, by contrast, is not one single structure but an *ensemble* of an exponentially large number of different tilings that are all nearly degenerate in energy.50 This *configurational entropy*—the $S$ in the free energy equation $F = E - TS$—is the dominant term that stabilizes the quasicrystal phase at finite temperatures.51

References:
- A hard-sphere quasicrystal stabilized by configurational entropy - arXiv, accessed on November 7, 2025, [https://arxiv.org/abs/2306.03549]  
- Quasicrystal of Binary Hard Spheres on a Plane Stabilized by Configurational Entropy | Phys. Rev. Lett., accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevLett.132.048202]

The phason flip is the microscopic mechanism that allows the system to *explore* this vast ensemble of tilings. The "random tiling-like growth" mode observed in simulations 21 is a direct physical manifestation of the system dynamically maximizing its configurational entropy via phason flips.

References:
- (PDF) Growth Modes of Quasicrystals - ResearchGate, accessed on November 7, 2025, [https://www.researchgate.net/publication/262526163_Growth_Modes_of_Quasicrystals]

Within the RTM, a phason elastic theory can be constructed.53 The entropy density is a function of the phason strain, and it is found to be maximal at *zero* phason strain.49 This confirms that the most "random" (highest entropy) state is, on average, the one with perfect quasiperiodic symmetry. This framework allows for the calculation of phason elastic constants 48, which are *entropic* in origin. This leads to a key, verifiable prediction: as temperature *decreases*, these entropic elastic constants weaken, or "become soft." This softening, confirmed in simulations, leads to a phase transition from the quasicrystal to a periodic *approximant*.48

References:
- Random square-triangle tilings: A model for twelvefold-symmetric quasicrystals | Phys. Rev. B, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevB.48.6966]  
- Random Tiling Models for Quasicrystals - ResearchGate, accessed on November 7, 2025, [https://www.researchgate.net/publication/300663177_Random_Tiling_Models_for_Quasicrystals]  
- Confirmation of the Random Tiling Hypothesis for a Decagonal ... | Phys. Rev. Lett., accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevLett.109.225502]

### (The rest of the document remains unchanged; Works cited retained at end.)

#### **Works cited**

1. Penrose tiling \- Wikipedia, accessed on November 7, 2025, [https://en.wikipedia.org/wiki/Penrose\_tiling]  
2. Penrose tiling \- Rosetta Code, accessed on November 7, 2025, [https://rosettacode.org/wiki/Penrose\_tiling]  
3. Two algorithms for randomly generating aperiodic tilings \- Chiark.greenend.org.uk, accessed on November 7, 2025, [https://www.chiark.greenend.org.uk/\~sgtatham/quasiblog/aperiodic-tilings/](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/aperiodic-tilings/)  
4. Penrose tiling quilt | Needlessly complex, accessed on November 7, 2025, [https://mzucker.github.io/2022/11/13/penrose-tiling-quilt.html](https://mzucker.github.io/2022/11/13/penrose-tiling-quilt.html)  
5. Penrose Tiling \- University of Utah Math Dept., accessed on November 7, 2025, [https://www.math.utah.edu/\~treiberg/PenroseSlides.pdf](https://www.math.utah.edu/~treiberg/PenroseSlides.pdf)  
6. Penrose Tiling \- Scientific Programming with Python, accessed on November 7, 2025, [https://scipython.com/blog/penrose-tiling-1/](https://scipython.com/blog/penrose-tiling-1/)  
7. Penrose Tiling Explained \- Preshing on Programming, accessed on November 7, 2025, [https://preshing.com/20110831/penrose-tiling-explained/](https://preshing.com/20110831/penrose-tiling-explained/)  
8. Just C++ \- Penrose tiling from python to C++ & Qt \- YouTube, accessed on November 7, 2025, [https://www.youtube.com/watch?v=iceyjo0wVT8](https://www.youtube.com/watch?v=iceyjo0wVT8)  
9. OXFORD MASTERCLASSES IN GEOMETRY 2014\. Part 2: Lectures on Penrose Tilings, Prof. Alexander F. Ritter. \- People, accessed on November 7, 2025, [https://people.maths.ox.ac.uk/ritter/masterclasses/ritter-lectures-on-penrose-tilings.pdf](https://people.maths.ox.ac.uk/ritter/masterclasses/ritter-lectures-on-penrose-tilings.pdf)  
10. Why Penrose Tiles Never Repeat \- YouTube, accessed on November 7, 2025, [https://www.youtube.com/watch?v=-eqdj63nEr4](https://www.youtube.com/watch?v=-eqdj63nEr4)  
11. Generating Quasicrystals with the Cut and Project Method \- YouTube, accessed on November 7, 2025, [https://www.youtube.com/watch?v=hwMAOFb6yvA](https://www.youtube.com/watch?v=hwMAOFb6yvA)  
12. Penrose Rhomb \- Tilings Encyclopedia, accessed on November 7, 2025, [https://tilings.math.uni-bielefeld.de/substitution/penrose-rhomb/](https://tilings.math.uni-bielefeld.de/substitution/penrose-rhomb/)  
13. pynrose \- P3 Penrose Tiling Generator \- PyPI, accessed on November 7, 2025, [https://pypi.org/project/pynrose/](https://pypi.org/project/pynrose/)  
14. Phason modes in quasicrystals \- ResearchGate, accessed on November 7, 2025, [https://www.researchgate.net/publication/263270522\_Phason\_modes\_in\_quasicrystals](https://www.researchgate.net/publication/263270522_Phason_modes_in_quasicrystals)  
15. Discussion of phasons in quasicrystals and their dynamics \- ResearchGate, accessed on November 7, 2025, [https://www.researchgate.net/publication/228342390\_Discussion\_of\_phasons\_in\_quasicrystals\_and\_their\_dynamics](https://www.researchgate.net/publication/228342390_Discussion_of_phasons_in_quasicrystals_and_their_dynamics)  
16. Defect-Free Growth of Decagonal Quasicrystals around Obstacles ..., accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/bsbs-rryl](https://link.aps.org/doi/10.1103/bsbs-rryl)  
17. defects in quasicrystals, revisited I− flips, approximants, phason defects \- arXiv, accessed on November 7, 2025, [https://arxiv.org/pdf/1303.5563](https://arxiv.org/pdf/1303.5563)  
18. Penrose Tiles and Aperiodic Tessellations, accessed on November 7, 2025, [https://e.math.cornell.edu/people/mann/classes/chicago/penrose%20reading.pdf](https://e.math.cornell.edu/people/mann/classes/chicago/penrose%20reading.pdf)  
19. Growth Modes of Quasicrystals | Phys. Rev. Lett., accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevLett.112.255501](https://link.aps.org/doi/10.1103/PhysRevLett.112.255501)  
20. Dislocation-free growth of quasicrystals from two seeds due to additional phasonic degrees of freedom | Phys. Rev. E, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevE.96.012602](https://link.aps.org/doi/10.1103/PhysRevE.96.012602)  
21. (PDF) Growth Modes of Quasicrystals \- ResearchGate, accessed on November 7, 2025, [https://www.researchgate.net/publication/262526163\_Growth\_Modes\_of\_Quasicrystals](https://www.researchgate.net/publication/262526163_Growth_Modes_of_Quasicrystals)  
22. Dislocation-free growth of quasicrystals from two seeds due to additional phasonic degrees of freedom \- PubMed, accessed on November 7, 2025, [https://pubmed.ncbi.nlm.nih.gov/29347123/](https://pubmed.ncbi.nlm.nih.gov/29347123/)  
23. Tuning the stability of a model quasicrystal and its approximants with a periodic substrate, accessed on November 7, 2025, [https://pubs.rsc.org/en/content/articlehtml/2024/sm/d4sm00191e](https://pubs.rsc.org/en/content/articlehtml/2024/sm/d4sm00191e)  
24. Monte Carlo study of the quasicrystal-to-crystal ... \- Sci-Hub, accessed on November 7, 2025, [https://2024.sci-hub.box/6404/d3663f3246e3d7fa7fb8a19ae6ead7a8/10.1524@zkri.217.3.109.20646.pdf](https://2024.sci-hub.box/6404/d3663f3246e3d7fa7fb8a19ae6ead7a8/10.1524@zkri.217.3.109.20646.pdf)  
25. Entropic formation of a thermodynamically stable colloidal quasicrystal with negligible phason strain | PNAS, accessed on November 7, 2025, [https://www.pnas.org/doi/10.1073/pnas.2011799118](https://www.pnas.org/doi/10.1073/pnas.2011799118)  
26. Self-Assembly of Monatomic Complex Crystals and Quasicrystals with a Double-Well Interaction Potential | Phys. Rev. Lett. \- Physical Review Link Manager, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevLett.98.225505](https://link.aps.org/doi/10.1103/PhysRevLett.98.225505)  
27. Dynamics of particle flips in two-dimensional quasicrystals | Phys. Rev. B, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevB.82.134206](https://link.aps.org/doi/10.1103/PhysRevB.82.134206)  
28. HOOMD-blue 5.4.0 documentation, accessed on November 7, 2025, [https://hoomd-blue.readthedocs.io/](https://hoomd-blue.readthedocs.io/)  
29. glotzerlab/hoomd-blue: Molecular dynamics and Monte Carlo soft matter simulation on GPUs. \- GitHub, accessed on November 7, 2025, [https://github.com/glotzerlab/hoomd-blue](https://github.com/glotzerlab/hoomd-blue)  
30. Software \- The Glotzer Group \- University of Michigan, accessed on November 7, 2025, [https://glotzerlab.engin.umich.edu/software/](https://glotzerlab.engin.umich.edu/software/)  
31. Computational Self-Assembly of a Six-Fold Chiral Quasicrystal \- arXiv, accessed on November 7, 2025, [https://arxiv.org/html/2408.01984v1](https://arxiv.org/html/2408.01984v1)  
32. Penrose tiling generator \- GitHub, accessed on November 7, 2025, [https://github.com/samm00/penrose](https://github.com/samm00/penrose)  
33. Structure of face-centred icosahedral quasicrystals with cluster close ..., accessed on November 7, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11532924/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11532924/)  
34. Entropic formation of a thermodynamically stable colloidal quasicrystal with negligible phason strain | Request PDF \- ResearchGate, accessed on November 7, 2025, [https://www.researchgate.net/publication/349171982\_Entropic\_formation\_of\_a\_thermodynamically\_stable\_colloidal\_quasicrystal\_with\_negligible\_phason\_strain](https://www.researchgate.net/publication/349171982_Entropic_formation_of_a_thermodynamically_stable_colloidal_quasicrystal_with_negligible_phason_strain)  
35. Steinhardt's parameters — pyscal 2.7.0 documentation, accessed on November 7, 2025, [https://docs.pyscal.org/en/doc_update/methods/steinhardtparameters/traditionalsteinhardtparameters.html](https://docs.pyscal.org/en/doc_update/methods/steinhardtparameters/traditionalsteinhardtparameters.html)  
36. freud.order.Steinhardt \- freud 3.5.0 documentation, accessed on November 7, 2025, [https://freud.readthedocs.io/en/latest/gettingstarted/examples/module_intros/order.Steinhardt.html](https://freud.readthedocs.io/en/latest/gettingstarted/examples/module_intros/order.Steinhardt.html)  
37. compute orientorder/atom command \- LAMMPS documentation, accessed on November 7, 2025, [https://docs.lammps.org/compute_orientorder_atom.html](https://docs.lammps.org/compute_orientorder_atom.html)  
38. Structure Factor \- LS Instruments, accessed on November 7, 2025, [https://lsinstruments.ch/en/theory/static-light-scattering-sls/structure-factor](https://lsinstruments.ch/en/theory/static-light-scattering-sls/structure-factor)  
39. Structure factor \- Wikipedia, accessed on November 7, 2025, [https://en.wikipedia.org/wiki/Structure_factor](https://en.wikipedia.org/wiki/Structure_factor)  
40. Structure factors of harmonic and anharmonic Fibonacci chains by molecular dynamics simulations | Phys. Rev. B \- Physical Review Link Manager, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevB.75.144203](https://link.aps.org/doi/10.1103/PhysRevB.75.144203)  
41. Quasicrystal \- Wikipedia, accessed on November 7, 2025, [https://en.wikipedia.org/wiki/Quasicrystal](https://en.wikipedia.org/wiki/Quasicrystal)  
42. Entropic formation of a thermodynamically stable colloidal quasicrystal with negligible phason strain \- PMC \- PubMed Central, accessed on November 7, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7896337/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7896337/)  
43. Classical Dimers on Penrose Tilings | Phys. Rev. X, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevX.10.011005](https://link.aps.org/doi/10.1103/PhysRevX.10.011005)  
44. Kai Zhang | Computational Soft Matter - Static Structure Factor S(q) or S(k) - Google Sites, accessed on November 7, 2025, [https://sites.google.com/site/kaizhangstatmech/code/structurefactorsq](https://sites.google.com/site/kaizhangstatmech/code/structurefactorsq)  
45. structure factor compute? \- LAMMPS Mailing List Mirror \- Materials Science Community Discourse, accessed on November 7, 2025, [https://matsci.org/t/structure-factor-compute/18745](https://matsci.org/t/structure-factor-compute/18745)  
46. Phonons, phasons and dislocations in quasicrystals \- Paul J. Steinhardt, accessed on November 7, 2025, [https://paulsteinhardt.org/wp-content/uploads/2020/10/PhoPhaDef.pdf](https://paulsteinhardt.org/wp-content/uploads/2020/10/PhoPhaDef.pdf)  
47. Dynamics of Phason Fluctuations in the Quasicrystal | Phys. Rev. Lett., accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevLett.91.225501](https://link.aps.org/doi/10.1103/PhysRevLett.91.225501)  
48. Confirmation of the Random Tiling Hypothesis for a Decagonal ..., accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevLett.109.225502](https://link.aps.org/doi/10.1103/PhysRevLett.109.225502)  
49. Random Tiling Models for Quasicrystals \- ResearchGate, accessed on November 7, 2025, [https://www.researchgate.net/publication/300663177\_Random\_Tiling\_Models\_for\_Quasicrystals](https://www.researchgate.net/publication/300663177_Random_Tiling_Models_for_Quasicrystals)  
50. \[2306.03549\] A hard-sphere quasicrystal stabilized by configurational entropy \- arXiv, accessed on November 7, 2025, [https://arxiv.org/abs/2306.03549](https://arxiv.org/abs/2306.03549)  
51. Quasicrystal of Binary Hard Spheres on a Plane Stabilized by Configurational Entropy | Phys. Rev. Lett. \- Physical Review Link Manager, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevLett.132.048202](https://link.aps.org/doi/10.1103/PhysRevLett.132.048202)  
52. arXiv:2308.09192v1 \[cond-mat.mtrl-sci\] 17 Aug 2023, accessed on November 7, 2025, [https://arxiv.org/pdf/2308.09192](https://arxiv.org/pdf/2308.09192)  
53. Random square-triangle tilings: A model for twelvefold-symmetric quasicrystals | Phys. Rev. B \- Physical Review Link Manager, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevB.48.6966](https://link.aps.org/doi/10.1103/PhysRevB.48.6966)  
54. Full article: Direct experimental evidence of phonon–phason coupling in an Al-Pd-Mn icosahedral quasicrystal \- Taylor & Francis Online, accessed on November 7, 2025, [https://www.tandfonline.com/doi/full/10.1080/14786435.2022.2052376](https://www.tandfonline.com/doi/full/10.1080/14786435.2022.2052376)  
55. Phason dynamics in one-dimensional lattices | Phys. Rev. B, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevB.81.064302](https://link.aps.org/doi/10.1103/PhysRevB.81.064302)  
56. Phason Dynamics in One-Dimensional Lattices : Hansjörg Lipp, accessed on November 7, 2025, [https://archive.org/details/arxiv-1002.1918](https://archive.org/details/arxiv-1002.1918)  
57. Toggling Bistable Atoms via Mechanical Switching of Bond Angle | Phys. Rev. Lett., accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevLett.106.136101](https://link.aps.org/doi/10.1103/PhysRevLett.106.136101)  
58. Hydrodynamic structure factor of quasicrystals | Phys. Rev. B, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevB.81.064205](https://link.aps.org/doi/10.1103/PhysRevB.81.064205)  
59. Elasto-Dynamics of Quasicrystals \- MDPI, accessed on November 7, 2025, [https://www.mdpi.com/2073-4352/6/11/152](https://www.mdpi.com/2073-4352/6/11/152)  
60. Phonon and phason \- Aperiodic crystals, accessed on November 7, 2025, [http://sig3.ecanews.org/isac2010/lectures/17_deboissieu_phasons.pdf](http://sig3.ecanews.org/isac2010/lectures/17_deboissieu_phasons.pdf)  
61. Symmetry origin of lattice vibration modes in twisted multilayer graphene: Phasons versus moiré phonons \- Physical Review Link Manager, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevB.106.075420](https://link.aps.org/doi/10.1103/PhysRevB.106.075420)  
62. Hydrodynamics as the effective field theory of strong-to-weak spontaneous symmetry breaking | Phys. Rev. B \- Physical Review Link Manager, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevB.111.125147](https://link.aps.org/doi/10.1103/PhysRevB.111.125147)  
63. Homogeneous holographic viscoelastic models and quasicrystals | Phys. Rev. Research, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevResearch.2.022022](https://link.aps.org/doi/10.1103/PhysRevResearch.2.022022)  
64. Effective field theory for quasicrystals and phasons dynamics (Journal Article) | OSTI.GOV, accessed on November 7, 2025, [https://www.osti.gov/biblio/1702449](https://www.osti.gov/biblio/1702449)  
65. SciPost Phys. 9, 062 (2020) \- Effective field theory for ... \- SciPost, accessed on November 7, 2025, [https://scipost.org/SciPostPhys.9.5.062](https://scipost.org/SciPostPhys.9.5.062)  
66. \[2008.05339\] Effective Field Theory for Quasicrystals and Phasons Dynamics \- arXiv, accessed on November 7, 2025, [https://arxiv.org/abs/2008.05339](https://arxiv.org/abs/2008.05339)  
67. Quantum simulations with ultracold atoms in optical lattices \- PubMed, accessed on November 7, 2025, [https://pubmed.ncbi.nlm.nih.gov/28883070/](https://pubmed.ncbi.nlm.nih.gov/28883070/)  
68. \[2006.06120\] Tools for quantum simulation with ultracold atoms in optical lattices \- arXiv, accessed on November 7, 2025, [https://arxiv.org/abs/2006.06120](https://arxiv.org/abs/2006.06120)  
69. A Quasicrystal for Quantum Simulations \- Physical Review Link Manager, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/Physics.12.31](https://link.aps.org/doi/10.1103/Physics.12.31)  
70. Two-dimensional optical quasicrystal potentials for ultracold atom experiments, accessed on November 7, 2025, [https://opg.optica.org/abstract.cfm?uri=ao-58-9-2256](https://opg.optica.org/abstract.cfm?uri=ao-58-9-2256)  
71. Aubry–André model \- Wikipedia, accessed on November 7, 2025, [https://en.wikipedia.org/wiki/Aubry%E2%80%93Andr%C3%A9\_model](https://en.wikipedia.org/wiki/Aubry%E2%80%93Andr%C3%A9_model)  
72. Topological transitions with an imaginary Aubry-Andr\'e-Harper potential | Phys. Rev. Research \- Physical Review Link Manager, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevResearch.5.023044](https://link.aps.org/doi/10.1103/PhysRevResearch.5.023044)  
73. Hubbard models for quasicrystalline potentials | Phys. Rev. B, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevB.107.144202](https://link.aps.org/doi/10.1103/PhysRevB.107.144202)  
74. Antiferromagnetic order in the Hubbard model on the Penrose lattice ..., accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevB.96.214402](https://link.aps.org/doi/10.1103/PhysRevB.96.214402)  
75. Mean-field study of the Bose-Hubbard model in the Penrose lattice ..., accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevB.102.224201](https://link.aps.org/doi/10.1103/PhysRevB.102.224201)  
76. Mean-field study of the Bose-Hubbard model in Penrose lattice \- ResearchGate, accessed on November 7, 2025, [https://www.researchgate.net/publication/341310334\_Mean-field\_study\_of\_the\_Bose-Hubbard\_model\_in\_Penrose\_lattice](https://www.researchgate.net/publication/341310334_Mean-field_study_of_the_Bose-Hubbard_model_in_Penrose_lattice)  
77. Reversible Phasonic Control of a Quantum Phase Transition in a Quasicrystal | Phys. Rev. Lett. \- Physical Review Link Manager, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevLett.133.083405](https://link.aps.org/doi/10.1103/PhysRevLett.133.083405)  
78. Quantum Many-Body Topology of Quasicrystals | Phys. Rev. X, accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevX.11.041051](https://link.aps.org/doi/10.1103/PhysRevX.11.041051)  
79. Phasonic Spectroscopy of a Quantum Gas in a Quasicrystalline Lattice \- PubMed, accessed on November 7, 2025, [https://pubmed.ncbi.nlm.nih.gov/31868404/](https://pubmed.ncbi.nlm.nih.gov/31868404/)  
80. Phasonic Spectroscopy of a Quantum Gas in a Quasicrystalline ..., accessed on November 7, 2025, [https://link.aps.org/doi/10.1103/PhysRevLett.123.223201](https://link.aps.org/doi/10.1103/PhysRevLett.123.223201)  
81. Nobel Prize: Quantum Tunneling on a Large Scale \- Physics Magazine, accessed on November 7, 2025, [https://physics.aps.org/articles/v18/170](https://physics.aps.org/articles/v18/170)  
82. Quantum Tunnelling to the Origin and Evolution of Life \- PMC \- PubMed Central, accessed on November 7, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC3768233/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3768233/)  
83. Experimental observation of carousel-like phason flips in the decagonal quasicrystal Al60Cr20Fe10Si10 \- ResearchGate, accessed on November 7, 2025, [https://www.researchgate.net/publication/353888269\_Experimental\_observation\_of\_carousel-like\_phason\_flips\_in\_the\_decagonal\_quasicrystal\_Al60Cr20Fe10Si10](https://www.researchgate.net/publication/353888269_Experimental_observation_of_carousel-like_phason_flips_in_the_decagonal_quasicrystal_Al60Cr20Fe10Si10)  
84. Quantum Codes from Penrose Tiling | PDF | Wave Function | Euclidean Space \- Scribd, accessed on November 7, 2025, [https://www.scribd.com/document/726860702/2311-13040](https://www.scribd.com/document/726860702/2311-13040)  
85. The Penrose Tiling is a Quantum Error-Correcting Code, accessed on November 7, 2025, [https://arxiv.org/pdf/2311.13040](https://arxiv.org/pdf/2311.13040)  
86. \[2311.13040\] The Penrose Tiling is a Quantum Error-Correcting Code \- arXiv, accessed on November 7, 2025, [https://arxiv.org/abs/2311.13040](https://arxiv.org/abs/2311.13040)  
87. Penrose Tilings, Quantum Error Correction, Fractal Patterns of Reality \- Ultra Unlimited, accessed on November 7, 2025, [https://www.ultra-unlimited.com/blog/penrose-tilings-quantum-error-correction-fractal-patterns-of-reality](https://www.ultra-unlimited.com/blog/penrose-tilings-quantum-error-correction-fractal-patterns-of-reality)  
88. Never-Repeating Tiles Can Safeguard Quantum Information ..., accessed on November 7, 2025, [https://www.quantamagazine.org/never-repeating-tiles-can-safeguard-quantum-information-20240223/](https://www.quantamagazine.org/never-repeating-tiles-can-safeguard-quantum-information-20240223/)