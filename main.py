import os
from threading import Thread
from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

PRODUCTS = {
    "💎 570 Алмаз": 55,
    "💎 1170 Алмаз": 110,
    "💎 2400 Алмаз": 210,
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(name, callback_data=name)] for name in PRODUCTS.keys()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("💎 NAZAROV SHOP DONAT TJ\n\nАлмаз танланг:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    prod = query.data
    price = PRODUCTS.get(prod, 0)
    await query.message.reply_text(f"Сиз танладингиз: {prod}\nНархи: {price} сомон")

def run_bot():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling()
if __name__ == "__main__":
    Thread(target=lambda: app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))).start()
    run_bot()
