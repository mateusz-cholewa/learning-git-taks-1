słownik_zakupow = {
    "piekarnia": "chleb, bułki, pączek",
    "warzywniak": "marchew, seler, rukola"
}

lista_zakupow = {'piekarnia': ['chleb', 'bułki', 'paczek'], 'warzywniak': ['marchew', 'seler', 'rukola']}

for sklep, produkty in słownik_zakupow.items():
    lista = słownik_zakupow[sklep]
    print('Wchodze do', sklep.capitalize(), 'i kupuję tam natępujące rzeczy:', lista.title())