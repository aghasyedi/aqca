import os

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | AQCA</title>
    <meta name="description" content="{description}">
    
    <!-- CSS -->
    <link rel="stylesheet" href="{root_path}css/style.css">
    <link rel="stylesheet" href="{root_path}css/responsive.css">
    {extra_css}
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Menlo&display=swap" rel="stylesheet">
    
    <!-- MathJax for LaTeX rendering -->
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

    <!-- Favicon -->
    <link rel="icon" type="image/png" href="{root_path}assets/icons/icon.png">
</head>
<body>
    <header class="site-header">
        <div class="header-left">
            <img src="{root_path}assets/logos/logo.png" alt="AQCA Logo" class="header-logo">
            <div class="site-title">
                <h1>AQCA</h1>
                <span class="subtitle">All Quantum Computing Algorithms</span>
            </div>
        </div>
        
        <div class="header-right">
            <img src="{root_path}assets/icons/icon.png" alt="Institute Logo" class="header-logo">
            <button id="mobile-menu-toggle" class="menu-toggle" aria-label="Toggle navigation">☰</button>
        </div>
    </header>

    <div class="layout-wrapper">
        <aside class="sidebar" id="sidebar">
            <nav class="nav-menu">
                <div class="nav-item">
                    <a href="{root_path}index.html" class="nav-link"><span class="step-num" style="background: var(--primary); color:#ffffff;">✦</span>Home</a>
                </div>
                <div class="nav-item">
                    <a href="{root_path}preface.html" class="nav-link">Preface</a>
                </div>
                <div class="nav-item">
                    <a href="{root_path}basics.html" class="nav-link">Quantum Computing Basics</a>
                </div>
                <div class="nav-item">
                    <a href="{root_path}appendix.html" class="nav-link">Appendix</a>
                </div>
                
                <div class="nav-item">
                    <button class="nav-group-toggle" aria-expanded="{algorithms_expanded}">
                        <span>Algorithms</span>
                        <span class="nav-group-icon">▼</span>
                    </button>
                    <ul class="nav-subgroup">
                        <li><a href="{root_path}algorithms.html" class="nav-link">Algorithm Catalogue</a></li>
                        
                        <li class="nav-category-label">1. Quantum Communication</li>
                        <li><a href="{root_path}algorithms/foundations/bell-state.html" class="nav-link">• Bell State Generator</a></li>
                        <li><a href="{root_path}algorithms/foundations/superdense-coding.html" class="nav-link">• Superdense Coding</a></li>
                        <li><a href="{root_path}algorithms/foundations/quantum-teleportation.html" class="nav-link">• Quantum Teleportation</a></li>
                        <li><a href="{root_path}algorithms/foundations/entanglement-swapping.html" class="nav-link">• Entanglement Swapping</a></li>
                        
                        <li class="nav-category-label">2. Early Oracle Algorithms</li>
                        <li><a href="{root_path}algorithms/oracle-based/deutsch.html" class="nav-link">• Deutsch's Algorithm</a></li>
                        <li><a href="{root_path}algorithms/oracle-based/deutsch-jozsa.html" class="nav-link">• Deutsch–Jozsa</a></li>
                        <li><a href="{root_path}algorithms/oracle-based/bernstein-vazirani.html" class="nav-link">• Bernstein–Vazirani</a></li>
                        <li><a href="{root_path}algorithms/oracle-based/simon.html" class="nav-link">• Simon's Algorithm</a></li>
                        
                        <li class="nav-category-label">3. Core Algorithms</li>
                        <li><a href="{root_path}algorithms/phase-amplitude/qft.html" class="nav-link">• Quantum Fourier Transform</a></li>
                        <li><a href="{root_path}algorithms/phase-amplitude/qpe.html" class="nav-link">• Quantum Phase Estimation</a></li>
                        <li><a href="{root_path}algorithms/phase-amplitude/grover.html" class="nav-link">• Grover's Search</a></li>
                        <li><a href="{root_path}algorithms/phase-amplitude/amplitude-amplification.html" class="nav-link">• Amplitude Amplification</a></li>
                        
                        <li class="nav-category-label">4. Top-End Algorithms</li>
                        <li><a href="{root_path}algorithms/flagship-hybrid/shor.html" class="nav-link">• Shor's Algorithm</a></li>
                        <li><a href="{root_path}algorithms/flagship-hybrid/vqe.html" class="nav-link">• Variational Quantum Eigensolver</a></li>
                        <li><a href="{root_path}algorithms/flagship-hybrid/qaoa.html" class="nav-link">• QAOA</a></li>
                        <li><a href="{root_path}algorithms/flagship-hybrid/hhl.html" class="nav-link">• HHL Algorithm</a></li>
                        
                        <li class="nav-category-label">5. Quantum Error Correction</li>
                        <li><a href="{root_path}algorithms/fault-tolerance/3-qubit-code.html" class="nav-link">• 3-Qubit Code</a></li>
                        <li><a href="{root_path}algorithms/fault-tolerance/shors-9-qubit-code.html" class="nav-link">• Shor's 9-Qubit Code</a></li>
                        <li><a href="{root_path}algorithms/fault-tolerance/steane-code.html" class="nav-link">• Steane 7-Qubit Code</a></li>
                    </ul>
                </div>
                
                <div class="nav-item">
                    <a href="{root_path}resources.html" class="nav-link">Visual Tools</a>
                </div>
                <div class="nav-item">
                    <a href="{root_path}resources.html" class="nav-link">Learning Resources</a>
                </div>
                <div class="nav-item">
                    <a href="{root_path}references.html" class="nav-link">References</a>
                </div>
                <div class="nav-item">
                    <a href="{root_path}developer.html" class="nav-link">Developer / Contact</a>
                </div>
                <div class="nav-item">
                    <a href="{root_path}preface.html" class="nav-link">About AQCA</a>
                </div>
            </nav>
        </aside>

        <main id="main-content" class="main-content">
            {content}
        </main>
    </div>

    <footer class="site-footer">
        <div class="footer-content" style="justify-content: center;">
            <div>
                &copy; 2026 AQCA - All Quantum Computing Algorithms
            </div>
        </div>
    </footer>

    <!-- JS -->
    <script src="{root_path}js/main.js"></script>
    <script src="{root_path}js/navigation.js"></script>
    {extra_js}
</body>
</html>
"""

def generate_global_page(filename, title, content):
    with open(f"/Users/aghatasheersyedi/Desktop/latex/class/qiskit/aqca/{filename}", 'w') as f:
        html = HTML_TEMPLATE.format(
            title=title,
            description=f"AQCA - {title}",
            root_path="",
            extra_css="",
            extra_js="",
            algorithms_expanded="false",
            content=content
        )
        f.write(html)

def generate_algorithm_page(category, filename, title, category_name):
    content = f"""
    <div class="breadcrumb">
        <a href="../../index.html">Home</a> <span class="breadcrumb-separator">›</span> 
        <a href="../../algorithms.html">Algorithms</a> <span class="breadcrumb-separator">›</span> 
        {category_name} <span class="breadcrumb-separator">›</span> 
        {title}
    </div>

    <div class="algorithm-header">
        <h1>{title}</h1>
        <div class="algorithm-meta">
            <span class="badge badge-category">{category_name}</span>
        </div>
    </div>

    <section class="content-section">
        <h2>1. Overview & Problem Definition</h2>
        <p>A high-level explanation of the problem {title} aims to solve.</p>
        <div class="complexity-comparison" style="margin-top: 1.5rem;">
            <div class="complexity-box">
                <h3>Classical Complexity</h3>
                <div class="complexity-value">O(?)</div>
            </div>
            <div class="complexity-box">
                <h3>Quantum Speedup</h3>
                <div class="complexity-value">O(?)</div>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>2. Intuition</h2>
        <p>The core conceptual idea behind the algorithm, explained without heavy mathematics.</p>
    </section>

    <section class="content-section">
        <h2>3. Required Gates & Circuit Schematic</h2>
        <p>The specific quantum gates required to build this circuit.</p>
        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="10" rx="2" ry="2"></rect><line x1="12" y1="3" x2="12" y2="7"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg></div>
            <h3>Circuit Visualisation</h3>
            <p>Interactive or static rendering of the quantum circuit.</p>
        </div>
    </section>

    <section class="content-section">
        <h2>4. Mathematical Proof & State Evolution</h2>
        <p>Rigorous step-by-step derivation tracking the exact state vector \\(|\\psi\\rangle\\) after every gate application.</p>
        <div class="math-container">
            <p>\\(|\\psi_0\\rangle = ...\\)</p>
            <p>\\(|\\psi_1\\rangle = ...\\)</p>
        </div>
        <h3 style="margin-top: 1.5rem;">Measurement</h3>
        <p>Explanation of the measurement basis and expected probability distribution.</p>
    </section>

    <section class="content-section">
        <h2>5. Interactive Visualisation</h2>
        <div class="simulation-placeholder">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg></div>
            <h3>Dynamic State Tracking</h3>
            <p>Interactive module (amplitude histograms, Bloch spheres) to simulate the algorithm live.</p>
        </div>
    </section>

    <section class="content-section">
        <h2>6. Python Code Implementation</h2>
        
        <h3>From Scratch (NumPy)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / NumPy</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre>
# NumPy implementation placeholder
import numpy as np

def simulate_{filename.replace('.html', '')}():
    pass
</pre>
            </div>
        </div>
        
        <h3 style="margin-top: 1.5rem;">Framework (Qiskit)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / Qiskit</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre>
# Qiskit implementation placeholder
from qiskit import QuantumCircuit

def create_circuit():
    qc = QuantumCircuit(2)
    return qc
</pre>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>7. Caveats & Real-World Limits</h2>
        <p>Assumptions (e.g. perfect oracles), hardware connectivity requirements, and noise limitations on NISQ devices.</p>
    </section>

    <section class="content-section">
        <h2>8. Applications</h2>
        <p>Where this algorithm is used in modern quantum computing.</p>
    </section>
    
    <section class="content-section">
        <h2>9. References</h2>
        <ul>
            <li>Primary academic sources and textbooks.</li>
        </ul>
    </section>

    <nav class="algorithm-nav">
        <a href="#" class="nav-button">
            <span class="nav-label">Previous</span>
            <span class="nav-title">Algorithm Title</span>
        </a>
        <a href="#" class="nav-button nav-next">
            <span class="nav-label">Next</span>
            <span class="nav-title">Algorithm Title</span>
        </a>
    </nav>
    """.replace("{title}", title).replace("{category_name}", category_name)
    
    with open(f"/Users/aghatasheersyedi/Desktop/latex/class/qiskit/aqca/algorithms/{category}/{filename}", 'w') as f:
        html = HTML_TEMPLATE.format(
            title=title,
            description=f"AQCA - {title}",
            root_path="../../",
            extra_css="",
            extra_js="",
            algorithms_expanded="true",
            content=content
        )
        f.write(html)

generate_global_page("index.html", "Home", """
    <div class="hero-section">
        <div class="hero-content">
            <h2 class="hero-title">Welcome to AQCA</h2>
            <div class="hero-subtitle">All Quantum Computing Algorithms</div>
            <p class="hero-desc">
                AQCA is an interactive educational platform that visualizes and simulates quantum algorithms, protocols, and error correction codes. Explore the quantum world step-by-step — from the fundamentals to the most advanced algorithms.
            </p>
            <div class="hero-actions">
                <a href="algorithms.html" class="btn"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 8px;"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg> Explore Algorithms</a>
                <a href="preface.html" class="btn btn-outline"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 8px;"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg> How to Use AQCA</a>
            </div>
        </div>
        <div class="hero-diagram">
            <span>[ Bloch Sphere / Circuit Image Placeholder ]</span>
        </div>
    </div>
    
    <h3 class="section-title"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg> Algorithm Categories</h3>
    
    <div class="categories-grid">
        <div class="category-card">
            <div class="category-icon"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></div>
            <h4 class="category-title">1. Quantum Communication</h4>
            <div class="category-count">4 Protocols</div>
            <p class="category-desc">Explore foundational communication protocols that leverage entanglement and quantum information.</p>
        </div>
        
        <div class="category-card">
            <div class="category-icon"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></div>
            <h4 class="category-title">2. Early Oracle Algorithms</h4>
            <div class="category-count">4 Algorithms</div>
            <p class="category-desc">The first quantum algorithms that demonstrate quantum advantage using oracles and interference.</p>
        </div>
        
        <div class="category-card">
            <div class="category-icon"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg></div>
            <h4 class="category-title">3. Core Algorithms</h4>
            <div class="category-count">4 Algorithms</div>
            <p class="category-desc">Algorithms that harness phase manipulation and amplitude amplification for powerful computation.</p>
        </div>
        
        <div class="category-card">
            <div class="category-icon"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></div>
            <h4 class="category-title">4. Top-End Algorithms</h4>
            <div class="category-count">4 Algorithms</div>
            <p class="category-desc">Advanced algorithms for factoring, optimization, and solving real-world quantum problems.</p>
        </div>
        
        <div class="category-card">
            <div class="category-icon"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>
            <h4 class="category-title">5. Quantum Error Correction</h4>
            <div class="category-count">3 Codes</div>
            <p class="category-desc">Protect quantum information against noise and errors using quantum error correction codes.</p>
        </div>
    </div>
    
    <div class="features-grid">
        <div class="feature-item">
            <div class="feature-header">
                <span class="feature-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg></span>
                <h4 class="feature-title">Interactive Visualizations</h4>
            </div>
            <p class="feature-desc">Step-by-step circuit execution, state evolution, and probability visualizations.</p>
        </div>
        
        <div class="feature-item">
            <div class="feature-header">
                <span class="feature-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="9" x2="20" y2="9"></line><line x1="4" y1="15" x2="20" y2="15"></line><line x1="10" y1="3" x2="8" y2="21"></line><line x1="16" y1="3" x2="14" y2="21"></line></svg></span>
                <h4 class="feature-title">Mathematical Insights</h4>
            </div>
            <p class="feature-desc">Dirac notation, state vectors, and mathematical explanations at every step.</p>
        </div>
        
        <div class="feature-item">
            <div class="feature-header">
                <span class="feature-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg></span>
                <h4 class="feature-title">Noise & Realism</h4>
            </div>
            <p class="feature-desc">Simulate noise, decoherence, and error correction in quantum systems.</p>
        </div>
        
        <div class="feature-item">
            <div class="feature-header">
                <span class="feature-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg></span>
                <h4 class="feature-title">Learn by Doing</h4>
            </div>
            <p class="feature-desc">Adjust parameters, run simulations, and see quantum phenomena in action.</p>
        </div>
    </div>
    
    <div style="margin-top: 3rem; padding: 1.25rem 1.5rem; background: var(--primary-light); border-radius: 6px; border-left: 4px solid var(--primary); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
        <div>
            <h4 style="margin: 0 0 0.25rem 0; color: var(--primary); font-family: var(--font-serif); font-size: 1.1rem;">Explore the BB84 Protocol</h4>
            <p style="margin: 0; font-size: 0.9rem;">I have also created a dedicated BB84 Simulator, an interactive visualizer for the foundational quantum communication protocol.</p>
        </div>
        <a href="https://bb84qkd.netlify.app/go.html" target="_blank" rel="noopener noreferrer" class="btn" style="padding: 0.4rem 1rem; font-size: 0.85rem; white-space: nowrap;">Launch Simulator <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-left: 6px;"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg></a>
    </div>
""")

generate_global_page("preface.html", "Preface & Setup", """
    <div class="page-header">
        <h1>Preface & Setup</h1>
    </div>
    <section class="content-section">
        <h2>Motivation</h2>
        <p>Quantum computing is frequently taught in two disconnected extremes: either as purely abstract linear algebra on a chalkboard, or as black-box function calls using software libraries where the underlying mechanics are hidden. When studying advanced quantum technology, navigating the space between these two extremes can be frustrating.</p>
        <p>AQCA (All Quantum Computing Algorithms) was born out of a desire to build a definitive, explorable atlas that bridges this gap. An atlas does not merely list locations; it maps the terrain. Similarly, AQCA maps the landscape of quantum computation—from the foundational principles of entanglement and teleportation to modern hybrid algorithms and error correction. The primary motivation is to strip away the opacity of quantum circuits, transforming them from static diagrams into dynamic, interactive systems where the evolution of every state vector is fully visible and mathematically rigorously defined.</p>

        <h2 style="margin-top: 2rem;">Educational Philosophy</h2>
        <p>The core philosophy of AQCA is that quantum algorithms cannot be truly understood by simply looking at a final circuit diagram. True comprehension requires tracking the journey from classical intuition to quantum implementation.</p>
        <p>To achieve this, every algorithm in AQCA follows a structured, multi-layered learning pipeline:</p>
        <ul style="line-height: 1.6;">
            <li><strong>The Core Problem &amp; Classical Intuition:</strong> We begin by defining the mathematical or computational problem. Before introducing quantum mechanics, we establish the classical limits (e.g., time complexity and oracle queries) to clearly highlight why a quantum approach is advantageous.</li>
            <li><strong>The Quantum Idea:</strong> We translate the classical problem into quantum terms, focusing on the specific mechanics—such as phase kickback, amplitude amplification, or quantum Fourier transforms—that generate the quantum speed-up.</li>
            <li><strong>Rigorous Mathematics:</strong> Every algorithm is broken down step-by-step using standard Dirac notation. The mathematical proofs show exactly how the state vector evolves after every gate application.</li>
            <li><strong>Interactive Visualisation:</strong> Mathematics can be abstract, so AQCA prioritises visual learning. Through interactive circuits, Bloch spheres, Q-spheres, and amplitude histograms, users can literally watch the probabilities and phases shift in real-time.</li>
            <li><strong>Dual-Track Implementation:</strong> Understanding theory is only half the battle. AQCA provides code implementations in two forms:
                <ul style="margin-top: 0.5rem; margin-bottom: 0.5rem;">
                    <li><em>From Scratch:</em> Using pure Python and NumPy matrix operations to prove an understanding of the fundamental mechanics without relying on external libraries.</li>
                    <li><em>Industry Standard:</em> Production-ready circuits built and transpiled using Qiskit.</li>
                </ul>
            </li>
        </ul>
        <p>By walking through this pipeline, AQCA ensures that you do not just learn how to run an algorithm, but that you fully conceptualise how and why it works.</p>
    </section>
    
    <section class="content-section">
        <h2>AQCA Environment Setup: Installing Qiskit</h2>
        <p>To run the AQCA algorithms, you need to set up a Python virtual environment and install Qiskit along with its visualization and scientific computing dependencies.</p>
        
        <h3>Step 1: Create a Virtual Environment</h3>
        <p>It is highly recommended to install Qiskit in an isolated virtual environment to avoid conflicts. Open your terminal (or Command Prompt/PowerShell) and navigate to your AQCA project folder. Run the following command:</p>
        
        <h4>On Windows:</h4>
        <pre><code>python -m venv .venv</code></pre>
        
        <h4>On macOS / Linux:</h4>
        <pre><code>python3 -m venv .venv</code></pre>

        <h3>Step 2: Activate the Environment</h3>
        <p>Before installing anything, you must activate the environment.</p>
        
        <h4>On Windows:</h4>
        <pre><code>.venv\\Scripts\\activate</code></pre>
        
        <h4>On macOS / Linux:</h4>
        <pre><code>source .venv/bin/activate</code></pre>
        <p><em>(You will know it is active when you see <code>(.venv)</code> at the beginning of your terminal prompt).</em></p>

        <h3>Step 3: Install Core Qiskit & The Aer Simulator</h3>
        <p>Qiskit and its high-performance simulator (<code>qiskit-aer</code>) are now packaged separately. Install them using pip:</p>
        <pre><code>pip install qiskit qiskit-aer</code></pre>

        <h3>Step 4: Install Visualization & Scientific Libraries</h3>
        <p>Your code snippets rely on advanced visualisations (<code>output="mpl"</code>, Bloch spheres, Q-spheres) and LaTeX rendering for state vectors. You also need Jupyter to run interactive notebooks. Install these dependencies:</p>
        <pre><code>pip install matplotlib pylatexenc seaborn jupyter ipython numpy</code></pre>
        <ul>
            <li><strong><code>matplotlib</code> &amp; <code>pylatexenc</code></strong>: Required for <code>qc.draw(output="mpl")</code> and LaTeX statevector rendering.</li>
            <li><strong><code>numpy</code> &amp; <code>seaborn</code></strong>: Required for matrix maths, pi calculations, and custom data plotting.</li>
            <li><strong><code>jupyter</code> &amp; <code>ipython</code></strong>: Required for <code>display()</code> and <code>Math()</code> functions and running notebook files.</li>
        </ul>

        <h3>Step 5: Setting up <code>state_decompose.py</code></h3>
        <p>In your scripts, you use the following import:</p>
        <pre><code>from state_decompose import find_components</code></pre>
        <p><strong>Note:</strong> This is <em>not</em> a standard Python package you can install via pip. This implies <code>state_decompose.py</code> is a custom file you (or a collaborator) wrote.</p>
        <p><strong>Action Required:</strong> Ensure that the <code>state_decompose.py</code> file is saved in the <strong>exact same directory</strong> as your main AQCA scripts/notebooks, otherwise Python will throw a <code>ModuleNotFoundError</code>.</p>

        <h3>Step 6: Verify the Installation</h3>
        <p>To ensure everything is working, open a new Jupyter Notebook (<code>jupyter notebook</code>) or Python file in your project directory and run this test block:</p>
<pre><code>import qiskit
import qiskit_aer
import pylatexenc
print(f"Qiskit version: {qiskit.__version__}")
print(f"Aer version: {qiskit_aer.__version__}")
print("Installation Successful!")</code></pre>
    </section>
""")

generate_global_page("basics.html", "Quantum Computing Basics", r"""
    <div class="page-header" style="display: flex; flex-direction: column; align-items: flex-start;">
        <h1 style="margin-bottom: 0.5rem;">Quantum Computing Basics</h1>
        <p style="color: var(--muted-text); margin-top: 0;">The foundational mathematics and physical principles of quantum information.</p>
        <div style="display: flex; gap: 1rem; align-items: center; margin-top: 1rem; margin-bottom: 3rem; flex-wrap: wrap; width: 100%;">
            <a href="#quantum-gates" id="jumpBtn" class="btn" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.4rem 1rem; font-size: 0.85rem; width: fit-content; text-decoration: none; height: fit-content; margin-top: 0;">
                Jump to Quantum Gates List
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><polyline points="19 12 12 19 5 12"></polyline></svg>
            </a>
            <input type="text" id="basicsSearch" placeholder="Search in page..." class="search-input" style="margin-bottom: 0; max-width: 300px; padding: 0.5rem 1rem; font-size: 0.9rem;">
        </div>
    </div>
    
    <details class="content-section basics-accordion" name="basics-accordion">
        <summary class="basics-summary" style="cursor: pointer; list-style: none; outline: none; margin-bottom: 1rem; display: flex; align-items: center; justify-content: space-between;">
            <h2>1. Dirac Notation & State Vectors</h2>
            <svg class="accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: transform 0.2s;"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </summary>
        <div class="basics-content">
<p>In quantum mechanics, the state of a system is represented by a vector in a complex Hilbert space. To simplify the mathematics, Paul Dirac introduced the <strong>Bra-Ket</strong> notation.</p>
        <ul style="line-height: 1.6;">
            <li><strong>Ket \(|\psi\rangle\)</strong>: <a href="appendix.html" style="font-size: 0.8rem; margin-left: 0.8rem; color: var(--primary); font-weight: 500; text-decoration: none; padding: 0.2rem 0.5rem; border-radius: 4px; background-color: var(--primary-light); display: inline-block; vertical-align: middle;">[click for more]</a> Represents a column vector describing a quantum state. For example, the computational basis states are \(|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}\) and \(|1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}\).</li>
            <li><strong>Bra \(\langle\psi|\)</strong>: <a href="appendix.html" style="font-size: 0.8rem; margin-left: 0.8rem; color: var(--primary); font-weight: 500; text-decoration: none; padding: 0.2rem 0.5rem; border-radius: 4px; background-color: var(--primary-light); display: inline-block; vertical-align: middle;">[click for more]</a> Represents a row vector, which is the complex conjugate transpose (Hermitian conjugate) of the ket. \(\langle\psi| = (|\psi\rangle)^\dagger\).</li>
            <li><strong>Inner Product (Bracket) \(\langle\phi|\psi\rangle\)</strong>: <a href="appendix.html" style="font-size: 0.8rem; margin-left: 0.8rem; color: var(--primary); font-weight: 500; text-decoration: none; padding: 0.2rem 0.5rem; border-radius: 4px; background-color: var(--primary-light); display: inline-block; vertical-align: middle;">[click for more]</a> Yields a scalar complex number. It represents the probability amplitude of state \(|\psi\rangle\) collapsing into state \(|\phi\rangle\). Orthogonal states have an inner product of 0 (e.g., \(\langle 0 | 1 \rangle = 0\)).</li>
            <li><strong>Tensor Product \(|\psi\rangle \otimes |\phi\rangle\) or \(|\psi\phi\rangle\)</strong>: <a href="appendix.html" style="font-size: 0.8rem; margin-left: 0.8rem; color: var(--primary); font-weight: 500; text-decoration: none; padding: 0.2rem 0.5rem; border-radius: 4px; background-color: var(--primary-light); display: inline-block; vertical-align: middle;">[click for more]</a> Used to describe multi-qubit systems. Two independent qubits combine their state spaces multiplicatively.</li>
        </ul>        </div>
    </details>

    <details class="content-section basics-accordion" name="basics-accordion">
        <summary class="basics-summary" style="cursor: pointer; list-style: none; outline: none; margin-bottom: 1rem; display: flex; align-items: center; justify-content: space-between;">
            <h2>2. Superposition & Entanglement</h2>
            <svg class="accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: transform 0.2s;"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </summary>
        <div class="basics-content">
<h3 style="margin-top: 1.5rem;">Superposition <a href="appendix.html" style="font-size: 0.8rem; margin-left: 0.8rem; color: var(--primary); font-weight: 500; text-decoration: none; padding: 0.2rem 0.5rem; border-radius: 4px; background-color: var(--primary-light); display: inline-block; vertical-align: middle;">[click for more]</a></h3>
        <p>Unlike classical bits that exist strictly as 0 or 1, a quantum bit (qubit) can exist in a linear combination of both states simultaneously until measured. This is expressed as:</p>
        <p style="text-align: center; font-size: 1.2rem; margin: 1.5rem 0;">\(|\psi\rangle = \alpha|0\rangle + \beta|1\rangle\)</p>
        <p>Here, \(\alpha\) and \(\beta\) are complex numbers known as probability amplitudes. The Born rule states that the probability of measuring \(|0\rangle\) is \(|\alpha|^2\) and measuring \(|1\rangle\) is \(|\beta|^2\). Due to the conservation of probability, they must satisfy the normalization condition: <strong>\(|\alpha|^2 + |\beta|^2 = 1\)</strong>.</p>
        
        <h3 style="margin-top: 2rem;">Entanglement <a href="appendix.html" style="font-size: 0.8rem; margin-left: 0.8rem; color: var(--primary); font-weight: 500; text-decoration: none; padding: 0.2rem 0.5rem; border-radius: 4px; background-color: var(--primary-light); display: inline-block; vertical-align: middle;">[click for more]</a></h3>
        <p>Entanglement is a purely quantum phenomenon where two or more qubits become perfectly correlated such that the state of one qubit cannot be described independently of the state of the others, no matter the physical distance between them. A classic example is the Bell state:</p>
        <p style="text-align: center; font-size: 1.2rem; margin: 1.5rem 0;">\(|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}\)</p>
        <p>Measuring the first qubit immediately determines the state of the second qubit. Entanglement is the primary resource for quantum communication (like Superdense Coding and Quantum Teleportation) and exponential computational speedups.</p>        </div>
    </details>

    <details class="content-section basics-accordion" name="basics-accordion">
        <summary class="basics-summary" style="cursor: pointer; list-style: none; outline: none; margin-bottom: 1rem; display: flex; align-items: center; justify-content: space-between;">
            <h2>3. Density Matrices & Mixed States</h2>
            <svg class="accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: transform 0.2s;"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </summary>
        <div class="basics-content">
<p>While state vectors (\(|\psi\rangle\)) perfectly describe <strong>pure states</strong> (systems fully isolated from their environment), understanding noisy quantum systems, thermal states, partial measurements, and decoherence requires the density matrix framework.</p>
        
        <h3 style="margin-top: 1.5rem;">Pure vs. Mixed States <a href="appendix.html" style="font-size: 0.8rem; margin-left: 0.8rem; color: var(--primary); font-weight: 500; text-decoration: none; padding: 0.2rem 0.5rem; border-radius: 4px; background-color: var(--primary-light); display: inline-block; vertical-align: middle;">[click for more]</a></h3>
        <ul style="line-height: 1.6;">
            <li><strong>Pure State:</strong> A system whose quantum state is fully known, represented by a single vector \(|\psi\rangle\). Its density matrix is defined as: <br><span style="display:block; text-align:center; font-size: 1.2rem; margin: 1rem 0;">\(\rho = |\psi\rangle\langle\psi|\)</span></li>
            <li><strong>Mixed State:</strong> A statistical ensemble of pure states \(|\psi_i\rangle\), each occurring with classical probability \(p_i\): <br><span style="display:block; text-align:center; font-size: 1.2rem; margin: 1rem 0;">\(\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|, \quad \text{where } \sum_i p_i = 1\)</span></li>
        </ul>

        <h3 style="margin-top: 1.5rem;">Key Properties <a href="appendix.html" style="font-size: 0.8rem; margin-left: 0.8rem; color: var(--primary); font-weight: 500; text-decoration: none; padding: 0.2rem 0.5rem; border-radius: 4px; background-color: var(--primary-light); display: inline-block; vertical-align: middle;">[click for more]</a></h3>
        <ul style="line-height: 1.6;">
            <li><strong>Trace Normalisation:</strong> \(\text{Tr}(\rho) = 1\) (preserves total probability).</li>
            <li><strong>Purity Test:</strong>
                <ul>
                    <li>For a pure state: \(\text{Tr}(\rho^2) = 1\)</li>
                    <li>For a mixed state: \(\text{Tr}(\rho^2) < 1\)</li>
                </ul>
            </li>
            <li><strong>Partial Trace:</strong> Used to extract the reduced density matrix \(\rho_A = \text{Tr}_B(\rho_{AB})\) of a sub-system A that is entangled with sub-system B.</li>
        </ul>        </div>
    </details>

    <details class="content-section basics-accordion" id="quantum-gates" name="basics-accordion">
        <summary class="basics-summary" style="cursor: pointer; list-style: none; outline: none; margin-bottom: 1rem; display: flex; align-items: center; justify-content: space-between;">
            <h2>4. Quantum Gates Reference</h2>
            <svg class="accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: transform 0.2s;"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </summary>
        <div class="basics-content">
