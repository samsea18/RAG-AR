from kedro.pipeline import Pipeline, node
from .nodes import split_text_node

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(split_text_node,
             inputs="documents",
             outputs="chunks",
             name="split_docs_node",
             tags=["split"])
    ])