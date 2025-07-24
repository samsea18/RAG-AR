from typing import List
from langchain.embeddings import HuggingFaceBgeEmbeddings

def embed_text_node(chunks: List[str]) -> List[List[float]]:
    model = HuggingFaceBgeEmbeddings(model_name="BAAI/bge-small-en-v1.5")
    return model.embed_documents(chunks)