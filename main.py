import os
from threading import Thread
from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot is running!"

PRODUCTS = {
    "110": "110 💎 — 12.50 СМ",
    "340": "340 💎 — 33 СМ",
    "570": "570 💎 — 55 СМ",
    "1170": "1170 💎 — 99 СМ",
    "2400": "2400 💎 — 215 СМ",
    "6200": "6200 💎 — 520 СМ",
    "v2600": "ВАУЧЕР МОХОНА 2600 💎 — 75 СМ",
    "v450": "ВАУЧЕР НЕДЕЛЯ 450 💎 — 22 СМ",
    "v90": "ВАУЧЕР ЛАЙТ 90 💎 — 8 СМ",
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(PRODUCTS["110"], callback_data="110")],
        [InlineKeyboardButton(PRODUCTS["340"], callback_data="340")],
        [InlineKeyboardButton(PRODUCTS["570"], callback_data="570")],
        [InlineKeyboardButton(PRODUCTS["1170"], callback_data="1170")],
        [InlineKeyboardButton(PRODUCTS["2400"], callback_data="2400")],
        [InlineKeyboardButton(PRODUCTS["6200"], callback_data="6200")],
        [InlineKeyboardButton(PRODUCTS["v2600"], callback_data="v2600")],
        [InlineKeyboardButton(PRODUCTS["v450"], callback_data="v450")],
        [InlineKeyboardButton(PRODUCTS["v90"], callback_data="v90")],
        [InlineKeyboardButton("🛒 Выбрать несколько", callback_data="multi")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="back")],
    ]
    await update.message.reply_text("💎 NAZAROV DONAT - Выберите товар:", reply_markup=InlineKeyboardMarkup(keyboard))

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    if q.data == "back":
        await start(update, context)
        return
    if q.data == "multi":
        await q.callback_query.message.reply_text("✍️ Напишите какие нужны: напр: 570 + 340")
        return
    tovar = PRODUCTS.get(q.data, q.data)
    await q.message.reply_text(f"✅ Вы выбрали: {tovar}\n\n💳 Оплата: DCity / Alif / Dushanbe City\n📱 Отправьте: ID + Скрин чека\n👨‍💼 Админ: @Sadi4a_Admin")

def run_flask():
    flask_app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

if __name__ == "__main__":
    Thread(target=run_flask).start()
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle))
    app.run_polling()
