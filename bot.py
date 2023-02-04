
# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования.

# user_name - python98156_bot

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,MessageHandler, filters
from bot_calculate import *

app = ApplicationBuilder().token("6118659428:AAErWajgtqVAhADvPJKzZ9Hfx2Cc5JbOTYM").build()


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Привет "{update.effective_user.first_name}"')
    await update.message.reply_text('Для работы с рациональными числами введите /rational_calc')
    await update.message.reply_text("Для работы с комлексными числами введите /complex_calc")
    

async def calculator(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    print(message.text)
    # await update.message.reply_text("Х")
    # print("hhh")
    
    
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("calculator", calculator))
    

# async def rational_calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     msg = update.message.text
#     items = msg.split()
#     z = int(items[1])

# async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_message = update.message.text

# # app.add_handler(MessageHandler(filters.TEXT & ~filters.Command, calculate))

print('server started')

app.run_polling()