<h3 style="margin-top: 1.5rem;">A. Single-Qubit Gates <a href="appendix.html" style="font-size: 0.8rem; margin-left: 0.8rem; color: var(--primary); font-weight: 500; text-decoration: none; padding: 0.2rem 0.5rem; border-radius: 4px; background-color: var(--primary-light); display: inline-block; vertical-align: middle;">[click for more]</a></h3>
        <table>
            <thead>
                <tr>
                    <th>Gate</th>
                    <th>Symbol / Matrix</th>
                    <th>Main Purpose</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Identity</td>
                    <td>\(I = \begin{bmatrix}1 & 0 \\ 0 & 1\end{bmatrix}\)</td>
                    <td>Does nothing</td>
                </tr>
                <tr>
                    <td>Pauli-X</td>
                    <td>\(X = \begin{bmatrix}0 & 1 \\ 1 & 0\end{bmatrix}\)</td>
                    <td>Quantum NOT / bit flip</td>
                </tr>
                <tr>
                    <td>Pauli-Y</td>
                    <td>\(Y = \begin{bmatrix}0 & -i \\ i & 0\end{bmatrix}\)</td>
                    <td>Bit + phase flip</td>
                </tr>
                <tr>
                    <td>Pauli-Z</td>
                    <td>\(Z = \begin{bmatrix}1 & 0 \\ 0 & -1\end{bmatrix}\)</td>
                    <td>Phase flip</td>
                </tr>
                <tr>
                    <td>Hadamard</td>
                    <td>\(H = \frac{1}{\sqrt{2}\begin{bmatrix}1 & 1 \\ 1 & -1\end{bmatrix}\)</td>
                    <td>Creates/removes superposition</td>
                </tr>
                <tr>
                    <td>Phase</td>
                    <td>\(S = \begin{bmatrix}1 & 0 \\ 0 & i\end{bmatrix}\)</td>
                    <td>\(90^\circ\) phase rotation</td>
                </tr>
                <tr>
                    <td>S-dagger</td>
                    <td>\(S^\dagger = \begin{bmatrix}1 & 0 \\ 0 & -i\end{bmatrix}\)</td>
                    <td>Inverse of \(S\)</td>
                </tr>
                <tr>
                    <td>T</td>
                    <td>\(T = \begin{bmatrix}1 & 0 \\ 0 & e^{i\pi/4}\end{bmatrix}\)</td>
                    <td>\(45^\circ\) phase rotation</td>
                </tr>
                <tr>
                    <td>T-dagger</td>
                    <td>\(T^\dagger = \begin{bmatrix}1 & 0 \\ 0 & e^{-i\pi/4}\end{bmatrix}\)</td>
                    <td>Inverse of \(T\)</td>
                </tr>
                <tr>
                    <td>Phase gate</td>
                    <td>\(P(\phi) = \begin{bmatrix}1 & 0 \\ 0 & e^{i\phi}\end{bmatrix}\)</td>
                    <td>Arbitrary phase</td>
                </tr>
            </tbody>
        </table>

        <h3 style="margin-top: 2rem;">B. Rotation Gates <a href="appendix.html" style="font-size: 0.8rem; margin-left: 0.8rem; color: var(--primary); font-weight: 500; text-decoration: none; padding: 0.2rem 0.5rem; border-radius: 4px; background-color: var(--primary-light); display: inline-block; vertical-align: middle;">[click for more]</a></h3>
        <p>These are especially important for <strong>variational quantum circuits</strong> and hardware-level circuits.</p>
        <div style="display: flex; gap: 2rem; flex-wrap: wrap; margin-bottom: 1.5rem;">
            <div>
                <p style="text-align: center;">\(R_x(\theta) = \begin{bmatrix}\cos\frac{\theta}{2} & -i\sin\frac{\theta}{2} \\ -i\sin\frac{\theta}{2} & \cos\frac{\theta}{2}\end{bmatrix}\)</p>
            </div>
            <div>
                <p style="text-align: center;">\(R_y(\theta) = \begin{bmatrix}\cos\frac{\theta}{2} & -\sin\frac{\theta}{2} \\ \sin\frac{\theta}{2} & \cos\frac{\theta}{2}\end{bmatrix}\)</p>
            </div>
            <div>
                <p style="text-align: center;">\(R_z(\theta) = \begin{bmatrix}e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2}\end{bmatrix}\)</p>
            </div>
        </div>
        <p>Also common is the general single-qubit gate:</p>
        <p style="text-align: center; font-size: 1.2rem; margin-bottom: 2rem;">
            \(U(\theta, \phi, \lambda) = \begin{bmatrix}\cos(\theta/2) & -e^{i\lambda}\sin(\theta/2) \\ e^{i\phi}\sin(\theta/2) & e^{i(\phi+\lambda)}\cos(\theta/2)\end{bmatrix}\)
        </p>

        <h3 style="margin-top: 2rem;">C. Two-Qubit Gates <a href="appendix.html" style="font-size: 0.8rem; margin-left: 0.8rem; color: var(--primary); font-weight: 500; text-decoration: none; padding: 0.2rem 0.5rem; border-radius: 4px; background-color: var(--primary-light); display: inline-block; vertical-align: middle;">[click for more]</a></h3>
        <table>
            <thead>
                <tr>
                    <th>Gate</th>
                    <th>Common Name</th>
                    <th>Purpose</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>CX / CNOT</td>
                    <td>Controlled-X</td>
                    <td>Flip target if control is \(|1\rangle\)</td>
                </tr>
                <tr>
                    <td>CY</td>
                    <td>Controlled-Y</td>
                    <td>Apply \(Y\) conditionally</td>
                </tr>
                <tr>
                    <td>CZ</td>
                    <td>Controlled-Z</td>
                    <td>Apply phase flip conditionally</td>
                </tr>
                <tr>
                    <td>CH</td>
                    <td>Controlled-H</td>
                    <td>Apply Hadamard conditionally</td>
                </tr>
                <tr>
                    <td>CP</td>
                    <td>Controlled-Phase</td>
                    <td>Conditional phase</td>
                </tr>
                <tr>
                    <td>CRX</td>
                    <td>Controlled-\(R_x\)</td>
                    <td>Conditional X rotation</td>
                </tr>
                <tr>
                    <td>CRY</td>
                    <td>Controlled-\(R_y\)</td>
                    <td>Conditional Y rotation</td>
                </tr>
                <tr>
                    <td>CRZ</td>
                    <td>Controlled-\(R_z\)</td>
                    <td>Conditional Z rotation</td>
                </tr>
                <tr>
                    <td>SWAP</td>
                    <td>Swap</td>
                    <td>Exchange two qubit states</td>
                </tr>
                <tr>
                    <td>iSWAP</td>
                    <td>iSwap</td>
                    <td>Swap with an \(i\) phase</td>
                </tr>
                <tr>
                    <td>\(\sqrt{\text{SWAP}\)</td>
                    <td>Root-SWAP</td>
                    <td>Partial swap</td>
                </tr>
                <tr>
                    <td>RXX, RYY, RZZ</td>
                    <td>XX, YY, ZZ rotation</td>
                    <td>Two-qubit interaction</td>
                </tr>
            </tbody>
        </table>
        
        <p>The most important ones are <strong>CNOT</strong> and <strong>SWAP</strong>:</p>
        <div style="display: flex; gap: 2rem; flex-wrap: wrap; margin-bottom: 1.5rem;">
            <div>
                <p style="text-align: center;">\(CX = \begin{bmatrix}1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0\end{bmatrix}\)</p>
            </div>
            <div>
                <p style="text-align: center;">\(SWAP = \begin{bmatrix}1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1\end{bmatrix}\)</p>
            </div>
        </div>

        <h3 style="margin-top: 2rem;">D. Three-Qubit and Multi-Qubit Gates <a href="appendix.html" style="font-size: 0.8rem; margin-left: 0.8rem; color: var(--primary); font-weight: 500; text-decoration: none; padding: 0.2rem 0.5rem; border-radius: 4px; background-color: var(--primary-light); display: inline-block; vertical-align: middle;">[click for more]</a></h3>
        <table>
            <thead>
                <tr>
                    <th>Gate</th>
                    <th>Name</th>
                    <th>Operation</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>CCX</td>
                    <td>Toffoli</td>
                    <td>Controlled-controlled-X</td>
                </tr>
                <tr>
                    <td>CCZ</td>
                    <td>Controlled-controlled-Z</td>
                    <td>Conditional phase</td>
                </tr>
                <tr>
                    <td>CSWAP</td>
                    <td>Fredkin</td>
                    <td>Controlled SWAP</td>
                </tr>
                <tr>
                    <td>MCX</td>
                    <td>Multi-controlled X</td>
                    <td>X with several controls</td>
                </tr>
                <tr>
                    <td>MCZ</td>
                    <td>Multi-controlled Z</td>
                    <td>Z with several controls</td>
                </tr>
            </tbody>
        </table>
        <p><strong>Toffoli (CCX)</strong> is particularly important. If the controls are \(a,b\) and target is \(c\),</p>
        <p style="text-align: center; font-size: 1.2rem; margin-bottom: 2rem;">\(|a, b, c\rangle \rightarrow |a, b, c \oplus (a \land b)\rangle\)</p>

        <h3 style="margin-top: 2rem;">E. Important Families to Know <a href="appendix.html" style="font-size: 0.8rem; margin-left: 0.8rem; color: var(--primary); font-weight: 500; text-decoration: none; padding: 0.2rem 0.5rem; border-radius: 4px; background-color: var(--primary-light); display: inline-block; vertical-align: middle;">[click for more]</a></h3>
        <p>A useful way to organise the gates is:</p>
        <ul style="line-height: 1.6;">
            <li><strong>Pauli:</strong> \(I, X, Y, Z\)</li>
            <li><strong>Clifford:</strong> \(H, S, X, Y, Z, \text{CNOT}\)</li>
            <li><strong>Phase:</strong> \(Z, S, T, P(\phi)\)</li>
            <li><strong>Rotation:</strong> \(R_x, R_y, R_z\)</li>
            <li><strong>Controlled:</strong> \(CX, CY, CZ, CH, CP, CRX, CRY, CRZ\)</li>
            <li><strong>Exchange / Interaction:</strong> \(SWAP, iSWAP, \sqrt{SWAP}, RXX, RYY, RZZ\)</li>
            <li><strong>Multi-qubit:</strong> \(CCX, CCZ, CSWAP, MCX, MCZ\)</li>
        </ul>

        <h3 style="margin-top: 2rem;">The Gates You Should Definitely Memorise <a href="appendix.html" style="font-size: 0.8rem; margin-left: 0.8rem; color: var(--primary); font-weight: 500; text-decoration: none; padding: 0.2rem 0.5rem; border-radius: 4px; background-color: var(--primary-light); display: inline-block; vertical-align: middle;">[click for more]</a></h3>
        <p>For your quantum-computing work, prioritise:</p>
        <ol style="line-height: 1.6;">
            <li>\(\boxed{X, Y, Z, H, S, T}\)</li>
            <li>\(\boxed{R_x, R_y, R_z, P}\)</li>
            <li>\(\boxed{CX, CZ, SWAP}\)</li>
            <li>\(\boxed{CCX, CSWAP}\)</li>
        </ol>
        <p>A particularly important result is that <strong>Clifford + T</strong> forms a universal gate set, while arbitrary single-qubit gates together with an entangling two-qubit gate such as <strong>CNOT</strong> can also provide universal quantum computation.</p>
        
        <h3 style="margin-top: 2rem;">Reversibility & Uncomputing <a href="appendix.html" style="font-size: 0.8rem; margin-left: 0.8rem; color: var(--primary); font-weight: 500; text-decoration: none; padding: 0.2rem 0.5rem; border-radius: 4px; background-color: var(--primary-light); display: inline-block; vertical-align: middle;">[click for more]</a></h3>
        <p>Unlike classical computation where logic gates like AND/OR discard information, quantum operations must be strictly unitary and reversible (\(U^\dagger U = I\)).</p>
        <p>When algorithms use extra workspace qubits (ancilla qubits) to compute intermediate steps, these ancillas often remain entangled with the main register. Measuring or discarding them prematurely destroys the superposition of the primary computation. To prevent this, quantum circuits use a technique called <strong>uncomputing</strong>:</p>
        <ol style="line-height: 1.6;">
            <li>Compute the intermediate value onto an ancilla qubit.</li>
            <li>Copy the final target result into an output qubit using a CNOT gate.</li>
            <li>Apply the inverse operation (\(U^\dagger\)) to the ancilla qubit to return it to its pristine \(|0\rangle\) state, disentangling it from the system.</li>
        </ol>        </div>
    </details>

    <details class="content-section basics-accordion" name="basics-accordion">
        <summary class="basics-summary" style="cursor: pointer; list-style: none; outline: none; margin-bottom: 1rem; display: flex; align-items: center; justify-content: space-between;">
            <h2>5. The Bloch Sphere Representation</h2>
            <svg class="accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: transform 0.2s;"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </summary>
        <div class="basics-content">
<div style="display: flex; flex-wrap: wrap; gap: 2rem; align-items: center; margin-top: 1.5rem;">
            <div style="flex: 1; min-width: 300px;">
                <p>The <strong>Bloch Sphere</strong> is a geometric representation of the pure state space of a single qubit. Because a qubit's state is normalized and global phase is physically unobservable, the entire state space maps elegantly onto the surface of a 3D sphere of radius 1.</p>
                <p>A general qubit state is represented by two angles, \(\theta\) (polar) and \(\phi\) (azimuthal):</p>
                <p style="text-align: center; font-size: 1.2rem; margin: 1.5rem 0;">\(|\psi\rangle = \cos(\frac{\theta}{2})|0\rangle + e^{i\phi}\sin(\frac{\theta}{2})|1\rangle\)</p>
                <ul style="line-height: 1.6;">
                    <li><strong>Z-Axis (Poles)</strong>: The North pole represents \(|0\rangle\) (\(\theta = 0\)) and the South pole represents \(|1\rangle\) (\(\theta = \pi\)).</li>
                    <li><strong>X-Axis (Equator)</strong>: Represents the \(|+\rangle\) and \(|-\rangle\) states (equal superposition with 0 or \(\pi\) relative phase).</li>
                    <li><strong>Y-Axis (Equator)</strong>: Represents the \(|i\rangle\) and \(|-i\rangle\) states (imaginary phase).</li>
                </ul>
                <p>Quantum gates like \(X, Y, Z\) correspond to \(180^\circ\) rotations around their respective axes on this sphere!</p>
            </div>
            <div style="flex: 1; min-width: 300px; background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 2rem; display: flex; align-items: center; justify-content: center; flex-direction: column;">
                <div style="width: 200px; height: 200px; border-radius: 50%; border: 2px solid var(--primary); position: relative; margin-bottom: 1rem; display: flex; align-items: center; justify-content: center;">
                    <div style="position: absolute; top: -25px; font-weight: bold; font-family: var(--font-serif);">|0⟩</div>
                    <div style="position: absolute; bottom: -25px; font-weight: bold; font-family: var(--font-serif);">|1⟩</div>
                    <div style="position: absolute; right: -25px; font-weight: bold; font-family: var(--font-serif);">|+⟩</div>
                    <div style="position: absolute; left: -25px; font-weight: bold; font-family: var(--font-serif);">|-⟩</div>
                    <div style="width: 100%; height: 2px; background: var(--border); position: absolute;"></div>
                    <div style="width: 2px; height: 100%; background: var(--border); position: absolute;"></div>
                    <div style="width: 100%; height: 40px; border-radius: 50%; border: 1px dashed var(--primary-hover); position: absolute;"></div>
                    <svg style="position: absolute; width: 100%; height: 100%; top: 0; left: 0;">
                        <line x1="100" y1="100" x2="160" y2="40" stroke="#e25555" stroke-width="3" stroke-linecap="round"></line>
                        <circle cx="160" cy="40" r="4" fill="#e25555"></circle>
                    </svg>
                </div>
                <span style="color: var(--muted-text); font-size: 0.85rem;">(Bloch Sphere Geometric Representation)</span>
            </div>
        </div>        </div>
    </details>

    <details class="content-section basics-accordion" name="basics-accordion">
        <summary class="basics-summary" style="cursor: pointer; list-style: none; outline: none; margin-bottom: 1rem; display: flex; align-items: center; justify-content: space-between;">
            <h2>6. Quantum Oracles & Phase Kickback</h2>
            <svg class="accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: transform 0.2s;"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </summary>
        <div class="basics-content">
<p>This is the single most important mathematical mechanism in quantum computing. Virtually every oracle-based algorithm (Deutsch–Jozsa, Bernstein–Vazirani, Simon’s, Grover’s, and Quantum Phase Estimation) relies on phase kickback.</p>
        
        <h3 style="margin-top: 1.5rem;">Quantum Oracles <a href="appendix.html" style="font-size: 0.8rem; margin-left: 0.8rem; color: var(--primary); font-weight: 500; text-decoration: none; padding: 0.2rem 0.5rem; border-radius: 4px; background-color: var(--primary-light); display: inline-block; vertical-align: middle;">[click for more]</a></h3>
        <p>To evaluate a classical function \(f(x)\) deterministically and reversibly on a quantum computer, we encode it as a unitary operator \(U_f\):</p>
        <p style="text-align: center; font-size: 1.2rem; margin: 1.5rem 0;">\(U_f |x\rangle |y\rangle = |x\rangle |y \oplus f(x)\rangle\)</p>
        <p>Here, \(|x\rangle\) is the input register and \(|y\rangle\) is a target/ancilla qubit.</p>

        <h3 style="margin-top: 1.5rem;">The Kickback Mechanism <a href="appendix.html" style="font-size: 0.8rem; margin-left: 0.8rem; color: var(--primary); font-weight: 500; text-decoration: none; padding: 0.2rem 0.5rem; border-radius: 4px; background-color: var(--primary-light); display: inline-block; vertical-align: middle;">[click for more]</a></h3>
        <p>If the target qubit is prepared in the orthogonal state \(|-\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}\), applying the oracle does not change the state of the target qubit. Instead, the function's output is "kicked back" as a phase factor onto the control input register:</p>
        <p style="text-align: center; font-size: 1.2rem; margin: 1.5rem 0;">\(U_f \left( |x\rangle |-\rangle \right) = (-1)^{f(x)} |x\rangle |-\rangle\)</p>        </div>
    </details>

    <details class="content-section basics-accordion" name="basics-accordion">
        <summary class="basics-summary" style="cursor: pointer; list-style: none; outline: none; margin-bottom: 1rem; display: flex; align-items: center; justify-content: space-between;">
            <h2>7. Quantum Parallelism & Interference</h2>
            <svg class="accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: transform 0.2s;"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </summary>
        <div class="basics-content">
