# Реализовать структуру данных «Товары». Она должна представлять собой
# список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с
# параметрами (характеристиками товара: название, цена, количество,
# единица измерения). Структуру нужно сформировать программно, т.е.
# запрашивать все данные у пользователя.

# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором
# каждый ключ — характеристика товара, например название, а значение —
# список значений-характеристик, например список названий товаров.

product_structure = {
    'Name': str,
    'Price': int,
    'Amount': int,
    'Единица измерения': str,
}

product_list = []
product_counter = 1

while True:
    decision = input(f'Товаров = {len(product_list)}, добавить? [y/n]').lower()

    if decision == 'n':
        break
    else:
        product_info = {}

        for property_name, property_type in product_structure.items():
            user_input = input(f"Заполните поле '{property_name}' >>> ")
            product_info[property_name] = property_type(user_input)

        product_list.append((product_counter, product_info))
        product_counter += 1

product_analytics = {}
for analytics_key in product_structure.keys():
    item_list = []

for product in product_list:
    item_list.append(product[1][analytics_key])
