# Local AI Chatbot

A command-line chatbot that runs a language model locally with
[Ollama](https://ollama.com). It remembers conversations between runs
by saving them to a JSON file.

## Features

- Chats with a local model (no API key, no cost)
- Keeps the full conversation history and sends it with each request
- Saves and loads history from `chat_history.json`
- Type `new` to start a fresh conversation, `quit` to exit
- Handles the case where Ollama is not running

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com) installed and running
- A downloaded model: `ollama pull llama3.2`

## Setup

```
git clone https://github.com/whoisclau/ollama-chatbot.git
cd ollama-chatbot
python3 -m pip install -r requirements.txt
python3 chatbot.py
```

## How it works

Language models have no memory between requests. The program keeps a list
of messages (`user` and `assistant` roles) and sends the whole list to
Ollama's `/api/chat` endpoint on every turn. The list is saved to disk
after each reply, so the conversation continues after a restart.

## What I learned

- Calling a local HTTP API with `requests`
- Reading and writing JSON files
- Error handling with `try/except`
- Why LLM chat apps must resend the conversation history
