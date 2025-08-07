import streamlit as st
import streamlit.components.v1 as components
with open('riskysurvey.html', 'r') as f:
    html_data = f.read()
    components.html(html_data, height=1000, scrolling=True)
