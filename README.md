# AQCA: All Quantum Computing Algorithms

AQCA is a comprehensive, academic-style information portal serving as an educational atlas for quantum computing. It provides deep theoretical insights, mathematical proofs, circuit visualizations, and executable Python/Qiskit implementations for 19 fundamental and advanced quantum algorithms.

## Features

- **19 Complete Algorithm Profiles:** Ranging from foundational states to advanced error correction protocols.
- **Deep Theoretical Explanations:** Every algorithm page breaks down the intuition, required gates, and mathematical state evolution step-by-step.
- **Executable Code:** Fully tested Qiskit code implementations for every algorithm, dynamically synced from a master Jupyter Notebook.
- **Visual Aids:** Automatically generated circuit schematics, Bloch spheres, Q-Spheres, and histogram visualizations for state evolution and measurement analysis.
- **Downloadable Notebooks:** Users can download a single master catalogue (`.ipynb`) containing all algorithms, or download specific notebooks for individual algorithms directly from their respective pages.

## Algorithm Catalogue

The algorithms are categorized into five primary educational pillars:

1. **Foundations & Protocols**
   - Bell State Generator
   - Superdense Coding
   - Quantum Teleportation
   - Entanglement Swapping
2. **Oracle-Based Algorithms**
   - Deutsch's Algorithm
   - Deutsch–Jozsa Algorithm
   - Bernstein–Vazirani Algorithm
   - Simon's Algorithm
3. **Phase & Amplitude Algorithms**
   - Quantum Fourier Transform (QFT)
   - Quantum Phase Estimation (QPE)
   - Grover's Search Algorithm
   - Generalized Amplitude Amplification
4. **Flagship & Hybrid Algorithms**
   - Shor's Algorithm
   - Variational Quantum Eigensolver (VQE)
   - Quantum Approximate Optimization Algorithm (QAOA)
   - HHL Algorithm
5. **Fault Tolerance & Error Correction**
   - 3-Qubit Bit-Flip / Phase-Flip Codes
   - Shor's 9-Qubit Code
   - Steane 7-Qubit Code

## Repository Structure

The project uses a hybrid architecture. The frontend is built strictly with HTML5, Vanilla CSS3, and Vanilla JS, while the backend relies on a master Jupyter Notebook (`AQAC.ipynb`) as the source of truth for all quantum code and output data.

- `AQAC.ipynb`: The master Jupyter notebook containing all algorithm implementations, text outputs, LaTeX equations, and generated plot images.
- `update_master.py`: A synchronization script that parses `AQAC.ipynb`, extracts the code and cell outputs, generates individual `.ipynb` files for each algorithm, and injects the updated HTML into the frontend pages.
- `algorithms/`: Contains individual algorithm HTML pages.
- `assets/`: Contains generated output images (`assets/images/outputs`), generated circuit schematics (`assets/images/circuits`), and downloadable notebooks (`assets/notebooks`).
- `css/`: Stylesheets (`style.css` for globals, `responsive.css` for layouts).
- `js/`: Vanilla JS for UI interactions (navigation, layout, and output modal rendering).

## How to Run & Update

### Viewing the Site
This is a fully static frontend. Simply clone the repository and open `index.html` in any modern web browser to navigate the portal. No local server is strictly required.

### Updating Algorithm Code
If you want to modify the quantum circuits, tweak the Python code, or change the algorithm outputs:

1. Open `AQAC.ipynb` using Jupyter Notebook or JupyterLab.
2. Edit the Python code block for the desired algorithm and run the cell to generate the new output.
3. Save the notebook.
4. Run the master sync script from the root of the project to inject your changes into the website:
   ```bash
   python3 update_master.py
   ```
5. Refresh the HTML page in your browser. The code block, the "View Code Output" modal, the circuit images, and the downloadable `.ipynb` file will all be automatically updated.

## Technologies Used

- **Frontend:** HTML5, CSS3, Vanilla JS
- **Quantum Backend:** Python 3, Qiskit, Qiskit-Aer
- **Notebook Processing:** Jupyter format parsing, Regex, Base64 decoding
