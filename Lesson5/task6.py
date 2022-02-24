# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.

# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


hours_dict = {}

with open('test-4.txt', 'r') as my_file:

    for line in my_file:

        line_another_split = line.split(":")

        subject = line_another_split[0]

        sum = 0

        other_words = line_another_split[1:]
        other_words = other_words[0].split(" ")

        for word in other_words:

            integers = [s for s in list(word) if s.isdigit()]

            if integers != []:

                integers_string = "".join(integers)
                integers_number = int(integers_string)

                sum += integers_number

        hours_dict[subject] = sum


for key, value in hours_dict.items():
    print(f"{key} : {value}")
