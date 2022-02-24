# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные
# о фирме: название, форма собственности, выручка, издержки.

# Пример строки файла: firm_1 ООО 10000 5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней
# прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

# Подсказка: использовать менеджер контекста.


import json

firm_dict = {}
profit_dict = {}
profit_average = 0
total_profit = 0
i = 0

with open('test-4.txt', 'r') as my_file:
    for line in my_file:
        line_split = line.split(' ')
        company_name = line_split[0]
        profit = int(line_split[2]) - int(line_split[3])

        i += 1
        total_profit += profit
        firm_dict[company_name] = profit

if i > 0:
    profit_average = total_profit / i

    profit_dict["average_profit"] = profit_average

    for key, value in firm_dict.items():
        print(f"Company : {key} profit: {value}")

    for key, value in profit_dict.items():
        print(f"{key} : {value}")

    result_list = [firm_dict, profit_dict]

    with open('output.txt', 'w') as outfile:
        json.dump(result_list, outfile)
