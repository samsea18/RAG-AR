from langchain.document_loaders import PyPDFLoader
from langchain.schema import Document
from typing import List, Union

def load_pdf_node(filepaths: Union[str, List[str]]) -> List[Document]:
    if isinstance(filepaths, str):
        filepaths = [filepaths]  # wrap single string in list

    all_docs = []
    for path in filepaths:
        loader = PyPDFLoader(path)
        docs = loader.load()

        # Filter out pages with very little text (logos, images, etc.)
        filtered = [doc for doc in docs if len(doc.page_content.strip()) > 200]
        for doc in filtered:
            doc.metadata['source'] = path
        all_docs.extend(filtered)

    return all_docs