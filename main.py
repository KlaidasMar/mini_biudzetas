import pandas
import sqlalchemy


class Irasas:
    def __init__(self, suma):
        self.suma = suma

class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_info):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_info = papildoma_info

class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga

class Biudzetas():
    def __init__(self):
        self.zurnalas = []

    def ivesti_pajamas(self, suma, siuntejas, papildoma_informacija):
        pajamu_irasas = PajamuIrasas(suma, siuntejas, papildoma_informacija)
        self.zurnalas.append(pajamu_irasas)

    def ivesti_islaidas(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        islaidu_irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(islaidu_irasas)

    def gauti_biudzeto_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                balansas += irasas.suma
            if isinstance(irasas, IslaiduIrasas):
                balansas -= irasas.suma
        return balansas

    def gauti_ataskaita(self):
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                print(f"Pajamos: {irasas.suma} {irasas.siuntejas} {irasas.papildoma_info}")
            if isinstance(irasas, IslaiduIrasas):
                print(f"Islaidos: {irasas.suma} {irasas.atsiskaitymo_budas} {irasas.isigyta_preke_paslauga}")

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