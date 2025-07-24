from PyPDF2 import PdfReader

def load_pdf_node(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)
    return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])