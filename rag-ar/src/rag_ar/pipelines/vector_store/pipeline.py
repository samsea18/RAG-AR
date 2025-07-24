from kedro.pipeline import Pipeline, node
from .nodes import vectorstore_node

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(vectorstore_node, inputs=["chunks", "embeddings"], outputs="vector_index", name="build_index_node")
    ])