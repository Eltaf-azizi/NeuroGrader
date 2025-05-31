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


## 🚀 Installation
### Prerequisites

 - Python 3.10+
 - OpenAI API Key (or Hugging Face token)
 - (Optional) Turnitin API Key

### Setup
1.  Clone the repo:

```bash
git clone https://github.com/yourusername/ai-assignment-grader.git  
cd ai-assignment-grader
``` 
2.  Install dependencies:
```bash
pip install -r requirements.txt
```

3.  Configure `.env`:
```env
OPENAI_API_KEY="your_key"  
MCP_THRESHOLD=0.75  # Model Context Protocol confidence threshold  
PLAGIARISM_MODE="local"  # "turnitin" or "local"
```
4.  Run the API:
```bash
uvicorn app.main:app --reload  
```

## 📌 Usage Examples
### 1. Grading via MCP + LLM
```python
from app.mcp.rule_engine import MCPGrader  
from app.llm.feedback import generate_feedback  

# Initialize MCP with subject-specific rules  
grader = MCPGrader(rubric="computer_science")  
score = grader.evaluate(submission_text, llm_assist=True)  

# Generate feedback  
feedback = generate_feedback(submission_text, score)  
```

### 2. Plagiarism Check
```bash
curl -X POST http://localhost:8000/check_plagiarism \  
-H "Content-Type: application/json" \  
-d '{"text": "student_submission_here", "mode": "local"}'  
```

## 🤝 How to Contribute

1. Fork the repo.
2. Add tests for new MCP rules/LLM integrations.
3. Submit a pull request (PR) with a clear description.
