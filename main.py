import os
from threading import Thread
from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

PRODUCTS = {
    "570 Алмаз": 55,
    "1170 Алмаз": 110,
    "2400 Алмаз": 210,
}

async def start(update, context):
    keyboard = [[InlineKeyboardButton(text=p, callback_data=p) for p in PRODUCTS]]
    await update.message.reply_text("Алмаз танланг:", reply_markup=InlineKeyboardMarkup(keyboard))

async def button(update, context):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(f"Танладингиз: {query.data}")

def run_bot():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling()

if __name__ == "__main__":
    Thread(target=lambda: app.run(host="0.0.0.0", port=10000)).start()
    run_bot()