<p>Superposition alone is not enough to give a quantum computer an advantage. You need both <strong>parallelism</strong> and <strong>destructive interference</strong> working together.</p>
        
        <h3 style="margin-top: 1.5rem;">Quantum Parallelism <a href="appendix.html" style="font-size: 0.8rem; margin-left: 0.8rem; color: var(--primary); font-weight: 500; text-decoration: none; padding: 0.2rem 0.5rem; border-radius: 4px; background-color: var(--primary-light); display: inline-block; vertical-align: middle;">[click for more]</a></h3>
        <p>By preparing an \(n\)-qubit register in an equal superposition of all \(2^n\) computational basis states, a single execution of a quantum gate or oracle evaluates \(f(x)\) for all inputs simultaneously:</p>
        <p style="text-align: center; font-size: 1.2rem; margin: 1.5rem 0;">\(U_f \left( \frac{1}{\sqrt{2^n} \sum_{x=0}^{2^n-1} |x\rangle |0\rangle \right) = \frac{1}{\sqrt{2^n} \sum_{x=0}^{2^n-1} |x\rangle |f(x)\rangle\)</p>

        <h3 style="margin-top: 1.5rem;">Constructive & Destructive Interference <a href="appendix.html" style="font-size: 0.8rem; margin-left: 0.8rem; color: var(--primary); font-weight: 500; text-decoration: none; padding: 0.2rem 0.5rem; border-radius: 4px; background-color: var(--primary-light); display: inline-block; vertical-align: middle;">[click for more]</a></h3>
        <p>Because measuring a superposition collapses it to a single random value, quantum parallelism alone yields no speed-up. Quantum algorithms use interference to alter probability amplitudes:</p>
        <ul style="line-height: 1.6;">
            <li><strong>Constructive Interference:</strong> Amplitudes corresponding to the correct answer reinforce one another.</li>
            <li><strong>Destructive Interference:</strong> Amplitudes corresponding to incorrect answers cancel each other out to zero.</li>
        </ul>        </div>
    </details>

    <details class="content-section basics-accordion" name="basics-accordion">
        <summary class="basics-summary" style="cursor: pointer; list-style: none; outline: none; margin-bottom: 1rem; display: flex; align-items: center; justify-content: space-between;">
            <h2>8. Measurement & Physical Limits</h2>
            <svg class="accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: transform 0.2s;"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </summary>
        <div class="basics-content">
<h3 style="margin-top: 1.5rem;">Measurement & Wavefunction Collapse <a href="appendix.html" style="font-size: 0.8rem; margin-left: 0.8rem; color: var(--primary); font-weight: 500; text-decoration: none; padding: 0.2rem 0.5rem; border-radius: 4px; background-color: var(--primary-light); display: inline-block; vertical-align: middle;">[click for more]</a></h3>
        <p>Measuring a quantum state irrevocably collapses its superposition. For example, if a qubit is in the state \(|+\rangle = \frac{1}{\sqrt{2}|0\rangle + \frac{1}{\sqrt{2}|1\rangle\), it has no definite computational value. The moment it is measured in the standard computational basis, the wavefunction collapses to either \(|0\rangle\) or \(|1\rangle\) with equal probability:</p>
        <p style="text-align: center; font-size: 1.2rem; margin: 1.5rem 0;">\(P(\text{measure } 0 \mid \text{state } |+\rangle) = |\langle 0 | + \rangle|^2 = \frac{1}{2}\)</p>
        <p>This is not a limitation of our measuring instruments—it is a fundamental physical law. There is no way to measure a generic qubit without causing collapse, which means reading quantum information inherently disturbs it.</p>
        
        <h3 style="margin-top: 2rem;">Mutually Unbiased Bases <a href="appendix.html" style="font-size: 0.8rem; margin-left: 0.8rem; color: var(--primary); font-weight: 500; text-decoration: none; padding: 0.2rem 0.5rem; border-radius: 4px; background-color: var(--primary-light); display: inline-block; vertical-align: middle;">[click for more]</a></h3>
        <p>In quantum cryptography (like the BB84 protocol), we often encode information in different bases, such as the Rectilinear (Z) basis (\(|0\rangle, |1\rangle\)) and the Diagonal (X) basis (\(|+\rangle, |-\rangle\)). These bases are <strong>mutually unbiased</strong>. This means that if a state is prepared in one basis but measured in the other, the outcome is completely random (50/50), carrying no information about the original encoded bit.</p>

        <h3 style="margin-top: 2rem;">Heisenberg Uncertainty Principle <a href="appendix.html" style="font-size: 0.8rem; margin-left: 0.8rem; color: var(--primary); font-weight: 500; text-decoration: none; padding: 0.2rem 0.5rem; border-radius: 4px; background-color: var(--primary-light); display: inline-block; vertical-align: middle;">[click for more]</a></h3>
        <p>In quantum mechanics, certain pairs of physical observables (like position and momentum) cannot both be known to arbitrary precision simultaneously:</p>
        <p style="text-align: center; font-size: 1.2rem; margin: 1.5rem 0;">\(\Delta x \cdot \Delta p \ge \frac{\hbar}{2}\)</p>
        <p>In quantum information, this generalizes to mutually unbiased observables. Measuring a qubit in the Z-basis gives you maximum information about its Z-state, but destroys all information about its X-state (and vice versa).</p>

        <h3 style="margin-top: 2rem;">The No-Cloning Theorem <a href="appendix.html" style="font-size: 0.8rem; margin-left: 0.8rem; color: var(--primary); font-weight: 500; text-decoration: none; padding: 0.2rem 0.5rem; border-radius: 4px; background-color: var(--primary-light); display: inline-block; vertical-align: middle;">[click for more]</a></h3>
        <p>The No-Cloning Theorem (Wootters & Zurek, 1982) proves that it is physically impossible to make a perfect copy of an arbitrary unknown quantum state. This is a direct mathematical consequence of the linearity of quantum mechanics:</p>
        <p style="text-align: center; font-size: 1.2rem; margin: 1.5rem 0;">\(\nexists \, U : U(|\psi\rangle \otimes |0\rangle) = |\psi\rangle \otimes |\psi\rangle \quad \forall |\psi\rangle\)</p>
        <p>This law is the cornerstone of quantum security. An eavesdropper cannot intercept a transmitting qubit, copy it perfectly, and measure the copy while sending the original onward. Any measurement made will unavoidably disturb the original state, leaving a detectable trace.</p>        </div>
    </details>

    <details class="content-section basics-accordion" name="basics-accordion">
        <summary class="basics-summary" style="cursor: pointer; list-style: none; outline: none; margin-bottom: 1rem; display: flex; align-items: center; justify-content: space-between;">
            <h2>9. The DiVincenzo Criteria</h2>
            <svg class="accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: transform 0.2s;"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </summary>
        <div class="basics-content">
<p>Theoretical physics must eventually map to actual physical hardware. The DiVincenzo criteria outline the fundamental requirements necessary to construct a functional, scalable quantum computer:</p>
        <ol style="line-height: 1.6;">
            <li>A scalable physical system with well-characterized qubits.</li>
            <li>The ability to initialize the state of the qubits to a simple fiducial state, such as \(|00\dots0\rangle\).</li>
            <li>Long relevant decoherence times, much longer than the gate operation time.</li>
            <li>A "universal" set of quantum gates.</li>
            <li>A qubit-specific measurement capability.</li>
        </ol>
        <p>Two additional criteria apply for quantum communication (networked systems):</p>
        <ol start="6" style="line-height: 1.6;">
            <li>The ability to interconvert stationary and flying qubits.</li>
            <li>The ability to faithfully transmit flying qubits between specified locations.</li>
        </ol>        </div>
    </details>

    <details class="content-section basics-accordion" name="basics-accordion">
        <summary class="basics-summary" style="cursor: pointer; list-style: none; outline: none; margin-bottom: 1rem; display: flex; align-items: center; justify-content: space-between;">
            <h2>10. Decoherence & Noise Channels</h2>
            <svg class="accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: transform 0.2s;"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </summary>
        <div class="basics-content">
<p>In reality, quantum systems are not perfectly isolated; they are coupled to an external environment. Interaction with this environment leads to <strong>decoherence</strong>, where quantum information leaks out and degrades over time.</p>
        <ul style="line-height: 1.6;">
            <li><strong>Bit Flip Channel:</strong> Flips the state \(|0\rangle \leftrightarrow |1\rangle\) with a probability \(p\).</li>
            <li><strong>Phase Flip Channel:</strong> Leaves the basis states unchanged but applies a relative phase flip (e.g., changes \(|+\rangle\) to \(|-\rangle\)).</li>
            <li><strong>Amplitude Damping:</strong> Models energy loss from a quantum system (like a photon escaping a cavity), causing states to decay to the ground state \(|0\rangle\).</li>
            <li><strong>Depolarising Channel:</strong> Replaces the qubit's state with a completely mixed state (pure noise) with probability \(p\).</li>
        </ul>
        <p>Understanding these channels is a crucial theoretical prerequisite for Fault Tolerance and Quantum Error Correction.</p>        </div>
    </details>

    <details class="content-section basics-accordion" name="basics-accordion">
        <summary class="basics-summary" style="cursor: pointer; list-style: none; outline: none; margin-bottom: 1rem; display: flex; align-items: center; justify-content: space-between;">
            <h2>11. State Verification & Tomography</h2>
            <svg class="accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: transform 0.2s;"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </summary>
        <div class="basics-content">
<p>How do experimental physicists verify that a quantum state created in the lab actually matches the theoretical math? This requires robust verification techniques.</p>
        <ul style="line-height: 1.6;">
            <li><strong>Fidelity (\(\mathcal{F}\)):</strong> A measure of "closeness" between two quantum states. For two pure states, it is simply the squared overlap: \(\mathcal{F} = |\langle \psi | \phi \rangle|^2\). For mixed states, the formula becomes \(\mathcal{F}(\rho, \sigma) = (\text{Tr}\sqrt{\sqrt{\rho}\sigma\sqrt{\rho})^2\).</li>
            <li><strong>Trace Distance:</strong> A metric that distinguishes how easily two quantum states can be differentiated by a single measurement.</li>
            <li><strong>Quantum State Tomography:</strong> The process of reconstructing the complete density matrix of an unknown quantum state by performing identical preparation and varied measurements (in multiple bases) over a large statistical ensemble.</li>
            <li><strong>Quantum Process Tomography:</strong> Extending state tomography to completely characterize an unknown quantum channel or gate operation.</li>
        </ul>        </div>
    </details>

    <style>
        .basics-accordion > summary::-webkit-details-marker {
            display: none;
        }
        .basics-accordion[open] > summary .accordion-icon {
            transform: rotate(180deg);
        }
        .basics-accordion {
            background-color: var(--surface);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 1.5rem 2rem;
            margin-bottom: 1rem;
            transition: box-shadow 0.2s;
        }
        .basics-accordion[open] {
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }
        .basics-accordion h2 {
            margin: 0 !important;
            border: none !important;
            padding: 0 !important;
        }
        .basics-content {
            padding-top: 1rem;
            border-top: 1px solid var(--border);
            margin-top: 1rem;
        }
    </style>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const details = document.querySelectorAll('details.basics-accordion');
            
            // Open first one by default
            if (details.length > 0) {
                details[0].setAttribute('open', '');
            }

            // Accordion polyfill/enhancement
            details.forEach(targetDetail => {
                targetDetail.addEventListener('click', (e) => {
                    // if clicking on a link inside, don't toggle
                    if(e.target.tagName === 'A') return;
                    
                    // We don't prevent default, we just ensure others close.
                    // The 'name' attribute natively does this in modern browsers, 
                    // but this is a fallback for older browsers.
                    details.forEach(detail => {
                        if (detail !== targetDetail && detail.hasAttribute('open')) {
                            // Only manually remove if the browser didn't already
                            setTimeout(() => {
                                detail.removeAttribute('open');
                            }, 0);
                        }
                    });
                });
            });

            // Jump Button functionality
            const jumpBtn = document.getElementById('jumpBtn');
            if (jumpBtn) {
                jumpBtn.addEventListener('click', (e) => {
                    const targetId = jumpBtn.getAttribute('href').substring(1);
                    const targetElement = document.getElementById(targetId);
                    
                    if (targetElement && targetElement.tagName.toLowerCase() === 'details') {
                        // Close others
                        details.forEach(detail => {
                            if (detail !== targetElement) {
                                detail.removeAttribute('open');
                            }
                        });
                        // Open target
                        targetElement.setAttribute('open', '');
                    }
                });
            }

            // Search functionality
            const searchInput = document.getElementById('basicsSearch');
            if (searchInput) {
                searchInput.addEventListener('input', (e) => {
                    const query = e.target.value.toLowerCase();
                    let firstVisible = null;
                    
                    details.forEach(detail => {
                        const text = detail.textContent.toLowerCase();
                        if (text.includes(query)) {
                            detail.style.display = '';
                            if (!firstVisible) firstVisible = detail;
                            
                            if (query.length > 0) {
                                detail.setAttribute('open', '');
                            } else {
                                detail.removeAttribute('open');
                            }
                        } else {
                            detail.style.display = 'none';
                        }
                    });
                    
                    // If search is cleared, open the first visible one
                    if (query.length === 0 && firstVisible) {
                        firstVisible.setAttribute('open', '');
                    }
                });
            }
        });
    </script>
""")
generate_global_page("algorithms.html", "Algorithms", """
    <div class="page-header">
        <h1>Algorithm Catalogue</h1>
        <p style="color: var(--muted-text);">An index of all implemented quantum algorithms and protocols.</p>
    </div>
    
    <div style="margin-top: 2rem;">
        <input type="text" id="algoSearch" placeholder="Search algorithms..." class="search-input">
    </div>
    
    <section class="content-section" id="algoList">
        <div class="algo-category">
            <h2>Foundations</h2>
            <ul>
                <li><a href="algorithms/foundations/bell-state.html">Bell State Generator</a></li>
                <li><a href="algorithms/foundations/superdense-coding.html">Superdense Coding</a></li>
                <li><a href="algorithms/foundations/quantum-teleportation.html">Quantum Teleportation</a></li>
                <li><a href="algorithms/foundations/entanglement-swapping.html">Entanglement Swapping</a></li>
            </ul>
        </div>
        
        <div class="algo-category">
            <h2>Oracle-Based Algorithms</h2>
            <ul>
                <li><a href="algorithms/oracle-based/deutsch.html">Deutsch's Algorithm</a></li>
                <li><a href="algorithms/oracle-based/deutsch-jozsa.html">Deutsch-Jozsa Algorithm</a></li>
                <li><a href="algorithms/oracle-based/bernstein-vazirani.html">Bernstein-Vazirani Algorithm</a></li>
                <li><a href="algorithms/oracle-based/simon.html">Simon's Algorithm</a></li>
            </ul>
        </div>
        
        <div class="algo-category">
            <h2>Phase & Amplitude</h2>
            <ul>
                <li><a href="algorithms/phase-amplitude/qft.html">Quantum Fourier Transform (QFT)</a></li>
                <li><a href="algorithms/phase-amplitude/qpe.html">Quantum Phase Estimation (QPE)</a></li>
                <li><a href="algorithms/phase-amplitude/grover.html">Grover's Search</a></li>
                <li><a href="algorithms/phase-amplitude/amplitude-amplification.html">Amplitude Amplification</a></li>
            </ul>
        </div>
        
        <div class="algo-category">
            <h2>Flagship & Hybrid Models</h2>
            <ul>
                <li><a href="algorithms/flagship-hybrid/shor.html">Shor's Algorithm</a></li>
                <li><a href="algorithms/flagship-hybrid/vqe.html">Variational Quantum Eigensolver (VQE)</a></li>
                <li><a href="algorithms/flagship-hybrid/qaoa.html">Quantum Approximate Optimisation Algorithm (QAOA)</a></li>
                <li><a href="algorithms/flagship-hybrid/hhl.html">HHL Algorithm</a></li>
            </ul>
        </div>
        
        <div class="algo-category">
            <h2>Fault Tolerance & Error Correction</h2>
            <ul>
                <li><a href="algorithms/fault-tolerance/3-qubit-code.html">3-Qubit Code</a></li>
                <li><a href="algorithms/fault-tolerance/shors-9-qubit-code.html">Shor's 9-Qubit Code</a></li>
                <li><a href="algorithms/fault-tolerance/steane-code.html">Steane 7-Qubit Code</a></li>
            </ul>
        </div>
    </section>
    
    <script>
        document.getElementById('algoSearch').addEventListener('input', function(e) {
            const query = e.target.value.toLowerCase();
            const categories = document.querySelectorAll('.algo-category');
            
            categories.forEach(cat => {
                let hasVisibleLinks = false;
                const links = cat.querySelectorAll('li');
                
                links.forEach(li => {
                    const text = li.textContent.toLowerCase();
                    if (text.includes(query)) {
                        li.style.display = '';
                        hasVisibleLinks = true;
                    } else {
                        li.style.display = 'none';
                    }
                });
                
                if (hasVisibleLinks) {
                    cat.style.display = '';
                } else {
                    cat.style.display = 'none';
                }
            });
        });
    </script>
""")
generate_global_page("resources.html", "Visual Tools & Resources", """
    <div class="page-header">
        <h1>Visual Tools & Resources</h1>
        <p style="color: var(--muted-text);">Interactive simulators and learning materials for quantum computing.</p>
    </div>
    <section class="content-section">
        <h2>Interactive Simulators</h2>
        <div style="background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; max-width: 500px; display: flex; align-items: flex-start; gap: 1rem; margin-top: 1rem;">
            <div class="category-icon" style="margin-bottom: 0; flex-shrink: 0;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg></div>
            <div>
                <h4 style="margin-top: 0; margin-bottom: 0.5rem; color: var(--primary); font-family: var(--font-serif); font-size: 1.1rem;">BB84 Protocol Simulator</h4>
                <p style="margin-top: 0; margin-bottom: 1.25rem; font-size: 0.9rem; color: var(--text); line-height: 1.5;">An interactive visual simulator for the BB84 Quantum Key Distribution (QKD) protocol. Visualize the generation, transmission, and measurement of qubits in different bases to establish a secure cryptographic key.</p>
                <a href="https://bb84qkd.netlify.app/go.html" target="_blank" rel="noopener noreferrer" class="btn" style="padding: 0.4rem 1rem; font-size: 0.85rem;">Launch Simulator <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-left: 6px;"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg></a>
            </div>
        </div>
        
        <h2 style="margin-top: 3rem;">External Resources</h2>
        <ul style="line-height: 1.8;">
            <li><a href="https://qiskit.org/" target="_blank" rel="noopener noreferrer">Qiskit (IBM Quantum)</a> - Open-source quantum development framework.</li>
            <li><a href="https://quantum-computing.ibm.com/" target="_blank" rel="noopener noreferrer">IBM Quantum Learning</a> - Platform to learn quantum computing.</li>
            <li><a href="https://algassert.com/quirk" target="_blank" rel="noopener noreferrer">Quirk</a> - A drag-and-drop quantum circuit simulator.</li>
        </ul>
    </section>
""")

generate_global_page("references.html", "References", """
    <div class="page-header">
        <h1>References</h1>
    </div>
    <section class="content-section">
        <h2>Textbooks</h2>
        <p>Nielsen & Chuang, etc. placeholder.</p>
        <h2>Research Papers</h2>
        <p>Original seminal papers placeholder.</p>
    </section>
""")

generate_global_page("developer.html", "Developer Info", """
    <div class="page-header">
        <h1>Developer Information</h1>
    </div>
    <section class="content-section">
        <div style="background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; display: flex; flex-direction: column; gap: 1.5rem; max-width: 450px;">
            <div style="display: flex; align-items: center; gap: 1rem;">
                <div style="width: 60px; height: 60px; background: var(--primary-light); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: var(--primary); flex-shrink: 0;">
                    <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                </div>
                <div>
                    <h2 style="margin: 0; font-family: var(--font-serif); color: var(--primary); font-size: 1.4rem;">Agha Tasheer Syedi</h2>
                    <p style="margin: 0.25rem 0 0 0; font-weight: 600; color: var(--text); font-size: 0.95rem;">MTech in Quantum Computing</p>
                    <p style="margin: 0; font-size: 0.85rem; color: var(--muted-text);">Subject: Quantum Communication</p>
                </div>
            </div>
            
            <div style="display: flex; flex-direction: column; gap: 0.75rem; border-top: 1px solid var(--border); padding-top: 1.25rem;">
                <div style="display: flex; align-items: center; gap: 1rem; color: var(--text); font-size: 0.95rem;">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                    <span>Pune, MH, India</span>
                </div>
                <div style="display: flex; align-items: center; gap: 1rem; font-size: 0.95rem;">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                    <a href="mailto:cs.aghasyedi@gmail.com" style="color: var(--text); text-decoration: none; font-weight: 500;">cs.aghasyedi@gmail.com</a>
                </div>
                <div style="display: flex; align-items: center; gap: 1rem; font-size: 0.95rem;">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
                    <a href="https://aghasyedi.netlify.app/" target="_blank" rel="noopener noreferrer" style="font-weight: 500;">Portfolio Website</a>
                </div>
            </div>
        </div>

        <h3 style="margin-top: 3rem;">Previous Projects</h3>
        <div style="background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; max-width: 450px; display: flex; align-items: flex-start; gap: 1rem; margin-top: 1rem;">
            <div class="category-icon" style="margin-bottom: 0; flex-shrink: 0;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg></div>
            <div>
                <h4 style="margin-top: 0; margin-bottom: 0.5rem; color: var(--primary); font-family: var(--font-serif); font-size: 1.1rem;">BB84 Protocol Simulator</h4>
                <p style="margin-top: 0; margin-bottom: 1.25rem; font-size: 0.9rem; color: var(--text); line-height: 1.5;">An interactive visual simulator for the BB84 Quantum Key Distribution (QKD) protocol, demonstrating secure key exchange.</p>
                <a href="https://bb84qkd.netlify.app/go.html" target="_blank" rel="noopener noreferrer" class="btn" style="padding: 0.4rem 1rem; font-size: 0.85rem;">Launch Simulator <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-left: 6px;"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg></a>
            </div>
        </div>
    </section>
""")

generate_global_page("contact.html", "Contact", """
    <div class="page-header">
        <h1>Contact</h1>
    </div>
    <section class="content-section">
        <p>Feedback form, bug reports, and academic collaboration placeholder.</p>
    </section>
""")

def generate_bell_state_page():
    title = "Bell State Generator"
    category_name = "Protocols & Foundations"
    filename = "bell-state.html"
    category = "foundations"
    
    content = r"""
    <div class="breadcrumb">
        <a href="../../index.html">Home</a> <span class="breadcrumb-separator">›</span> 
        <a href="../../algorithms.html">Algorithms</a> <span class="breadcrumb-separator">›</span> 
        {category_name} <span class="breadcrumb-separator">›</span> 
        {title}
    </div>

    <div class="algorithm-header">
        <h1>{title}</h1>
        <div class="algorithm-meta">
            <span class="badge badge-category">{category_name}</span>
        </div>
    </div>

    <section class="content-section">
        <h2>1. Overview & Problem Definition</h2>
        <p>The <strong>Bell State Generator</strong> is the foundational circuit used to prepare maximally entangled two-qubit states, known as <strong>Bell states</strong> or <strong>EPR (Einstein-Podolsky-Rosen) pairs</strong>.</p>
        <p>In classical computing, the state of a multi-bit system is always separable—knowing the global state gives complete information about each individual bit. In quantum computing, entanglement allows two qubits to share a unified quantum state such that neither qubit possesses a definite individual state independent of the other. The Bell State Generator solves the problem of deterministically generating these non-local quantum correlations from simple computational basis inputs.</p>
        <div class="complexity-comparison" style="margin-top: 1.5rem;">
            <div class="complexity-box">
                <h3>Classical Complexity</h3>
                <div class="complexity-value">Impossible \(\mathcal{O}(\infty)\)</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">Classical physics cannot generate non-local quantum entanglement that violates Bell's inequalities.</p>
            </div>
            <div class="complexity-box">
                <h3>Quantum Circuit Depth</h3>
                <div class="complexity-value">\(\mathcal{O}(1)\)</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">Constant depth: requires exactly 2 qubits and 2 gate operations (\(H\) and \(CX\)).</p>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>2. Intuition</h2>
        <p>To create maximal entanglement between two independent, unentangled qubits:</p>
        <ol style="line-height: 1.6; margin-left: 1.5rem;">
            <li><strong>Create Superposition:</strong> We start with both qubits in the ground state \(|00\rangle\). We apply a Hadamard (\(H\)) gate to the first qubit (control qubit). This puts Qubit 0 into an equal superposition of \(|0\rangle\) and \(|1\rangle\), while Qubit 1 remains strictly \(|0\rangle\). At this stage, the system is still separable:
                <div class="math-container" style="margin: 1rem 0;">
                    <p>\(\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \otimes |0\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |10\rangle)\)</p>
                </div>
            </li>
            <li><strong>Entangle via Control:</strong> We then apply a Controlled-NOT (\(CX\)) gate, using Qubit 0 as the control and Qubit 1 as the target:
                <ul style="margin-top: 0.5rem; margin-bottom: 0.5rem;">
                    <li>If Qubit 0 is \(|0\rangle\), Qubit 1 remains \(|0\rangle \longrightarrow |00\rangle\).</li>
                    <li>If Qubit 0 is \(|1\rangle\), Qubit 1 flips to \(|1\rangle \longrightarrow |11\rangle\).</li>
                </ul>
            </li>
        </ol>
        <p>Because Qubit 0 is in a superposition of both states simultaneously, the \(CX\) gate executes both actions in superposition, entangling the two qubits into the state \(|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)\). Neither qubit has a defined state on its own, but measuring Qubit 0 instantly determines the state of Qubit 1.</p>
    </section>

    <section class="content-section">
        <h2>3. Required Gates & Circuit Schematic</h2>
        <p>The standard Bell State Generator utilizes:</p>
        <ul style="line-height: 1.6;">
            <li><strong>Hadamard Gate (\(H\)):</strong> Creates an equal superposition.</li>
            <li><strong>Controlled-NOT Gate (\(CX\)):</strong> Generates two-qubit conditional entanglement.</li>
            <li><strong>Pauli-X (\(X\)) / Pauli-Z (\(Z\)) Gates:</strong> Optional pre-rotation gates used on the inputs to select which of the four orthogonal Bell states to prepare.</li>
        </ul>

        <h3 style="margin-top: 1.5rem;">Input-to-Bell State Mapping</h3>
        <p>Depending on the initial computational basis input \(|q_1 q_0\rangle\), the circuit constructs one of four distinct maximally entangled Bell states:</p>
        
        <table style="width: 100%; border-collapse: collapse; margin-top: 1rem;">
            <thead>
                <tr style="border-bottom: 2px solid var(--border-color); text-align: left;">
                    <th style="padding: 0.5rem;">Input State \(|q_1 q_0\rangle\)</th>
                    <th style="padding: 0.5rem;">Pre-Gates Applied</th>
                    <th style="padding: 0.5rem;">Resulting Bell State</th>
                    <th style="padding: 0.5rem;">State Equation</th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom: 1px solid var(--border-color);">
                    <td style="padding: 0.5rem;">\(|00\rangle\)</td>
                    <td style="padding: 0.5rem;">None</td>
                    <td style="padding: 0.5rem;">\(|\Phi^+\rangle\)</td>
                    <td style="padding: 0.5rem;">\(\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)\)</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border-color);">
                    <td style="padding: 0.5rem;">\(|01\rangle\)</td>
                    <td style="padding: 0.5rem;">\(X\) on \(q_0\)</td>
                    <td style="padding: 0.5rem;">\(|\Phi^-\rangle\)</td>
                    <td style="padding: 0.5rem;">\(\frac{1}{\sqrt{2}}(|00\rangle - |11\rangle)\)</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border-color);">
                    <td style="padding: 0.5rem;">\(|10\rangle\)</td>
                    <td style="padding: 0.5rem;">\(X\) on \(q_1\)</td>
                    <td style="padding: 0.5rem;">\(|\Psi^+\rangle\)</td>
                    <td style="padding: 0.5rem;">\(\frac{1}{\sqrt{2}}(|01\rangle + |10\rangle)\)</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border-color);">
                    <td style="padding: 0.5rem;">\(|11\rangle\)</td>
                    <td style="padding: 0.5rem;">\(X\) on \(q_1\) &amp; \(q_0\)</td>
                    <td style="padding: 0.5rem;">\(|\Psi^-\rangle\)</td>
                    <td style="padding: 0.5rem;">\(\frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)\)</td>
                </tr>
            </tbody>
        </table>

        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="10" rx="2" ry="2"></rect><line x1="12" y1="3" x2="12" y2="7"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg></div>
            <h3>Circuit Diagram (\(|\Phi^+\rangle\) Generation)</h3>
            <pre style="background: var(--code-bg); padding: 1rem; border-radius: 4px; overflow-x: auto; margin-top: 1rem; color: var(--text-color);">
q_0: ──|0⟩───[ H ]───■───
                     │   
q_1: ──|0⟩───────────■───</pre>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Circuit image placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>4. Mathematical Proof & State Evolution</h2>
        <p><em>(Note: Standard textbook Dirac convention \(|q_0\rangle \otimes |q_1\rangle = |q_0 q_1\rangle\) is used below).</em></p>
        
        <h3 style="margin-top: 1.5rem;">Step 0: Initial State Preparation</h3>
        <p>The system starts in the pure computational ground state:</p>
        <div class="math-container">
            <p>\(|\psi_0\rangle = |0\rangle \otimes |0\rangle = |00\rangle = \begin{bmatrix} 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 1: Applying the Hadamard Gate to Qubit 0</h3>
        <p>We apply \(H \otimes I\) to the composite system:</p>
        <div class="math-container">
            <p>\(H = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}, \quad I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}\)</p>
            <p>\(|\psi_1\rangle = (H \otimes I)|\psi_0\rangle = \left( \frac{|0\rangle + |1\rangle}{\sqrt{2}} \right) \otimes |0\rangle = \frac{1}{\sqrt{2}}|00\rangle + \frac{1}{\sqrt{2}}|10\rangle = \begin{bmatrix} \frac{1}{\sqrt{2}} \\ 0 \\ \frac{1}{\sqrt{2}} \\ 0 \end{bmatrix}\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 2: Applying the Controlled-NOT (\(CX\)) Gate</h3>
        <p>The \(CX\) gate operator with control on qubit 0 and target on qubit 1 is represented in matrix form as:</p>
        <div class="math-container">
            <p>\(CX = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \end{bmatrix}\)</p>
        </div>
        <p>Multiplying \(CX\) by \(|\psi_1\rangle\):</p>
        <div class="math-container">
            <p>\(|\psi_2\rangle = CX |\psi_1\rangle = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \end{bmatrix} \begin{bmatrix} \frac{1}{\sqrt{2}} \\ 0 \\ \frac{1}{\sqrt{2}} \\ 0 \end{bmatrix} = \begin{bmatrix} \frac{1}{\sqrt{2}} \\ 0 \\ 0 \\ \frac{1}{\sqrt{2}} \end{bmatrix}\)</p>
        </div>
        <p>Rewriting in Dirac notation yields the entangled Bell state \(|\Phi^+\rangle\):</p>
        <div class="math-container">
            <p>\(|\psi_2\rangle = \frac{1}{\sqrt{2}}|00\rangle + \frac{1}{\sqrt{2}}|11\rangle = |\Phi^+\rangle\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Measurement Distribution</h3>
        <p>When measuring both qubits in the computational \(Z\)-basis:</p>
        <ul style="line-height: 1.6;">
            <li>\(P(00) = \left| \frac{1}{\sqrt{2}} \right|^2 = \frac{1}{2} \quad (50\%)\)</li>
            <li>\(P(01) = |0|^2 = 0 \quad (0\%)\)</li>
            <li>\(P(10) = |0|^2 = 0 \quad (0\%)\)</li>
            <li>\(P(11) = \left| \frac{1}{\sqrt{2}} \right|^2 = \frac{1}{2} \quad (50\%)\)</li>
        </ul>
    </section>

    <section class="content-section">
        <h2>5. Interactive Visualisation</h2>
        <p>When observing a Bell State generator inside an interactive tracking module, notice these distinct behaviors:</p>
        <ul style="line-height: 1.6;">
            <li><strong>Amplitude Histogram:</strong> Shows two distinct probability peaks of height \(0.5\) at \(|00\rangle\) and \(|11\rangle\), with zero probability for cross-terms \(|01\rangle\) and \(|10\rangle\).</li>
            <li><strong>Single-Qubit Bloch Spheres:</strong> For a maximally entangled Bell state, inspecting Qubit 0 or Qubit 1 on an individual single-qubit Bloch sphere shows the state vector shrinking to the center point \((0,0,0)\). This represents a <strong>maximally mixed reduced state</strong> (\(\\rho_A = \frac{1}{2}I\)), visually demonstrating that individual qubit states do not exist independently in an entangled pair.</li>
            <li><strong>Density Matrix Heatmap:</strong> Shows non-zero off-diagonal coherences (\(\\rho_{00, 11} = \\rho_{11, 00} = 0.5\)), which prove the presence of quantum coherence rather than classical statistical uncertainty.</li>
        </ul>
        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg></div>
            <h3>Dynamic State Tracking</h3>
            <p>Interactive module (amplitude histograms, Bloch spheres) to simulate the algorithm live.</p>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Interactive visualization placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>6. Python Code Implementation</h2>
        
        <h3>From Scratch (NumPy)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / NumPy</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>import numpy as np

def generate_bell_state(initial_bits=(0, 0)):
    \"\"\"
    Simulates a Bell State Generator using pure NumPy matrix multiplication.
    initial_bits: tuple (q1, q0) representing the input computational state.
    \"\"\"
    # 1. Fundamental basis states
    ket_0 = np.array([[1], [0]], dtype=complex)
    ket_1 = np.array([[0], [1]], dtype=complex)
    
    # 2. Gate Definitions
    I = np.eye(2, dtype=complex)
    H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    
    # CNOT matrix (Control: Qubit 0, Target: Qubit 1)
    CX = np.array([
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0]
    ], dtype=complex)

    # 3. Prepare initial state
    q1_in = ket_1 if initial_bits[0] == 1 else ket_0
    q0_in = ket_1 if initial_bits[1] == 1 else ket_0
    psi_0 = np.kron(q0_in, q1_in)

    # 4. Apply Hadamard to Qubit 0
    H_tensor_I = np.kron(H, I)
    psi_1 = np.dot(H_tensor_I, psi_0)

    # 5. Apply CNOT
    psi_2 = np.dot(CX, psi_1)

    # 6. Calculate Probability Distribution
    probabilities = np.abs(psi_2.flatten())**2
    state_names = ['|00>', '|01>', '|10>', '|11>']
    
    return psi_2, dict(zip(state_names, probabilities))

# Example Execution
state_vector, probs = generate_bell_state(initial_bits=(0, 0))
print("Final State Vector:\\n", state_vector.ravel())
print("Measurement Probabilities:\\n", probs)
</code></pre>
            </div>
        </div>
        
        <h3 style="margin-top: 1.5rem;">Framework (Qiskit 1.0+)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / Qiskit</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

def build_bell_circuit(bell_type="Phi+"):
    \"\"\"
    Constructs a Qiskit Quantum Circuit for generating Bell States.
    \"\"\"
    qc = QuantumCircuit(2, 2, name=f"Bell_{bell_type}")
    
    # Configure input state according to desired Bell state
    if bell_type in ["Psi+", "Psi-"]:
        qc.x(1)  # Flip Qubit 1
    if bell_type in ["Phi-", "Psi-"]:
        qc.x(0)  # Flip Qubit 0

    qc.barrier(label="Input")
    
    # Core Bell State Generator
    qc.h(0)
    qc.cx(0, 1)
    
    return qc

# 1. Simulate exact Statevector
circuit = build_bell_circuit("Phi+")
state = Statevector.from_instruction(circuit)

print("Quantum Circuit Layout:")
print(circuit.draw(output='text'))

print("\\nStatevector Representation:")
print(state.draw('latex_source'))

# 2. Run Shot-based Simulation
circuit.measure([0, 1], [0, 1])
simulator = AerSimulator()
result = simulator.run(circuit, shots=1024).result()
counts = result.get_counts()

print("\\nShot Measurement Counts (1024 shots):", counts)
</code></pre>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>7. Caveats & Real-World Limits</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Two-Qubit Gate Error Rates:</strong> On modern NISQ (Noisy Intermediate-Scale Quantum) devices, single-qubit gates (\(H\)) achieve high fidelities (&gt;99.9%), but two-qubit entangling gates (\(CX\)) are roughly an order of magnitude noisier (~99.0% to 99.5% fidelity).</li>
            <li><strong>Decoherence (\(T_1\) and \(T_2\)):</strong> Entanglement is exceptionally fragile. Thermal relaxation (\(T_1\)) and dephasing (\(T_2\)) cause the pristine state \(|\Phi^+\rangle\) to degrade over time into a mixed state described as a <strong>Werner State</strong>:
                <div class="math-container" style="margin: 1rem 0;">
                    <p>\(\\rho = p |\Phi^+\rangle\langle\Phi^+| + \frac{1-p}{4} I_4\)</p>
                </div>
            </li>
            <li><strong>Measurement Readout Errors:</strong> Imperfections in state discrimination can cause an physical detector to misclassify a \(|00\rangle\) state as \(|01\rangle\) or \(|10\rangle\), creating false noise in the output histogram.</li>
        </ul>
    </section>

    <section class="content-section">
        <h2>8. Applications</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Quantum Teleportation:</strong> The prepared Bell pair serves as the non-local quantum resource channel required to transmit an unknown qubit state across classical links.</li>
            <li><strong>Superdense Coding:</strong> Allows two classical bits of information to be sent using a single physical qubit transmission by manipulating an entangled Bell pair.</li>
            <li><strong>Quantum Key Distribution (E91 Protocol):</strong> Uses the violation of Bell's inequalities (CHSH testing) on generated Bell pairs to detect eavesdroppers in quantum networks.</li>
            <li><strong>Entanglement Swapping:</strong> Forms the baseline building block for quantum repeaters, enabling long-distance quantum communication across disparate nodes.</li>
        </ul>
    </section>
    
    <section class="content-section">
        <h2>9. References</h2>
        <ol style="line-height: 1.6;">
            <li>Nielsen, M. A., &amp; Chuang, I. L. (2010). <em>Quantum Computation and Quantum Information</em> (10th Anniversary ed.). Cambridge University Press.</li>
            <li>Einstein, A., Podolsky, B., &amp; Rosen, N. (1935). Can quantum-mechanical description of physical reality be considered complete? <em>Physical Review</em>, 47(10), 777.</li>
            <li>Kaye, P., Laflamme, R., &amp; Mosca, M. (2007). <em>An Introduction to Quantum Computing</em>. Oxford University Press.</li>
        </ol>
    </section>

    <nav class="algorithm-nav">
        <!-- No previous for the first algorithm -->
        <a href="superdense-coding.html" class="nav-button nav-next" style="margin-left: auto;">
            <span class="nav-label">Next</span>
            <span class="nav-title">Superdense Coding</span>
        </a>
    </nav>
    """.replace("{title}", title).replace("{category_name}", category_name)
    
    with open(f"/Users/aghatasheersyedi/Desktop/latex/class/qiskit/aqca/algorithms/{category}/{filename}", 'w') as f:
        html = HTML_TEMPLATE.format(
            title=title,
            description=f"AQCA - {title}",
            root_path="../../",
            extra_css="",
            extra_js="",
            algorithms_expanded="true",
            content=content
        )
        f.write(html)

def generate_superdense_coding_page():
    title = "Superdense Coding"
    category_name = "Protocols & Foundations"
    filename = "superdense-coding.html"
    category = "foundations"
    
    content = r"""
    <div class="breadcrumb">
        <a href="../../index.html">Home</a> <span class="breadcrumb-separator">›</span> 
        <a href="../../algorithms.html">Algorithms</a> <span class="breadcrumb-separator">›</span> 
        {category_name} <span class="breadcrumb-separator">›</span> 
        {title}
    </div>

    <div class="algorithm-header">
        <h1>{title}</h1>
        <div class="algorithm-meta">
            <span class="badge badge-category">{category_name}</span>
        </div>
    </div>

    <section class="content-section">
        <h2>1. Overview & Problem Definition</h2>
        <p>In classical information theory, transmitting two bits of information strictly requires sending two physical bits. Superdense coding is a quantum communication protocol that solves this problem of transmission efficiency. It allows a sender (Alice) to transmit two classical bits of information to a receiver (Bob) by sending only a single quantum bit (qubit). This remarkable feat is achieved under the assumption that the sender and receiver pre-share a maximally entangled resource, such as a Bell pair.</p>
        <div class="complexity-comparison" style="margin-top: 1.5rem;">
            <div class="complexity-box">
                <h3>Classical Bit Cost</h3>
                <div class="complexity-value">2 bits</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">Sending two classical bits requires transmitting two physical bits.</p>
            </div>
            <div class="complexity-box">
                <h3>Quantum Qubit Cost</h3>
                <div class="complexity-value">1 qubit</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">Sends two classical bits by transmitting only one qubit, doubling the information density.</p>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>2. Intuition</h2>
        <p>Superdense coding can be conceptualised as the inverse of quantum teleportation. While teleportation uses two classical bits to transmit one quantum state, superdense coding uses one quantum state to transmit two classical bits.</p>
        <ol style="line-height: 1.6; margin-left: 1.5rem;">
            <li><strong>Pre-shared Entanglement:</strong> Alice and Bob share an entangled pair of qubits (e.g., the state \(|\Phi^+\rangle\)). Alice holds the first qubit, and Bob holds the second.</li>
            <li><strong>Local Encoding:</strong> Alice wishes to send a two-bit classical message (<code>00</code>, <code>01</code>, <code>10</code>, or <code>11</code>). Instead of sending classical signals, she applies a specific quantum gate to her single qubit. Because her qubit is entangled with Bob's, her local operation shifts the global state of the entire two-qubit system into one of four orthogonal Bell states.</li>
            <li><strong>Transmission & Decoding:</strong> Alice sends her single qubit to Bob. Bob now possesses both qubits of the entangled pair. He applies a joint measurement (decoding operation) to determine which of the four Bell states the system is in, thereby extracting Alice's original two-bit message.</li>
        </ol>
    </section>

    <section class="content-section">
        <h2>3. Required Gates & Circuit Schematic</h2>
        <p>The circuit requires gates for entanglement generation, message encoding, and decoding.</p>
        <ul style="line-height: 1.6;">
            <li><strong>Hadamard (\(H\)) & Controlled-NOT (\(CX\)):</strong> Used initially to create the shared Bell state.</li>
            <li><strong>Pauli-\(X\) and Pauli-\(Z\) Gates:</strong> Used by Alice to encode the classical bits.</li>
            <li><strong>Controlled-NOT (\(CX\)) & Hadamard (\(H\)):</strong> Used by Bob in reverse order to decode the Bell state back into computational basis states.</li>
        </ul>

        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="10" rx="2" ry="2"></rect><line x1="12" y1="3" x2="12" y2="7"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg></div>
            <h3>Circuit Schematic</h3>
            <pre style="background: var(--code-bg); padding: 1rem; border-radius: 4px; overflow-x: auto; margin-top: 1rem; color: var(--text-color);">
       ┌───┐      Encoding        Sending       Decoding
q_0: ──┤ H ├──■───[ I/X/Z/XZ ]──────(►)───────■───┌───┐─── ✂ Measure
       └───┘  │                               │   └───┘
q_1: ─────────■───────────────────────────────■─────────── ✂ Measure
             Shared Entanglement             Bob's lab</pre>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Circuit image placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>4. Mathematical Proof & State Evolution</h2>
        
        <h3 style="margin-top: 1.5rem;">Step 1: Sharing Entanglement</h3>
        <p>The protocol begins with the preparation of the Bell state \(|\Phi^+\rangle\) shared between Alice and Bob:</p>
        <div class="math-container">
            <p>\(|\psi_0\rangle = |\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)\)</p>
        </div>
        <p>Alice possesses the first qubit (left), and Bob possesses the second (right).</p>

        <h3 style="margin-top: 1.5rem;">Step 2: Encoding the Message</h3>
        <p>Alice applies a unitary operation to her qubit based on the two-bit message she wishes to send. This transforms the global state:</p>
        <ul style="line-height: 1.6;">
            <li><strong>Message <code>00</code> (Apply \(I\)):</strong>
                <div class="math-container" style="margin: 0.5rem 0;">
                    <p>\((I \otimes I)|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle) = |\Phi^+\rangle\)</p>
                </div>
            </li>
            <li><strong>Message <code>01</code> (Apply \(X\)):</strong>
                <div class="math-container" style="margin: 0.5rem 0;">
                    <p>\((X \otimes I)|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|10\rangle + |01\rangle) = |\Psi^+\rangle\)</p>
                </div>
            </li>
            <li><strong>Message <code>10</code> (Apply \(Z\)):</strong>
                <div class="math-container" style="margin: 0.5rem 0;">
                    <p>\((Z \otimes I)|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle - |11\rangle) = |\Phi^-\rangle\)</p>
                </div>
            </li>
            <li><strong>Message <code>11</code> (Apply \(Z\) then \(X\)):</strong>
                <div class="math-container" style="margin: 0.5rem 0;">
                    <p>\((XZ \otimes I)|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|10\rangle - |01\rangle) = |\Psi^-\rangle\)</p>
                </div>
            </li>
        </ul>

        <h3 style="margin-top: 1.5rem;">Step 3: Decoding the Message</h3>
        <p>Alice sends her qubit to Bob, who now applies a \(CX\) gate (with Alice's qubit as control and his as target), followed by a Hadamard gate on Alice's qubit.<br>Let us trace the evolution for the encoded message <code>01</code> (\(|\Psi^+\rangle\)):</p>
        <ol style="line-height: 1.6; margin-left: 1.5rem;">
            <li><strong>Apply \(CX\):</strong>
                <div class="math-container" style="margin: 0.5rem 0;">
                    <p>\(CX \left( \frac{1}{\sqrt{2}}(|10\rangle + |01\rangle) \right) = \frac{1}{\sqrt{2}}(|11\rangle + |01\rangle) = \frac{1}{\sqrt{2}}(|1\rangle + |0\rangle) \otimes |1\rangle\)</p>
                </div>
            </li>
            <li><strong>Apply Hadamard to Qubit 0:</strong>
                <div class="math-container" style="margin: 0.5rem 0;">
                    <p>\((H \otimes I) \left( \frac{|0\rangle + |1\rangle}{\sqrt{2}} \otimes |1\rangle \right) = |0\rangle \otimes |1\rangle = |01\rangle\)</p>
                </div>
            </li>
        </ol>

        <h3 style="margin-top: 1.5rem;">Measurement</h3>
        <p>Measuring the two qubits in the computational basis perfectly yields the classical string <code>01</code> with \(100\%\) probability. This deterministically works for all four encoded states.</p>
    </section>

    <section class="content-section">
        <h2>5. Interactive Visualisation</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Bloch Spheres (During Encoding):</strong> When Alice applies her gates, her local reduced density matrix remains completely mixed (a point at the centre of the Bloch sphere). No local measurement can reveal the message, illustrating the security of the protocol against eavesdropping.</li>
            <li><strong>Statevector Histogram (Post-Decoding):</strong> After Bob applies his \(CX\) and \(H\) gates, the histogram collapses from a superposition of Bell states entirely into a single computational basis bar (e.g., a single peak at <code>10</code> of height 1.0).</li>
        </ul>
        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg></div>
            <h3>Dynamic State Tracking</h3>
            <p>Interactive module (amplitude histograms, Bloch spheres) to simulate the algorithm live.</p>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Interactive visualization placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>6. Python Code Implementation</h2>
        
        <h3>From Scratch (NumPy)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / NumPy</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>import numpy as np

def simulate_superdense_coding(message):
    \"\"\"
    Simulates Superdense Coding using pure NumPy matrix multiplication.
    message: string '00', '01', '10', or '11'
    \"\"\"
    I = np.eye(2, dtype=complex)
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)
    CX = np.array([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]], dtype=complex)

    # 1. Shared Entanglement (Phi+)
    phi_plus = np.array([[1/np.sqrt(2)], [0], [0], [1/np.sqrt(2)]])

    # 2. Alice's Encoding
    encode_gate = I
    if message == '01':
        encode_gate = X
    elif message == '10':
        encode_gate = Z
    elif message == '11':
        encode_gate = np.dot(X, Z) # Apply Z then X

    # Apply Alice's gate to her qubit (tensor with Identity for Bob's qubit)
    psi_encoded = np.dot(np.kron(encode_gate, I), phi_plus)

    # 3. Bob's Decoding
    # Apply CX
    psi_decoded = np.dot(CX, psi_encoded)
    # Apply H to Qubit 0
    psi_final = np.dot(np.kron(H, I), psi_decoded)

    # 4. Measurement
    probabilities = np.abs(psi_final.flatten())**2
    state_names = ['00', '01', '10', '11']
    
    return dict(zip(state_names, np.round(probabilities, 5)))

