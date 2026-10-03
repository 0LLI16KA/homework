import math

x = float(input("Введите угол в градусах: "))
radian = math.radians(x)
resultat = math.sin(radian) + math.cos(radian) + math.tan(radian)**2
print("Ответ:", resultat)
