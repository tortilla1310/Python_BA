# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("hours")
parser.add_argument("rate")
parser.add_argument("bonus")
args = parser.parse_args()
print(args.hours)
print(args.rate)
print(args.bonus)


def payroll(hours, rate, bonus):
    result = hours * rate + bonus
    return result


print(payroll(float(args.hours), float(args.rate), float(args.bonus)))

"""
python3 task1.py 60 30 1000
"""
