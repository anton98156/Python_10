
# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования.

# user_name - python98156_bot

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from bot_commands import *


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("6118659428:AAErWajgtqVAhADvPJKzZ9Hfx2Cc5JbOTYM").build()

app.add_handler(CommandHandler("hi", hello_command))

print('server started')

app.run_polling()