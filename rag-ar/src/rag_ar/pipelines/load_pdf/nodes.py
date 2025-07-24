from PyPDF2 import PdfReader
from pathlib import Path
import pandas as pd
from typing import List


def load_pdf_node(pdf_path: str) -> List[str]:
    docs = []
    for file in Path(pdf_path).glob("*.pdf"):
        reader = PdfReader(file)
        text = "\n".join(
            page.extract_text() for page in reader.pages if page.extract_text()
        )
        docs.append(text)

    return docs