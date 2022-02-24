# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

my_list = ['капуста\n', 'носорог\n', 'пляж и море\n']


with open('test-2.txt', 'a') as my_file:
    my_file.writelines(my_list)

with open('test-2.txt', 'r') as my_file:
    lines = 0
    letter = 0
    for line in my_file:
        lines += line.count(line)
        letters = len(line) - 1
        print(f'{letters} letters in line')
    print(f'str count in {lines}')
