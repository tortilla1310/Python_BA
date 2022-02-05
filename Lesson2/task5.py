# Реализовать структуру «Рейтинг», представляющую собой не возрастающий
# набор натуральных чисел. У пользователя необходимо запрашивать новый
# элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться
# после них.

# Variant 1
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

# Variant 2
rating = [9, 8, 8, 7, 6, 6, 6, 5, 3, 2, 1]

while True:
    try:
        print(f'Rating = {rating}')
        user_rate = int(input(' Введите новый рейтинг >>> '))

        # простой, но долгий
        rating.append(user_rate)
        rating.sort(reverse=True)

        # сложнее, но быстрее на больших объемах
        # current_rate_count = rating.count(user_rate)

        # if current_rate_count:
        #     last_current_idx = rating.index(user_rate) + current_rate_count
        #     rating.insert(last_current_idx, user_rate)
        # else:
        #     if user_rate > rating[0]:
        #         rating.insert(0, user_rate)
        #     elif user_rate < rating[-1]:
        #         rating.append(user_rate)
        #     else:
        #         for idx, rate in enumerate(rating):
        #             if rate < user_rate:
        #                 rating.insert(idx, user_rate)
        #                 break

        print(rating)

    except ValueError:
        print('wrong number')
    except KeyboardInterrupt:
        exit()
