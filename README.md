# AQCA: All Quantum Computing Algorithms

**Live Website:** [https://aqca.netlify.app/](https://aqca.netlify.app/)

AQCA (**All Quantum Computing Algorithms**) is a state-of-the-art, academic-grade educational atlas and interactive simulation platform for quantum computing. Developed as a comprehensive reference portal, AQCA provides deep mathematical derivations, physical state evolutions, circuit schematics, interactive visualisers, and verified Python/Qiskit implementations for 19 foundational and advanced quantum algorithms, communication protocols, and error-correcting codes.

---

## Key Features

- **19 Complete Algorithm Profiles:** Comprehensive documentation spanning quantum communication, oracle query models, phase/amplitude manipulation, hybrid variational models, and fault-tolerant stabilizer codes.
- **Interactive Visualisers:** Web-based simulation interfaces allowing users to step through quantum circuits, inspect phase kickback, observe amplitude amplification, and analyse measurement statistics in real-time.
- **Deep Mathematical Rigor:** Every algorithm page features complete state vector evolutions in Dirac bra-ket notation ($\langle\psi|$, $|\psi\rangle$), operator matrices, and computational complexity bounds rendered using MathJax v3.
- **Analysis Centre & Comparison Matrix:** An interactive benchmarking dashboard powered by Chart.js that dynamically plots classical vs. quantum scaling curves and generates side-by-side feature comparisons with real-time MathJax rendering.
- **Curated Scholarly References:** Every algorithm section in the reference library includes 3 to 4 authoritative citations including peer-reviewed papers (Physical Review Letters, Nature, FOCS/STOC), Wikipedia articles, and IBM Qiskit documentation.
- **Single Source of Truth (`AQCA.ipynb`):** All Python code blocks, circuit schematics, and measurement output plots are dynamically maintained and tested within a master Jupyter Notebook (`AQCA.ipynb`).

---

## Complete Algorithm & Protocol Catalogue

The portal organizes 19 quantum computing algorithms into five core educational pillars:

### 1. Quantum Communication & Protocols

| Protocol | Key Operation / Concept | Primary Application |
|---|---|---|
| **Bell State Generator** | Creates maximal 2-qubit entanglement ($/\Phi^\pm\rangle, /\Psi^\pm\rangle$) | Entanglement resource & channel setup |
| **Superdense Coding** | Transmits 2 classical bits using 1 qubit + pre-shared Bell pair | Quantum bandwidth multiplication |
| **Quantum Teleportation** | Transfers unknown state $/\psi\rangle$ via Bell measurement & classical bits | Quantum networking & state transfer |
| **Entanglement Swapping** | Entangles independent qubits without direct interaction | Quantum repeaters & long-distance QKD |

### 2. Early Oracle Algorithms

| Algorithm | Problem Solved | Quantum vs. Classical Complexity |
|---|---|---|
| **Deutsch's Algorithm** | Test if 1-bit boolean function $f(x)$ is constant or balanced | $O(1)$ query vs. $2$ classical queries |
| **Deutsch–Jozsa Algorithm** | Generalisation to $n$-bit boolean functions | $O(1)$ query vs. $O(2^{n-1}+1)$ deterministic |
| **Bernstein–Vazirani Algorithm** | Extract secret bitstring $s \in \{0,1\}^n$ from oracle $f(x)=s\cdot x$ | $1$ query vs. $n$ classical queries |
| **Simon's Algorithm** | Find period $s$ for 2-to-1 function $f(x)=f(x \oplus s)$ | $O(n)$ queries vs. $O(2^{n/2})$ classical |

### 3. Phase & Amplitude Core Algorithms

| Algorithm | Core Mechanism / Operation | Speedup & Complexity |
|---|---|---|
| **Quantum Fourier Transform (QFT)** | Linear transformation mapping state to Fourier basis | $O(n^2)$ gates vs. classical FFT $O(n 2^n)$ |
| **Quantum Phase Estimation (QPE)** | Estimate eigenvalue phase $\theta$ for $U /u\rangle = e^{2\pi i \theta} /u\rangle$ | Fundamental subroutine for Shor & HHL |
| **Grover's Search Algorithm** | Phase inversion & amplitude amplification about mean | Quadratic speedup $O(\sqrt{N})$ for search |
| **Generalized Amplitude Amplification** | Arbitrary initial state & target subspace amplification | Generalized quantum search framework |

### 4. Flagship & Hybrid Models `[In-Progress]`

| Model | Domain / Problem | Key Operational Mechanism |
|---|---|---|
| **Shor's Algorithm** | Integer factorisation & RSA breaking | Period finding via IQFT in $O((\log N)^3)$ operations |
| **Variational Quantum Eigensolver (VQE)** | Ground state energy of molecular Hamiltonians | Ritz variational principle on NISQ hardware |
| **Quantum Approximate Optimisation (QAOA)** | Combinatorial optimisation (e.g. Max-Cut) | Alternating problem & mixer Hamiltonians |
| **HHL Algorithm** | Solving linear systems $A\vec{x} = \vec{b}$ | Quantum phase estimation & inversion in $O(\log N)$ |

### 5. Fault Tolerance & Error Correction `[In-Progress]`

| Code | Protection Target | Code Parameters & Structure |
|---|---|---|
| **3-Qubit Codes** | Protects single qubit against single $X$ or $Z$ error | $[[3, 1, 1]]$ bit/phase repetition code |
| **Shor's 9-Qubit Code** | Protects single qubit against arbitrary single error ($X, Z, Y$) | $[[9, 1, 3]]$ concatenated code |
| **Steane 7-Qubit Code** | Protects arbitrary single-qubit error with transversal gates | $[[7, 1, 3]]$ CSS stabilizer code |

---

## Platform Architecture & Portal Modules

AQCA is built with a modular, responsive architecture comprising the following dedicated sections in sequence:

- **Home Portal (`index.html`):** Platform entry point featuring an interactive vector Bloch Sphere diagram, overview of algorithm categories, feature breakdowns, and quick navigation.
- **About AQCA (`about.html`):** Information regarding the mission, philosophy, and overarching goals of the platform.
- **Preface (`preface.html`):** Guidance on navigating the atlas, educational roadmap, and prerequisites.
- **Quantum Computing Basics (`basics.html`):** Foundational tutorial covering Hilbert space geometry, Bloch Sphere coordinates, Pauli matrices, phase kickback, and Dirac bra-ket formalism.
- **Algorithms Catalogue (`algorithms.html`):** Searchable atlas listing all 19 algorithms with filter controls and direct links to theoretical profiles and code implementations.
- **Visualise (`visualise.html`):** The central hub for interactive, web-based simulation interfaces allowing users to execute circuits step-by-step and observe real-time state changes.
- **Analysis Centre (`analysis.html`):** Benchmarking dashboard allowing side-by-side metric comparison, interactive time/space complexity chart plotting via Chart.js, and dynamic math typesetting.
- **Resources (`resources.html`):** Curated external learning materials, including textbooks, courses, and documentation.
- **Literature & Reference Library (`references.html`):** Complete bibliography providing 3 to 4 verified scholarly links (Physical Review, Nature, IEEE, Wikipedia, Qiskit Textbook) for every single algorithm section.
- **Appendix (`appendix.html`):** Detailed glossary and deep-dive explanations of specific quantum phenomena (e.g. No-Cloning Theorem, Trace Distance, Mutually Unbiased Bases, Decoherence).
- **Developer Information (`developer.html`):** Author background, subject matter specialization (Quantum Communication), and contact information.

---

## Tech Stack & Infrastructure

- **Frontend Interface:** Semantic HTML5, Vanilla CSS3 (Custom design system, glassmorphism, responsive grid), Vanilla JavaScript (ES6+).
- **Mathematical Engine:** MathJax v3 (`tex-mml-chtml.js`) for LaTeX mathematical notation and Dirac equation rendering.
- **Data Visualisation:** Chart.js for complexity scaling curves, SVG graphics for state representations and Bloch sphere diagrams.
- **Quantum Backend:** Python 3, Qiskit, Qiskit-Aer simulator framework, Matplotlib for histogram and circuit plot rendering.
- **Source of Truth:** Master Jupyter Notebook (`AQCA.ipynb`).

---

## Developer & Attribution

- **Developer:** Agha Tasheer Syedi
- **Degree:** MTech in Quantum Computing
- **Specialisation:** Quantum Communication & Quantum Algorithms
- **Live Website:** [https://aqca.netlify.app/](https://aqca.netlify.app/)
- **Contact Email:** [cs.aghasyedi@gmail.com](mailto:cs.aghasyedi@gmail.com)
- **Repository:** [aghasyedi/aqca](https://github.com/aghasyedi/aqca)

---

&copy; 2026 AQCA - All Quantum Computing Algorithms. Educational and Research Platform.
