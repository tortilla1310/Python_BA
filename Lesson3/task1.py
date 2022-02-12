# Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def divideNumbers(n1, n2):
    try:
        result = n1 / n2
        return result
    except ZeroDivisionError:
        print("division by zero")


number1_str = input('Please provide the first number: ')
n1 = float(number1_str)

number2_str = input('Please provide the second number: ')
n2 = float(number2_str)
print(n1, n2)

print(divideNumbers(n1, n2))
