import json
import requests

url = "http://localhost:11434/api/chat"
HISTORY_FILE = "chat_history.json"


def load_messages():
    try:
        with open(HISTORY_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_messages(messages):
    with open(HISTORY_FILE, "w") as f:
        json.dump(messages, f, indent=2)


messages = load_messages()

print("Chat with the AI. Type 'quit' to exit.")
print(f"Loaded {len(messages)} earlier messages.")

while True:
    user_text = input("You: ")
    command = user_text.strip().lower()

    if command == "quit":
        print("Bye!")
        break

    if command == "new":
        messages = []
        save_messages(messages)
        print("Starting a new conversation.")
        continue

    if not command:
        continue

    messages.append({"role": "user", "content": user_text})

    payload = {
        "model": "llama3.2",
        "messages": messages,
        "stream": False,
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"Could not reach Ollama: {error}")
        messages.pop()
        continue

    reply = response.json()["message"]["content"]
    print(f"AI: {reply}")

    messages.append({"role": "assistant", "content": reply})
    save_messages(messages)