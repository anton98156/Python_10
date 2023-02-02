from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('log.txt', 'a')
    file.write(f'{update.message.text}\n')
    file.close()