n = int(input("Введите количество строк: "))

vse_simv = []

for i in range(n):
    s = input("Введите любой символ: ")
    for simv in s:
        vse_simv.append(simv)

print(vse_simv)