# Example
print("Transmitted Message '10':", simulate_superdense_coding('10'))
</code></pre>
            </div>
        </div>
        
        <h3 style="margin-top: 1.5rem;">Framework (Qiskit)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / Qiskit</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

def superdense_coding_circuit(message):
    qc = QuantumCircuit(2, 2)
    
    # 1. Prepare Entanglement
    qc.h(0)
    qc.cx(0, 1)
    qc.barrier(label="Shared")
    
    # 2. Alice Encodes
    if message[1] == '1': # Check least significant bit
        qc.x(0)
    if message[0] == '1': # Check most significant bit
        qc.z(0)
    
    qc.barrier(label="Transmitted")
    
    # 3. Bob Decodes
    qc.cx(0, 1)
    qc.h(0)
    
    # 4. Measure
    qc.measure([0, 1], [0, 1])
    return qc

# Simulate
circuit = superdense_coding_circuit('11')
simulator = AerSimulator()
result = simulator.run(circuit, shots=1024).result()
print("Measurement Counts:", result.get_counts())
</code></pre>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>7. Caveats & Real-World Limits</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Requires Pre-shared Entanglement:</strong> If Alice and Bob do not have prior entanglement established, transmitting two classical bits with one qubit is physically impossible and would violate Holevo's bound.</li>
            <li><strong>Noise and Decoherence:</strong> Physical quantum channels are prone to depolarising noise. If the entangled pair degrades due to environmental decoherence before Bob can decode it, the error rate in the transmitted classical bits will rise dramatically.</li>
            <li><strong>Transmission Loss:</strong> If Alice's qubit is absorbed or lost in the optical fibre en route to Bob, the entire protocol fails, and the message cannot be recovered.</li>
        </ul>
    </section>

    <section class="content-section">
        <h2>8. Applications</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Quantum Networks & Communication:</strong> Superdense coding is a fundamental protocol for the future quantum internet, allowing for higher information density across optical networks.</li>
            <li><strong>Secure Communication:</strong> It acts as a form of secure quantum communication. If an eavesdropper (Eve) intercepts Alice's qubit en route, they only obtain part of a maximally mixed state. Without Bob's entangled half, no classical information can be extracted.</li>
        </ul>
    </section>
    
    <section class="content-section">
        <h2>9. References</h2>
        <ol style="line-height: 1.6;">
            <li>Bennett, C. H., &amp; Wiesner, S. J. (1992). Communication via one- and two-particle operators on Einstein-Podolsky-Rosen states. <em>Physical Review Letters</em>, 69(20), 2881.</li>
            <li>Mattle, K., Weinfurter, H., Kwiat, P. G., &amp; Zeilinger, A. (1996). Dense coding in experimental quantum communication. <em>Physical Review Letters</em>, 76(25), 4656.</li>
            <li>Nielsen, M. A., &amp; Chuang, I. L. (2010). <em>Quantum Computation and Quantum Information</em> (10th Anniversary ed.). Cambridge University Press.</li>
        </ol>
    </section>

    <nav class="algorithm-nav">
        <a href="bell-state.html" class="nav-button">
            <span class="nav-label">Previous</span>
            <span class="nav-title">Bell State Generator</span>
        </a>
        <a href="quantum-teleportation.html" class="nav-button nav-next">
            <span class="nav-label">Next</span>
            <span class="nav-title">Quantum Teleportation</span>
        </a>
    </nav>
    """.replace("{title}", title).replace("{category_name}", category_name)
    
    with open(f"/Users/aghatasheersyedi/Desktop/latex/class/qiskit/aqca/algorithms/{category}/{filename}", 'w') as f:
        html = HTML_TEMPLATE.format(
            title=title,
            description=f"AQCA - {title}",
            root_path="../../",
            extra_css="",
            extra_js="",
            algorithms_expanded="true",
            content=content
        )
        f.write(html)


def generate_quantum_teleportation_page():
    title = "Quantum Teleportation"
    category_name = "Protocols & Foundations"
    filename = "quantum-teleportation.html"
    category = "foundations"
    
    content = r"""
    <div class="breadcrumb">
        <a href="../../index.html">Home</a> <span class="breadcrumb-separator">›</span> 
        <a href="../../algorithms.html">Algorithms</a> <span class="breadcrumb-separator">›</span> 
        {category_name} <span class="breadcrumb-separator">›</span> 
        {title}
    </div>

    <div class="algorithm-header">
        <h1>{title}</h1>
        <div class="algorithm-meta">
            <span class="badge badge-category">{category_name}</span>
        </div>
    </div>

    <section class="content-section">
        <h2>1. Overview & Problem Definition</h2>
        <p>The <strong>Quantum Teleportation</strong> protocol solves the problem of transmitting an arbitrary, unknown quantum state from a sender (Alice) to a receiver (Bob) without physically moving the particle that stores the state. Because of the No-Cloning Theorem, Alice cannot simply read the quantum state and send a classical description to Bob. Instead, by leveraging a pre-shared entangled resource and a classical communication channel, the state is destroyed at Alice's location and perfectly recreated at Bob's.</p>
        <div class="complexity-comparison" style="margin-top: 1.5rem;">
            <div class="complexity-box">
                <h3>Classical Bit Cost</h3>
                <div class="complexity-value">2 bits</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">Alice must transmit two classical bits to Bob to complete the teleportation.</p>
            </div>
            <div class="complexity-box">
                <h3>Quantum Qubit Cost</h3>
                <div class="complexity-value">1 EPR pair</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">The protocol consumes one maximally entangled Bell pair to teleport one qubit.</p>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>2. Intuition</h2>
        <p>Teleportation can be understood through a four-step narrative:</p>
        <ol style="line-height: 1.6; margin-left: 1.5rem;">
            <li><strong>Pre-shared Entanglement:</strong> Alice and Bob share an entangled pair of qubits (a Bell state). Alice keeps one half, and Bob takes the other half to his distant location.</li>
            <li><strong>Entangling the Message:</strong> Alice possesses a third qubit holding the unknown state \(|\psi\rangle\) she wants to send. She forces this message qubit to interact with her half of the entangled pair.</li>
            <li><strong>Bell Basis Measurement:</strong> Alice measures both of her qubits. This measurement collapses her qubits into definite classical states (yielding two classical bits) and instantly collapses Bob's distant qubit into a state that is mathematically related to the original message \(|\psi\rangle\).</li>
            <li><strong>Classical Communication & Correction:</strong> Bob's qubit is now holding the original state, but it might be rotated or flipped. Alice sends her two classical bits to Bob over a standard network (like the internet). Bob uses these bits as instructions to apply the correct quantum gates (Pauli-X and/or Pauli-Z) to fix his qubit, perfectly recovering \(|\psi\rangle\).</li>
        </ol>
    </section>

    <section class="content-section">
        <h2>3. Required Gates & Circuit Schematic</h2>
        <p>The circuit requires gates for entanglement generation, a change of basis, and classically-controlled corrections.</p>
        <ul style="line-height: 1.6;">
            <li><strong>Hadamard (\(H\)) & Controlled-NOT (\(CX\)):</strong> Used to create the initial shared Bell state, and later used by Alice to change the basis before her measurement.</li>
            <li><strong>Measurement (\(M\)):</strong> Alice measures her two qubits in the computational \(Z\)-basis.</li>
            <li><strong>Pauli-\(X\) and Pauli-\(Z\) Gates:</strong> Applied by Bob as corrective rotations, controlled by Alice's classical measurement outcomes.</li>
        </ul>

        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="10" rx="2" ry="2"></rect><line x1="12" y1="3" x2="12" y2="7"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg></div>
            <h3>Circuit Schematic</h3>
            <pre style="background: var(--code-bg); padding: 1rem; border-radius: 4px; overflow-x: auto; margin-top: 1rem; color: var(--text-color);">
       Input State           Alice's Measurement        Classical Channel
|ψ⟩: ─────[   ]────────■──────────[ H ]───────── ✂ Measure ═══════════════ (c_1) ══╗
           │           │                                                           ║
q_0: ──|0⟩─┤   ├───■───X──────────────────────── ✂ Measure ════════ (c_0) ══╗      ║
           │   │   │                                                        ║      ║
q_1: ──|0⟩─[   ]───X────────────────────────────────────────────────────────X──────Z───── |ψ⟩
               Shared Entanglement                                    Bob's Corrections</pre>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Circuit image placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>4. Mathematical Proof & State Evolution</h2>
        
        <h3 style="margin-top: 1.5rem;">Step 1: Initial State</h3>
        <p>Alice wants to teleport an unknown pure state \(|\psi\rangle = \alpha|0\rangle + \beta|1\rangle\).<br>The system starts with this state and a pre-shared Bell pair \(|\Phi^+\rangle\) between Alice (\(q_0\)) and Bob (\(q_1\)):</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_0\rangle = |\psi\rangle \otimes |\Phi^+\rangle = (\alpha|0\rangle + \beta|1\rangle) \otimes \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)\)</p>
        </div>
        <p>Expanding this three-qubit state yields:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_0\rangle = \frac{1}{\sqrt{2}} \left[ \alpha|000\rangle + \alpha|011\rangle + \beta|100\rangle + \beta|111\rangle \right]\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 2: Alice Applies CNOT</h3>
        <p>Alice applies a \(CX\) gate using her message qubit \(|\psi\rangle\) as the control and her entangled half (\(q_0\)) as the target.</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_1\rangle = \frac{1}{\sqrt{2}} \left[ \alpha|000\rangle + \alpha|011\rangle + \beta|110\rangle + \beta|101\rangle \right]\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 3: Alice Applies Hadamard</h3>
        <p>Alice applies a Hadamard gate to the message qubit:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_2\rangle = \frac{1}{2} \left[ \alpha(|0\rangle+|1\rangle)|00\rangle + \alpha(|0\rangle+|1\rangle)|11\rangle + \beta(|0\rangle-|1\rangle)|10\rangle + \beta(|0\rangle-|1\rangle)|01\rangle \right]\)</p>
        </div>
        <p>By rearranging and grouping the terms based on Alice's two qubits (the first two qubits), we reveal the state of Bob's qubit for each possible measurement outcome:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_2\rangle = \frac{1}{2} \left[ |00\rangle(\alpha|0\rangle + \beta|1\rangle) + |01\rangle(\alpha|1\rangle + \beta|0\rangle) + |10\rangle(\alpha|0\rangle - \beta|1\rangle) + |11\rangle(\alpha|1\rangle - \beta|0\rangle) \right]\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 4: Measurement and Correction</h3>
        <p>Alice measures her two qubits. Bob's qubit collapses into one of four states. He applies corrections based on the classical bits (\(c_1, c_0\)) Alice sends him:</p>
        
        <table style="width: 100%; border-collapse: collapse; margin-top: 1rem;">
            <thead>
                <tr style="border-bottom: 2px solid var(--border-color); text-align: left;">
                    <th style="padding: 0.5rem;">Alice Measures (\(c_1 c_0\))</th>
                    <th style="padding: 0.5rem;">Bob's Resulting State</th>
                    <th style="padding: 0.5rem;">Bob's Correction</th>
                    <th style="padding: 0.5rem;">Final State</th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom: 1px solid var(--border-color);">
                    <td style="padding: 0.5rem;"><code>00</code></td>
                    <td style="padding: 0.5rem;">\(\alpha|0\rangle + \beta|1\rangle\)</td>
                    <td style="padding: 0.5rem;">Apply \(I\) (Do nothing)</td>
                    <td style="padding: 0.5rem;">\(\alpha|0\rangle + \beta|1\rangle = |\psi\rangle\)</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border-color);">
                    <td style="padding: 0.5rem;"><code>01</code></td>
                    <td style="padding: 0.5rem;">\(\alpha|1\rangle + \beta|0\rangle\)</td>
                    <td style="padding: 0.5rem;">Apply \(X\) (Bit flip)</td>
                    <td style="padding: 0.5rem;">\(\alpha|0\rangle + \beta|1\rangle = |\psi\rangle\)</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border-color);">
                    <td style="padding: 0.5rem;"><code>10</code></td>
                    <td style="padding: 0.5rem;">\(\alpha|0\rangle - \beta|1\rangle\)</td>
                    <td style="padding: 0.5rem;">Apply \(Z\) (Phase flip)</td>
                    <td style="padding: 0.5rem;">\(\alpha|0\rangle + \beta|1\rangle = |\psi\rangle\)</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border-color);">
                    <td style="padding: 0.5rem;"><code>11</code></td>
                    <td style="padding: 0.5rem;">\(\alpha|1\rangle - \beta|0\rangle\)</td>
                    <td style="padding: 0.5rem;">Apply \(X\) then \(Z\)</td>
                    <td style="padding: 0.5rem;">\(\alpha|0\rangle + \beta|1\rangle = |\psi\rangle\)</td>
                </tr>
            </tbody>
        </table>
    </section>

    <section class="content-section">
        <h2>5. Interactive Visualisation</h2>
        <ul style="line-height: 1.6;">
            <li><strong>State Destruction (No-Cloning):</strong> As Alice applies her initial \(CX\) and \(H\) gates, the Bloch sphere representing her input message \(|\psi\rangle\) will visibly degrade into a completely mixed state (the vector vanishes to the centre of the sphere). The information leaves her local possession.</li>
            <li><strong>Conditional Recreation:</strong> Watch Bob's Bloch sphere. Upon Alice's measurement, his vector jumps to a seemingly random position. When the classical bits arrive and the \(X/Z\) gates are applied, his vector snaps instantly to match the exact original coordinates of \(|\psi\rangle\).</li>
        </ul>
        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg></div>
            <h3>Dynamic State Tracking</h3>
            <p>Interactive module (amplitude histograms, Bloch spheres) to simulate the algorithm live.</p>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Interactive visualization placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>6. Python Code Implementation</h2>
        
        <h3>From Scratch (NumPy)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / NumPy</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>import numpy as np

def simulate_teleportation(alpha, beta):
    \"\"\"
    Simulates Quantum Teleportation using pure NumPy matrix multiplication.
    alpha, beta: Complex probability amplitudes of the initial state.
    \"\"\"
    I = np.eye(2, dtype=complex)
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)
    
    # 3-Qubit Identity
    I_8 = np.eye(8, dtype=complex)

    # Prepare initial state: |psi> x |Phi+>
    psi_in = np.array([[alpha], [beta]])
    phi_plus = np.array([[1/np.sqrt(2)], [0], [0], [1/np.sqrt(2)]])
    state_0 = np.kron(psi_in, phi_plus)

    # Alice applies CX(0 -> 1)
    # (Matrix formulation of CX on Q0, Q1 tensored with I on Q2 omitted for brevity in scratch code)
    # The mathematical logic dictates Bob's state collapses based on Alice's measurement.
    
    # Simulating the post-measurement collapse for outcome '11'
    # Bob's uncorrected state is (alpha|1> - beta|0>)
    bob_uncorrected = np.array([[-beta], [alpha]]) 
    
    # Bob receives '11' and applies X then Z
    bob_corrected = np.dot(Z, np.dot(X, bob_uncorrected))
    
    return bob_corrected

# Example: Teleporting a specific state
alpha_val = np.sqrt(0.8)
beta_val = np.sqrt(0.2)
teleported_state = simulate_teleportation(alpha_val, beta_val)
print("Teleported State:\\n", teleported_state)
</code></pre>
            </div>
        </div>
        
        <h3 style="margin-top: 1.5rem;">Framework (Qiskit)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / Qiskit</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

def teleportation_circuit():
    qr = QuantumRegister(3, name="q")
    crz, crx = ClassicalRegister(1, name="crz"), ClassicalRegister(1, name="crx")
    qc = QuantumCircuit(qr, crz, crx)

    # 1. Prepare an arbitrary state to teleport (e.g., Rx rotation)
    qc.rx(1.57, 0)
    qc.barrier()

    # 2. Create shared Bell pair between Alice (q1) and Bob (q2)
    qc.h(1)
    qc.cx(1, 2)
    qc.barrier()

    # 3. Alice applies operations to her two qubits
    qc.cx(0, 1)
    qc.h(0)
    qc.barrier()

    # 4. Alice measures
    qc.measure(0, crz) # Measurement stored in crz
    qc.measure(1, crx) # Measurement stored in crx
    qc.barrier()

    # 5. Bob applies corrections dynamically
    qc.x(2).c_if(crx, 1) # Apply X if crx == 1
    qc.z(2).c_if(crz, 1) # Apply Z if crz == 1

    return qc

circuit = teleportation_circuit()
print(circuit.draw(output='text'))
</code></pre>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>7. Caveats & Real-World Limits</h2>
        <ul style="line-height: 1.6;">
            <li><strong>No Faster-than-Light Communication:</strong> Quantum Teleportation does not violate relativity. The state is only recovered after Bob receives the classical bits (\(c_1, c_0\)) from Alice. Since classical bits cannot travel faster than the speed of light, the teleportation protocol is bound by standard physical speed limits.</li>
            <li><strong>Entanglement Degradation:</strong> Teleporting over long distances (like via optical fibre or satellite) requires the initial Bell pair to remain pristine. In reality, environmental noise causes decoherence, meaning Bob will recreate a noisy, mixed version of \(|\psi\rangle\) rather than a perfect copy.</li>
            <li><strong>Destruction of the Original:</strong> In strict adherence to the No-Cloning Theorem, the input state \(|\psi\rangle\) is irrevocably destroyed on Alice's side during the Bell basis measurement.</li>
        </ul>
    </section>

    <section class="content-section">
        <h2>8. Applications</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Quantum Repeaters & Networks:</strong> It is impossible to amplify quantum signals like classical signals. Teleportation allows states to be "hopped" across a chain of entangled nodes, forming the backbone of the future Quantum Internet.</li>
            <li><strong>Distributed Quantum Computing:</strong> Allows multiple small, noisy quantum processors to be linked together to perform large-scale calculations by teleporting qubits between computational nodes.</li>
            <li><strong>Fault-Tolerant Gate Execution (Magic States):</strong> In error-corrected quantum computers, certain non-Clifford gates (like the T gate) are extremely difficult to implement directly. They are applied indirectly by preparing a special "magic state" offline and teleporting it into the main computation.</li>
        </ul>
    </section>
    
    <section class="content-section">
        <h2>9. References</h2>
        <ol style="line-height: 1.6;">
            <li>Bennett, C. H., Brassard, G., Crépeau, C., Jozsa, R., Peres, A., &amp; Wootters, W. K. (1993). Teleporting an unknown quantum state via dual classical and Einstein-Podolsky-Rosen channels. <em>Physical Review Letters</em>, 70(13), 1895–1899.</li>
            <li>Nielsen, M. A., &amp; Chuang, I. L. (2010). <em>Quantum Computation and Quantum Information</em> (10th Anniversary ed.). Cambridge University Press.</li>
        </ol>
    </section>

    <nav class="algorithm-nav">
        <a href="superdense-coding.html" class="nav-button">
            <span class="nav-label">Previous</span>
            <span class="nav-title">Superdense Coding</span>
        </a>
        <a href="entanglement-swapping.html" class="nav-button nav-next">
            <span class="nav-label">Next</span>
            <span class="nav-title">Entanglement Swapping</span>
        </a>
    </nav>
    """.replace("{title}", title).replace("{category_name}", category_name)
    
    with open(f"/Users/aghatasheersyedi/Desktop/latex/class/qiskit/aqca/algorithms/{category}/{filename}", 'w') as f:
        html = HTML_TEMPLATE.format(
            title=title,
            description=f"AQCA - {title}",
            root_path="../../",
            extra_css="",
            extra_js="",
            algorithms_expanded="true",
            content=content
        )
        f.write(html)


def generate_entanglement_swapping_page():
    title = "Entanglement Swapping"
    category_name = "Protocols & Foundations"
    filename = "entanglement-swapping.html"
    category = "foundations"
    
    content = r"""
    <div class="breadcrumb">
        <a href="../../index.html">Home</a> <span class="breadcrumb-separator">›</span> 
        <a href="../../algorithms.html">Algorithms</a> <span class="breadcrumb-separator">›</span> 
        {category_name} <span class="breadcrumb-separator">›</span> 
        {title}
    </div>

    <div class="algorithm-header">
        <h1>{title}</h1>
        <div class="algorithm-meta">
            <span class="badge badge-category">{category_name}</span>
        </div>
    </div>

    <section class="content-section">
        <h2>1. Overview & Problem Definition</h2>
        <p>The <strong>Entanglement Swapping</strong> protocol solves the problem of establishing quantum entanglement between two distant particles that have never directly interacted. It is effectively the teleportation of entanglement itself. If Alice and Charlie share an entangled pair, and Charlie and Bob share a separate entangled pair, Charlie can perform a local measurement that destroys his pairs but instantly entangles Alice's particle with Bob's.</p>
        <div class="complexity-comparison" style="margin-top: 1.5rem;">
            <div class="complexity-box">
                <h3>Classical Bit Cost</h3>
                <div class="complexity-value">2 bits</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">Charlie must transmit two classical bits to Bob to complete the swap.</p>
            </div>
            <div class="complexity-box">
                <h3>Quantum Qubit Cost</h3>
                <div class="complexity-value">2 EPR pairs</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">The protocol consumes two independent Bell pairs to generate one new long-distance Bell pair.</p>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>2. Intuition</h2>
        <p>Entanglement swapping can be conceptualised as a network relay for quantum correlations.</p>
        <ol style="line-height: 1.6; margin-left: 1.5rem;">
            <li><strong>Independent Pairs:</strong> Imagine two completely independent Bell pairs. Pair 1 is held by Alice and Charlie. Pair 2 is held by Charlie and Bob. At this stage, Alice's qubit has absolutely no quantum correlation with Bob's qubit.</li>
            <li><strong>The Intermediary (Charlie):</strong> Charlie now holds two unentangled qubits (one from Pair 1, one from Pair 2). He performs a joint Bell State Measurement (BSM) on his two qubits.</li>
            <li><strong>The Swap:</strong> Measuring Charlie's qubits forces them into an entangled state. Because of the mathematical structure of the combined four-qubit system, entangling the middle two qubits instantly collapses the outer two qubits (Alice's and Bob's) into an entangled state, despite them being separated by an arbitrary distance and never having crossed paths.</li>
            <li><strong>Correction:</strong> Just like in quantum teleportation, Charlie's measurement result is random. He sends his measurement outcome (two classical bits) to Bob, who applies the appropriate Pauli gates to rotate the new Alice-Bob entanglement into a predictable, standard Bell state.</li>
        </ol>
    </section>

    <section class="content-section">
        <h2>3. Required Gates & Circuit Schematic</h2>
        <p>The circuit requires gates to generate two separate Bell pairs, followed by a Bell-basis measurement and classical feedback.</p>
        <ul style="line-height: 1.6;">
            <li><strong>Hadamard (\(H\)) & Controlled-NOT (\(CX\)):</strong> Used on (\(q_0, q_1\)) and (\(q_2, q_3\)) to create the two initial Bell states.</li>
            <li><strong>Measurement (\(M\)):</strong> Charlie measures \(q_1\) and \(q_2\) in the Bell basis using a \(CX\), an \(H\), and standard \(Z\)-basis measurements.</li>
            <li><strong>Pauli-\(X\) and Pauli-\(Z\) Gates:</strong> Applied by Bob (\(q_3\)) as corrective rotations, controlled by Charlie's classical measurement outcomes.</li>
        </ul>

        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="10" rx="2" ry="2"></rect><line x1="12" y1="3" x2="12" y2="7"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg></div>
            <h3>Circuit Schematic</h3>
            <pre style="background: var(--code-bg); padding: 1rem; border-radius: 4px; overflow-x: auto; margin-top: 1rem; color: var(--text-color);">
       Pair 1 Creation       Charlie's BSM           Classical Channel
q_0: ──[ H ]───■──────────────────────────────────────────────────────── (Alice)
               │
q_1: ──────────X───────────────■─────[ H ]───── ✂ Measure ════ (c_1) ══╗
                               │                                       ║
q_2: ──[ H ]───■───────────────X─────────────── ✂ Measure ══ (c_0) ══╗ ║
               │                                                     ║ ║
q_3: ──────────X─────────────────────────────────────────────────────X─Z─ (Bob)
       Pair 2 Creation                                    Bob's Corrections</pre>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Circuit image placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>4. Mathematical Proof & State Evolution</h2>
        
        <h3 style="margin-top: 1.5rem;">Step 1: Preparing Two Independent Bell Pairs</h3>
        <p>Alice (\(q_0\)) and Charlie (\(q_1\)) share a Bell pair. Charlie (\(q_2\)) and Bob (\(q_3\)) share a second Bell pair. The global initial state is:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_0\rangle = |\Phi^+\rangle_{01} \otimes |\Phi^+\rangle_{23} = \left( \frac{|00\rangle + |11\rangle}{\sqrt{2}} \right)_{01} \otimes \left( \frac{|00\rangle + |11\rangle}{\sqrt{2}} \right)_{23}\)</p>
        </div>
        <p>Expanding this four-qubit state yields:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_0\rangle = \frac{1}{2} \big( |0000\rangle + |0011\rangle + |1100\rangle + |1111\rangle \big)_{0123}\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 2: Bell Basis Rewrite</h3>
        <p>Charlie holds qubits \(q_1\) and \(q_2\). We can mathematically regroup the terms by rewriting the computational basis of Charlie's qubits in terms of the four Bell states (\(|\Phi^\pm\rangle_{12}, |\Psi^\pm\rangle_{12}\)). Through algebraic rearrangement, the global state can be perfectly re-expressed as:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_0\rangle = \frac{1}{2} \Big[ |\Phi^+\rangle_{12}|\Phi^+\rangle_{03} + |\Phi^-\rangle_{12}|\Phi^-\rangle_{03} + |\Psi^+\rangle_{12}|\Psi^+\rangle_{03} + |\Psi^-\rangle_{12}|\Psi^-\rangle_{03} \Big]\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 3: Bell State Measurement (BSM)</h3>
        <p>Charlie applies a \(CX\) gate (control \(q_1\), target \(q_2\)) followed by a Hadamard on \(q_1\), and then measures both. According to the rearranged equation above, finding his qubits in a specific Bell state instantly collapses the state of the outer qubits (\(q_0\) and \(q_3\)) into the corresponding entangled Bell state.</p>

        <h3 style="margin-top: 1.5rem;">Step 4: Classical Communication and Correction</h3>
        <p>Charlie sends his two classical measurement bits (\(c_1, c_0\)) to Bob. Bob applies Pauli corrections to \(q_3\) to deterministically align their shared state back to the standard \(|\Phi^+\rangle_{03}\).</p>
        
        <table style="width: 100%; border-collapse: collapse; margin-top: 1rem;">
            <thead>
                <tr style="border-bottom: 2px solid var(--border-color); text-align: left;">
                    <th style="padding: 0.5rem;">Charlie Measures (\(c_1 c_0\))</th>
                    <th style="padding: 0.5rem;">Implies State (\(q_1, q_2\))</th>
                    <th style="padding: 0.5rem;">Collapsed State (\(q_0, q_3\))</th>
                    <th style="padding: 0.5rem;">Bob's Correction</th>
                    <th style="padding: 0.5rem;">Final State (\(q_0, q_3\))</th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom: 1px solid var(--border-color);">
                    <td style="padding: 0.5rem;"><code>00</code></td>
                    <td style="padding: 0.5rem;">\(|\Phi^+\rangle\)</td>
                    <td style="padding: 0.5rem;">\(|\Phi^+\rangle\)</td>
                    <td style="padding: 0.5rem;">Apply \(I\)</td>
                    <td style="padding: 0.5rem;">\(|\Phi^+\rangle\)</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border-color);">
                    <td style="padding: 0.5rem;"><code>01</code></td>
                    <td style="padding: 0.5rem;">\(|\Psi^+\rangle\)</td>
                    <td style="padding: 0.5rem;">\(|\Psi^+\rangle\)</td>
                    <td style="padding: 0.5rem;">Apply \(X\)</td>
                    <td style="padding: 0.5rem;">\(|\Phi^+\rangle\)</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border-color);">
                    <td style="padding: 0.5rem;"><code>10</code></td>
                    <td style="padding: 0.5rem;">\(|\Phi^-\rangle\)</td>
                    <td style="padding: 0.5rem;">\(|\Phi^-\rangle\)</td>
                    <td style="padding: 0.5rem;">Apply \(Z\)</td>
                    <td style="padding: 0.5rem;">\(|\Phi^+\rangle\)</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border-color);">
                    <td style="padding: 0.5rem;"><code>11</code></td>
                    <td style="padding: 0.5rem;">\(|\Psi^-\rangle\)</td>
                    <td style="padding: 0.5rem;">\(|\Psi^-\rangle\)</td>
                    <td style="padding: 0.5rem;">Apply \(X\) then \(Z\)</td>
                    <td style="padding: 0.5rem;">\(|\Phi^+\rangle\)</td>
                </tr>
            </tbody>
        </table>
    </section>

    <section class="content-section">
        <h2>5. Interactive Visualisation</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Density Matrix Trace (Pre-BSM):</strong> If you trace out Charlie's qubits before he measures them, the reduced density matrix of Alice and Bob's qubits (\(q_0, q_3\)) is a completely mixed separable state \(\rho_{03} = \frac{1}{4} I_4\). There is no entanglement between them.</li>
            <li><strong>Density Matrix Trace (Post-BSM):</strong> The moment Charlie's measurement completes, the reduced density matrix \(\rho_{03}\) instantaneously snaps into a pure entangled state.</li>
            <li><strong>Corrective Snapping:</strong> When watching the \(q_0\) and \(q_3\) state vector visually, it will appear as one of the four Bell states randomly. As the classical bits arrive and Bob applies \(X/Z\), the state will always align into the \(|\Phi^+\rangle\) configuration.</li>
        </ul>
        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg></div>
            <h3>Dynamic State Tracking</h3>
            <p>Interactive module (amplitude histograms, Bloch spheres) to simulate the algorithm live.</p>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Interactive visualization placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>6. Python Code Implementation</h2>
        
        <h3>From Scratch (NumPy)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / NumPy</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>import numpy as np

