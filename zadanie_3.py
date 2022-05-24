słownik_zakupow = {
    "piekarnia": "chleb, bułki, pączek",
    "warzywniak": "marchew, seler, rukola"
}

lista_zakupow = {'piekarnia': ['chleb', 'bułki', 'paczek'], 'warzywniak': ['marchew', 'seler', 'rukola']}

for sklep, produkty in słownik_zakupow.items():
    lista = słownik_zakupow[sklep]
    print('Wchodze do', sklep.capitalize(), 'i kupuję tam natępujące rzeczy:', lista.title())

    suma = 0
for value in lista_zakupow:
    value_list = lista_zakupow[value]
    policz = len(value_list)
    suma = suma + policz

print(f"W sumie kupuję {suma} produktów")

print("To jest commit numer 1")