
# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с
#  прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое
# слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(word):
    phrase_up = word.title()
    return phrase_up


words = input('Введите слово с маленькой латинской буквы\n')
words_list = words.strip().split(" ")

words_capitalized = []
for word in words_list:
    words_capitalized.append(int_func(word))

# words_capitalized = [int_func(word) for word in words_list]


print(" ".join(words_capitalized))
