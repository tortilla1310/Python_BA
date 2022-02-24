# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше
# предыдущего элемента.

# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать
# генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

# A list of numbers is presented. It is necessary to display the elements of the source list, the values
# of which are greater than the previous element.

# Hint: Arrange the elements that satisfy the condition in the form of a list. Use a generator to generate
# a list.
# Initial list example: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Result: [12, 44, 4, 10, 78, 123].


user_list_str = input("enter list: ")
user_list = eval(user_list_str)
print(user_list)

new_list = []
for i in range(len(user_list)):
    if user_list[i] > user_list[i-1] and i > 0:
        new_list.append(user_list[i])
print(new_list)


"""
python3 task2.py 
  [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

"""
