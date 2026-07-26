import re

with open("generate_pages.py", "r") as f:
    text = f.read()

# 1. Fix the double braces issue
text = text.replace("{{", "{").replace("}}", "}")

# 2. Fix the Bell State navigation (remove Previous)
bell_nav_old = """    <nav class="algorithm-nav">
        <a href="#" class="nav-button">
            <span class="nav-label">Previous</span>
            <span class="nav-title">Algorithm Title</span>
        </a>
        <a href="superdense-coding.html" class="nav-button nav-next">
            <span class="nav-label">Next</span>
            <span class="nav-title">Superdense Coding</span>
        </a>
    </nav>"""
    
bell_nav_new = """    <nav class="algorithm-nav">
        <!-- No previous for the first algorithm -->
        <a href="superdense-coding.html" class="nav-button nav-next" style="margin-left: auto;">
            <span class="nav-label">Next</span>
            <span class="nav-title">Superdense Coding</span>
        </a>
    </nav>"""
text = text.replace(bell_nav_old, bell_nav_new)

# 3. Fix Entanglement Swapping navigation (Next should be Deutsch)
es_nav_old = """    <nav class="algorithm-nav">
        <a href="quantum-teleportation.html" class="nav-button">
            <span class="nav-label">Previous</span>
            <span class="nav-title">Quantum Teleportation</span>
        </a>
        <a href="../../algorithms.html" class="nav-button nav-next">
            <span class="nav-label">Next</span>
            <span class="nav-title">Algorithm Catalogue</span>
        </a>
    </nav>"""

es_nav_new = """    <nav class="algorithm-nav">
        <a href="quantum-teleportation.html" class="nav-button">
            <span class="nav-label">Previous</span>
            <span class="nav-title">Quantum Teleportation</span>
        </a>
        <a href="../oracle-based/deutsch.html" class="nav-button nav-next">
            <span class="nav-label">Next</span>
            <span class="nav-title">Deutsch\'s Algorithm</span>
        </a>
    </nav>"""
text = text.replace(es_nav_old, es_nav_new)

with open("generate_pages.py", "w") as f:
    f.write(text)