def simulate_entanglement_swapping():
    \"\"\"
    Simulates Entanglement Swapping using pure NumPy matrix multiplication.
    \"\"\"
    I = np.eye(2, dtype=complex)
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    
    # Define Bell state Phi+
    phi_plus = np.array([[1/np.sqrt(2)], [0], [0], [1/np.sqrt(2)]])
    
    # Initial state: |Phi+>_01 (X) |Phi+>_23
    psi_init = np.kron(phi_plus, phi_plus)
    
    # Charlie performs BSM on q1 and q2
    # In a full matrix implementation, you would construct the 16x16 CX and H matrices
    # For simulation, we can directly collapse the state based on the theoretical math.
    
    # Assume Charlie measures '01' (which corresponds to |Psi+>_12)
    # The state of q0 and q3 collapses to |Psi+>_03
    q0_q3_collapsed = np.array([[0], [1/np.sqrt(2)], [1/np.sqrt(2)], [0]])
    
    # Bob receives '01' and applies X to q3 to correct it back to |Phi+>
    correction = np.kron(I, X) # I on q0, X on q3
    q0_q3_final = np.dot(correction, q0_q3_collapsed)
    
    return q0_q3_final

print("Final Swapped State (q0, q3):\\n", simulate_entanglement_swapping())
</code></pre>
            </div>
        </div>
        
        <h3 style="margin-top: 1.5rem;">Framework (Qiskit)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / Qiskit</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

def entanglement_swapping_circuit():
    qr = QuantumRegister(4, name="q")
    crz = ClassicalRegister(1, name="crz")
    crx = ClassicalRegister(1, name="crx")
    qc = QuantumCircuit(qr, crz, crx)

    # 1. Prepare Pair 1 (Alice q0, Charlie q1)
    qc.h(0)
    qc.cx(0, 1)

    # 2. Prepare Pair 2 (Charlie q2, Bob q3)
    qc.h(2)
    qc.cx(2, 3)
    qc.barrier(label="Pairs Ready")

    # 3. Charlie performs Bell State Measurement on q1 and q2
    qc.cx(1, 2)
    qc.h(1)
    qc.barrier()

    qc.measure(1, crz)
    qc.measure(2, crx)
    qc.barrier(label="Classical Channel")

    # 4. Bob applies corrections to q3
    qc.x(3).c_if(crx, 1)
    qc.z(3).c_if(crz, 1)

    return qc

circuit = entanglement_swapping_circuit()
print(circuit.draw(output='text'))
</code></pre>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>7. Caveats & Real-World Limits</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Photon Loss:</strong> In practical free-space or optical fibre implementations, transmitting the initial pairs to Charlie suffers from severe attenuation. If Charlie fails to receive even one photon, the swapping protocol fails entirely.</li>
            <li><strong>Detector Inefficiency:</strong> Real-world Bell state measurements relying on linear optics cannot deterministically distinguish all four Bell states (they are limited to a maximum success rate of 50% without hyper-entanglement or nonlinear interactions).</li>
            <li><strong>Fidelity Degradation:</strong> Every time entanglement is swapped, the noise from the initial pairs and the measurement errors compound. The final swapped pair (\(\rho_{03}\)) will always have a lower entanglement fidelity than the starting pairs.</li>
        </ul>
    </section>

    <section class="content-section">
        <h2>8. Applications</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Quantum Repeaters:</strong> Because quantum states cannot be cloned to boost signal strength, entanglement swapping is the only physical mechanism capable of distributing entanglement across intercontinental distances. A chain of repeaters swaps entanglement node-by-node until Alice and Bob share a link.</li>
            <li><strong>Quantum Network Routing:</strong> Allows a quantum internet to dynamically route connections. If a node goes down, entanglement swapping can bridge alternative paths to maintain the network topology.</li>
            <li><strong>Device-Independent Cryptography:</strong> Enables secure key distribution protocols that do not require trusting the intermediate nodes (like Charlie's relay station).</li>
        </ul>
    </section>
    
    <section class="content-section">
        <h2>9. References</h2>
        <ol style="line-height: 1.6;">
            <li>Żukowski, M., Zeilinger, A., Horne, M. A., &amp; Ekert, A. K. (1993). "Event-ready-detectors" Bell experiment via entanglement swapping. <em>Physical Review Letters</em>, 71(26), 4287–4290.</li>
            <li>Pan, J. W., Bouwmeester, D., Weinfurter, H., &amp; Zeilinger, A. (1998). Experimental entanglement swapping: entangling photons that never interacted. <em>Physical Review Letters</em>, 80(18), 3891–3894.</li>
            <li>Nielsen, M. A., &amp; Chuang, I. L. (2010). <em>Quantum Computation and Quantum Information</em> (10th Anniversary ed.). Cambridge University Press.</li>
        </ol>
    </section>

    <nav class="algorithm-nav">
        <a href="quantum-teleportation.html" class="nav-button">
            <span class="nav-label">Previous</span>
            <span class="nav-title">Quantum Teleportation</span>
        </a>
        <a href="../oracle-based/deutsch.html" class="nav-button nav-next">
            <span class="nav-label">Next</span>
            <span class="nav-title">Deutsch's Algorithm</span>
        </a>
    </nav>
    """.replace("{title}", title).replace("{category_name}", category_name)
    
    with open(f"/Users/aghatasheersyedi/Desktop/latex/class/qiskit/aqca/algorithms/{category}/{filename}", 'w') as f:
        html = HTML_TEMPLATE.format(
            title=title,
            description=f"AQCA - {title}",
            root_path="../../",
            extra_css="",
            extra_js="",
            algorithms_expanded="true",
            content=content
        )
        f.write(html)


def generate_deutsch_algorithm_page():
    title = "Deutsch's Algorithm"
    category_name = "Oracle-Based"
    filename = "deutsch.html"
    category = "oracle-based"
    
    content = r"""
    <div class="breadcrumb">
        <a href="../../index.html">Home</a> <span class="breadcrumb-separator">›</span> 
        <a href="../../algorithms.html">Algorithms</a> <span class="breadcrumb-separator">›</span> 
        {category_name} <span class="breadcrumb-separator">›</span> 
        {title}
    </div>

    <div class="algorithm-header">
        <h1>{title}</h1>
        <div class="algorithm-meta">
            <span class="badge badge-category">{category_name}</span>
        </div>
    </div>

    <section class="content-section">
        <h2>1. Overview & Problem Definition</h2>
        <p><strong>Deutsch’s Algorithm</strong> was the first algorithm to demonstrate a rigorous, mathematical quantum advantage over classical computers.</p>
        <p>Imagine you are given a "black box" function (an oracle) that takes a single binary input (0 or 1) and produces a single binary output (0 or 1). There are only four possible such functions, which fall into two categories:</p>
        <ul style="line-height: 1.6;">
            <li><strong>Constant:</strong> The output is the same for both inputs (always 0, or always 1). So, \(f(0) = f(1)\).</li>
            <li><strong>Balanced:</strong> The output is different for both inputs (returns 0 for one input and 1 for the other). So, \(f(0) \neq f(1)\).</li>
        </ul>
        <p>The problem is to determine whether the hidden function is constant or balanced with the absolute minimum number of queries to the oracle.</p>

        <div class="complexity-comparison" style="margin-top: 1.5rem;">
            <div class="complexity-box">
                <h3>Classical Complexity</h3>
                <div class="complexity-value">\(\mathcal{O}(2)\)</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">A classical computer must evaluate both \(f(0)\) and \(f(1)\) to compare them.</p>
            </div>
            <div class="complexity-box">
                <h3>Quantum Speedup</h3>
                <div class="complexity-value">\(\mathcal{O}(1)\)</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">A quantum computer evaluates the oracle exactly once to find the answer.</p>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>2. Intuition</h2>
        <p>To solve this classically, you have to query the black box twice, looking at the answers one by one.</p>
        <p>In the quantum world, we can query the function using a <strong>superposition</strong> of both 0 and 1 simultaneously. However, simply getting a superposition of the answers is not enough, because measuring it would just randomly collapse it to one answer, forcing us to run it again.</p>
        <p>The brilliance of Deutsch's Algorithm lies in a trick called <strong>Phase Kickback</strong>. By preparing the target (output) qubit in a specific negative superposition state, the oracle's output does not alter the state of the target qubit; instead, it "kicks back" a phase shift (a minus sign) onto the input qubit.</p>
        <ul style="line-height: 1.6;">
            <li>If the function is constant, the phases of the input superposition stay aligned.</li>
            <li>If the function is balanced, the phases shift, inverting the superposition.</li>
        </ul>
        <p>A final Hadamard gate then perfectly maps this phase difference into a deterministic measurement: \(|0\rangle\) means constant, and \(|1\rangle\) means balanced.</p>
    </section>

    <section class="content-section">
        <h2>3. Required Gates & Circuit Schematic</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Pauli-\(X\) (\(X\)):</strong> Used to flip the target qubit from \(|0\rangle\) to \(|1\rangle\) prior to the Hadamard gate.</li>
            <li><strong>Hadamard (\(H\)):</strong> Used to create superpositions and later to interfere the phases back into a measurable basis state.</li>
            <li><strong>Quantum Oracle (\(U_f\)):</strong> A unitary matrix representing the black box function, acting on the input and target qubits as \(U_f |x\rangle|y\rangle = |x\rangle|y \oplus f(x)\rangle\).</li>
        </ul>

        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="10" rx="2" ry="2"></rect><line x1="12" y1="3" x2="12" y2="7"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg></div>
            <h3>Circuit Schematic</h3>
            <pre style="background: var(--code-bg); padding: 1rem; border-radius: 4px; overflow-x: auto; margin-top: 1rem; color: var(--text-color);">
       ┌───┐                ┌───┐
q_0: ──┤ H ├───────■────────┤ H ├─── ✂ Measure
       ├───┤ ┌───┐ │ (U_f)  └───┘
q_1: ──┤ X ├─┤ H ├─■────────────────
       └───┘ └───┘</pre>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">*(Note: \(q_0\) is the input qubit, and \(q_1\) is the target/ancilla qubit).*</p>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Circuit image placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>4. Mathematical Proof & State Evolution</h2>
        
        <h3 style="margin-top: 1.5rem;">Step 1: Initialisation</h3>
        <p>The system starts with the input qubit in \(|0\rangle\) and the target qubit flipped to \(|1\rangle\) using an \(X\) gate:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_0\rangle = |0\rangle \otimes |1\rangle\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 2: Applying the Hadamard Gates</h3>
        <p>We apply Hadamard gates to both qubits to create the required superpositions:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_1\rangle = (H \otimes H)|\psi_0\rangle = \left( \frac{|0\rangle + |1\rangle}{\sqrt{2}} \right) \otimes \left( \frac{|0\rangle - |1\rangle}{\sqrt{2}} \right)\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 3: The Oracle Query & Phase Kickback</h3>
        <p>We apply the oracle \(U_f\). Because the target qubit is in the \(|-\rangle\) state, the action \(y \oplus f(x)\) translates into a phase factor \((-1)^{f(x)}\) on the input state:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_2\rangle = U_f |\psi_1\rangle = \frac{1}{2} \left[ (-1)^{f(0)}|0\rangle + (-1)^{f(1)}|1\rangle \right] \otimes (|0\rangle - |1\rangle)\)</p>
        </div>
        <p>We can factor out \((-1)^{f(0)}\) from the input qubit:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_2\rangle = (-1)^{f(0)} \left( \frac{|0\rangle + (-1)^{f(0) \oplus f(1)}|1\rangle}{\sqrt{2}} \right) \otimes |-\rangle\)</p>
        </div>
        <ul style="line-height: 1.6;">
            <li><strong>If Constant (\(f(0) = f(1)\)):</strong> \(f(0) \oplus f(1) = 0\), so \((-1)^0 = 1\). The input state is \(\frac{|0\rangle + |1\rangle}{\sqrt{2}} = |+\rangle\).</li>
            <li><strong>If Balanced (\(f(0) \neq f(1)\)):</strong> \(f(0) \oplus f(1) = 1\), so \((-1)^1 = -1\). The input state is \(\frac{|0\rangle - |1\rangle}{\sqrt{2}} = |-\rangle\).</li>
        </ul>

        <h3 style="margin-top: 1.5rem;">Step 4: Final Interference</h3>
        <p>We apply a final Hadamard gate to the input qubit (\(q_0\)). The target qubit is ignored.</p>
        <ul style="line-height: 1.6;">
            <li><strong>If Constant:</strong> \(H|+\rangle = |0\rangle\). (The global phase \((-1)^{f(0)}\) is physically unobservable).</li>
            <li><strong>If Balanced:</strong> \(H|-\rangle = |1\rangle\).</li>
        </ul>

        <h3 style="margin-top: 1.5rem;">Measurement</h3>
        <p>Measuring \(q_0\) in the computational basis perfectly yields:</p>
        <ul style="line-height: 1.6;">
            <li><code>0</code> with \(100\%\) probability if the function is <strong>constant</strong>.</li>
            <li><code>1</code> with \(100\%\) probability if the function is <strong>balanced</strong>.</li>
        </ul>
    </section>

    <section class="content-section">
        <h2>5. Interactive Visualisation</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Bloch Sphere (Input Qubit):</strong>
                <ol>
                    <li>After the first \(H\) gate, the vector points along the positive X-axis (\(|+\rangle\)).</li>
                    <li>As the Oracle is applied, watch the phase kickback: if the function is balanced, the vector immediately rotates 180 degrees around the Z-axis to point along the negative X-axis (\(|-\rangle\)). If constant, it stays still.</li>
                    <li>The final \(H\) gate forces the vector to snap to the North Pole (\(|0\rangle\)) if constant, or the South Pole (\(|1\rangle\)) if balanced.</li>
                </ol>
            </li>
            <li><strong>Amplitude Histogram:</strong> Before the final \(H\) gate, both \(|0\rangle\) and \(|1\rangle\) have a 50% probability, regardless of the oracle. The interference step is what deterministically shifts all the amplitude to a single correct bar.</li>
        </ul>
        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg></div>
            <h3>Dynamic State Tracking</h3>
            <p>Interactive module (amplitude histograms, Bloch spheres) to simulate the algorithm live.</p>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Interactive visualization placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>6. Python Code Implementation</h2>
        
        <h3>From Scratch (NumPy)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / NumPy</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>import numpy as np

def simulate_deutsch(oracle_type):
    \"\"\"
    Simulates Deutsch's Algorithm using pure NumPy.
    oracle_type: 'constant_0', 'constant_1', 'balanced_id', 'balanced_not'
    \"\"\"
    H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)
    I = np.eye(2, dtype=complex)
    
    # Oracles (acting on |input> (x) |target>)
    oracles = {
        'constant_0': np.eye(4, dtype=complex),
        'constant_1': np.kron(I, np.array([[0, 1], [1, 0]], dtype=complex)), # X on target
        'balanced_id': np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], dtype=complex), # CNOT
        'balanced_not': np.array([[0, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0]], dtype=complex) # Zero-controlled NOT
    }
    
    U_f = oracles[oracle_type]
    
    # 1. Initialise |0>|1>
    q0 = np.array([[1], [0]])
    q1 = np.array([[0], [1]])
    psi_0 = np.kron(q0, q1)
    
    # 2. Apply H to both
    H2 = np.kron(H, H)
    psi_1 = np.dot(H2, psi_0)
    
    # 3. Apply Oracle
    psi_2 = np.dot(U_f, psi_1)
    
    # 4. Apply H to input qubit
    psi_final = np.dot(np.kron(H, I), psi_2)
    
    # 5. Measure input qubit
    prob_0 = np.abs(psi_final[0][0])**2 + np.abs(psi_final[1][0])**2
    return 'Constant' if prob_0 > 0.99 else 'Balanced'

print("Testing Balanced Oracle:", simulate_deutsch('balanced_id'))
</code></pre>
            </div>
        </div>
        
        <h3 style="margin-top: 1.5rem;">Framework (Qiskit)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / Qiskit</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def deutsch_circuit(oracle_type="balanced"):
    qc = QuantumCircuit(2, 1)
    
    # 1. Prepare target qubit in |-> state
    qc.x(1)
    qc.h(0)
    qc.h(1)
    qc.barrier()
    
    # 2. Oracle Application
    if oracle_type == "balanced":
        qc.cx(0, 1) # CNOT creates a balanced function (f(x) = x)
    elif oracle_type == "constant":
        pass # Identity creates a constant function (f(x) = 0)
        
    qc.barrier()
    
    # 3. Final Interference
    qc.h(0)
    
    # 4. Measurement
    qc.measure(0, 0)
    return qc

# Simulate
circuit = deutsch_circuit("balanced")
simulator = AerSimulator()
result = simulator.run(circuit, shots=1).result()
counts = result.get_counts()
print("Result (0=Constant, 1=Balanced):", counts)
</code></pre>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>7. Caveats & Real-World Limits</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Oracle Implementation Cost:</strong> The algorithm assumes the oracle \(U_f\) is given to us as a black box that takes \(\mathcal{O}(1)\) time to run. In reality, building the reversible quantum circuit to represent a complex classical function can require significant gate depth, which introduces noise.</li>
            <li><strong>Limited Utility:</strong> Deutsch's algorithm solves a highly contrived mathematical problem that has no practical real-world application. Its true value is purely educational—proving that quantum computers can perform tasks with fewer operations than classical computers.</li>
        </ul>
    </section>

    <section class="content-section">
        <h2>8. Applications</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Pedagogical Foundation:</strong> It is universally used as the first teaching algorithm in quantum computing because it perfectly demonstrates superposition, quantum parallelism, phase kickback, and interference in a two-qubit circuit.</li>
            <li><strong>The Precursor:</strong> It forms the direct mathematical baseline for the <strong>Deutsch–Jozsa algorithm</strong> (which scales the problem up to \(n\) qubits) and later algorithms like Grover's and Simon's, which utilise the exact same phase kickback mechanism.</li>
        </ul>
    </section>
    
    <section class="content-section">
        <h2>9. References</h2>
        <ol style="line-height: 1.6;">
            <li>Deutsch, D. (1985). Quantum theory, the Church-Turing principle and the universal quantum computer. <em>Proceedings of the Royal Society of London. A. Mathematical and Physical Sciences</em>, 400(1818), 97–117.</li>
            <li>Nielsen, M. A., &amp; Chuang, I. L. (2010). <em>Quantum Computation and Quantum Information</em> (10th Anniversary ed.). Cambridge University Press.</li>
        </ol>
    </section>

    <nav class="algorithm-nav">
        <a href="../../algorithms.html" class="nav-button">
            <span class="nav-label">Previous</span>
            <span class="nav-title">Algorithm Catalogue</span>
        </a>
        <a href="deutsch-jozsa.html" class="nav-button nav-next">
            <span class="nav-label">Next</span>
            <span class="nav-title">Deutsch-Jozsa Algorithm</span>
        </a>
    </nav>
    """.replace("{title}", title).replace("{category_name}", category_name)
    
    with open(f"/Users/aghatasheersyedi/Desktop/latex/class/qiskit/aqca/algorithms/{category}/{filename}", 'w') as f:
        html = HTML_TEMPLATE.format(
            title=title,
            description=f"AQCA - {title}",
            root_path="../../",
            extra_css="",
            extra_js="",
            algorithms_expanded="true",
            content=content
        )
        f.write(html)


def generate_deutsch_jozsa_algorithm_page():
    title = "Deutsch–Jozsa Algorithm"
    category_name = "Oracle-Based"
    filename = "deutsch-jozsa.html"
    category = "oracle-based"
    
    content = r"""
    <div class="breadcrumb">
        <a href="../../index.html">Home</a> <span class="breadcrumb-separator">›</span> 
        <a href="../../algorithms.html">Algorithms</a> <span class="breadcrumb-separator">›</span> 
        {category_name} <span class="breadcrumb-separator">›</span> 
        {title}
    </div>

    <div class="algorithm-header">
        <h1>{title}</h1>
        <div class="algorithm-meta">
            <span class="badge badge-category">{category_name}</span>
        </div>
    </div>

    <section class="content-section">
        <h2>1. Overview & Problem Definition</h2>
        <p>The <strong>Deutsch–Jozsa Algorithm</strong> is the generalisation of Deutsch’s Algorithm. It expands the problem from a single input bit to a function that takes an \(n\)-bit string as input.</p>
        <p>You are given a black-box quantum oracle that evaluates a function \(f: \{0,1\}^n \rightarrow \{0,1\}\). You are given a strict promise: the function is either <strong>exactly constant</strong> (returns the same value for all \(2^n\) possible inputs) or <strong>exactly balanced</strong> (returns 0 for exactly half of the inputs, and 1 for the other half). The goal is to determine which property the function holds with the fewest possible queries to the oracle.</p>

        <div class="complexity-comparison" style="margin-top: 1.5rem;">
            <div class="complexity-box">
                <h3>Classical Complexity</h3>
                <div class="complexity-value">\(\mathcal{O}(2^{n-1} + 1)\)</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">In the worst-case scenario, you must evaluate half the possible inputs plus one to be absolutely certain it is not balanced.</p>
            </div>
            <div class="complexity-box">
                <h3>Quantum Speedup</h3>
                <div class="complexity-value">\(\mathcal{O}(1)\)</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">A quantum computer evaluates the oracle exactly once to determine the answer, yielding an <strong>exponential speedup</strong> in query complexity.</p>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>2. Intuition</h2>
        <p>If you have \(n\) bits, there are \(2^n\) possible combinations. Classically, you have to check them one by one.</p>
        <p>The Deutsch–Jozsa algorithm leverages <strong>quantum parallelism</strong> to evaluate the function for all \(2^n\) inputs simultaneously using an equal superposition. By applying the phase kickback trick to a target qubit in the \(|-\rangle\) state, the oracle writes the function's output as a phase shift (a positive or negative sign) directly onto the corresponding amplitude of each input state.</p>
        <p>When you apply a final layer of Hadamard gates, these phases cause <strong>quantum interference</strong>:</p>
        <ul style="line-height: 1.6;">
            <li>If the function is constant, all the amplitudes have the same sign. They constructively interfere, snapping the state perfectly back to the all-zero state \(|00\dots0\rangle\).</li>
            <li>If the function is balanced, exactly half the amplitudes are positive and half are negative. They destructively interfere, cancelling out the probability of measuring the all-zero state to exactly zero.</li>
        </ul>
    </section>

    <section class="content-section">
        <h2>3. Required Gates & Circuit Schematic</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Pauli-\(X\) (\(X\)):</strong> Used to prepare the target (ancilla) qubit in the \(|1\rangle\) state.</li>
            <li><strong>Hadamard (\(H^{\otimes n}\)):</strong> Applied to all \(n\) input qubits to create a massive superposition, and later to interfere the states.</li>
            <li><strong>Quantum Oracle (\(U_f\)):</strong> An \((n+1)\)-qubit unitary matrix that applies \(U_f |x\rangle|y\rangle = |x\rangle|y \oplus f(x)\rangle\).</li>
        </ul>

        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="10" rx="2" ry="2"></rect><line x1="12" y1="3" x2="12" y2="7"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg></div>
            <h3>Circuit Schematic</h3>
            <pre style="background: var(--code-bg); padding: 1rem; border-radius: 4px; overflow-x: auto; margin-top: 1rem; color: var(--text-color);">
         ┌───┐                ┌───┐
  q_0: ──┤ H ├───────■────────┤ H ├─── ✂ Measure
         ├───┤       │        ├───┤
  q_1: ──┤ H ├───────■────────┤ H ├─── ✂ Measure
        ...         ...        ...
         ├───┤       │        ├───┤
q_n-1: ──┤ H ├───────■────────┤ H ├─── ✂ Measure
         ├───┤ ┌───┐ │ (U_f)  └───┘
  q_n: ──┤ X ├─┤ H ├─■──────────────── (Target)
         └───┘ └───┘</pre>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Circuit image placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>4. Mathematical Proof & State Evolution</h2>
        
        <h3 style="margin-top: 1.5rem;">Step 1: Initialisation</h3>
        <p>We start with \(n\) input qubits in \(|0\rangle\) and one target qubit in \(|1\rangle\):</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_0\rangle = |0\rangle^{\otimes n} \otimes |1\rangle\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 2: Applying the Hadamard Gates</h3>
        <p>Applying \(H\) to all qubits creates an equal superposition over all \(x \in \{0,1\}^n\):</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_1\rangle = (H^{\otimes n} \otimes H) |\psi_0\rangle = \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} |x\rangle \otimes \left( \frac{|0\rangle - |1\rangle}{\sqrt{2}} \right) = \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} |x\rangle \otimes |-\rangle\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 3: The Oracle Query & Phase Kickback</h3>
        <p>Applying the oracle \(U_f\) shifts the phase of each computational basis state \(|x\rangle\) based on the output of \(f(x)\):</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_2\rangle = U_f |\psi_1\rangle = \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} (-1)^{f(x)} |x\rangle \otimes |-\rangle\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 4: Final Interference</h3>
        <p>We apply \(H^{\otimes n}\) to the input register. The standard mathematical action of \(H^{\otimes n}\) on a basis state \(|x\rangle\) is \(\frac{1}{\sqrt{2^n}} \sum_{z} (-1)^{x \cdot z} |z\rangle\), where \(x \cdot z\) is the bitwise inner product modulo 2.</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_3\rangle = \frac{1}{2^n} \sum_{z=0}^{2^n-1} \left( \sum_{x=0}^{2^n-1} (-1)^{f(x) \oplus (x \cdot z)} \right) |z\rangle \otimes |-\rangle\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Measurement</h3>
        <p>We measure the input register. We are only interested in the probability of measuring the specific state where all qubits are zero, i.e., \(|z\rangle = |00\dots0\rangle\). For \(z=0\), the dot product \(x \cdot z = 0\) for all \(x\). The amplitude for the \(|00\dots0\rangle\) state is:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(A_{00\dots0} = \frac{1}{2^n} \sum_{x=0}^{2^n-1} (-1)^{f(x)}\)</p>
        </div>
        <ul style="line-height: 1.6;">
            <li><strong>If Constant:</strong> \(f(x)\) is always 0 or always 1. \(A_{00\dots0} = \pm \frac{2^n}{2^n} = \pm 1\). The probability of measuring all zeros is \(|\pm 1|^2 = 1\) (\(100\%\)).</li>
            <li><strong>If Balanced:</strong> \(f(x)\) is 0 for half the inputs and 1 for the other half. The \(+1\) and \(-1\) terms cancel each other out perfectly. \(A_{00\dots0} = 0\). The probability of measuring all zeros is \(0\%\).</li>
        </ul>
        <p>Therefore, if the measurement yields all zeros, the function is constant; if it yields any other string, the function is balanced.</p>
    </section>

    <section class="content-section">
        <h2>5. Interactive Visualisation</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Amplitude Histogram:</strong> During the intermediate stage (after the oracle), the histogram shows an equal probability for all \(2^n\) basis states. The final set of Hadamard gates initiates a massive interference event. If balanced, the \(|00\dots0\rangle\) bar visually drops to 0, while the remaining probability is spread across the other states. If constant, all bars shrink to 0 except \(|00\dots0\rangle\), which shoots up to 1.0.</li>
            <li><strong>Phase Disks:</strong> Representing the amplitudes as disks with phase-pointer arrows allows the user to see exactly half of the arrows flip their direction (180 degrees) after the balanced oracle query, visualising the kickback before the final interference.</li>
        </ul>
        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg></div>
            <h3>Dynamic State Tracking</h3>
            <p>Interactive module (amplitude histograms, Bloch spheres) to simulate the algorithm live.</p>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Interactive visualization placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>6. Python Code Implementation</h2>
        
        <h3>From Scratch (NumPy)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / NumPy</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>import numpy as np

def simulate_deutsch_jozsa_2bit(oracle_type):
    \"\"\"
    Simulates a 2-qubit input (+1 ancilla) Deutsch-Jozsa algorithm using NumPy.
    oracle_type: 'constant_0', 'balanced_cx'
    \"\"\"
    H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)
    I = np.eye(2, dtype=complex)
    
    # Tensored Hadamards for 2 inputs and 1 target
    H3 = np.kron(np.kron(H, H), H)
    H_in = np.kron(np.kron(H, H), I) # H on inputs, I on target
    
    # Oracles (8x8 matrices)
    if oracle_type == 'constant_0':
        U_f = np.eye(8, dtype=complex)
    elif oracle_type == 'balanced_cx':
        # CNOT controlled by q0 targeting q2
        U_f = np.array([
            [1,0,0,0,0,0,0,0], [0,1,0,0,0,0,0,0],
            [0,0,1,0,0,0,0,0], [0,0,0,1,0,0,0,0],
            [0,0,0,0,0,1,0,0], [0,0,0,0,1,0,0,0],
            [0,0,0,0,0,0,0,1], [0,0,0,0,0,0,1,0]
        ], dtype=complex)

    # 1. Initialise |00>|1>
    state_001 = np.zeros((8, 1), dtype=complex)
    state_001[1] = 1.0  # Index 1 corresponds to 001 in binary
    
    # 2. H on all qubits
    psi_1 = np.dot(H3, state_001)
    
    # 3. Apply Oracle
    psi_2 = np.dot(U_f, psi_1)
    
    # 4. Final H on input qubits
    psi_final = np.dot(H_in, psi_2)
    
    # 5. Measure input qubits (Checking probability of |00> target |0> or |1>)
    prob_00 = np.abs(psi_final[0][0])**2 + np.abs(psi_final[1][0])**2
    return 'Constant' if np.isclose(prob_00, 1.0) else 'Balanced'

print("NumPy DJ (Balanced Oracle):", simulate_deutsch_jozsa_2bit('balanced_cx'))
</code></pre>
            </div>
        </div>
        
        <h3 style="margin-top: 1.5rem;">Framework (Qiskit)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / Qiskit</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def dj_oracle(case, n):
    \"\"\"Generates an n-qubit Deutsch-Jozsa oracle.\"\"\"
    oracle_qc = QuantumCircuit(n + 1)
    
    if case == "balanced":
        # Apply CNOTs from each input to the target
        for qubit in range(n):
            oracle_qc.cx(qubit, n)
            
    elif case == "constant":
        # Do nothing (constant 0) or flip target (constant 1)
        pass 
        
    return oracle_qc

def dj_circuit(case, n):
    qc = QuantumCircuit(n + 1, n)
    
    # 1. Prepare Target in |->
    qc.x(n)
    qc.h(n)
    
    # 2. Prepare Inputs in superpositions
    for qubit in range(n):
        qc.h(qubit)
        
    qc.barrier()
    
    # 3. Apply Oracle
    oracle = dj_oracle(case, n)
    qc.compose(oracle, inplace=True)
    
    qc.barrier()
    
    # 4. Interfere Inputs
    for qubit in range(n):
        qc.h(qubit)
        
    # 5. Measure
    for i in range(n):
        qc.measure(i, i)
        
    return qc

