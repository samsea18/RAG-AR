from kedro.pipeline import Pipeline, node
from .nodes import embed_text_node

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(embed_text_node,
             inputs="chunks",
             outputs="embeddings",
             name="embed_chunks_node",
             tags=["embed"])
    ])