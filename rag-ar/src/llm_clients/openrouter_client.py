import requests

def call_openrouter(prompt: str, query: str, model: str, api_key: str) -> str:
    full_prompt = f"Answer the following question using the provided context.\nContext:\n{prompt}\n\nQuestion:\n{query}"
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