# Simulate for n=3 qubits
n_qubits = 3
circuit = dj_circuit("balanced", n_qubits)
simulator = AerSimulator()
counts = simulator.run(circuit, shots=1024).result().get_counts()

# If counts are '000', it is constant. Anything else is balanced.
print("Result counts:", counts)
</code></pre>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>7. Caveats & Real-World Limits</h2>
        <ul style="line-height: 1.6;">
            <li><strong>The Oracle Promise:</strong> The algorithm only works because of the absolute promise that the function is strictly constant or strictly balanced. If the function is arbitrary (e.g., returns 0 for 75% of inputs and 1 for 25%), the final state will not perfectly destructively interfere, resulting in a noisy, probabilistic measurement that gives no definitive answer.</li>
            <li><strong>Oracle Scaling:</strong> While the algorithm requires only \(\mathcal{O}(1)\) query to the oracle, the physical gates required to <em>build</em> the unitary oracle \(U_f\) on hardware may scale exponentially with \(n\). Therefore, the overall time complexity of running the circuit is not necessarily \(\mathcal{O}(1)\).</li>
        </ul>
    </section>

    <section class="content-section">
        <h2>8. Applications</h2>
        <ul style="line-height: 1.6;">
            <li><strong>First Proof of Exponential Separation:</strong> Like Deutsch’s Algorithm, this algorithm has no immediate commercial application. Its importance is historical and mathematical. It was the first algorithm to rigorously prove that a quantum computer could solve a specific problem exponentially faster than any possible deterministic classical Turing machine.</li>
            <li><strong>Foundation for Modern Algorithms:</strong> The framework used here—creating an equal superposition, using an oracle to imprint phases, and then using a linear transform (like the Hadamard transform) to interfere the results—is the exact blueprint used in <strong>Simon's Algorithm</strong> and <strong>Shor's Algorithm</strong>.</li>
        </ul>
    </section>
    
    <section class="content-section">
        <h2>9. References</h2>
        <ol style="line-height: 1.6;">
            <li>Deutsch, D., &amp; Jozsa, R. (1992). Rapid solution of problems by quantum computation. <em>Proceedings of the Royal Society of London. Series A: Mathematical and Physical Sciences</em>, 439(1907), 553-558.</li>
            <li>Nielsen, M. A., &amp; Chuang, I. L. (2010). <em>Quantum Computation and Quantum Information</em> (10th Anniversary ed.). Cambridge University Press.</li>
        </ol>
    </section>

    <nav class="algorithm-nav">
        <a href="deutsch.html" class="nav-button">
            <span class="nav-label">Previous</span>
            <span class="nav-title">Deutsch's Algorithm</span>
        </a>
        <a href="bernstein-vazirani.html" class="nav-button nav-next">
            <span class="nav-label">Next</span>
            <span class="nav-title">Bernstein-Vazirani Algorithm</span>
        </a>
    </nav>
    """.replace("{title}", title).replace("{category_name}", category_name)
    
    with open(f"/Users/aghatasheersyedi/Desktop/latex/class/qiskit/aqca/algorithms/{category}/{filename}", 'w') as f:
        html = HTML_TEMPLATE.format(
            title=title,
            description=f"AQCA - {title}",
            root_path="../../",
            extra_css="",
            extra_js="",
            algorithms_expanded="true",
            content=content
        )
        f.write(html)


def generate_bernstein_vazirani_algorithm_page():
    title = "Bernstein–Vazirani Algorithm"
    category_name = "Oracle-Based"
    filename = "bernstein-vazirani.html"
    category = "oracle-based"
    
    content = r"""
    <div class="breadcrumb">
        <a href="../../index.html">Home</a> <span class="breadcrumb-separator">›</span> 
        <a href="../../algorithms.html">Algorithms</a> <span class="breadcrumb-separator">›</span> 
        {category_name} <span class="breadcrumb-separator">›</span> 
        {title}
    </div>

    <div class="algorithm-header">
        <h1>{title}</h1>
        <div class="algorithm-meta">
            <span class="badge badge-category">{category_name}</span>
        </div>
    </div>

    <section class="content-section">
        <h2>1. Overview & Problem Definition</h2>
        <p>The <strong>Bernstein–Vazirani Algorithm</strong> is an extension of the Deutsch–Jozsa framework, but it solves a much more specific and practical problem: learning a hidden linear function.</p>
        <p>Imagine you are given a black-box oracle that calculates the bitwise inner product of your input string \(x\) and a secret, hidden string \(s\) (both of length \(n\)), modulo 2. The function is defined as:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(f(x) = s \cdot x \pmod 2 = (s_0 x_0 \oplus s_1 x_1 \oplus \dots \oplus s_{n-1} x_{n-1})\)</p>
        </div>
        <p>The goal is to determine the exact value of the secret string \(s \in \{0,1\}^n\) with the absolute minimum number of queries to the oracle.</p>

        <div class="complexity-comparison" style="margin-top: 1.5rem;">
            <div class="complexity-box">
                <h3>Classical Complexity</h3>
                <div class="complexity-value">\(\mathcal{O}(n)\)</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">You must query the oracle \(n\) times using inputs with a single '1' (e.g., <code>100</code>, <code>010</code>, <code>001</code>) to reveal the string bit by bit.</p>
            </div>
            <div class="complexity-box">
                <h3>Quantum Speedup</h3>
                <div class="complexity-value">\(\mathcal{O}(1)\)</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">A quantum computer evaluates the oracle exactly once to reveal the entire \(n\)-bit string.</p>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>2. Intuition</h2>
        <p>If you have a 100-bit secret string, a classical computer must ask the oracle 100 distinct questions to find every bit.</p>
        <p>The quantum approach uses <strong>quantum parallelism</strong> and <strong>phase kickback</strong> to bypass this. By querying the oracle with a massive superposition of all possible inputs, the oracle's output (which depends on the secret string \(s\)) is kicked back as a phase factor.</p>
        <p>The brilliant part is that the phase shifts perfectly encode the binary representation of \(s\) into the Fourier basis of the quantum state. When you apply a final layer of Hadamard gates—which effectively acts as an inverse quantum Fourier transform over the Boolean cube—the phases perfectly constructively interfere to form the exact computational basis state corresponding to the secret string \(s\). You measure it, and the string is revealed in a single shot.</p>
    </section>

    <section class="content-section">
        <h2>3. Required Gates & Circuit Schematic</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Pauli-\(X\) (\(X\)):</strong> Used to prepare the target (ancilla) qubit in the \(|1\rangle\) state.</li>
            <li><strong>Hadamard (\(H^{\otimes n}\)):</strong> Applied to the input qubits to create the initial superposition, and later to interfere the phases to extract \(s\).</li>
            <li><strong>Quantum Oracle (\(U_f\)):</strong> An \((n+1)\)-qubit unitary matrix that applies \(U_f |x\rangle|y\rangle = |x\rangle|y \oplus (s \cdot x)\rangle\). Inside the oracle, a \(CX\) (CNOT) gate connects each input qubit \(i\) to the target qubit if and only if the corresponding secret bit \(s_i = 1\).</li>
        </ul>

        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="10" rx="2" ry="2"></rect><line x1="12" y1="3" x2="12" y2="7"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg></div>
            <h3>Circuit Schematic</h3>
            <pre style="background: var(--code-bg); padding: 1rem; border-radius: 4px; overflow-x: auto; margin-top: 1rem; color: var(--text-color);">
         ┌───┐                ┌───┐
  q_0: ──┤ H ├───────■────────┤ H ├─── ✂ Measure
         ├───┤       │        ├───┤
  q_1: ──┤ H ├───────┼────────┤ H ├─── ✂ Measure (e.g. s_1 = 0)
        ...         ...        ...
         ├───┤       │        ├───┤
q_n-1: ──┤ H ├───────■────────┤ H ├─── ✂ Measure
         ├───┤ ┌───┐ │ (U_f)  └───┘
  q_n: ──┤ X ├─┤ H ├─■──────────────── (Target)
         └───┘ └───┘</pre>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Circuit image placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>4. Mathematical Proof & State Evolution</h2>
        
        <h3 style="margin-top: 1.5rem;">Step 1: Initialisation</h3>
        <p>We start with \(n\) input qubits in \(|0\rangle\) and one target qubit in \(|1\rangle\):</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_0\rangle = |0\rangle^{\otimes n} \otimes |1\rangle\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 2: Applying the Hadamard Gates</h3>
        <p>Applying \(H\) to all qubits creates an equal superposition over all \(x \in \{0,1\}^n\), and places the target in the \(|-\rangle\) state:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_1\rangle = (H^{\otimes n} \otimes H) |\psi_0\rangle = \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} |x\rangle \otimes |-\rangle\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 3: The Oracle Query & Phase Kickback</h3>
        <p>Applying the oracle \(U_f\) shifts the phase of each computational basis state \(|x\rangle\) by \((-1)^{f(x)}\). Since \(f(x) = s \cdot x\):</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_2\rangle = U_f |\psi_1\rangle = \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} (-1)^{s \cdot x} |x\rangle \otimes |-\rangle\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 4: Final Interference</h3>
        <p>We apply \(H^{\otimes n}\) to the input register. The standard mathematical action of \(H^{\otimes n}\) on any state is to transform it according to the rule \(H^{\otimes n}|y\rangle = \frac{1}{\sqrt{2^n}} \sum_{z} (-1)^{y \cdot z} |z\rangle\). Applying this to our current state gives:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_3\rangle = \left( \frac{1}{2^n} \sum_{x=0}^{2^n-1} \sum_{z=0}^{2^n-1} (-1)^{s \cdot x} (-1)^{x \cdot z} |z\rangle \right) \otimes |-\rangle\)</p>
        </div>
        <p>We can combine the exponents: \((-1)^{s \cdot x + x \cdot z} = (-1)^{x \cdot (s \oplus z)}\).</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_3\rangle = \left( \frac{1}{2^n} \sum_{z=0}^{2^n-1} \left[ \sum_{x=0}^{2^n-1} (-1)^{x \cdot (s \oplus z)} \right] |z\rangle \right) \otimes |-\rangle\)</p>
        </div>
        <p>Look at the inner sum: \(\sum_x (-1)^{x \cdot (s \oplus z)}\).</p>
        <ul style="line-height: 1.6;">
            <li>If \(z = s\), then \(s \oplus z = 0\). The sum becomes \(\sum_x (-1)^0 = \sum_x 1 = 2^n\).</li>
            <li>If \(z \neq s\), the positive and negative terms cancel each other out perfectly, and the sum is \(0\).</li>
        </ul>
        <p>Therefore, the entire input state collapses deterministically into the state \(|s\rangle\):</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_3\rangle = |s\rangle \otimes |-\rangle\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Measurement</h3>
        <p>When we measure the input register in the computational basis, we will observe the secret string \(s\) with \(100\%\) probability.</p>
    </section>

    <section class="content-section">
        <h2>5. Interactive Visualisation</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Amplitude Histogram:</strong> Before the final layer of Hadamard gates, the histogram shows an equal probability distribution across all \(2^n\) basis states (a flat line). The moment the final Hadamards are applied, massive constructive interference occurs at the index corresponding to \(s\), and destructive interference occurs everywhere else. A single bar shoots up to 1.0 at state \(|s\rangle\).</li>
            <li><strong>Circuit Behaviour (Phase Disks):</strong> If you view the phase disks for the input register after the oracle, you will see a unique pattern of alternating phases. This specific geometric pattern of phases is precisely the Fourier transform of the basis state \(|s\rangle\).</li>
        </ul>
        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg></div>
            <h3>Dynamic State Tracking</h3>
            <p>Interactive module (amplitude histograms, Bloch spheres) to simulate the algorithm live.</p>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Interactive visualization placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>6. Python Code Implementation</h2>
        
        <h3>From Scratch (NumPy)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / NumPy</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>import numpy as np

def simulate_bernstein_vazirani(secret_string):
    \"\"\"
    Simulates a 2-qubit input (+1 ancilla) Bernstein-Vazirani algorithm using NumPy.
    secret_string: A 2-bit string, e.g., '10', '11'
    \"\"\"
    n = len(secret_string)
    if n != 2: raise ValueError("This NumPy scratch example is hardcoded for n=2.")
    
    H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)
    I = np.eye(2, dtype=complex)
    
    # Tensored Hadamards
    H3 = np.kron(np.kron(H, H), H)
    H_in = np.kron(np.kron(H, H), I)
    
    # 1. Initialise |00>|1>
    state_001 = np.zeros((8, 1), dtype=complex)
    state_001[1] = 1.0  # |001>
    
    # 2. H on all qubits
    psi_1 = np.dot(H3, state_001)
    
    # 3. Construct and apply Oracle based on secret string
    U_f = np.eye(8, dtype=complex)
    
    # Matrix construction for CNOTs
    # In a real implementation, you build the 8x8 matrix by tensoring the 
    # control conditions. For brevity in this simulation, we compute the output manually:
    psi_2 = np.zeros_like(psi_1)
    for i in range(8):
        # binary representation: input q0, input q1, target q2
        binary = format(i, '03b')
        x0, x1, y = int(binary[0]), int(binary[1]), int(binary[2])
        s0, s1 = int(secret_string[0]), int(secret_string[1])
        
        # f(x) = s dot x mod 2
        f_x = (s0 * x0 + s1 * x1) % 2
        new_y = y ^ f_x
        
        new_index = int(f"{x0}{x1}{new_y}", 2)
        psi_2[new_index] += psi_1[i]
        
    # 4. Final H on input qubits
    psi_final = np.dot(H_in, psi_2)
    
    # 5. Find highest probability state
    probs = np.abs(psi_final.flatten())**2
    measured_index = np.argmax(probs)
    measured_binary = format(measured_index, '03b')[:2] # Strip ancilla
    
    return measured_binary

print("Hidden String '11' Found:", simulate_bernstein_vazirani('11'))
</code></pre>
            </div>
        </div>
        
        <h3 style="margin-top: 1.5rem;">Framework (Qiskit)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / Qiskit</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def bv_circuit(secret_string):
    n = len(secret_string)
    qc = QuantumCircuit(n + 1, n)
    
    # 1. Prepare Target in |->
    qc.x(n)
    qc.h(n)
    
    # 2. Prepare Inputs
    for qubit in range(n):
        qc.h(qubit)
        
    qc.barrier()
    
    # 3. Apply Oracle (f(x) = s * x)
    # Reversing the string because Qiskit orders qubits from bottom to top (q_n-1 ... q_0)
    secret_string = secret_string[::-1]
    for qubit in range(n):
        if secret_string[qubit] == '1':
            qc.cx(qubit, n)
            
    qc.barrier()
    
    # 4. Interfere Inputs
    for qubit in range(n):
        qc.h(qubit)
        
    # 5. Measure
    for i in range(n):
        qc.measure(i, i)
        
    return qc

# Simulate
secret = "1011"
circuit = bv_circuit(secret)
simulator = AerSimulator()
counts = simulator.run(circuit, shots=1).result().get_counts()

print(f"Secret string: {secret}")
print(f"Measured string: {list(counts.keys())[0]}")
</code></pre>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>7. Caveats & Real-World Limits</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Oracle Complexity:</strong> Much like Deutsch–Jozsa, the magic happens inside the black box \(U_f\). If you are physically constructing the circuit for the oracle, you must add a \(CX\) gate for every '1' in the secret string. Therefore, constructing the oracle itself requires \(\mathcal{O}(n)\) gates. The algorithm proves a query speedup, but not necessarily a gate-time speedup in physical construction.</li>
            <li><strong>Hardware Noise:</strong> On NISQ hardware, applying a large number of CNOT gates to a single ancilla qubit can lead to significant cross-talk and phase errors, meaning the final measurement might yield an incorrect bit string probabilistically.</li>
        </ul>
    </section>

    <section class="content-section">
        <h2>8. Applications</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Learning Parity with Noise (LPN):</strong> The Bernstein–Vazirani algorithm is the foundational quantum approach to the problem of learning parities. This has significant implications for post-quantum cryptography, particularly in evaluating the security of lattice-based cryptographic schemes against quantum attacks.</li>
            <li><strong>Quantum Machine Learning:</strong> It serves as a primitive subroutine for learning linear functions and gradient estimation in quantum machine learning architectures.</li>
        </ul>
    </section>
    
    <section class="content-section">
        <h2>9. References</h2>
        <ol style="line-height: 1.6;">
            <li>Bernstein, E., &amp; Vazirani, U. (1993). Quantum complexity theory. <em>Proceedings of the 25th Annual ACM Symposium on Theory of Computing</em>, 11–20.</li>
            <li>Nielsen, M. A., &amp; Chuang, I. L. (2010). <em>Quantum Computation and Quantum Information</em> (10th Anniversary ed.). Cambridge University Press.</li>
        </ol>
    </section>

    <nav class="algorithm-nav">
        <a href="deutsch-jozsa.html" class="nav-button">
            <span class="nav-label">Previous</span>
            <span class="nav-title">Deutsch-Jozsa Algorithm</span>
        </a>
        <a href="simon.html" class="nav-button nav-next">
            <span class="nav-label">Next</span>
            <span class="nav-title">Simon's Algorithm</span>
        </a>
    </nav>
    """.replace("{title}", title).replace("{category_name}", category_name)
    
    with open(f"/Users/aghatasheersyedi/Desktop/latex/class/qiskit/aqca/algorithms/{category}/{filename}", 'w') as f:
        html = HTML_TEMPLATE.format(
            title=title,
            description=f"AQCA - {title}",
            root_path="../../",
            extra_css="",
            extra_js="",
            algorithms_expanded="true",
            content=content
        )
        f.write(html)


def generate_simon_algorithm_page():
    title = "Simon's Algorithm"
    category_name = "Oracle-Based"
    filename = "simon.html"
    category = "oracle-based"
    
    content = r"""
    <div class="breadcrumb">
        <a href="../../index.html">Home</a> <span class="breadcrumb-separator">›</span> 
        <a href="../../algorithms.html">Algorithms</a> <span class="breadcrumb-separator">›</span> 
        {category_name} <span class="breadcrumb-separator">›</span> 
        {title}
    </div>

    <div class="algorithm-header">
        <h1>{title}</h1>
        <div class="algorithm-meta">
            <span class="badge badge-category">{category_name}</span>
        </div>
    </div>

    <section class="content-section">
        <h2>1. Overview & Problem Definition</h2>
        <p><strong>Simon's Algorithm</strong> represents a monumental leap in quantum computing history, as it was the first algorithm to demonstrate an exponential speedup over any classical algorithm for a specific problem.</p>
        <p>Imagine you are given a black-box function \(f\) that takes an \(n\)-bit input and produces an \(n\)-bit output. You are given a promise: the function is a "two-to-one" function that hides a secret string \(s\). Specifically, for any two distinct inputs \(x\) and \(y\), they will produce the exact same output (\(f(x) = f(y)\)) if and only if they are related by a bitwise XOR with the secret string: \(x \oplus y = s\).</p>
        <p>The goal is to find the secret string \(s \in \{0,1\}^n\) with the minimum number of oracle queries.</p>

        <div class="complexity-comparison" style="margin-top: 1.5rem;">
            <div class="complexity-box">
                <h3>Classical Complexity</h3>
                <div class="complexity-value">\(\mathcal{O}(2^{n/2})\)</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">A classical computer must query the oracle until it finds a collision (two inputs yielding the same output). By the Birthday Paradox, this takes roughly \(2^{n/2}\) queries.</p>
            </div>
            <div class="complexity-box">
                <h3>Quantum Speedup</h3>
                <div class="complexity-value">\(\mathcal{O}(n)\)</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">A quantum computer requires only \(\approx n\) queries, yielding an <strong>exponential speedup</strong>.</p>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>2. Intuition</h2>
        <p>Classically, finding \(s\) requires guessing inputs until you accidentally stumble upon two that give the same output.</p>
        <p>The quantum approach does not search for collisions directly. Instead, we query the oracle with a massive superposition of all possible inputs. Because the function is two-to-one, the output register becomes entangled with the input register in a very specific way. If we were to measure the output register, the input register would collapse into a superposition of exactly two states: \(|x\rangle\) and \(|x \oplus s\rangle\).</p>
        <p>Instead of measuring the input directly (which would just yield a random \(x\)), we apply a final layer of Hadamard gates. This creates quantum interference. The mathematics of the Hadamard transform dictates that the amplitude for any state \(|z\rangle\) will perfectly destructively interfere to zero <em>unless</em> \(z\) is orthogonal to the secret string \(s\) (meaning their bitwise dot product is even: \(s \cdot z = 0 \pmod 2\)).</p>
        <p>By running the circuit slightly more than \(n\) times, we collect a series of random bitstrings \(z_1, z_2, \dots, z_n\). We then use a classical computer to solve this system of linear equations to reveal the secret string \(s\).</p>
    </section>

    <section class="content-section">
        <h2>3. Required Gates & Circuit Schematic</h2>
        <p>Unlike Deutsch-Jozsa and Bernstein-Vazirani, Simon's algorithm does not use Phase Kickback. Instead, it relies on entanglement between two \(n\)-qubit registers.</p>
        <ul style="line-height: 1.6;">
            <li><strong>Hadamard (\(H^{\otimes n}\)):</strong> Applied to the input register to create the initial superposition, and later to interfere the states.</li>
            <li><strong>Quantum Oracle (\(U_f\)):</strong> A \(2n\)-qubit unitary matrix that applies \(U_f |x\rangle|0\rangle = |x\rangle|f(x)\rangle\).</li>
            <li><strong>Classical Post-Processing:</strong> Gaussian elimination over \(GF(2)\) to solve the linear equations.</li>
        </ul>

        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="10" rx="2" ry="2"></rect><line x1="12" y1="3" x2="12" y2="7"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg></div>
            <h3>Circuit Schematic</h3>
            <pre style="background: var(--code-bg); padding: 1rem; border-radius: 4px; overflow-x: auto; margin-top: 1rem; color: var(--text-color);">
         ┌───┐                ┌───┐
  q_0: ──┤ H ├───────■────────┤ H ├─── ✂ Measure (yields z_0)
         ├───┤       │        ├───┤
  q_1: ──┤ H ├───────┼────────┤ H ├─── ✂ Measure (yields z_1)
        ...         ...        ...
         ├───┤       │        ├───┤
q_n-1: ──┤ H ├───────■────────┤ H ├─── ✂ Measure (yields z_{n-1})
         ├───┤ ┌───┐ │ (U_f)  
  q_n: ──┤ I ├─┤ I ├─■──────────────── ✂ Measure (optional)
         └───┘ └───┘
        ... (Target register has n qubits) ...</pre>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Circuit image placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>4. Mathematical Proof & State Evolution</h2>
        
        <h3 style="margin-top: 1.5rem;">Step 1: Initialisation</h3>
        <p>We start with two \(n\)-qubit registers, both initialised to \(|0\rangle^{\otimes n}\):</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_0\rangle = |0\rangle^{\otimes n} \otimes |0\rangle^{\otimes n}\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 2: Applying the Hadamard Gates</h3>
        <p>Applying \(H^{\otimes n}\) to the first register creates an equal superposition over all \(x \in \{0,1\}^n\):</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_1\rangle = \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} |x\rangle \otimes |0\rangle^{\otimes n}\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 3: The Oracle Query</h3>
        <p>Applying the oracle \(U_f\) writes the function evaluation into the second register. This entangles the two registers:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_2\rangle = \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} |x\rangle \otimes |f(x)\rangle\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 4: Final Interference</h3>
        <p>We apply \(H^{\otimes n}\) to the first register. Recall that \(H^{\otimes n}|x\rangle = \frac{1}{\sqrt{2^n}} \sum_{z} (-1)^{x \cdot z} |z\rangle\):</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_3\rangle = \frac{1}{2^n} \sum_{x=0}^{2^n-1} \sum_{z=0}^{2^n-1} (-1)^{x \cdot z} |z\rangle \otimes |f(x)\rangle\)</p>
        </div>
        <p>Because \(f(x)\) is a two-to-one function where \(f(x) = f(x \oplus s)\), for every unique output \(y\), there are exactly two inputs, \(x\) and \(x \oplus s\), that produce it. We can rewrite the sum by pairing these terms together:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_3\rangle = \frac{1}{2^{n-1}} \sum_{y} \sum_{z=0}^{2^n-1} \left[ (-1)^{x \cdot z} + (-1)^{(x \oplus s) \cdot z} \right] |z\rangle \otimes |y\rangle\)</p>
        </div>
        <p>Factor out \((-1)^{x \cdot z}\) from the bracket:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\((-1)^{x \cdot z} \left[ 1 + (-1)^{s \cdot z} \right]\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Measurement</h3>
        <p>Look at the term \(\left[ 1 + (-1)^{s \cdot z} \right]\):</p>
        <ul style="line-height: 1.6;">
            <li>If \(s \cdot z = 1 \pmod 2\), then \((-1)^1 = -1\), and the amplitude is \(1 - 1 = 0\). This state perfectly destructively interferes.</li>
            <li>If \(s \cdot z = 0 \pmod 2\), then \((-1)^0 = 1\), and the amplitude is \(1 + 1 = 2\). This state constructively interferes.</li>
        </ul>
        <p>Therefore, when we measure the first register, we have a \(100\%\) probability of observing a state \(z\) such that \(s \cdot z = 0 \pmod 2\).</p>
    </section>

    <section class="content-section">
        <h2>5. Interactive Visualisation</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Entanglement View:</strong> After the oracle, the visualizer should show the input and output registers bound together. If the user simulates measuring the output register (collapsing it to a specific \(y\)), the input register will instantly collapse into a visually clear two-state superposition: \(\frac{1}{\sqrt{2}}(|x\rangle + |x \oplus s\rangle)\).</li>
            <li><strong>Amplitude Histogram:</strong> After the final Hadamard gates, the histogram will show non-zero probabilities only for the bitstrings \(z\) that satisfy the dot product condition. Exactly half of the states in the Hilbert space will drop to zero.</li>
        </ul>
        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg></div>
            <h3>Dynamic State Tracking</h3>
            <p>Interactive module (amplitude histograms, Bloch spheres) to simulate the algorithm live.</p>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Interactive visualization placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>6. Python Code Implementation</h2>
        
        <h3>From Scratch (NumPy)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / NumPy</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>import numpy as np

def simulate_simon_2bit():
    \"\"\"
    Simulates a 2-qubit input (+ 2-qubit target) Simon's algorithm using NumPy.
    Secret string s = '11'.
    \"\"\"
    H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)
    I = np.eye(2, dtype=complex)
    
    # Tensored Hadamards for input register
    H2 = np.kron(H, H)
    H_in = np.kron(H2, np.eye(4)) # H on input, I on target
    
    # 1. Initialise |00>|00>
    state_0000 = np.zeros((16, 1), dtype=complex)
    state_0000[0] = 1.0  
    
    # 2. H on input register
    psi_1 = np.dot(H_in, state_0000)
    
    # 3. Construct Oracle for s = '11'
    # f(00)=00, f(11)=00
    # f(01)=10, f(10)=10
    U_f = np.zeros((16, 16), dtype=complex)
    mapping = {0:0, 1:2, 2:2, 3:0} # Decimal representations of x -> f(x)
    for x in range(4):
        for y in range(4):
            new_y = y ^ mapping[x]
            U_f[x*4 + new_y, x*4 + y] = 1.0
            
    psi_2 = np.dot(U_f, psi_1)
    
    # 4. Final H on input qubits
    psi_final = np.dot(H_in, psi_2)
    
    # 5. Calculate probabilities for the input register (tracing out the target)
    probs = np.zeros(4)
    for i in range(16):
        input_state = i // 4
        probs[input_state] += np.abs(psi_final[i][0])**2
        
    # Strings with non-zero probability must satisfy z dot s = 0 mod 2. 
    # For s='11', valid z's are '00' and '11'.
    measured_states = [format(i, '02b') for i in range(4) if probs[i] > 0.01]
    
    return measured_states

print("Possible measurement outcomes (z) for secret s='11':", simulate_simon_2bit())
</code></pre>
            </div>
        </div>
        
        <h3 style="margin-top: 1.5rem;">Framework (Qiskit)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / Qiskit</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def simon_oracle(s):
    \"\"\"Generates an oracle for Simon's algorithm given a secret string s.\"\"\"
    n = len(s)
    qc = QuantumCircuit(2 * n)
    
    # Copy inputs to outputs (f(x) = x initially)
    for i in range(n):
        qc.cx(i, i + n)
        
    # Create the collision for s
    # Find first index where s is 1
    pivot = s.find('1')
    if pivot != -1:
        # Reverse string for Qiskit bit ordering
        s = s[::-1] 
        for i in range(n):
            if s[i] == '1':
                qc.cx(pivot, i + n)
    return qc

def simon_circuit(s):
    n = len(s)
    qc = QuantumCircuit(2 * n, n)
    
    # 1. H on input register
    for i in range(n):
        qc.h(i)
    qc.barrier()
    
    # 2. Oracle
    qc.compose(simon_oracle(s), inplace=True)
    qc.barrier()
    
    # 3. Final H on input register
    for i in range(n):
        qc.h(i)
        
    # 4. Measure input register
    for i in range(n):
        qc.measure(i, i)
        
    return qc

# Simulate
secret = "11"
circuit = simon_circuit(secret)
simulator = AerSimulator()
# Run it multiple times to gather the linear equations
counts = simulator.run(circuit, shots=1024).result().get_counts()

