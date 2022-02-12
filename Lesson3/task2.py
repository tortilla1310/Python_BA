# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год
# рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

from unicodedata import name


def userData(name, surname, year, city, email, phone):
    print(name, surname, year, city, email, phone)


name_in = input('Please provide the name: ')
surname_in = input('Please provide the surname: ')
year_in = input('Please provide the year: ')
city_in = input('Please provide the city: ')
email_in = input('Please provide the email: ')
phone_in = input('Please provide the phone: ')


userData(name=name_in, surname=surname_in, year=year_in,
         city=city_in, email=email_in, phone=phone_in)
