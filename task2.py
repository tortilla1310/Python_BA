my_list_str = input('Enter list in Python notation:')
my_list = eval(my_list_str)

# my_list = [1, 2.344, 'Ivan', 3, 4]
print(my_list)

new_list = []
for i in range(len(my_list)):
    if i < len(my_list)-1 and i % 2 == 0:
        new_list.append(my_list[i+1])
        new_list.append(my_list[i])

print(new_list)
