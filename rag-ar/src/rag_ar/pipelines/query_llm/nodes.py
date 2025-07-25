from typing import List, Dict
from langchain.vectorstores import FAISS
from llm_clients.openrouter_client import call_openrouter

from kedro.config import OmegaConfigLoader
from kedro.framework.context import KedroContext
from kedro.framework.project import settings


def query_node(queries: List[str], vectorstore: FAISS, top_k: int, model: str,) -> List[Dict]:

    conf_loader = OmegaConfigLoader(conf_source=settings.CONF_SOURCE)
    print(conf_loader)
    api_key = conf_loader['credentials']['openrouter']['api_key']

    results = []
    for q in queries:
        rel_docs = vectorstore.similarity_search(q, k=top_k)
        context = "\n---\n".join([d.page_content for d in rel_docs])
        response = call_openrouter(prompt=context, query=q, model=model, api_key=api_key)
        results.append({"query": q, "response": response, "context": context})
    return results