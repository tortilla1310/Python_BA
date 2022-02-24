# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

user_input = input('Введите числа через пробел ')
numbers = [int(i) for i in user_input.split() if i.isdigit()]

with open('test-3.txt', 'r+') as file_obj:
    print(sum(numbers))
    file_obj.write(str(numbers))
