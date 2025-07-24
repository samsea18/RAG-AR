from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text_node(raw_text: str) -> List[str]:
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_text(raw_text)