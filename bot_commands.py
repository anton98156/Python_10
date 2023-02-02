from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from logger import *

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')