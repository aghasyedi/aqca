import re

with open("generate_pages.py", "r") as f:
    text = f.read()

# Change all content = rf""" to content = r"""
text = text.replace('content = rf"""', 'content = r"""')

# The closing is:
old_closing = '''    """
    
    with open(f"/Users/aghatasheersyedi/Desktop/latex/class/qiskit/aqca/algorithms/{category}/{filename}", 'w') as f:'''

new_closing = '''    """.replace("{title}", title).replace("{category_name}", category_name)
    
    with open(f"/Users/aghatasheersyedi/Desktop/latex/class/qiskit/aqca/algorithms/{category}/{filename}", 'w') as f:'''

text = text.replace(old_closing, new_closing)

# Revert my {{f(0)}} changes
text = text.replace("{{f(0)}}", "{f(0)}")
text = text.replace("{{f(1)}}", "{f(1)}")
text = text.replace("{{f(x)}}", "{f(x)}")
text = text.replace("{{f(0) \\oplus f(1)}}", "{f(0) \\oplus f(1)}")

with open("generate_pages.py", "w") as f:
    f.write(text)
