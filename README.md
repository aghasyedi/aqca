# AQCA: All Quantum Computing Algorithms

AQCA (**All Quantum Computing Algorithms**) is a state-of-the-art, academic-grade educational atlas and interactive simulation platform for quantum computing. Developed as a comprehensive reference portal, AQCA provides deep mathematical derivations, physical state evolutions, circuit schematics, interactive visualizers, and verified Python/Qiskit implementations for 19 foundational and advanced quantum algorithms, communication protocols, and error-correcting codes.

---

## Key Features

- **19 Complete Algorithm Profiles:** Comprehensive documentation spanning quantum communication, oracle query models, phase/amplitude manipulation, hybrid variational models, and fault-tolerant stabilizer codes.
- **Interactive Visualizers:** Web-based simulation interfaces allowing users to step through quantum circuits, inspect phase kickback, observe amplitude amplification, and analyze measurement statistics in real-time.
- **Deep Mathematical Rigor:** Every algorithm page features complete state vector evolutions in Dirac bra-ket notation ($\langle\psi|$, $|\psi\rangle$), operator matrices, and computational complexity bounds rendered using MathJax v3.
- **Analysis Centre & Comparison Matrix:** An interactive benchmarking dashboard powered by Chart.js that dynamically plots classical vs. quantum scaling curves and generates side-by-side feature comparisons with real-time MathJax rendering.
- **Curated Scholarly References:** Every algorithm section in the reference library includes 3 to 4 authoritative citations including peer-reviewed papers (Physical Review Letters, Nature, FOCS/STOC), Wikipedia articles, and IBM Qiskit documentation.
- **Single Source of Truth (`AQAC.ipynb`):** All Python code blocks, circuit schematics, and measurement output plots are dynamically maintained and tested within a master Jupyter Notebook (`AQAC.ipynb`).

---

## Complete Algorithm & Protocol Catalogue

The portal organizes 19 quantum computing algorithms into five core educational pillars:

### 1. Quantum Communication & Protocols
- **Bell State Generator:** Creation of maximal two-qubit entanglement ($|\Phi^+\rangle$, $|\Phi^-\rangle$, $|\Psi^+\rangle$, $|\Psi^-\rangle$).
- **Superdense Coding:** Transmission of two classical bits using a single physical qubit and pre-shared entanglement.
- **Quantum Teleportation:** Exact transmission of an arbitrary unknown quantum state $|\psi\rangle$ across classical channels using Bell measurement.
- **Entanglement Swapping:** Entangling two independent qubits that have never interacted directly via joint Bell measurement.

### 2. Early Oracle Algorithms
- **Deutsch's Algorithm:** Determining whether a 1-bit boolean function $f: \{0,1\} \to \{0,1\}$ is constant or balanced in $O(1)$ query.
- **Deutsch–Jozsa Algorithm:** Generalization of Deutsch's problem to $n$-bit boolean functions with guaranteed exponential quantum speedup over classical deterministic algorithms.
- **Bernstein–Vazirani Algorithm:** Reconstructing a hidden secret bitstring $s \in \{0,1\}^n$ from an oracle $f(x) = s \cdot x \pmod 2$ in a single query vs. $n$ classical queries.
- **Simon's Algorithm:** Finding a hidden bitstring $s$ for a 2-to-1 function $f(x) = f(x \oplus s)$ in $O(n)$ queries, providing the historical blueprint for Shor's algorithm.

### 3. Phase & Amplitude Core Algorithms
- **Quantum Fourier Transform (QFT):** Quantum linear transformation mapping computational basis states to Fourier basis states in $O(n^2)$ gate complexity vs. classical FFT $O(n 2^n)$.
- **Quantum Phase Estimation (QPE):** Estimating the unknown phase $\theta$ of an eigenvector $|u\rangle$ for a unitary operator $U|u\rangle = e^{2\pi i \theta}|u\rangle$.
- **Grover's Search Algorithm:** Quadratic speedup $O(\sqrt{N})$ for unstructured database search using phase inversion and amplitude amplification about the mean.
- **Generalized Amplitude Amplification:** Framework extending Grover's search to arbitrary initial states and non-uniform target subspaces.

