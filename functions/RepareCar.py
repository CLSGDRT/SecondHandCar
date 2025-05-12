from model.Car import *
from model.Customer import *
from shop.accounting.Repare import Repare
from shop.stock.Garage import *
from shop.stock.Hall import *


def repareCar(hall, garage, reporting):

    # vérification présence voiture dans le showroom
    if not hall.cars:
        print("Aucune voiture disponible dans le hall pour réparation.")
        return
    
    # choix de la voiture à déplacer vers le garrage par son id
    print("Choisissez une voiture à réparer (par son ID) :")
    for car in hall.cars:
        print(f"ID: {car.id}, {car}")
    
    car_id = int(input("Entrez l'ID de la voiture à réparer : "))
    selected_car = next((car for car in hall.cars if car.id == car_id), None)

    # suppression de la voiture du showroom puis ajout de la voiture au garage
    if selected_car:
        hall.delCar(selected_car)
        garage.addCar(selected_car)
        
        price = float(input("Quel est le prix de la réparation ? "))
        repare_date = input("Entrez la date de réparation (YYYY-MM-DD) : ")

    # instanciation de la réparation et ajout au reporting
        repair = Repare(repare_date, price, selected_car)
        reporting.add_repair(repair)
        print(f"Réparation ajoutée: {repair}")
    
    else:
        print("Aucune voiture trouvée avec cet ID.")

