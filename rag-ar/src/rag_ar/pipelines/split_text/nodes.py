from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


def clean_chunk(text: str) -> str:
    # Remove empty lines and all-uppercase lines (common in headings/boilerplate)
    lines = text.splitlines()
    lines = [l for l in lines if l.strip() and not l.strip().isupper()]
    return "\n".join(lines).strip()

def split_text_node(docs: List[Document], chunk_size=500, chunk_overlap=50) -> List[str]:
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    cleaned_docs = []
    for doc in docs:
        chunks = splitter.split_text(doc.page_content)

        # Clean each chunk
        for chunk in chunks:
            cleaned = clean_chunk(chunk)
            if len(cleaned.split()) > 30:  # Filter out very short chunks
                cleaned_docs.append(cleaned)
    return cleaned_docs
