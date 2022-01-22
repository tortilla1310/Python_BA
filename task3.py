# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

my_month = int(input('Enter month as a number: '))

# 1 Via list
month_list = ["Winter",  # january
              "Winter",  # Februar
              "Spring",  # March
              "Spring",  # April
              "Spring",  # May
              "Summer",  # June
              "Summer",  # July
              "Summer",  # August
              "Autumn",  # September
              "Autumn",  # October
              "Autumn",  # November
              "Winter",  # December
              ]
print(month_list[my_month])


# 2 Via dict
months_dic = {1: "Winter",
              2: "Winter",
              3: "Spring",
              4: "Spring",
              5: "Spring",
              6: "Summer",
              7: "Summer",
              8: "Summer",
              9: "Autumn",
              10: "Autumn",
              11: "Autumn",
              12: "Winter"
              }
print(months_dic[my_month])
