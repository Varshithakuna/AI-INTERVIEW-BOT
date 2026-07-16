from llm import ask_llm

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "Say hello in one sentence."
    }
]

response = ask_llm(messages)

print(response)