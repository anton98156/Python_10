# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# from logger import *

# async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     log(update, context)
#     await update.message.reply_text(f'Привет "{update.effective_user.first_name}"')
#     await update.message.reply_text('Для работы с рациональными числами введите /rational_calc x y ')
#     await update.message.reply_text("Для работы с комлексными числами введите /complex_calc")

# async def operator(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     msg = update.message.text
#     log(update, context)
#     items = msg.split()
#     z = str(items[1])
#     'Веберите одну из пераций: "+" "-" "/" "*" '

# async def rational_calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     msg = update.message.text
#     log(update, context)
#     items = msg.split()
#     z = int(items[1,2,3])
    
    
# if operator()


# async def option(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     msg = update.message.text
#     log(update, context)
#     items = msg.split()
#     z = int(items[1])
#     if z == 1:
#         await update.message.reply_text('Работаем с рациональными числами')
#     elif z == 2:
#         await update.message.reply_text('Работаем с комлексными числами')
#     else:
#          await update.message.reply_text("Такой опции не существует.")


def option():
    print("Для работы с рациональными числами нажмите 1: ")
    print("Для работы с комлексными числами нажмите 2: ")
    q = int(input())
    if q == 1:
        x = float(input('Введите x: '))
        y = float(input('Введите y: '))
    elif q == 2:
        x = complex(input("Введите число: "))
        y = complex(input("Введите число: "))
    else:
        print("Такой опции не существует.")
    return(x,y)

# a,b = option()

def operation():
    z = str(input('Веберите одну из пераций: "+" "-" "/" "*" '))
    if z == "+":
        print(f'x + y = {a+b}')
    elif z == "-":
        print(f'x - y = {a-b}')
    elif z == "*":
        print(f'x * y = {a*b}')
    elif z == "/":
        print(f'x / y = {a/b}')
    else:
        print('Такой операции не существует')

# operation()
