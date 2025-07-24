from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text_node(docs: List[str]) -> List[str]:

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    all_chunks = []
    for doc in docs:
        all_chunks.extend(splitter.split_text(doc))

    return all_chunks