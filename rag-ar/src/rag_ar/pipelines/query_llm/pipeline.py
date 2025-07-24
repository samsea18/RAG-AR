from kedro.pipeline import Pipeline, node
from .nodes import query_node

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(query_node,
             inputs=["params:queries", "vector_index", "params:top_k", "params:model"],
             outputs="rag_outputs",
             name="query_llm_node",
             tags=["query"])
    ])