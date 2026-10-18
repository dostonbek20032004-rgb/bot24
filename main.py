import os
from flask import Flask
from threading import ThrАлrom teАлмэram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

app = Flask(__name__)
@app.route('/')
def home(): return "Bot is running!"

PRODUCTS = {
    "💎 570 Алмаз": 55,
    "💎 1170 Алмаз": 110,
    "💎 2400 Алмаз": 210,
}

user_data = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(k, callback_data=k)] for k in PRODUCTS.keys()]
    text = "💎 NAZAROV SHOP DONAT TJ 💎\n\nСалом! Хуш омадед!\n👇 Товарро интихоб кунед:"
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    prod = query.data
    price = PRODUCTS[prod]
    user_data[query.from_user.id] = {'product': prod, 'price': price}
    text = f"✅ {prod}\n💰 Нарх: {price} сомонӣ\n\n📝 UID-и худро равон кунед:"
    await query.message.reply_text(text)

async def get_uid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.message.text
    data = user_data.get(update.from_user.id)
    if not data: return
    await context.bot.send_message(chat_id=ADMIN_ID, text=f"🔥 ЗАКАЗИ НАВ!\n👤 @{update.from_user.username}\n🎮 UID: {uid}\n📦 {data['product']}\n💰 {data['price']}")
    await update.message.reply_text("✅ Кабул шуд! Админ тез орада алоқа қи
