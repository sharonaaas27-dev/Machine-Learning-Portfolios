import PyPDF2

def extract_text_from_pdf(file):
    text = ""
    reader = PyPDF2.PdfReader(file)
    
    for page in reader.pages:
        text += page.extract_text()
    
    return text
