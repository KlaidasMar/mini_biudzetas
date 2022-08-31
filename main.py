import pandas
import sqlalchemy
from modules.biudzetas import Biudzetas


mano_biudzetas = Biudzetas()

while True:
    print("Pasirinkite veiksma: ")
    print("1. Ivesti pajamas")
    print("2. Ivesti islaidas")
    print("3. Gauti balansa")
    print("4. Gauti ataskaita")
    print("0. Exit")
    action = input()
    if action == "1":
        print("Iveskite pajamas: ")
        suma = int(input("Suma: "))
        siuntejas = input("Siuntejas: ")
        papildoma_informacija = input("Papildoma informacija: ")
        mano_biudzetas.ivesti_pajamas(suma, siuntejas, papildoma_informacija)
        print("Pajamos ivestos sekmingai!")
    if action == "2":
        print("Iveskite islaidas: ")
        suma = int(input("Suma: "))
        atsiskaitymo_budas = input("Atsiskaitymo budas: ")
        isigyta_preke_paslauga = input("Isigyta preke/paslauga: ")
        mano_biudzetas.ivesti_islaidas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        print("Islaidos ivestos sekmingai!")
    if action == "3":
        print(f"Balansas: {mano_biudzetas.gauti_biudzeto_balansa()}")
    if action == "4":
        mano_biudzetas.gauti_ataskaita()
    if action == "0":
        break