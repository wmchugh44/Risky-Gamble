import streamlit as st
import streamlit.components.v1 as components

# Fix: Instead of trying to read a .py file as HTML, we should use the HTML content directly
# The issue was that this file was trying to read 'risk-survey4.py' which contains a Python script
# that generates HTML, not HTML itself.

# Get the HTML content from the risk-survey4.py file properly
import sys
import os
sys.path.append(os.path.dirname(__file__))

# Import and execute the risk-survey4 module to get its HTML content
try:
    from importlib import import_module
    risk_survey_module = import_module('risk-survey4')
    # Extract the html_code variable from the module
    if hasattr(risk_survey_module, 'html_code'):
        html_data = risk_survey_module.html_code
    else:
        # Fallback: if the module doesn't have html_code, read it as a string
        with open('risk-survey4.py', 'r') as f:
            content = f.read()
            # Extract HTML content between triple quotes
            start_marker = 'html_code = """'
            end_marker = '"""'
            start_idx = content.find(start_marker)
            if start_idx != -1:
                start_idx += len(start_marker)
                end_idx = content.find(end_marker, start_idx)
                if end_idx != -1:
                    html_data = content[start_idx:end_idx]
                else:
                    html_data = "<p>Error: Could not extract HTML content</p>"
            else:
                html_data = "<p>Error: Could not find HTML content in risk-survey4.py</p>"
except Exception as e:
    html_data = f"<p>Error loading HTML content: {str(e)}</p>"

components.html(html_data, height=1000, scrolling=True)
