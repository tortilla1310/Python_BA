# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции
# my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
import math


def my_func(x, y):
    temp = 1
    for i in range(-1*y):
        temp = temp*x
    return float(1 / temp)


number1_str = input('Introduce real positive number: ')
n1 = float(number1_str)

number2_str = input('Introduce negative integer: ')
n2 = int(number2_str)

print(my_func(n1, n2))
