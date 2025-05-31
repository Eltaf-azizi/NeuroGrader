<h1 align="center">AI Assignment Grader</h1>

An advanced AI-powered system for automated assignment grading, combining Large Language Models (LLMs), Model Context Protocol (MCP) for structured evaluation, and Plagiarism Detection for academic integrity.

## ✨ Key Features
✅ **LLM-Powered Grading** – Evaluates essays, code, and free-text responses using GPT-4, LLaMA, or Mistral.<br>
✅ **Model Context Protocol (MCP)** – Ensures structured, context-aware assessment with rule-based consistency.<br>
✅ **Plagiarism Detection** – Integrates with Turnitin or uses text similarity (e.g., cosine similarity, fingerprinting).<br>
✅ **Dynamic Rubrics** – Customizable grading criteria aligned with course objectives.<br>
✅ **Bias Mitigation** – Fairness checks to reduce subjective discrepancies.<br>
✅ **Scalable Deployment** – Supports cloud (AWS/GCP) and local (Docker) setups.<br>


## 🛠 Tech Stack

| COMPONENT	    | TECHNOLOGY
|---------------|----------------
| Backend	      | Python (FastAPI/Flask)
| AI Models	    | OpenAI GPT-4, LLaMA-3, Mistral (via Hugging Face)
| MCP Engine	  | Custom rule-based + LLM context blending
| Plagiarism	  | Turnitin API / DiffLib / NLP-based similarity
| Database	    |PostgreSQL / Firebase
| Frontend	    | Streamlit (Teacher Dashboard)
