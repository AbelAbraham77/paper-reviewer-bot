import streamlit as st
import requests

st.set_page_config(page_title="AI Paper Reviewer", layout="wide")

st.title("📄 AI-Powered Research Paper Reviewer")
st.markdown("Upload a research paper (PDF) and get instant section-wise reviews using LLMs.")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    with st.spinner("Uploading and reviewing..."):
        response = requests.post(
            "http://localhost:8000/review/",
            files={"file": (uploaded_file.name, uploaded_file, "application/pdf")}
        )

        if response.status_code != 200:
            st.error("❌ Failed to get response from backend.")
        else:
            reviews = response.json()

            if "error" in reviews:
                st.error(reviews["error"])
            else:
                # Display each section review
                for section, review in reviews.items():
                    st.subheader(f"{section} Review")
                    st.markdown(review)

                # 📝 Combine all reviews and allow download
                full_review_text = "\n\n".join(
                    f"{section} Review:\n{content}" for section, content in reviews.items()
                )

                st.download_button(
                    label="💾 Download Full Review",
                    data=full_review_text,
                    file_name="paper_review.txt",
                    mime="text/plain"
                )
