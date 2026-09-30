try:
# sbor data
    num2, num1 = input("Введите два любых числа через пробел: ").split()
    num1 = int(num1)
    num2 = int(num2)
    print(num1,"\n", num2)
# num2 plus num1
    sum = num1 + num2
    print("Результат:", sum)
except ValueError:
    print("Ввод не корректен! Вводите только целые числа.")
