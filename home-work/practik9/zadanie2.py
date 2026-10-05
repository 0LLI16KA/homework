# Критерии
print("Введите имена участников (каждое с новой строки).")
print("Когда закончите, введите 'Стоп'.")

# Считает кол-во имён между Александрой и Левоном
schetchik = 0

# Встретили ли Александру
aleksandra = False

# Закончился ли ввод
finished = False

while not finished:
    name = input()
    if name == "Стоп":
        finished = True
    elif name == "Александра":
        aleksandra = True
    elif name == "Левон":
        # Встретили Левона, ввод закончен
        finished = True
    elif aleksandra:
        # Видели Александру, но не видели Левона
        schetchik = schetchik + 1

# Вывод
print(schetchik)
