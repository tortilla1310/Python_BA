# Реализовать структуру «Рейтинг», представляющую собой не возрастающий
# набор натуральных чисел. У пользователя необходимо запрашивать новый
# элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться
# после них.

my_list = [8, 6, 6, 5, 2, 1, 1]
print(my_list)

element = int(input('Введите новый элемент '))
a = my_list.count(element)
for el in my_list:
    if a > 0:
        i = my_list.index(element)
        my_list.insert(i + a, element)
        break
    else:
        if element > el:
            j = my_list.index(el)
            my_list.insert(j, element)
            break
        elif element < my_list[len(my_list) - 1]:
            my_list.append(element)

print(my_list)
