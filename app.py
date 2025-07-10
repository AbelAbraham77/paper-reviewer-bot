import streamlit as st
import PyPDF2
from reviewer_engine import review_section

st.set_page_config(page_title="Paper Reviewer Bot", layout="centered")

st.title("📄 AI-Powered Paper Reviewer")

st.markdown("""
Upload a research paper PDF and get a detailed academic-style review of each section.
""")

uploaded_file = st.file_uploader("Upload your research paper (PDF)", type="pdf")

if uploaded_file:
    st.success("✅ PDF uploaded successfully.")

    # Read text from PDF
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    raw_text = ""
    for page in pdf_reader.pages:
        raw_text += page.extract_text() or ""

    # Split text into sections (simple heuristic)
    section_headers = ["abstract", "introduction", "method", "results", "discussion", "conclusion"]
    sections = {}
    current_section = "abstract"
    sections[current_section] = ""

    for line in raw_text.split("\n"):
        lower_line = line.lower().strip()
        if any(header in lower_line for header in section_headers):
            for header in section_headers:
                if header in lower_line:
                    current_section = header
                    sections[current_section] = ""
                    break
        sections[current_section] += line + "\n"

    st.markdown("### 🧠 Review Results")
    review_output = ""
    for section, content in sections.items():
        if content.strip():
            st.markdown(f"#### 📌 {section.capitalize()}")
            with st.spinner(f"Reviewing {section}..."):
                review = review_section(content, section)
                st.write(review)
                review_output += f"{section.capitalize()} Review\n{review}\n\n"

    # Downloadable review
    st.markdown("### 📥 Download Full Review")
    st.download_button(
        label="Download Review as TXT",
        data=review_output,
        file_name="paper_review.txt",
        mime="text/plain"
    )
