kurs = 95.50
def convert_usd_to_rub(amount_usd):
    return amount_usd * kurs
dolari = float(input("Введите сумму в долларах: "))
rubli = convert_usd_to_rub(dolari)
print(f"{dolari:.2f} USD = {rubli:.2f} RUB")
