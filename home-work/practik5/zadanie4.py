import math

def calculate_rectangle_area(width, height):
    return width * height
def calculate_circle_area(radius):
    return math.pi * radius * radius
print("Прямоугольник:")
w = float(input("Ширина: "))
h = float(input("Высота: "))
print(f"Площадь: {calculate_rectangle_area(w, h):.2f}")
print("Круг:")
r = float(input("Радиус: "))
print(f"Площадь: {calculate_circle_area(r):.2f}")
