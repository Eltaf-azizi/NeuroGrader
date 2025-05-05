import streamlit as st
import requests
import json
import os
import tempfile
import time
import logging



# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)



# HARDCODED API KEYS - DO NOT SHARE THIS FILE
OPENAI_API_KEY = ""
GOOGLE_API_KEY = ""
GOOGLE_CX = ""



# Initialize session state variables
if 'api_server_url' not in st.session_state:
    st.session_state['api_server_url'] = "http://localhost:8088"



# Always use our hardcoded keys - don't get them from session_state
st.session_state['openai_api_key'] = OPENAI_API_KEY
st.session_state['google_api_key'] = GOOGLE_API_KEY
st.session_state['google_cx'] = GOOGLE_CX



# Function to call API tools
def call_api_tool(tool_name, data):
    """
    Call a tool on the API server with hardcoded API keys.
    """
    



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
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            file_path = tmp_file.name


        st.session_state['file_path'] = file_path
        st.session_state['file_name'] = uploaded_file.name


        # Parse the document
        if st.button("Process Document"):
            with st.spinner("Processing document..."):
                result = call_mcp_tool("parse_file", {"file_path": file_path})


                if result is None:
                    st.error("Failed to process document. Check server connection.")
                
                elif isinstance(result, str):
                    # If result is a string, it's either the document text or an error 
                    st.session_state['document_text'] = result
                    st.success(f"Document processed successfuly!")
                    st.info(f"Document contains {len(result.split())} words.")


                    # Show a preview
                    with st.expander("Document Preview"):
                        st.text(result[:1000] + ("..." if len(result) > 1000 else "")) 

                else:
                    # If result is a dict, might be error information
                    st.session_state['document_text'] = str(result)
                    st.success(f"Document processed!")


                # Show a preview
                with st.expander("Document Preview"):
                    st.json(result)




# Tab 2: Grade Assignment
with tab2:
    st.header("Gradign configuration")


    # Rubic input
    st.subheader("Grading Rubric")
    rubric = st.text_area(
        "Enter your grading rubric here: ",
        height=200,
        help =  "Specify the criteria on which the assignment should be graded",
        value = """Content (40%): The assignment should demonstrate a thorough understanding of the topic.
                Structure (20%): The assignment should be well-organized with a clear introduction, body, and conclusion.
                Analysis (30%): The assignment should include critical analusis backed by evidence.
                Grammar & Style (10%): The assignment should be free of grammatical errors and use appropriate academic language."""
    )



    # Plagiarism check option
    check_plagiarism_option = st.checkbox("Check for plagiarism", value=True)

    if 'document_text' in st.session_state and st.button("Grade Assignment"):
        # Store rubric in session
        st.session_state['rubric'] = rubric


        with st.spinner("Grading for progress..."):
            # Optional plagiarism check
            if check_plagiarism_option:
                st.info("Checking for plagiarism...")
                plagiarism_results = call_mcp_tool("check_plagiarism", {"text": st.session_state['document_text']})
                st.session_state['plagiarism_results'] = plagiarism_results
                if plagiarism_results is None:
                    st.warning("Plagiarism check failed or returned no results.")


            
            #Generate grade
            st.info("Generating grade...")
            grade_results = call_mcp_tool("grade_text", {
                "text": st.session_state['document_text'],
                "rubric": rubric
            })
            st.session_state['grade_results'] = grade_results

            if grade_results is None:
                st.warning("Grade generation failed or returned no results.")

            
            # Generate feedback
            st.info("Generating feedback...")
            feedback = call_mcp_tool("generating_feedback", {
                "text": st.session_state['document_text'],
                "rubric": rubric
            })
            st.session_state['feedback'] = feedback
            if feedback is None:
                st.warning("Feedback generation failed or returned no results.")


            if grade_results is not None or feedback is not None:
                st.success("Grading completed!")
                st.balloons()
            
            else:
                st.error("Grading process ecountered errors. Please check your server connection and API settings.")




# Tab 3: Results
with tab3:
    st.header("Grading Results")

    if all(k in st.session_state for k in ['file_name', 'grade_results', 'feedback']):
        st.subheader(f"Results for: {st.session_state['file_name']}")


        # Display grade
        if 'grade_results' in st.session_state:
            if st.session_state['grade_results'] is not None:
                grade = st.session_state['grade_results'].get('grade', 'Not Available')
                st.metric("Grade", grade)

            else:
                st.warning("Grade information not available. There might have been an error during grading")
                st.metric("Grade", "Not available")


        
        # Display feedback
        if 'feedback' in st.session_state:
            if st.session_state['feedback'] is not None:
                st.subheader("Feedback")
                st.markdown(st.session_state['feedback'])
            else:
                st.st.warning("Feedback is not available. There might have been an error generating feedback.")

        

        # Display plagiarism results if available
        if 'plagiarism_results' in st.session_state and st.session_state['plagiarism_results']:
            st.subheader("Plagiarism Check")
            results = st.session_state['plagiarism_results']

            if results is None:
                st.warning("Plagiarism check results are not available. There might have been an error during the checking")
            elif 'error' in results:
                st.error(f"Plagiarism check error: {results['error']}")
            
            else:
                st.markdown("**Similarity matches found: **")
                for url, similarity in results.items():
                    if similarity > 70:
                        st.warning(f"High Similarity ({similarity}%): [{url}]({url})")
                    elif similarity > 40:
                        st.info(f"Moderate Similarity ({similarity}%): [{url}]({url})")
                    else:
                        st.success(f"Low Similarity ({similarity}%): [{url}]({url})")

        

        # Export options
        st.subheader("Export Options")
        if st.button("Export to PDF"):
            st.info("PDF export functionality would go here")


        if st.button("Save to Database"):
            st.info("Database save functionality would go here")

    else:
        st.info("No grading results available. Please upload and grab an assignment first.")