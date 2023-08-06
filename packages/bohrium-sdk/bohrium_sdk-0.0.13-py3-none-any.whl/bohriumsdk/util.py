import requests
def chat(prompt, temperature=0):
    post_data = {
        "messages":[{"role":"user","content":f"{prompt}"}],
        "stream":False,
        "model":"gpt-3.5-turbo",
        "temperature":temperature,
        "presence_penalty":0
    }

    resp = requests.post("https://bohrium-chat.dp.tech/api/openai/v1/chat/completions", json=post_data)
    resp = resp.json()
    return resp["choices"][0]["message"]["content"]