print(f"Secret string: {secret}")
print(f"Measured equations (z): {list(counts.keys())}")
</code></pre>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>7. Caveats & Real-World Limits</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Hybrid Dependency:</strong> Simon's algorithm is a hybrid quantum-classical algorithm. The quantum computer does not give you \(s\) directly; it only gives you the string \(z\). You must run the circuit \(\mathcal{O}(n)\) times, feed the results into a classical computer, and run Gaussian elimination (\(\mathcal{O}(n^3)\) classical time) to actually deduce \(s\).</li>
            <li><strong>Oracle Overhead:</strong> Just like DJ and BV algorithms, constructing the specific \(2n\)-qubit oracle \(U_f\) requires a number of physical gates that scale with the complexity of the function, which introduces deep circuits susceptible to decoherence on NISQ devices.</li>
        </ul>
    </section>

    <section class="content-section">
        <h2>8. Applications</h2>
        <ul style="line-height: 1.6;">
            <li><strong>The Blueprint for Shor's Algorithm:</strong> Simon's algorithm is historically vital because it introduced the concept of using the Quantum Fourier Transform (which the Hadamard cascade acts as over the Boolean cube) to find hidden periodicity. Peter Shor directly cited Simon's work when he formulated his famous factoring algorithm. Simon finds a period in \(GF(2)^n\), while Shor finds a period over the integers.</li>
            <li><strong>Cryptanalysis:</strong> Simon’s algorithm has direct applications in cryptography. It can be used to break certain symmetric-key cryptographic constructions, such as the Even-Mansour cipher, provided the attacker can query the encryption black box in a quantum superposition.</li>
        </ul>
    </section>
    
    <section class="content-section">
        <h2>9. References</h2>
        <ol style="line-height: 1.6;">
            <li>Simon, D. R. (1994). On the power of quantum computation. <em>Proceedings of the 35th Annual Symposium on Foundations of Computer Science</em>, 116-123.</li>
            <li>Nielsen, M. A., &amp; Chuang, I. L. (2010). <em>Quantum Computation and Quantum Information</em> (10th Anniversary ed.). Cambridge University Press.</li>
        </ol>
    </section>

    <nav class="algorithm-nav">
        <a href="bernstein-vazirani.html" class="nav-button">
            <span class="nav-label">Previous</span>
            <span class="nav-title">Bernstein-Vazirani Algorithm</span>
        </a>
        <a href="../phase-amplitude/qft.html" class="nav-button nav-next">
            <span class="nav-label">Next</span>
            <span class="nav-title">Quantum Fourier Transform</span>
        </a>
    </nav>
    """.replace("{title}", title).replace("{category_name}", category_name)
    
    with open(f"/Users/aghatasheersyedi/Desktop/latex/class/qiskit/aqca/algorithms/{category}/{filename}", 'w') as f:
        html = HTML_TEMPLATE.format(
            title=title,
            description=f"AQCA - {title}",
            root_path="../../",
            extra_css="",
            extra_js="",
            algorithms_expanded="true",
            content=content
        )
        f.write(html)


def generate_qft_algorithm_page():
    title = "Quantum Fourier Transform (QFT)"
    category_name = "Phase & Amplitude Core"
    filename = "qft.html"
    category = "phase-amplitude"
    
    content = r"""
    <div class="breadcrumb">
        <a href="../../index.html">Home</a> <span class="breadcrumb-separator">›</span> 
        <a href="../../algorithms.html">Algorithms</a> <span class="breadcrumb-separator">›</span> 
        {category_name} <span class="breadcrumb-separator">›</span> 
        {title}
    </div>

    <div class="algorithm-header">
        <h1>{title}</h1>
        <div class="algorithm-meta">
            <span class="badge badge-category">{category_name}</span>
        </div>
    </div>

    <section class="content-section">
        <h2>1. Overview & Problem Definition</h2>
        <p>The <strong>Quantum Fourier Transform (QFT)</strong> is the quantum analogue of the classical Discrete Fourier Transform (DFT). It is not typically used as a standalone algorithm to solve a specific problem; rather, it is one of the most powerful subroutines in all of quantum computing.</p>
        <p>Its primary function is to transform a quantum state encoded in the computational basis (where information is stored in binary probabilities) into the Fourier basis (where information is stored in relative quantum phases). It is the engine that allows quantum computers to find hidden periodicities and estimate eigenvalues.</p>

        <div class="complexity-comparison" style="margin-top: 1.5rem;">
            <div class="complexity-box">
                <h3>Classical Complexity (FFT)</h3>
                <div class="complexity-value">\(\mathcal{O}(n 2^n)\)</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">The classical Fast Fourier Transform operates on \(N = 2^n\) data points.</p>
            </div>
            <div class="complexity-box">
                <h3>Quantum Speedup</h3>
                <div class="complexity-value">\(\mathcal{O}(n^2)\)</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">A quantum computer performs the transform using only \(\approx n^2/2\) gates, yielding an <strong>exponential speedup</strong>.</p>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>2. Intuition</h2>
        <p>In a classical computer, you can think of the Fourier transform as taking a complex audio wave and breaking it down into its fundamental frequencies.</p>
        <p>In a quantum computer, we use the QFT to manipulate the phase of a superposition. Imagine the probability amplitude of a quantum state as a clock face with a hand pointing in a specific direction (its phase).</p>
        <ul style="line-height: 1.6;">
            <li>In the computational basis, a number like <code>5</code> (\(|101\rangle\)) is just a binary string.</li>
            <li>When we apply the QFT to this state, we create an equal superposition of all possible states, but we twist the clock hands. The amount of "twist" (phase shift) applied to each state's clock hand is directly proportional to the original number <code>5</code>.</li>
        </ul>
        <p>Because different original numbers produce distinct, predictable twisting patterns, we can use the QFT (and its inverse) to decode highly complex phase patterns back into readable binary numbers.</p>
    </section>

    <section class="content-section">
        <h2>3. Required Gates & Circuit Schematic</h2>
        <p>The QFT circuit requires a cascading sequence of Hadamard gates and increasingly smaller Controlled-Phase rotations, followed by a reversal of the qubit order.</p>
        <ul style="line-height: 1.6;">
            <li><strong>Hadamard (\(H\)):</strong> Creates the initial equal superposition and applies a fundamental phase shift based on the qubit's binary value.</li>
            <li><strong>Controlled-Phase (\(CP\) or \(R_k\)):</strong> Applies a fractional phase rotation \(\theta = 2\pi / 2^k\) to a target qubit, controlled by the state of another qubit.</li>
            <li><strong>SWAP:</strong> Reverses the order of the qubits at the end of the circuit to match the standard mathematical definition of the QFT.</li>
        </ul>

        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="10" rx="2" ry="2"></rect><line x1="12" y1="3" x2="12" y2="7"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg></div>
            <h3>Circuit Schematic (3-Qubit Example)</h3>
            <pre style="background: var(--code-bg); padding: 1rem; border-radius: 4px; overflow-x: auto; margin-top: 1rem; color: var(--text-color);">
       ┌───┐ ┌─────────┐ ┌─────────┐                                 
q_0: ──┤ H ├─┤ CP(π/2) ├─┤ CP(π/4) ├───────────────────────────X─
       └───┘ └────┬────┘ └────┬────┘ ┌───┐ ┌─────────┐         │ 
q_1: ─────────────■───────────┼──────┤ H ├─┤ CP(π/2) ├─────────┼─
                              │      └───┘ └────┬────┘ ┌───┐   │ 