### 4. Flagship & Hybrid Models `[In-Progress / Beta]`
- **Shor's Algorithm:** Exponential speedup for integer factorization and discrete logarithms in $O((\log N)^3)$ operations using modular exponentiation and inverse QFT.
- **Variational Quantum Eigensolver (VQE):** Hybrid classical-quantum algorithm utilizing the Ritz variational principle to find ground state energies of molecular Hamiltonians on NISQ devices.
- **Quantum Approximate Optimization Algorithm (QAOA):** Variational algorithm solving combinatorial optimization problems (e.g., Max-Cut) using alternating problem and mixer Hamiltonians.
- **HHL Algorithm:** Quantum algorithm for solving sparse linear systems $A\vec{x} = \vec{b}$ in logarithmic time $O(\log N)$ relative to system dimension.

### 5. Fault Tolerance & Error Correction `[In-Progress / Beta]`
- **3-Qubit Bit-Flip / Phase-Flip Codes:** Repetition codes protecting single physical qubits against single $X$ (bit-flip) or $Z$ (phase-flip) errors using syndrome measurement.
- **Shor's 9-Qubit Code:** The first quantum error-correcting code capable of protecting a logical qubit against arbitrary single-qubit errors ($X$, $Z$, or $Y = iXZ$).
- **Steane 7-Qubit Code:** CSS code encoding 1 logical qubit into 7 physical qubits using 6 stabilizer generators, enabling fault-tolerant transversal $H$, $S$, and $CNOT$ operations.

---

## Platform Architecture & Portal Modules

AQCA is built with a modular, responsive architecture comprising dedicated modules:

- **Home Portal (`index.html`):** Platform entry point featuring an interactive vector Bloch Sphere diagram, overview of algorithm categories, feature breakdowns, and quick navigation.
- **Algorithms Catalogue (`algorithms.html`):** Searchable atlas listing all 19 algorithms with filter controls and direct links to visualizers and theoretical profiles.
- **Analysis Centre (`analysis.html`):** Benchmarking dashboard allowing side-by-side metric comparison, interactive time/space complexity chart plotting via Chart.js, and dynamic MathJax math typesetting.
- **Quantum Basics (`basics.html`):** Foundational tutorial covering Hilbert space geometry, Bloch Sphere coordinates $(\theta, \phi)$, Pauli matrices ($\sigma_x, \sigma_y, \sigma_z$), Hadamard ($H$), CNOT, phase kickback, and Dirac bra-ket formalism.
- **Literature & Reference Library (`references.html`):** Complete bibliography providing 3 to 4 verified scholarly links (Physical Review, Nature, IEEE, Wikipedia, Qiskit Textbook) for every single algorithm section.
- **Developer Information (`developer.html`):** Author background, subject matter specialization (Quantum Communication), and contact information.
- **Preface (`preface.html`) & Resources (`resources.html`):** User guidance, pedagogical roadmaps, and curated external learning materials.

---

## Tech Stack & Infrastructure

- **Frontend Interface:** Semantic HTML5, Vanilla CSS3 (Custom design system, glassmorphism, responsive grid), Vanilla JavaScript (ES6+).
- **Mathematical Engine:** MathJax v3 (`tex-mml-chtml.js`) for LaTeX mathematical notation and Dirac equation rendering.
- **Data Visualization:** Chart.js for complexity scaling curves, SVG graphics for state representations and Bloch sphere diagrams.
- **Quantum Backend:** Python 3, Qiskit, Qiskit-Aer simulator framework, Matplotlib for histogram and circuit plot rendering.
- **Source of Truth:** Master Jupyter Notebook (`AQAC.ipynb`).

---

## Developer & Attribution

- **Developer:** Agha Tasheer Syedi
- **Degree:** MTech in Quantum Computing
- **Specialization:** Quantum Communication & Quantum Algorithms
- **Contact Email:** [cs.aghasyedi@gmail.com](mailto:cs.aghasyedi@gmail.com)
- **Repository:** [aghasyedi/aqca](https://github.com/aghasyedi/aqca)

---

&copy; 2026 AQCA - All Quantum Computing Algorithms. Educational and Research Platform.
