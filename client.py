import streamlit as st
import requests
import json
import os
import tempfile
import time


st.set_page_config(
    page_title="Assignment Grader",
    page_icon="📝",
    layout="wide"
)


# Main title
st.title("📝 Assignment Grader")
st.markdown("upload assignments and grade them automatically with AI")



st.sidebar.header("About")
st.sidebar.info("""
                This is a demo of the Assignment Grader using FastMCP and OpenAI.
                Upload assignmebt in PDF or DOCX format, set your grading rubic,
                and get instnat AI-powered grades detailde feedback.
                """)



# Create tabs
tab1, tab2, tab3 = st.tabs(["Upload Assignment", "Grade Assignment", "Results"])


# Tab 1: Upload Assignment
with tab1:
    st.header("Upload Assignment")

    # File upload
    uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'docx']) 