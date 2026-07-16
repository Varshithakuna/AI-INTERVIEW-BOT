from resume_parser import extract_resume_text

with open("sample_resume.pdf", "rb") as f:
    text = extract_resume_text(f)

print(text)