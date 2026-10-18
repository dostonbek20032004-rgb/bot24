import os
from flask import Flask
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

app = Flask(__name__)
@app.route('/')
def home(): return "Bot is running!"

PRODUCTS = {
    "💎 570 UC": 55,
    "💎 1170 UC": 110,
    "💎 2400 UC": 210,
    "💎 6200 UC": 570,
    "🌙 МОХОНА 2600": 70,
    "📅 НЕДЕЛЯ 450": 20,
    "
