from kedro.pipeline import Pipeline, node
from .nodes import load_pdf_node

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(load_pdf_node, inputs="params:pdf_path", outputs="documents", name="load_pdfs_node")
    ])