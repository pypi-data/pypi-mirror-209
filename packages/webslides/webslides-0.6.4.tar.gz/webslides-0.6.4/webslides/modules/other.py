import os
import re


def extract_version(file_name: str) -> str:
    version_pattern = r'version="(\d+\.\d+\.\d+)"'
    version = None

    with open(file_name, "r") as file:
        file_contents = file.read()
        match = re.search(version_pattern, file_contents)
        if match:
            version = match.group(1)

    return version


def hello_world_html():
    fname = 'hello_world.py'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    fpath = os.path.join(current_dir)
    with open(f"{fpath}/{fname}", 'r') as f:
        code_lines = f.readlines()

    html_lines = [
        '<div style="font-size:1.1em;padding:15px;background-color:#fdffc7; display: inline-block;"><pre><code>']
    for line in code_lines:
        line = line.replace('import sys', '')
        line = line.replace('import os', '')
        line = line.replace("sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))", "")
        line = line.replace('import main as ws', 'import webslides as ws')
        html_line = line.rstrip().replace('<', '&lt;').replace('>', '&gt;')
        html_lines.append(html_line)
    html_lines.append('</code></pre></div>')

    # add copy button
    html_lines.append(
        """<br><br><button style="font-size: 1.3em; background-color: #00bb00;color: white;border-color: #c7c7c7 !important; border-radius: 6px;" onclick="navigator.clipboard.writeText(`""" + '\n'.join(
            html_lines[1:-1]) + """`);alert('Code copied to clipboard');"><b>COPY CODE</b></button>""")

    return '\n'.join(html_lines)


def code_to_html(code):
    # return f'<div style="font-family: Courier New; font-weight: normal; background-color:#fdffc7; display: inline-block; padding:15px;">{code}</div>'
    return f'<div style="background-color:#fdffc7; display: inline-block;font-size:1.1em;padding:15px;"><pre><code>{code}</code></pre></div>'
