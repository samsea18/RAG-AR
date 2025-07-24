from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

from .pipelines.load_pdf import pipeline as pdf_loader_pipeline
from .pipelines.split_text import pipeline as splitter_pipeline
from .pipelines.embeddings import pipeline as embedder_pipeline
from .pipelines.vector_store import pipeline as vectorstore_pipeline
from .pipelines.query_llm import pipeline as query_llm_pipeline
from .pipelines.format_output import pipeline as formatter_pipeline


def register_pipelines() -> dict[str, Pipeline]:
    pdf = pdf_loader_pipeline.create_pipeline()
    split = splitter_pipeline.create_pipeline()
    embed = embedder_pipeline.create_pipeline()
    store = vectorstore_pipeline.create_pipeline()
    query = query_llm_pipeline.create_pipeline()
    format_out = formatter_pipeline.create_pipeline()

    return {
        "__default__": pdf + split + embed + store + query + format_out,
        "pdf_loader": pdf,
        "splitter": split,
        "embedder": embed,
        "vectorstore": store,
        "query_llm": query,
        "formatter": format_out,
    }


__version__ = "0.1"
