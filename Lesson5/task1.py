# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка

my_file = open('test.txt', 'w')

my_list = []
while True:
    line = input('ВВедите данные ')
    print(line)
    if line == ' ':
        print(my_list)
        break
    else:
        print('Если захотите выйти, нажмите пробел')
        my_list.append(line)


for i in my_list:
    my_file.write('%s\n' % i)

print(my_list)
