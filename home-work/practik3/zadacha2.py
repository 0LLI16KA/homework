print("\t -Задание №1-\n")
my_list = [1, 2, 3]
print("Было:", my_list)
my_list[0] = 100
print("Стало:", my_list)
# Всё спокойно меняется

print("\t -Задание №2-\n")
my_tuple = (1, 2, 3)
print("Было:", my_tuple)
my_tuple[0] = 100
# Не получается изменить
# Выдаёт ошибку: TypeError: 'tuple' object does not support item assignment

print("\t -Задание №3-\n")
my_string = "cat"
print("Было:", my_string)
my_string[0] = "b"
# Не получается изменить
# Выдаёт ошибку: TypeError: 'str' object does not support item assignment
