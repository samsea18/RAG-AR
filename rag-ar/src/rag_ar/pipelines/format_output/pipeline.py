from kedro.pipeline import Pipeline, node
from .nodes import format_rag_output

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(format_rag_output, inputs="rag_outputs", outputs="rag_responses", name="format_json_node")
    ])