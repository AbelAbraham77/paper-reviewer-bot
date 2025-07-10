# 🧠 AI-Powered Research Paper Reviewer

Upload a research paper PDF and get section-wise reviews (Clarity, Novelty, Suggestions) using an LLM.

This is a personal project built with Streamlit and LLM APIs (Groq) to help researchers, reviewers, and students quickly evaluate the quality of academic papers.

## 🚀 Features

- Upload any research paper as PDF
- Extract and review key sections:
  - Abstract
  - Introduction
  - Method
  - Results
  - Discussion
  - Conclusion
- LLM-generated scoring (Clarity, Novelty)
- Actionable suggestions per section
- One-click download of full review as `.txt`

## 🧰 Tech Stack

- Python
- Streamlit (frontend)
- OpenAI / Groq / Gemini (LLMs for review)
- PyPDF2 (PDF parsing)

## 🔧 Local Setup

1. Clone this repo:
   git clone https://github.com/yourusername/paper-reviewer-bot.git
   cd paper-reviewer-bot

2. Create a virtual environment (recommended):
   python -m venv venv
   source venv/bin/activate        # On Linux/Mac
   venv\Scripts\activate           # On Windows

3. Install dependencies:
   pip install -r requirements.txt

4. Set your API key:
   Create a `.env` file with this line:
   GROQ_API_KEY=your_api_key_here
   (Or use Streamlit secrets if deploying on Streamlit Cloud)

5. Run the app locally:
   streamlit run app.py


## 📄 Sample Output

"Clarity: 8/10. The abstract is well-structured and clearly conveys the novelty of the research..."

## 🙋‍♂️ Why This?

Academic paper reviewing is time-consuming. This tool automates initial quality checks to:
- Save researchers time
- Speed up literature filtering
- Improve early drafts with feedback

## 📬 Contact

Made with 💡 by Abel Abraham  
https://github.com/AbelAbraham77
