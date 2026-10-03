number = int(input("Введите четырехзначное число: "))
a = number // 1000
b = (number // 100) % 10
c = (number // 10) % 10
d = number % 10
print("Тысячи:", a)
print("Сотни:", b)
print("Десятки:", c)
print("Единицы:", d)
