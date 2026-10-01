def add(a, b):
    return a + b

def subtract(a, b):
    # ОШИБКА: здесь должно быть вычитание, а не умножение
    return a - b  

def divide(a, b):
    # ОШИБКА: нет проверки деления на ноль
    return a / b
    if b == 0:
        return "ошибка"
def multiply(a,b):
    return a * b