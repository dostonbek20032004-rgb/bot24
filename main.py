import os
from flask import Flask
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

PRODUCTS = {
    "💎 570 Алмаз": 55,
    "💎 1170 Алмаз": 110,
    "💎 2400 Алмаз": 210,
}

user_data = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(k, callback_data=k) for k in PRODUCTS.keys()]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = "💎 NAZAROV SHOP DONAT TJ 💎\nТанланг:"
    await update.message.reply_text(text, reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    prod = query.data
    price = PRODUCTS[prod]
    await query.message.reply_text(f"Сиз танладингиз: {prod}\nНархи: {price} сомони\n\nАдминга ёзинг: @nazarov_shop")

def run_bot():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling()

if __name__ == "__main__":
    Thread(target=lambda: app.run(host="0.0.0.0", port=10000)).start()
    run_bot()
