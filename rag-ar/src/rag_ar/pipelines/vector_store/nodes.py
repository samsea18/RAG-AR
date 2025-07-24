from typing import List, Tuple
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import FAISS

def vectorstore_node(chunks: List[str], embeddings: List[List[float]]) -> FAISS:

    text_embeddings: List[Tuple[str, List[float]]] = list(zip(chunks, embeddings))
    model = HuggingFaceBgeEmbeddings(model_name="BAAI/bge-small-en-v1.5")

    return FAISS.from_embeddings(text_embeddings, model)