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



    if uploaded_file is not None:
        #save the uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete-False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            file_path = tmp_file.name


        st.session_state['file_path'] = file_path
        st.session_state['file_name'] = uploaded_file.name


        # Parse the document
        if st.button("Process Document"):
            with st.spinner("Processing document..."):
                result = call_mcp_tool("parse_file", {"file_path": file_path})

