from typing import List, Dict

def format_rag_output(results: List[Dict]) -> List[Dict]:

    return [{
        "query": r["query"],
        "response": r["response"],
        "context": r["context"]
    } for r in results]