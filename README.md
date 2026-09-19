# Telegram AI Chatbot

A Telegram chatbot powered by the Groq API and the `openai/gpt-oss-120b` model.

## Features

- Responds to the `/start` command
- Sends typing status while generating a response
- Answers text messages using Groq
- Logs API errors without exposing them to users
- Loads credentials from environment variables

## Requirements

- Python 3.10 or newer
- A Telegram bot token from [BotFather](https://t.me/BotFather)
- A Groq API key from [Groq Console](https://console.groq.com/keys)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/faizerumar/telegram-bot.git
   cd telegram-bot
   ```

2. Create and activate a virtual environment:

   **Windows PowerShell**

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS/Linux**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Configuration

Set these environment variables before starting the bot.

**Windows PowerShell**

```powershell
$env:TELEGRAM_BOT_TOKEN="your-telegram-bot-token"
$env:GROQ_API_KEY="your-groq-api-key"
```

**macOS/Linux**

```bash
export TELEGRAM_BOT_TOKEN="your-telegram-bot-token"
export GROQ_API_KEY="your-groq-api-key"
```

Do not put real credentials directly in `bot.py`, `README.md`, or any committed file. Local `.env` files are ignored by Git, but this project currently reads variables from the environment directly.

## Run the bot

```bash
python bot.py
```

The bot will print `Bot is running...` after startup. Open the bot in Telegram, send `/start`, and then send a text message.

## Project files

- `bot.py` - Telegram handlers and Groq API integration
- `requirements.txt` - Python dependencies
- `.gitignore` - Local files excluded from Git

## Security

If a token or API key is ever committed or shared, revoke it immediately and create a replacement. Removing it from the latest file is not enough because it may remain in Git history.
