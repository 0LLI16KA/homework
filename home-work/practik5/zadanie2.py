# Ввод данных
ves, rost = map(float, input("Введите ваш вес и рост через пробел: ").split())
# Расчёт ИМТ
IMT = ves / (rost * rost)
# Вывод ИМТ
print(f"Ваш ИМТ: {IMT:,.1f}")
