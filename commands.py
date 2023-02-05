from telegram import Update
from telegram.ext import ContextTypes
from logger import *

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text('Добро пожаловать в калькулятор!')
    await update.message.reply_text('Введите "х" через /x_input "..."')
    await update.message.reply_text('Введите "y" через /y_input "..."')
    await update.message.reply_text('Выберите 1 из операторов "+" "-" "*" "/" через /operator "..."')
    await update.message.reply_text('Запросите результат вычисления для рациональых чисел через /rational_calc')
    await update.message.reply_text('Запросите результат вычисления для комплексных чисел через /complex_calc')

async def x_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    log(update, context)
    items = msg.split()
    x = str(items[1])
    file = open('x.txt', 'w')
    file.write(x)
    file.close()

async def y_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    log(update, context)
    items = msg.split()
    y = str(items[1])
    file = open('y.txt', 'w')
    file.write(y)
    file.close()

async def operator(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    log(update, context)
    items = msg.split()
    z = str(items[1])
    file = open('operator.txt', 'w')
    file.write(z)
    file.close()

async def rational_calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    
    path = 'x.txt'
    data = open(path, 'r')
    for line in data:
        x = float(line)
    print(x)
    data.close()
    
    path = 'y.txt'
    data = open(path, 'r')
    for line in data:
        y = float(line)
    print(y)
    data.close()
    
    path = 'operator.txt'
    data = open(path, 'r')
    for line in data:
        z = str(line)
    print(z)
    data.close()
    
    if z == "+":
        await update.message.reply_text(f'{x} + {y} = {x+y}')
    elif z == "-":
        await update.message.reply_text(f'{x} - {y} = {x-y}')
    elif z == "*":
        await update.message.reply_text(f'{x} * {y} = {x*y}')
    elif z == "/":
        await update.message.reply_text(f'{x} / {y} = {x/y}')
    else:
        await update.message.reply_text('Введены неверные данные')

async def complex_calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    
    path = 'x.txt'
    data = open(path, 'r')
    for line in data:
        x = complex(line)
    print(x)
    data.close()
    
    path = 'y.txt'
    data = open(path, 'r')
    for line in data:
        y = complex(line)
    print(y)
    data.close()
    
    path = 'operator.txt'
    data = open(path, 'r')
    for line in data:
        z = str(line)
    print(z)
    data.close()
    
    if z == "+":
        await update.message.reply_text(f'{x} + {y} = {x+y}')
    elif z == "-":
        await update.message.reply_text(f'{x} - {y} = {x-y}')
    elif z == "*":
        await update.message.reply_text(f'{x} * {y} = {x*y}')
    elif z == "/":
        await update.message.reply_text(f'{x} / {y} = {x/y}')
    else:
        await update.message.reply_text('Введены неверные данные')