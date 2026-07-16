import fitz  # PyMuPDF


def extract_resume_text(uploaded_file):
    """
    Extracts text from an uploaded PDF resume.
    """

    if uploaded_file is None:
        return ""

    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    text = ""

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text.strip()