from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PyPDF2 import PdfReader
from reviewer_engine import review_section
import uvicorn

app = FastAPI()

# Allow frontend to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def extract_sections_from_pdf(pdf_text):
    import re

    sections = {
        "Abstract": "",
        "Introduction": "",
        "Method": "",
        "Results": "",
        "Discussion": "",
        "Conclusion": ""
    }

    # Find positions
    positions = {}
    for section in sections:
        match = re.search(rf'\b{section}\b', pdf_text, re.IGNORECASE)
        if match:
            positions[section] = match.start()

    sorted_sections = sorted(positions.items(), key=lambda x: x[1])

    for i, (section, start_idx) in enumerate(sorted_sections):
        end_idx = sorted_sections[i+1][1] if i + 1 < len(sorted_sections) else len(pdf_text)
        sections[section] = pdf_text[start_idx:end_idx].strip()

    return sections

@app.post("/review/")
async def review_paper(file: UploadFile = File(...)):
    try:
        reader = PdfReader(file.file)
        raw_text = "\n".join([page.extract_text() or "" for page in reader.pages])
        sections = extract_sections_from_pdf(raw_text)

        reviews = {}
        for s, t in sections.items():
            if t.strip():
                result = review_section(t, s)
                if result and "error" not in result.lower():
                    reviews[s] = result

        if not reviews:
            reviews["error"] = "❗ No reviewable sections found or all failed to process. Try a different paper."

        return reviews

    except Exception as e:
        return {"error": f"Failed to process PDF: {str(e)}"}

if __name__ == "__main__":
    uvicorn.run("backend:app", host="0.0.0.0", port=8000, reload=True)
