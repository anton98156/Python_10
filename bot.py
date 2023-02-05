
# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования.

# bot_name - python98156_bot


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
from commands import *

app = ApplicationBuilder().token("6118659428:AAErWajgtqVAhADvPJKzZ9Hfx2Cc5JbOTYM").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("x_input", x_input))
app.add_handler(CommandHandler("y_input", y_input))
app.add_handler(CommandHandler("operator", operator))
app.add_handler(CommandHandler("rational_calc", rational_calc))
app.add_handler(CommandHandler("complex_calc", complex_calc))
print('server started')
app.run_polling()