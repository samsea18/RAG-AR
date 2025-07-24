from typing import List, Tuple
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document

def vectorstore_node(chunks: List[str], embeddings: List[List[float]]) -> FAISS:
    docs = [Document(page_content=c) for c in chunks]
    return FAISS.from_embeddings(docs, embeddings)