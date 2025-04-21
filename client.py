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


#Main title
st.title("📝 Assignment Grader")
st.markdown("upload assignments and grade them automatically with AI")