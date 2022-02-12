# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
# выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
# специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def sumOfNumbers(new_input, current_sum):
    numbers_list_str = new_input.strip().split(" ")
    numbers_ints = [int(val) for val in numbers_list_str]
    new_sum = sum(numbers_ints)
    return new_sum + current_sum


total_sum = 0


new_input = input("Please enter numbers separated by space or symbol 'q' :\n")


while new_input != 'q':

    total_sum = sumOfNumbers(new_input, total_sum)
    new_input = input("Please enter numbers or symbol, to exit press 'q'\n")


print(f"your sum is {total_sum}")
