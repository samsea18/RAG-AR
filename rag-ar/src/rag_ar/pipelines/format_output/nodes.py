from typing import List, Dict

def format_rag_output(results: List[Dict]) -> List[Dict]:
    return [{
        "query": r["query"],
        "response": r["response"],
        "contexts": r["contexts"]
    } for r in results]