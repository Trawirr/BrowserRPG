import requests

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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"
}

payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": "Hello, ChatGPT!"}
    ]
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()
print(data)
