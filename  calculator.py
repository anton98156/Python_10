# x = float(input('Введите x: '))
# y = float(input('Введите y: '))

def operation():
    a = str(input('Веберите одну из пераций: "+" "-" "/" "*" '))
    if a == "+":
        print('Сумма')
    elif a == "-":
        print('Вычитание')
    elif a == "/":
        print('Деление')
    elif a == "*":
        print('Умножение')
    else:
        print('Такой операции не существует')
    return a