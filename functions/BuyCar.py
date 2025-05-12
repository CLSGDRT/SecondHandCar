from model.Car import *
from model.Customer import *
from shop.accounting.Purchase import Purchase
from shop.accounting.Reporting import *


def buyCar(hall, customer, reporting):
    
    print("Renseigner Voiture")

    # création de la voiture achetée
    car = Car.createCar()

    # ajout de la voiture au showroom
    hall.addCar(car)

    # instanciation d'un achat de véhicule
    price = car.price
    purchase_date = input("Entrez la date d'achat (YYYY-MM-DD) : ")
    customer.addCar(car)
    purchase = Purchase(purchase_date, price, car, customer)

    # ajout du mouvement au reporting
    reporting.add_purchase(purchase)
    print(f"Achat effectué: \n{purchase}")

    return hall

    