q_2: ─────────────────────────■─────────────────■──────┤ H ├───X─
                                                       └───┘     </pre>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Circuit image placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>4. Mathematical Proof & State Evolution</h2>
        
        <h3 style="margin-top: 1.5rem;">Step 1: Definition of the QFT</h3>
        <p>For an \(n\)-qubit state \(|x\rangle\) (where \(x\) is an integer from \(0\) to \(2^n-1\)), the QFT is defined as:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(QFT|x\rangle = \frac{1}{\sqrt{2^n}} \sum_{y=0}^{2^n-1} e^{\frac{2\pi i x y}{2^n}} |y\rangle\)</p>
        </div>
        <p>This can be factored into a beautiful product state, which dictates the circuit design. Using binary fractional notation (\(0.x_1 x_2 \dots = x_1/2 + x_2/4 + \dots\)), the state becomes:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(QFT|x\rangle = \frac{1}{\sqrt{2^n}} \left( |0\rangle + e^{2\pi i 0.x_n} |1\rangle \right) \otimes \left( |0\rangle + e^{2\pi i 0.x_{n-1}x_n} |1\rangle \right) \otimes \dots \otimes \left( |0\rangle + e^{2\pi i 0.x_1x_2\dots x_n} |1\rangle \right)\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 2: Evolving a 3-Qubit State</h3>
        <p>Let the initial state be \(|x\rangle = |x_1 x_2 x_3\rangle\).</p>
        <ol style="line-height: 1.6;">
            <li><strong>Apply \(H\) to \(q_0\) (\(x_1\)):</strong>
                <div class="math-container" style="margin: 0.5rem 0;">
                    <p>\(|x_1 x_2 x_3\rangle \xrightarrow{H_0} \frac{1}{\sqrt{2}} \left( |0\rangle + e^{2\pi i 0.x_1} |1\rangle \right) \otimes |x_2 x_3\rangle\)</p>
                </div>
            </li>
            <li><strong>Apply \(CP(\pi/2)\) controlled by \(q_1\) (\(x_2\)):</strong><br>
                This adds a phase if both qubits are \(1\), modifying the phase of \(q_0\) to include \(x_2/4\).
                <div class="math-container" style="margin: 0.5rem 0;">
                    <p>\(\xrightarrow{CP_{1,0}} \frac{1}{\sqrt{2}} \left( |0\rangle + e^{2\pi i 0.x_1 x_2} |1\rangle \right) \otimes |x_2 x_3\rangle\)</p>
                </div>
            </li>
            <li><strong>Apply \(CP(\pi/4)\) controlled by \(q_2\) (\(x_3\)):</strong>
                <div class="math-container" style="margin: 0.5rem 0;">
                    <p>\(\xrightarrow{CP_{2,0}} \frac{1}{\sqrt{2}} \left( |0\rangle + e^{2\pi i 0.x_1 x_2 x_3} |1\rangle \right) \otimes |x_2 x_3\rangle\)</p>
                </div>
            </li>
        </ol>
        <p>We repeat this process for \(q_1\) (using \(H\) and one \(CP\) from \(q_2\)) and then for \(q_2\) (just an \(H\)).</p>

        <h3 style="margin-top: 1.5rem;">Step 3: SWAP and Final State</h3>
        <p>The sequence above produces the correct product states, but in reverse order. Applying SWAP gates between \(q_0 \leftrightarrow q_2\) yields the exact mathematical definition outlined in Step 1.</p>

        <h3 style="margin-top: 1.5rem;">Measurement</h3>
        <p>If you input a computational basis state \(|x\rangle\) and apply the QFT, you produce a state with equal probability amplitudes across all \(2^n\) possible outcomes. Measuring the QFT directly yields a completely random bitstring. The QFT is almost never measured on its own; it is instead used as an internal transformation before an <em>Inverse QFT</em> translates the phases back into measurable probabilities.</p>
    </section>

    <section class="content-section">
        <h2>5. Interactive Visualisation</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Amplitude Histogram:</strong> Boring for the forward QFT. If you input a single basis state (e.g., \(|5\rangle\)), the final histogram will be a completely flat line, showing a probability of \(1/2^n\) for every possible state.</li>
            <li><strong>Phase Disks (Q-Spheres):</strong> This is where the QFT shines. While all disks have the same radius (amplitude), the internal arrows (phases) will exhibit a stunning spiral pattern. The frequency of this phase wrapping is directly proportional to the integer value of the input state \(|x\rangle\).</li>
        </ul>
        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg></div>
            <h3>Dynamic State Tracking</h3>
            <p>Interactive module (amplitude histograms, Bloch spheres) to simulate the algorithm live.</p>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Interactive visualization placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>6. Python Code Implementation</h2>
        
        <h3>From Scratch (NumPy)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / NumPy</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>import numpy as np

def simulate_qft(n_qubits, input_state):
    \"\"\"
    Simulates the Quantum Fourier Transform matrix acting on a state.
    \"\"\"
    N = 2**n_qubits
    
    # Generate the QFT Matrix
    omega = np.exp(2 * np.pi * 1j / N)
    qft_matrix = np.zeros((N, N), dtype=complex)
    
    for row in range(N):
        for col in range(N):
            qft_matrix[row, col] = (omega ** (row * col)) / np.sqrt(N)
            
    # Apply to input state
    state_vector = np.zeros((N, 1), dtype=complex)
    state_vector[input_state] = 1.0
    
    transformed_state = np.dot(qft_matrix, state_vector)
    
    return transformed_state

# Example: QFT on state |1> for 3 qubits
print("Transformed State (phases): \n", np.round(simulate_qft(3, 1), 3))
</code></pre>
            </div>
        </div>
        
        <h3 style="margin-top: 1.5rem;">Framework (Qiskit)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / Qiskit</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np

def build_qft_circuit(n):
    \"\"\"Builds a QFT circuit for n qubits.\"\"\"
    qc = QuantumCircuit(n)
    
    for target in range(n):
        qc.h(target)
        for control in range(target + 1, n):
            # Phase is pi / 2^(distance)
            theta = np.pi / (2 ** (control - target))
            qc.cp(theta, control, target)
        qc.barrier()
        
    # Swap qubits to match mathematical ordering
    for i in range(n // 2):
        qc.swap(i, n - i - 1)
        
    return qc

# Generate 4-qubit QFT
n_qubits = 4
circuit = build_qft_circuit(n_qubits)
print(circuit.draw(output='text'))
</code></pre>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>7. Caveats & Real-World Limits</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Hardware Noise on Tiny Rotations:</strong> The standard QFT requires \(CP\) gates with incredibly small angles (e.g., \(\pi/2^{10}\)). On modern NISQ devices, such minute rotations get completely drowned out by hardware noise.</li>
            <li><strong>Approximate QFT (AQFT):</strong> To run on real hardware, physicists often discard the smallest \(CP\) gates (where the distance between qubits is \(> 3\) or \(4\)). This drastically reduces the circuit depth \(\mathcal{O}(n \log n)\) and noise without severely impacting the algorithm's accuracy.</li>
            <li><strong>No Direct Classical Extraction:</strong> Although the QFT calculates the Fourier transform exponentially faster than a classical computer, you cannot extract the full array of Fourier coefficients. Measurement collapses the state, giving you only one random sample.</li>
        </ul>
    </section>

    <section class="content-section">
        <h2>8. Applications</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Quantum Phase Estimation (QPE):</strong> Uses the Inverse QFT to measure the phase eigenvalues of a unitary operator.</li>
            <li><strong>Shor's Algorithm:</strong> Uses QPE and the Inverse QFT to find the period of a modular exponentiation function, which is the key to factoring RSA primes.</li>
            <li><strong>Quantum Addition (Draper Adder):</strong> Allows two quantum registers to be added together in the Fourier basis without requiring ancilla qubits to track carry operations.</li>
        </ul>
    </section>
    
    <section class="content-section">
        <h2>9. References</h2>
        <ol style="line-height: 1.6;">
            <li>Coppersmith, D. (1994). An approximate Fourier transform useful in quantum factoring. <em>arXiv preprint quant-ph/0201067</em>.</li>
            <li>Nielsen, M. A., &amp; Chuang, I. L. (2010). <em>Quantum Computation and Quantum Information</em> (10th Anniversary ed.). Cambridge University Press.</li>
        </ol>
    </section>

    <nav class="algorithm-nav">
        <a href="../oracle-based/simon.html" class="nav-button">
            <span class="nav-label">Previous</span>
            <span class="nav-title">Simon's Algorithm</span>
        </a>
        <a href="qpe.html" class="nav-button nav-next">
            <span class="nav-label">Next</span>
            <span class="nav-title">Quantum Phase Estimation</span>
        </a>
    </nav>
    """.replace("{title}", title).replace("{category_name}", category_name)
    
    with open(f"/Users/aghatasheersyedi/Desktop/latex/class/qiskit/aqca/algorithms/{category}/{filename}", 'w') as f:
        html = HTML_TEMPLATE.format(
            title=title,
            description=f"AQCA - {title}",
            root_path="../../",
            extra_css="",
            extra_js="",
            algorithms_expanded="true",
            content=content
        )
        f.write(html)


def generate_qpe_algorithm_page():
    title = "Quantum Phase Estimation (QPE)"
    category_name = "Phase & Amplitude Core"
    filename = "qpe.html"
    category = "phase-amplitude"
    
    content = r"""
    <div class="breadcrumb">
        <a href="../../index.html">Home</a> <span class="breadcrumb-separator">›</span> 
        <a href="../../algorithms.html">Algorithms</a> <span class="breadcrumb-separator">›</span> 
        {category_name} <span class="breadcrumb-separator">›</span> 
        {title}
    </div>

    <div class="algorithm-header">
        <h1>{title}</h1>
        <div class="algorithm-meta">
            <span class="badge badge-category">{category_name}</span>
        </div>
    </div>

    <section class="content-section">
        <h2>1. Overview & Problem Definition</h2>
        <p><strong>Quantum Phase Estimation (QPE)</strong> is a central subroutine in quantum algorithms. It is designed to solve the following problem: suppose you are given a unitary operator \(U\) and a quantum state \(|\psi\rangle\) which is an exact eigenvector of \(U\). By definition, applying \(U\) to \(|\psi\rangle\) simply multiplies the state by a global phase:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(U|\psi\rangle = e^{2\pi i \theta}|\psi\rangle\)</p>
        </div>
        <p>The problem is to estimate the unknown phase \(\theta\) (where \(0 \le \theta &lt; 1\)) to a high degree of precision using \(t\) bits.</p>

        <div class="complexity-comparison" style="margin-top: 1.5rem;">
            <div class="complexity-box">
                <h3>Classical Complexity</h3>
                <div class="complexity-value">\(\mathcal{O}(2^n)\)</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">Classically finding eigenvalues of an exponentially large \(2^n \times 2^n\) matrix is computationally intractable.</p>
            </div>
            <div class="complexity-box">
                <h3>Quantum Speedup</h3>
                <div class="complexity-value">\(\mathcal{O}(t^2)\)</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">A quantum computer extracts the phase using \(\mathcal{O}(t^2)\) gates alongside controlled applications of \(U\), yielding an <strong>exponential speedup</strong> over classical eigensolvers.</p>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>2. Intuition</h2>
        <p>If you apply \(U\) to an eigenvector, the phase \(\theta\) is purely global, meaning it is physically unobservable.</p>
        <p>To measure it, QPE uses the <strong>Phase Kickback</strong> trick across two distinct quantum registers: a "target register" holding the state \(|\psi\rangle\), and a "counting register" holding \(t\) qubits initialised in a superposition.</p>
        <p>By applying controlled versions of \(U\) (specifically \(U^1, U^2, U^4, \dots, U^{2^{t-1}}\)), the global phase generated by the eigenvector is "kicked back" as a relative phase into the counting register. The successive squaring of \(U\) shifts the binary decimal point of the phase, systematically writing the binary representation of \(\theta\) into the relative phases of the counting qubits.</p>
        <p>At this point, the counting register contains the Quantum Fourier Transform of the phase. By applying an <strong>Inverse Quantum Fourier Transform (\(QFT^\dagger\))</strong>, we translate these abstract phase rotations back into a standard computational basis state. Measuring the counting register then directly yields a binary string representing \(\theta\).</p>
    </section>

    <section class="content-section">
        <h2>3. Required Gates & Circuit Schematic</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Hadamard (\(H^{\otimes t}\)):</strong> Applied to the counting register to create an equal superposition of all measurement outcomes.</li>
            <li><strong>Controlled-Unitary (\(CU^{2^j}\)):</strong> A sequence of controlled gates applying \(U\) raised to increasing powers of 2.</li>
            <li><strong>Inverse Quantum Fourier Transform (\(QFT^\dagger\)):</strong> A subroutine of \(H\) and \(CP^\dagger\) gates used to map the phase state back to the computational basis.</li>
        </ul>

        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="10" rx="2" ry="2"></rect><line x1="12" y1="3" x2="12" y2="7"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg></div>
            <h3>Circuit Schematic</h3>
            <pre style="background: var(--code-bg); padding: 1rem; border-radius: 4px; overflow-x: auto; margin-top: 1rem; color: var(--text-color);">
Counting Register (t qubits)
         ┌───┐                                                       ┌───────┐
  q_0: ──┤ H ├─■─────────────────────────────────────────────────────┤       ├── ✂ Measure
         ├───┤ │                                                     │       │
  q_1: ──┤ H ├─┼────────■────────────────────────────────────────────┤ QFT^† ├── ✂ Measure
        ...    │        │                                            │       │
         ├───┤ │        │                                            │       │
q_t-1: ──┤ H ├─┼────────┼────────────────────────■───────────────────┤       ├── ✂ Measure
         └───┘ │        │                        │                   └───────┘
Target Register (n qubits)
               │        │                        │
|ψ⟩_0: ────────U^1──────U^2────── ... ───────────U^{2^{t-1}}──────────────────</pre>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Circuit image placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>4. Mathematical Proof & State Evolution</h2>
        
        <h3 style="margin-top: 1.5rem;">Step 1: Initialisation</h3>
        <p>We start with a \(t\)-qubit counting register initialised to \(|0\rangle^{\otimes t}\) and an \(n\)-qubit target register initialised to the eigenvector \(|\psi\rangle\):</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_0\rangle = |0\rangle^{\otimes t} \otimes |\psi\rangle\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 2: Applying the Hadamard Gates</h3>
        <p>Applying \(H^{\otimes t}\) to the counting register creates a superposition over all integers \(x\) from \(0\) to \(2^t-1\):</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_1\rangle = \frac{1}{\sqrt{2^t}} \sum_{x=0}^{2^t-1} |x\rangle \otimes |\psi\rangle\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 3: Controlled Unitary Operations & Phase Kickback</h3>
        <p>We apply the sequence of controlled-\(U^{2^j}\) operations. For a specific state \(|x\rangle\) in the superposition, the operator \(U\) is applied exactly \(x\) times. Since \(U|\psi\rangle = e^{2\pi i \theta}|\psi\rangle\), applying \(U\) \(x\) times yields a phase factor of \(e^{2\pi i x \theta}\):</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_2\rangle = \frac{1}{\sqrt{2^t}} \sum_{x=0}^{2^t-1} e^{2\pi i x \theta} |x\rangle \otimes |\psi\rangle\)</p>
        </div>
        <p>The target register remains \(|\psi\rangle\) and is completely unentangled from the counting register. We can ignore it for the rest of the algorithm. The counting register is now exactly in the state of a Quantum Fourier Transform applied to the value \(2^t \theta\).</p>

        <h3 style="margin-top: 1.5rem;">Step 4: Inverse Quantum Fourier Transform</h3>
        <p>We apply the \(QFT^\dagger\) to the counting register. The mathematical action of \(QFT^\dagger\) on a state \(|x\rangle\) is to map it to \(\frac{1}{\sqrt{2^t}} \sum_{y=0}^{2^t-1} e^{-2\pi i x y / 2^t} |y\rangle\):</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_3\rangle = \frac{1}{2^t} \sum_{y=0}^{2^t-1} \sum_{x=0}^{2^t-1} e^{2\pi i x \left(\theta - \frac{y}{2^t}\right)} |y\rangle\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Measurement</h3>
        <p>If \(\theta\) can be expressed exactly in \(t\) bits, then there exists some integer \(y\) such that \(\theta = y/2^t\). For this specific \(y\), the exponent becomes \(0\), the inner sum constructively interferes to \(2^t\), and the amplitude for \(|y\rangle\) becomes \(1\).</p>
        <p>If \(\theta\) is not exactly representable in \(t\) bits, the probability distribution peaks sharply around the integer \(y\) that is closest to \(2^t \theta\). Measuring the counting register yields this integer \(y\), allowing us to estimate \(\theta \approx y/2^t\).</p>
    </section>

    <section class="content-section">
        <h2>5. Interactive Visualisation</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Phase Disks (Post-Kickback):</strong> Before the \(QFT^\dagger\), the amplitude for every counting state \(|x\rangle\) is equal. However, the phase arrows form a perfect corkscrew pattern. The "tightness" of this spiral is proportional to the unknown phase \(\theta\).</li>
            <li><strong>Amplitude Histogram:</strong> Following the \(QFT^\dagger\), the flat probability distribution collapses. A single, dominant bar will appear at the integer \(y\). As you dynamically change \(\theta\) in the interactive module, you will see this peak slide continuously across the histogram.</li>
        </ul>
        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg></div>
            <h3>Dynamic State Tracking</h3>
            <p>Interactive module (amplitude histograms, Bloch spheres) to simulate the algorithm live.</p>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Interactive visualization placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>6. Python Code Implementation</h2>
        
        <h3>From Scratch (NumPy)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / NumPy</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>import numpy as np

def simulate_qpe(theta, t_qubits):
    \"\"\"
    Simulates QPE mathematically using NumPy for a 1-qubit unitary.
    \"\"\"
    N = 2**t_qubits
    
    # 1. Prepare the counting register after phase kickback
    # State is 1/sqrt(N) * sum_x exp(2 * pi * i * x * theta) |x>
    psi_2 = np.zeros(N, dtype=complex)
    for x in range(N):
        psi_2[x] = np.exp(2 * np.pi * 1j * x * theta) / np.sqrt(N)
        
    # 2. Build the Inverse QFT Matrix
    omega = np.exp(-2 * np.pi * 1j / N) # Notice the negative sign for inverse
    iqft_matrix = np.zeros((N, N), dtype=complex)
    for row in range(N):
        for col in range(N):
            iqft_matrix[row, col] = (omega ** (row * col)) / np.sqrt(N)
            
    # 3. Apply IQFT
    psi_final = np.dot(iqft_matrix, psi_2)
    
    # 4. Measure
    probabilities = np.abs(psi_final)**2
    measured_y = np.argmax(probabilities)
    estimated_theta = measured_y / N
    
    return estimated_theta, probabilities

# Estimate theta = 0.375 using 3 qubits (0.375 * 8 = 3.0, should peak at exactly 3)
estimated, probs = simulate_qpe(0.375, 3)
print(f"Estimated Phase: {estimated}")
</code></pre>
            </div>
        </div>
        
        <h3 style="margin-top: 1.5rem;">Framework (Qiskit)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / Qiskit</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT
from qiskit_aer import AerSimulator
import numpy as np

def qpe_circuit(theta, t_qubits):
    # Total qubits = counting qubits (t) + target qubits (1)
    qc = QuantumCircuit(t_qubits + 1, t_qubits)
    
    # 1. Prepare target eigenvector (for a simple P gate, |1> is the eigenvector)
    qc.x(t_qubits)
    
    # 2. Apply H to counting register
    for q in range(t_qubits):
        qc.h(q)
        
    qc.barrier()
    
    # 3. Controlled Unitary operations (U = PhaseGate(2 * pi * theta))
    repetitions = 1
    for counting_qubit in range(t_qubits):
        for _ in range(repetitions):
            # Apply controlled phase rotation
            qc.cp(2 * np.pi * theta, counting_qubit, t_qubits)
        repetitions *= 2
        
    qc.barrier()
    
    # 4. Apply Inverse QFT to counting register
    iqft = QFT(num_qubits=t_qubits, inverse=True, do_swaps=True).to_gate()
    qc.append(iqft, range(t_qubits))
    
    # 5. Measure counting register
    qc.measure(range(t_qubits), range(t_qubits))
    
    return qc
# Simulate
t = 3
actual_theta = 0.375 # Corresponds to 3/8
circuit = qpe_circuit(actual_theta, t)
simulator = AerSimulator()
counts = simulator.run(circuit, shots=1024).result().get_counts()

print(f"Actual Phase: {actual_theta}")
print(f"Measurement Counts: {counts}")
# The result '011' in binary is 3. 3 / (2^3) = 0.375.
</code></pre>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>7. Caveats & Real-World Limits</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Circuit Depth:</strong> The algorithm requires \(U\) to be applied up to \(2^{t-1}\) times. If \(U\) is a complex operation (like a molecular Hamiltonian simulation), the circuit depth becomes exponentially long. On NISQ hardware, decoherence will completely destroy the state long before the \(QFT^\dagger\) can be applied.</li>
            <li><strong>Eigenvector Preparation:</strong> QPE assumes you can perfectly prepare the eigenvector \(|\psi\rangle\). In reality, finding the exact eigenvector is often as hard as finding the eigenvalue. If you prepare an imperfect state (a superposition of eigenvectors \(\sum_i c_i |\psi_i\rangle\)), QPE will probabilistically collapse the target state and yield the phase of \(|\psi_i\rangle\) with probability \(|c_i|^2\).</li>
        </ul>
    </section>

    <section class="content-section">
        <h2>8. Applications</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Shor's Algorithm:</strong> QPE is the core subroutine used to find the period of the modular exponentiation function, which directly leads to integer factorisation.</li>
            <li><strong>Quantum Chemistry:</strong> Used to estimate the exact ground-state energies of molecular Hamiltonians (though VQE is generally preferred for near-term hardware due to QPE's prohibitive circuit depth).</li>
            <li><strong>HHL Algorithm:</strong> The Harrow-Hassidim-Lloyd algorithm uses QPE to find the eigenvalues of a Hermitian matrix \(A\), which it then conditionally inverts to solve systems of linear equations exponentially faster than classical methods.</li>
        </ul>
    </section>
    
    <section class="content-section">
        <h2>9. References</h2>
        <ol style="line-height: 1.6;">
            <li>Kitaev, A. Y. (1995). Quantum measurements and the Abelian Stabilizer Problem. <em>arXiv preprint quant-ph/9511026</em>.</li>
            <li>Cleve, R., Ekert, A., Macchiavello, C., &amp; Mosca, M. (1998). Quantum algorithms revisited. <em>Proceedings of the Royal Society of London. Series A: Mathematical, Physical and Engineering Sciences</em>, 454(1969), 339-354.</li>
            <li>Nielsen, M. A., &amp; Chuang, I. L. (2010). <em>Quantum Computation and Quantum Information</em> (10th Anniversary ed.). Cambridge University Press.</li>
        </ol>
    </section>

    <nav class="algorithm-nav">
        <a href="qft.html" class="nav-button">
            <span class="nav-label">Previous</span>
            <span class="nav-title">Quantum Fourier Transform</span>
        </a>
        <a href="grover.html" class="nav-button nav-next">
            <span class="nav-label">Next</span>
            <span class="nav-title">Grover's Search Algorithm</span>
        </a>
    </nav>
    """.replace("{title}", title).replace("{category_name}", category_name)
    
    with open(f"/Users/aghatasheersyedi/Desktop/latex/class/qiskit/aqca/algorithms/{category}/{filename}", 'w') as f:
        html = HTML_TEMPLATE.format(
            title=title,
            description=f"AQCA - {title}",
            root_path="../../",
            extra_css="",
            extra_js="",
            algorithms_expanded="true",
            content=content
        )
        f.write(html)


def generate_grover_algorithm_page():
    title = "Grover's Search Algorithm"
    category_name = "Phase & Amplitude Core"
    filename = "grover.html"
    category = "phase-amplitude"
    
    content = r"""
    <div class="breadcrumb">
        <a href="../../index.html">Home</a> <span class="breadcrumb-separator">›</span> 
        <a href="../../algorithms.html">Algorithms</a> <span class="breadcrumb-separator">›</span> 
        {category_name} <span class="breadcrumb-separator">›</span> 
        {title}
    </div>

    <div class="algorithm-header">
        <h1>{title}</h1>
        <div class="algorithm-meta">
            <span class="badge badge-category">{category_name}</span>
        </div>
    </div>

    <section class="content-section">
        <h2>1. Overview & Problem Definition</h2>
        <p><strong>Grover’s Search Algorithm</strong> provides a quantum method for searching an unstructured dataset or solving an unstructured search problem.</p>
        <p>Imagine you are looking for a specific marked item (or multiple marked items) in an unsorted list of \(N\) total items. Classically, because the list has no structure or index, you have no choice but to check the items one by one. You are given a black-box oracle function \(f(x)\) that returns \(1\) if \(x\) is the target item, and \(0\) otherwise.</p>

        <div class="complexity-comparison" style="margin-top: 1.5rem;">
            <div class="complexity-box">
                <h3>Classical Complexity</h3>
                <div class="complexity-value">\(\mathcal{O}(N)\)</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">On average, a classical computer must check \(N/2\) items, and in the worst case, all \(N\) items.</p>
            </div>
            <div class="complexity-box">
                <h3>Quantum Speedup</h3>
                <div class="complexity-value">\(\mathcal{O}(\sqrt{N})\)</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">A quantum computer finds the marked item in roughly \(\sqrt{N}\) steps, yielding a <strong>quadratic speedup</strong>.</p>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>2. Intuition</h2>
        <p>To understand Grover's algorithm, we must abandon the idea of "checking" items sequentially. Instead, we use <strong>Amplitude Amplification</strong>.</p>
        <ol style="line-height: 1.6;">
            <li><strong>Equal Superposition:</strong> We start by placing all \(N\) possible items into a massive, equal superposition. At this stage, if we measured the system, we would get any item with an equal, tiny probability.</li>
            <li><strong>The Oracle (Phase Inversion):</strong> We pass this superposition into the oracle. The oracle recognises the target item and flips its quantum phase (multiplying its amplitude by \(-1\)). Geometrically, if you picture all the probability amplitudes as bars on a graph, the target bar is now pointing downwards.</li>
            <li><strong>The Diffuser (Inversion about the Mean):</strong> We apply a secondary operation that calculates the average height of all the amplitude bars. Because one bar is now negative, the overall average is pulled down slightly. The operation then inverts every bar around this new average. The non-target bars shrink, and the target bar (which was negative) shoots up massively in the positive direction.</li>
        </ol>
        <p>By repeating Steps 2 and 3 a specific number of times, we systematically drain the probability from all incorrect answers and pump it into the correct answer. Once the target's probability approaches 100%, we measure the system to find the needle in the haystack.</p>
    </section>

    <section class="content-section">
        <h2>3. Required Gates & Circuit Schematic</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Hadamard (\(H^{\otimes n}\)):</strong> Creates the initial equal superposition state \(|s\rangle\).</li>
            <li><strong>Oracle (\(U_\omega\)):</strong> A unitary operator that applies a phase flip to the marked state(s). \(U_\omega = I - 2|\omega\rangle\langle\omega|\).</li>
            <li><strong>Diffusion Operator (\(U_s\)):</strong> Often called the Grover Diffuser. It performs inversion about the mean. \(U_s = 2|s\rangle\langle s| - I\).</li>
        </ul>

        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="10" rx="2" ry="2"></rect><line x1="12" y1="3" x2="12" y2="7"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg></div>
            <h3>Circuit Schematic</h3>
            <pre style="background: var(--code-bg); padding: 1rem; border-radius: 4px; overflow-x: auto; margin-top: 1rem; color: var(--text-color);">
       ┌───┐ ┌────────┐ ┌─────────┐
q_0: ──┤ H ├─┤        ├─┤         ├─ ... ─ ✂ Measure
       ├───┤ │ Oracle │ │ Diffuser│
q_1: ──┤ H ├─┤  U_w   ├─┤   U_s   ├─ ... ─ ✂ Measure
      ...    │        │ │         │
       ├───┤ │        │ │         │
q_n: ──┤ H ├─┤        ├─┤         ├─ ... ─ ✂ Measure
       └───┘ └────────┘ └─────────┘
             \________  __________/
                      \/
      Repeat ≈ (π/4)√N times (Grover Iteration)</pre>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Circuit image placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>4. Mathematical Proof & State Evolution</h2>
        
        <h3 style="margin-top: 1.5rem;">Step 1: Initialisation</h3>
        <p>We start with \(n\) qubits (where \(N = 2^n\)) initialised to \(|0\rangle^{\otimes n}\). Applying Hadamard gates creates the uniform superposition state \(|s\rangle\):</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|s\rangle = H^{\otimes n} |0\rangle^{\otimes n} = \frac{1}{\sqrt{N}} \sum_{x=0}^{N-1} |x\rangle\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 2: The Oracle (\(U_\omega\))</h3>
        <p>Let the marked state be \(|\omega\rangle\). The oracle applies a negative phase only to \(|\omega\rangle\):</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(U_\omega |x\rangle = \begin{cases} -|x\rangle & \text{if } x = \omega \\ |x\rangle & \text{if } x \neq \omega \end{cases}\)</p>
        </div>
        <p>The state becomes:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\psi_1\rangle = U_\omega |s\rangle = \frac{1}{\sqrt{N}} \sum_{x \neq \omega} |x\rangle - \frac{1}{\sqrt{N}} |\omega\rangle\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 3: The Diffusion Operator (\(U_s\))</h3>
        <p>The diffuser is defined as \(U_s = 2|s\rangle\langle s| - I\). When applied to an arbitrary state \(\sum \alpha_x |x\rangle\), it transforms each amplitude \(\alpha_x\) into \(2\mu - \alpha_x\), where \(\mu\) is the mean of all amplitudes.</p>
        <p>Applying it to \(|\psi_1\rangle\) amplifies the amplitude of \(|\omega\rangle\) while suppressing the others.</p>

        <h3 style="margin-top: 1.5rem;">Step 4: Geometric Rotation (The Grover Operator \(G\))</h3>
        <p>One full iteration is \(G = U_s U_\omega\).</p>
        <p>Geometrically, the state vector of the system sits in a 2D plane defined by two orthogonal vectors: the target state \(|\omega\rangle\) and the superposition of all non-target states \(|s'\rangle\).</p>
        <p>The initial state \(|s\rangle\) is very close to the \(|s'\rangle\) axis, separated by a tiny angle \(\theta\), where \(\sin(\theta) = 1/\sqrt{N}\).</p>
        <p>Every application of the Grover operator \(G\) rotates the state vector closer to the target \(|\omega\rangle\) by exactly \(2\theta\).</p>

        <h3 style="margin-top: 1.5rem;">Measurement</h3>
        <p>After \(k\) iterations, the state is rotated by \((2k + 1)\theta\). To align the vector perfectly with \(|\omega\rangle\), we need:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\((2k + 1)\theta \approx \frac{\pi}{2}\)</p>
        </div>
        <p>Since \(\theta \approx 1/\sqrt{N}\) for large \(N\), the optimal number of iterations \(k\) is:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(k \approx \frac{\pi}{4}\sqrt{N}\)</p>
        </div>
        <p>Measuring the system after exactly \(k\) iterations yields the marked state \(|\omega\rangle\) with a probability approaching \(100\%\).</p>
    </section>

    <section class="content-section">
        <h2>5. Interactive Visualisation</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Amplitude Histogram:</strong> In an interactive module, users should step through the circuit.
                <ol>
                    <li>Initialisation: A completely flat histogram.</li>
                    <li>Oracle step: One specific bar flips upside down to negative.</li>
                    <li>Diffusion step: The flat line drops slightly, and the negative bar rockets upwards into the positive domain.</li>
                </ol>
                <em>Repeating this loop shows the target bar growing steadily while the others shrink into nothing.</em>
            </li>
            <li><strong>2D Vector Plane:</strong> Displays the state vector in the \(|\omega\rangle\) vs \(|s'\rangle\) plane. Each Grover iteration visually rotates the arrow by a fixed angle \(2\theta\) until it aligns with the vertical axis.</li>
        </ul>
        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg></div>
            <h3>Dynamic State Tracking</h3>
            <p>Interactive module (amplitude histograms, Bloch spheres) to simulate the algorithm live.</p>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Interactive visualization placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>6. Python Code Implementation</h2>
        
        <h3>From Scratch (NumPy)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / NumPy</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>import numpy as np

def simulate_grover(n_qubits, target_index):
    \"\"\"
    Simulates Grover's algorithm mathematically using pure NumPy.
    \"\"\"
    N = 2**n_qubits
    
    # 1. Initialise equal superposition |s>
    s = np.ones((N, 1), dtype=complex) / np.sqrt(N)
    
    # 2. Construct Oracle (U_w)
    # Identity matrix, but with -1 at the target_index
    U_w = np.eye(N, dtype=complex)
    U_w[target_index, target_index] = -1.0
    
    # 3. Construct Diffuser (U_s)
    # U_s = 2|s&gt;&lt;s| - I
    U_s = 2 * np.dot(s, s.conj().T) - np.eye(N, dtype=complex)
    
    # 4. Calculate optimal iterations k = pi/4 * sqrt(N)
    k = int(np.round((np.pi / 4) * np.sqrt(N)))
    
    # 5. Apply Grover operator G = U_s * U_w for k iterations
    state = s
    for _ in range(k):
        state = np.dot(U_s, np.dot(U_w, state))
        
    # 6. Measure
    probabilities = np.abs(state.flatten())**2
    measured_index = np.argmax(probabilities)
    
    return measured_index, probabilities[measured_index], k

# Search for item at index '5' in an 8-item dataset (3 qubits)
found_idx, prob, iterations = simulate_grover(3, 5)
print(f"Found target {found_idx} with probability {prob:.4f} after {iterations} iterations.")
</code></pre>
            </div>
        </div>
        
        <h3 style="margin-top: 1.5rem;">Framework (Qiskit)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / Qiskit</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np

def grover_circuit(n, target_binary_string):
    qc = QuantumCircuit(n, n)
    
    # 1. Initialise superposition
    qc.h(range(n))
    qc.barrier()
    
    # Calculate optimal iterations
    iterations = int(np.round((np.pi / 4) * np.sqrt(2**n)))
    
    for _ in range(iterations):
        # 2. Oracle (Phase Flip the target state)
        # Flip qubits corresponding to '0's in the target string to apply multi-controlled Z
        for idx, bit in enumerate(target_binary_string[::-1]):
            if bit == '0':
                qc.x(idx)
                
        # Multi-controlled Z (applied via H, multi-controlled X, H trick)
        qc.h(n-1)
        qc.mcx(list(range(n-1)), n-1)
        qc.h(n-1)
        
        # Undo X gates
        for idx, bit in enumerate(target_binary_string[::-1]):
            if bit == '0':
                qc.x(idx)
        qc.barrier()
        
        # 3. Diffuser (Inversion about mean)
        qc.h(range(n))
        qc.x(range(n))
        
        qc.h(n-1)
        qc.mcx(list(range(n-1)), n-1)
        qc.h(n-1)
        
        qc.x(range(n))
        qc.h(range(n))
        qc.barrier()
        
    # 4. Measure
    qc.measure(range(n), range(n))
    return qc

# Simulate for a 3-qubit system looking for '101'
circuit = grover_circuit(3, '101')
simulator = AerSimulator()
counts = simulator.run(circuit, shots=1024).result().get_counts()

print("Measurement Counts:", counts)
</code></pre>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>7. Caveats & Real-World Limits</h2>
        <ul style="line-height: 1.6;">
            <li><strong>The Over-Rotation Problem:</strong> Unlike classical loops where running more iterations is safe, Grover's algorithm rotates a state vector. If you exceed the optimal number of iterations \(k\), the state vector rotates <em>past</em> the target \(|\omega\rangle\), and the probability of finding the correct answer begins to decrease back towards zero. You must know (or estimate) the number of marked items to calculate the correct stopping point.</li>
            <li><strong>The I/O Bottleneck:</strong> Grover's algorithm assumes the oracle can evaluate the database in a quantum superposition. If you are searching a classical database, you must first construct a quantum RAM (qRAM) representation of that database. The computational time required to load classical data into qRAM is \(\mathcal{O}(N)\), which completely eliminates the \(\mathcal{O}(\sqrt{N})\) quantum speedup.</li>
            <li><strong>Hardware Scaling:</strong> The algorithm requires multi-controlled gates (like the Toffoli gate scaled to \(n\) qubits), which decompose into extremely deep circuits. On NISQ hardware, these deep circuits introduce catastrophic levels of noise before the iterations finish.</li>
        </ul>
    </section>

    <section class="content-section">
        <h2>8. Applications</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Cryptography & Hash Inversion:</strong> Grover's algorithm poses a direct threat to symmetric-key cryptography. It can be used to brute-force a 256-bit AES key in \(2^{128}\) operations. This is why the cybersecurity industry is migrating to AES-256 (which offers 128 bits of post-quantum security) to replace AES-128 (which is broken by Grover's).</li>
            <li><strong>Accelerating NP-Complete Problems:</strong> By treating a complex boolean satisfiability problem (like 3-SAT) as an unstructured search space, Grover's algorithm can provide a quadratic speedup for finding valid solutions, provided the problem can be efficiently encoded into a quantum oracle.</li>
        </ul>
    </section>
    
    <section class="content-section">
        <h2>9. References</h2>
        <ol style="line-height: 1.6;">
            <li>Grover, L. K. (1996). A fast quantum mechanical algorithm for database search. <em>Proceedings of the 28th Annual ACM Symposium on Theory of Computing</em>, 212–219.</li>
            <li>Boyer, M., Brassard, G., Høyer, P., &amp; Tapp, A. (1998). Tight bounds on quantum searching. <em>Fortschritte der Physik: Progress of Physics</em>, 46(4-5), 493-505.</li>
            <li>Nielsen, M. A., &amp; Chuang, I. L. (2010). <em>Quantum Computation and Quantum Information</em> (10th Anniversary ed.). Cambridge University Press.</li>
        </ol>
    </section>

    <nav class="algorithm-nav">
        <a href="qpe.html" class="nav-button">
            <span class="nav-label">Previous</span>
            <span class="nav-title">Quantum Phase Estimation</span>
        </a>
        <a href="amplitude-amplification.html" class="nav-button nav-next">
            <span class="nav-label">Next</span>
            <span class="nav-title">Generalised Amplitude Amplification</span>
        </a>
    </nav>
    """.replace("{title}", title).replace("{category_name}", category_name)
    
    with open(f"/Users/aghatasheersyedi/Desktop/latex/class/qiskit/aqca/algorithms/{category}/{filename}", 'w') as f:
        html = HTML_TEMPLATE.format(
            title=title,
            description=f"AQCA - {title}",
            root_path="../../",
            extra_css="",
            extra_js="",
            algorithms_expanded="true",
            content=content
        )
        f.write(html)


def generate_amplitude_amplification_algorithm_page():
    title = "Generalised Amplitude Amplification"
    category_name = "Phase & Amplitude Core"
    filename = "amplitude-amplification.html"
    category = "phase-amplitude"
    
    content = r"""
    <div class="breadcrumb">
        <a href="../../index.html">Home</a> <span class="breadcrumb-separator">›</span> 
        <a href="../../algorithms.html">Algorithms</a> <span class="breadcrumb-separator">›</span> 
        {category_name} <span class="breadcrumb-separator">›</span> 
        {title}
    </div>

    <div class="algorithm-header">
        <h1>{title}</h1>
        <div class="algorithm-meta">
            <span class="badge badge-category">{category_name}</span>
        </div>
    </div>

    <section class="content-section">
        <h2>1. Overview & Problem Definition</h2>
        <p><strong>Generalised Amplitude Amplification (GAA)</strong> is the broader mathematical framework that encompasses Grover’s Search. While Grover’s Algorithm assumes you are searching a completely unstructured dataset (starting with a uniform distribution where every item has an equal probability), real-world problems often have heuristics.</p>
        <p>Suppose you have an arbitrary quantum algorithm (let us call it \(\mathcal{A}\)) that guesses the correct answer to a problem with a small probability \(p\). Classically, you would just run \(\mathcal{A}\) repeatedly until it succeeds. Generalised Amplitude Amplification allows a quantum computer to boost that success probability to near \(100\%\) using quadratically fewer repetitions than a classical computer.</p>

        <div class="complexity-comparison" style="margin-top: 1.5rem;">
            <div class="complexity-box">
                <h3>Classical Complexity</h3>
                <div class="complexity-value">\(\mathcal{O}(1/p)\)</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">You must run the classical heuristic algorithm roughly \(1/p\) times to find a successful outcome.</p>
            </div>
            <div class="complexity-box">
                <h3>Quantum Speedup</h3>
                <div class="complexity-value">\(\mathcal{O}(1/\sqrt{p})\)</div>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">GAA applies the quantum operator roughly \(1/\sqrt{p}\) times, achieving a <strong>quadratic speedup</strong>.</p>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>2. Intuition</h2>
        <p>Think of your initial quantum algorithm \(\mathcal{A}\) as a biased coin. Instead of a 50/50 chance, it might have a 1% chance of landing on "heads" (the correct answer).</p>
        <p>In standard Grover's search, the "Diffuser" acts like a mirror reflecting probability amplitudes around the <em>average</em> of a perfectly uniform flat line.</p>
        <p>In Generalised Amplitude Amplification, the mirror is tilted. We replace the standard diffuser with a custom operator that reflects amplitudes around the specific, biased distribution created by algorithm \(\mathcal{A}\). By wrapping your algorithm \(\mathcal{A}\) inside this custom reflection loop, the quantum interference systematically siphons probability away from the incorrect outputs of \(\mathcal{A}\) and pumps it into the correct outputs, rotating the state towards a successful measurement.</p>
    </section>

    <section class="content-section">
        <h2>3. Required Gates & Circuit Schematic</h2>
        <ul style="line-height: 1.6;">
            <li><strong>State Preparation (\(\mathcal{A}\)):</strong> Any arbitrary quantum circuit that prepares the initial superposition. (In standard Grover's, \(\mathcal{A} = H^{\otimes n}\)).</li>
            <li><strong>Oracle (\(U_\omega\)):</strong> Flips the phase of the "good" (target) states.</li>
            <li><strong>Inverse Preparation (\(\mathcal{A}^{-1}\) or \(\mathcal{A}^\dagger\)):</strong> The exact reverse of the preparation circuit.</li>
            <li><strong>Zero-Reflection (\(S_0\)):</strong> Flips the phase of the \(|00\dots0\rangle\) state.</li>
        </ul>
        <p>The custom Diffuser is constructed as \(Q = -\mathcal{A} S_0 \mathcal{A}^{-1} U_\omega\).</p>

        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="10" rx="2" ry="2"></rect><line x1="12" y1="3" x2="12" y2="7"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg></div>
            <h3>Circuit Schematic</h3>
            <pre style="background: var(--code-bg); padding: 1rem; border-radius: 4px; overflow-x: auto; margin-top: 1rem; color: var(--text-color);">
       ┌───┐ ┌────────┐ ┌───────┐ ┌──────┐ ┌───┐
q_0: ──┤   ├─┤        ├─┤       ├─┤      ├─┤   ├─ ... ─ ✂ Measure
       │   │ │ Oracle │ │       │ │ Zero │ │   │
q_1: ──┤ A ├─┤  U_w   ├─┤ A^{-1}├─┤ Phase├─┤ A ├─ ... ─ ✂ Measure
      ...  │ │        │ │       │ │ Flip │ │   │
       │   │ │        │ │       │ │      │ │   │
q_n: ──┤   ├─┤        ├─┤       ├─┤      ├─┤   ├─ ... ─ ✂ Measure
       └───┘ └────────┘ └───────┘ └──────┘ └───┘
             \________  _______________________/
                      \/
      Repeat ≈ (π/4√p) times (Amplification Loop)</pre>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Circuit image placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>4. Mathematical Proof & State Evolution</h2>
        
        <h3 style="margin-top: 1.5rem;">Step 1: Initialisation</h3>
        <p>We begin with the zero state and apply our arbitrary algorithm \(\mathcal{A}\):</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\Psi\rangle = \mathcal{A}|0\rangle^{\otimes n}\)</p>
        </div>
        <p>We can split this state into two orthogonal components: the "good" states we want to find (\(|\Psi_{good}\rangle\)) and the "bad" states (\(|\Psi_{bad}\rangle\)). Let \(p\) be the probability of measuring a good state. We can rewrite \(|\Psi\rangle\) using an angle \(\theta\), where \(\sin^2(\theta) = p\):</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(|\Psi\rangle = \sin(\theta)|\Psi_{good}\rangle + \cos(\theta)|\Psi_{bad}\rangle\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 2: The Oracle (\(U_\omega\))</h3>
        <p>The oracle isolates the good states and flips their phase:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(U_\omega |\Psi\rangle = -\sin(\theta)|\Psi_{good}\rangle + \cos(\theta)|\Psi_{bad}\rangle\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Step 3: The Custom Diffuser</h3>
        <p>The diffuser operator is defined as \(U_s = -\mathcal{A} S_0 \mathcal{A}^{-1}\), where \(S_0 = I - 2|0\rangle\langle0|\) flips the phase of the all-zero state.</p>
        <p>Mathematically, this evaluates to \(U_s = 2|\Psi\rangle\langle\Psi| - I\), which is an inversion about the initial state \(|\Psi\rangle\).</p>

        <h3 style="margin-top: 1.5rem;">Step 4: Geometric Rotation (The Q Operator)</h3>
        <p>One full amplification iteration is \(Q = -U_s U_\omega\).</p>
        <p>Just like Grover's, applying \(Q\) performs a rotation in the 2D plane defined by \(|\Psi_{good}\rangle\) and \(|\Psi_{bad}\rangle\). Because our initial state \(|\Psi\rangle\) is offset from the bad axis by the angle \(\theta\), each application of \(Q\) rotates the state vector by exactly \(2\theta\) towards \(|\Psi_{good}\rangle\).</p>
        <p>After \(k\) iterations, the state becomes:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(Q^k |\Psi\rangle = \sin((2k+1)\theta)|\Psi_{good}\rangle + \cos((2k+1)\theta)|\Psi_{bad}\rangle\)</p>
        </div>

        <h3 style="margin-top: 1.5rem;">Measurement</h3>
        <p>To maximise the probability of measuring a good state, we need \(\sin((2k+1)\theta) \approx 1\).</p>
        <p>This requires \((2k+1)\theta \approx \pi/2\). Since \(\sin(\theta) = \sqrt{p}\), for small \(p\), \(\theta \approx \sqrt{p}\).</p>
        <p>Solving for \(k\) gives the optimal number of iterations:</p>
        <div class="math-container" style="margin: 0.5rem 0;">
            <p>\(k \approx \frac{\pi}{4\sqrt{p}}\)</p>
        </div>
        <p>Measuring the system after \(k\) iterations yields a "good" state with a probability approaching \(100\%\).</p>
    </section>

    <section class="content-section">
        <h2>5. Interactive Visualisation</h2>
        <ul style="line-height: 1.6;">
            <li><strong>2D Vector Plane:</strong> The visualizer will show the \(|\Psi_{good}\rangle\) vs \(|\Psi_{bad}\rangle\) plane. Unlike Grover's where the initial arrow is practically flat against the horizontal axis (because \(1/\sqrt{N}\) is tiny), GAA allows the user to set a custom initial probability \(p\). If \(p=25\%\), the initial arrow sits at a steep \(30^\circ\) angle (\(\theta\)). The user can watch how only one iteration (\(2\theta = 60^\circ\)) rotates the vector to exactly \(90^\circ\), requiring vastly fewer steps than a uniform search.</li>
            <li><strong>Amplitude Histogram:</strong> Displays the highly irregular initial distribution created by \(\mathcal{A}\). During the diffusion step, the user can see the amplitudes reflecting not around a flat average, but mirroring across the specific "shape" of the initial distribution.</li>
        </ul>
        <div class="simulation-placeholder" style="margin-top: 1.5rem;">
            <div class="simulation-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg></div>
            <h3>Dynamic State Tracking</h3>
            <p>Interactive module (amplitude histograms, Bloch spheres) to simulate the algorithm live.</p>
            <p style="margin-top: 0.5rem; font-style: italic; color: var(--muted-text);">[Interactive visualization placeholder to be added later]</p>
        </div>
    </section>

    <section class="content-section">
        <h2>6. Python Code Implementation</h2>
        
        <h3>From Scratch (NumPy)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / NumPy</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>import numpy as np

def simulate_amplitude_amplification(p_success):
    \"\"\"
    Simulates Generalised Amplitude Amplification mathematically using NumPy.
    p_success: The initial probability p of the algorithm A finding the target.
    \"\"\"
    # Define the 2D subspace: |bad> = [1, 0]^T, |good> = [0, 1]^T
    theta = np.arcsin(np.sqrt(p_success))
    
    # Initial state |Psi> created by A
    psi = np.array([[np.cos(theta)], [np.sin(theta)]])
    
    # 1. Oracle U_w (flips phase of |good>)
    U_w = np.array([[1, 0], [0, -1]])
    
    # 2. Diffuser U_s = 2|Psi&gt;&lt;Psi| - I
    U_s = 2 * np.dot(psi, psi.T) - np.eye(2)
    
    # 3. The Amplification Operator Q
    Q = np.dot(U_s, U_w)
    
    # 4. Calculate optimal iterations k
    k = int(np.round(np.pi / (4 * theta) - 0.5))
    if k < 0: k = 0
    
    # 5. Apply Q for k iterations
    state = psi
    for _ in range(k):
        state = np.dot(Q, state)
        
    prob_good = np.abs(state[1, 0])**2
    return prob_good, k

# If our heuristic has a 10% chance of success
final_prob, iterations = simulate_amplitude_amplification(0.10)
print(f"Boosted to {final_prob*100:.2f}% success in {iterations} iterations.")
</code></pre>
            </div>
        </div>
        
        <h3 style="margin-top: 1.5rem;">Framework (Qiskit)</h3>
        <div class="code-block">
            <div class="code-header">
                <span>Python / Qiskit</span>
                <button>Copy Code</button>
            </div>
            <div class="code-content">
<pre><code>from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np

def create_A_operator():
    \"\"\"Custom algorithm A that biases towards the target state |11>.\"\"\"
    qc = QuantumCircuit(2)
    # Using Ry rotations to create a biased probability instead of pure Hadamards
    qc.ry(np.pi/3, 0) 
    qc.ry(np.pi/3, 1)
    return qc

def create_A_inverse():
    \"\"\"The exact inverse of A.\"\"\"
    return create_A_operator().inverse()

def gaa_circuit(target_state='11'):
    qc = QuantumCircuit(2, 2)
    
    # 1. Prepare initial state using A
    qc.compose(create_A_operator(), inplace=True)
    qc.barrier()
    
    iterations = 2 # Calculated based on the specific Ry angles used
    
    for _ in range(iterations):
        # 2. Oracle (CZ gate for |11>)
        qc.cz(0, 1)
        qc.barrier()
        
        # 3. Custom Diffuser: A^{-1} -> Zero Reflection -> A
        qc.compose(create_A_inverse(), inplace=True)
        
        # Zero reflection S_0 (flips |00>)
        qc.x([0, 1])
        qc.cz(0, 1)
        qc.x([0, 1])
        
        qc.compose(create_A_operator(), inplace=True)
        qc.barrier()
        
    qc.measure([0,1], [0,1])
    return qc

circuit = gaa_circuit()
simulator = AerSimulator()
counts = simulator.run(circuit, shots=1024).result().get_counts()
print("Measurement Counts:", counts)
</code></pre>
            </div>
        </div>
    </section>

    <section class="content-section">
        <h2>7. Caveats & Real-World Limits</h2>
        <ul style="line-height: 1.6;">
            <li><strong>The Over-Rotation Problem (Soufflé Problem):</strong> Just like standard Grover's, if you apply the \(Q\) operator too many times, the state vector will rotate past the \(|\Psi_{good}\rangle\) axis, and your probability of success will plummet. You must have a reasonable estimate of \(p\) to know when to stop. If \(p\) is entirely unknown, you must use a schedule of varying iterations (Quantum Amplitude Estimation) to find it.</li>
            <li><strong>Circuit Depth Multiplication:</strong> If your initial heuristic algorithm \(\mathcal{A}\) is already a deep, complex circuit, GAA requires you to run \(\mathcal{A}\) and its inverse \(\mathcal{A}^{-1}\) repeatedly. This multiplies the total circuit depth by \(\mathcal{O}(1/\sqrt{p})\), making it highly susceptible to decoherence on uncorrected hardware.</li>
        </ul>
    </section>

    <section class="content-section">
        <h2>8. Applications</h2>
        <ul style="line-height: 1.6;">
            <li><strong>Quantum Machine Learning:</strong> Used as a subroutine to boost the probability of measuring specific basis states in quantum neural networks and clustering algorithms.</li>
            <li><strong>Monte Carlo Speedup:</strong> The mathematical core of GAA is the backbone for Quantum Amplitude Estimation, which is used in quantum finance to perform Monte Carlo simulations (like option pricing and risk analysis) quadratically faster than classical supercomputers.</li>
            <li><strong>State Preparation:</strong> When trying to prepare a highly complex quantum state (where standard deterministic preparation is too deep), GAA can be used to boost a simpler, probabilistic state preparation circuit.</li>
        </ul>
    </section>
    
    <section class="content-section">
        <h2>9. References</h2>
        <ol style="line-height: 1.6;">
            <li>Brassard, G., Høyer, P., Mosca, M., &amp; Tapp, A. (2002). Quantum amplitude amplification and estimation. <em>Contemporary Mathematics</em>, 305, 53-74.</li>
            <li>Nielsen, M. A., &amp; Chuang, I. L. (2010). <em>Quantum Computation and Quantum Information</em> (10th Anniversary ed.). Cambridge University Press.</li>
        </ol>
    </section>

    <nav class="algorithm-nav">
        <a href="grover.html" class="nav-button">
            <span class="nav-label">Previous</span>
            <span class="nav-title">Grover's Search Algorithm</span>
        </a>
        <a href="../flagship-hybrid/vqe.html" class="nav-button nav-next">
            <span class="nav-label">Next</span>
            <span class="nav-title">Variational Quantum Eigensolver</span>
        </a>
    </nav>
    """.replace("{title}", title).replace("{category_name}", category_name)
    
    with open(f"/Users/aghatasheersyedi/Desktop/latex/class/qiskit/aqca/algorithms/{category}/{filename}", 'w') as f:
        html = HTML_TEMPLATE.format(
            title=title,
            description=f"AQCA - {title}",
            root_path="../../",
            extra_css="",
            extra_js="",
            algorithms_expanded="true",
            content=content
        )
        f.write(html)


# Algorithm Pages
generate_bell_state_page()
generate_superdense_coding_page()
generate_quantum_teleportation_page()
generate_entanglement_swapping_page()
generate_deutsch_algorithm_page()
generate_deutsch_jozsa_algorithm_page()
generate_bernstein_vazirani_algorithm_page()
generate_simon_algorithm_page()
generate_qft_algorithm_page()
generate_qpe_algorithm_page()
generate_grover_algorithm_page()
generate_amplitude_amplification_algorithm_page()

generate_algorithm_page("flagship-hybrid", "shor.html", "Shor's Algorithm", "Flagship & Hybrid")
generate_algorithm_page("flagship-hybrid", "vqe.html", "Variational Quantum Eigensolver (VQE)", "Flagship & Hybrid")
generate_algorithm_page("flagship-hybrid", "qaoa.html", "Quantum Approximate Optimisation Algorithm (QAOA)", "Flagship & Hybrid")
generate_algorithm_page("flagship-hybrid", "hhl.html", "HHL Algorithm", "Flagship & Hybrid")

generate_algorithm_page("fault-tolerance", "3-qubit-code.html", "3-Qubit Bit-Flip / Phase-Flip Codes", "Fault Tolerance")
generate_algorithm_page("fault-tolerance", "shors-9-qubit-code.html", "Shor's 9-Qubit Code", "Fault Tolerance")
generate_algorithm_page("fault-tolerance", "steane-code.html", "Steane 7-Qubit Code", "Fault Tolerance")

generate_global_page("appendix.html", "Appendix", r"""
    <div class="page-header" style="display: flex; flex-direction: column; align-items: flex-start; margin-bottom: 3rem;">
        <h1 style="margin-bottom: 0.5rem;">Appendix</h1>
        <p style="color: var(--muted-text); margin-top: 0;">Everything from Quantum Computing Basics is derived rigorously and in detailed mathematical form here.</p>
    </div>
    
    <div class="content-section" style="background-color: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-top: 0; margin-bottom: 2rem; border: none; padding: 0;">QC Basics Detailed Derivations</h2>
        
        <div class="appendix-links" style="line-height: 2.8; font-size: 0.95rem;">
<a href="details/ket.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Ket</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/bra.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Bra</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/inner-product.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Inner Product</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/tensor-product.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Tensor Product</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/superposition.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Superposition</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/entanglement.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Entanglement</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/pure-vs-mixed-states.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Pure vs. Mixed States</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/key-properties.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Key Properties</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/partial-trace.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Partial Trace</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/single-qubit-gates.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Single-Qubit Gates</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/rotation-gates.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Rotation Gates</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/two-qubit-gates.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Two-Qubit Gates</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/multi-qubit-gates.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Multi-Qubit Gates</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/reversibility-and-uncomputing.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Reversibility & Uncomputing</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/quantum-oracles.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Quantum Oracles</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/the-kickback-mechanism.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">The Kickback Mechanism</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/quantum-parallelism.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Quantum Parallelism</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/measurement-and-wavefunction-collapse.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Measurement & Wavefunction Collapse</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/mutually-unbiased-bases.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Mutually Unbiased Bases</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/heisenberg-uncertainty-principle.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Heisenberg Uncertainty Principle</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/the-no-cloning-theorem.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">The No-Cloning Theorem</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/divincenzo's-criteria.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">DiVincenzo's Criteria</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/quantum-noise-channels.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Quantum Noise Channels</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/decoherence-times.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Decoherence Times</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/fidelity.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Fidelity</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/trace-distance.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Trace Distance</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/quantum-state-tomography.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Quantum State Tomography</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/threshold-theorem.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Threshold Theorem</a> <span style='color: #a0aabf; margin: 0 0.2rem;'>•</span> <a href="details/logical-qubits.html" style="color: var(--primary); font-weight: 600; text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 6px; background-color: var(--surface-hover); transition: all 0.2s;" onmouseover="this.style.backgroundColor='var(--primary-light)'; this.style.color='var(--primary)'" onmouseout="this.style.backgroundColor='var(--surface-hover)'; this.style.color='var(--primary)'">Logical Qubits</a>
        </div>
    </div>
""")

print("All HTML pages generated successfully.")
