import openai
import streamlit as st

# Use Streamlit's secrets
openai.api_key = st.secrets["GROQ_API_KEY"]
openai.api_base = "https://api.groq.com/openai/v1"

def review_section(text, section_name):
    prompt = f"""
You are an expert academic reviewer. Carefully evaluate the {section_name} section of a research paper.

Return the following:
1. Clarity (1–10) with a short justification
2. Novelty (1–10) with a short justification
3. Three actionable suggestions for improvement

--- Begin Section ---
{text}
--- End Section ---
"""

    try:
        response = openai.ChatCompletion.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]

    except Exception as e:
        print(f"🔥 Groq (LLaMA3) error: {e}")
        return "Error generating review."
