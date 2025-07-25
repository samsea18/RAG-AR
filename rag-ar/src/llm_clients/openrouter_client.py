import requests

def call_openrouter(prompt: str, query: str, model: str, api_key: str) -> str:
    full_prompt = f"""\
    You are a financial analyst working on an equities desk, specializing in company valuation and financial modeling.
    
    Using the following context from internal reports, financial statements, or earnings call transcripts, provide a concise and professional analysis.
    
    Context:
    {prompt}
    
    Question:
    {query}
    
    Respond as if you're preparing an internal memo for a portfolio manager or investment committee. 
    Use precise financial terminology and focus on valuation-relevant insights.
    
    Make the response as concise as possible.
    """
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": model,
            "messages": [{"role": "user", "content": full_prompt}],
        },
        timeout=60,
    )
    return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")