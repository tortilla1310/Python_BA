# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

# 1
userStr = input('введите строку из нескольких слов через пробел ')
words = []
number = 1
for element in range(userStr.count(' ') + 1):
    words = userStr.split()
    if len(str(words)) <= 10:
        print(f'{number} {words [element]}')
        number += 1
    else:
        print(f'{number} {words [element] [0:10]}')
        number += 1

# 2
words = input('введите строку из нескольких слов').split()

for idx, value in enumerate(words, start=1):
    print(f'{idx}. {value[:10]}')
