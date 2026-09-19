import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from groq import Groq

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not TELEGRAM_BOT_TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN is not set")
if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY is not set")

# Initialize Groq client
groq_client = Groq(api_key=GROQ_API_KEY)

# Set up logging to see errors in console
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = "Hello! I am your AI Chatbot powered by Groq & Llama 3. Ask me anything!"
    await update.message.reply_text(welcome_text)

# Message handler to process incoming text and generate response
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    # Show "typing..." indicator in Telegram
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")

    try:
        response = groq_client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": "You are a helpful, friendly AI assistant in a Telegram chat."},
                {"role": "user", "content": user_text}
            ],
            temperature=0.7,
            max_tokens=1000
        )

        bot_reply = response.choices[0].message.content
        await update.message.reply_text(bot_reply)

    except Exception:
        logging.exception("Error calling Groq API")
        await update.message.reply_text(
            "Sorry, I could not process that request right now. Please try again later."
        )

if __name__ == '__main__':
    # Build and run the Telegram bot
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("Bot is running...")
    app.run_polling()