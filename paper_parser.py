import fitz

def extract_sections(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = "\n".join(page.get_text() for page in doc)

    sections = {
        "abstract": "",
        "introduction": "",
        "method": "",
        "results": "",
        "discussion": "",
        "conclusion": ""
    }

    current = None
    for line in full_text.splitlines():
        for sec in sections:
            if sec in line.lower():
                current = sec
                break
        if current:
            sections[current] += line + "\n"

    return sections