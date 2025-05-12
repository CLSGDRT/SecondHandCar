#remplacement d'un main.py "plus propre"

from model.Car import Car
from model.Customer import Customer
from shop.accounting.Purchase import Purchase
from shop.accounting.Repare import Repare
from shop.accounting.Reporting import Reporting
from shop.accounting.Sale import Sale
from shop.stock.Garage import Garage
from shop.stock.Hall import Hall
from functions.BuyCar import buyCar
from functions.RepareCar import repareCar
from functions.SellCar import sellCar
from functions.ViewStock import viewStock

class Application:
    def __init__(self, name):
        self._name = name

    def run(self):
        print(f"Lancement du {self._name}...")

def main():
    app = Application("Programme de gestion de concession")
    app.run()

    menu_id = 0
    listOfCar = []
    listOfCar2 = []
    listOfnewSeller = []
    showroom = Hall("Showroom", listOfCar)
    workshop = Garage("Atelier", listOfCar2)
    reporting = Reporting()

    while menu_id == 0:
        print("Entrer le numéro correspondant à votre demande")
        print("1 - Acheter un véhicule")
        print("2 - Vendre un véhicule")
        print("3 - Réparer un véhicule")
        print("4 - Voir le stock garage")
        print("5 - Voir le stock hall")
        print("6 - Reporting complet")
        print("7 - Quitter")
        menu_id = int(input("=>"))

        match menu_id:
            case 1:
                customer = Customer(listOfnewSeller)
                showroom = buyCar(showroom, customer, reporting)
                menu_id = 0
            case 2:
                sellCar(showroom, reporting)
                menu_id = 0
            case 3:
                repareCar(showroom, workshop, reporting)
                menu_id = 0
            case 4:
                viewStock("garage", showroom)
                menu_id = 0
            case 5:
                viewStock("hall", showroom)
                menu_id = 0
            case 6:
                reporting.display_all()
                menu_id = 0
            case 7:
                exit()
            case _:
                print("Entrée non valide !!")
                menu_id = 0
                continue

if __name__ == "__main__":
    main()