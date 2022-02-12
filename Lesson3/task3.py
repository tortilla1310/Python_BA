# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.

from re import S


def my_func(n1, n2, n3):
    my_list = [n1, n2, n3]
    print(my_list)
    my_list.sort()
    print('my_list sorted', my_list)
    return my_list[1] + my_list[2]


number1_str = input('Please provide the first number: ')
n1 = float(number1_str)

number2_str = input('Please provide the second number: ')
n2 = float(number2_str)

number3_str = input('Please provide the third number: ')
n3 = float(number3_str)
print(n1, n2, n3)

print(my_func(n1, n2, n3))
