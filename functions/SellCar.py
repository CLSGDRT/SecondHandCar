from model.Car import *
from model.Customer import *
from shop.accounting.Sale import Sale
from shop.stock.Garage import *
from shop.stock.Hall import *

def sellCar(hall, reporting):

    # vérification de la présence de voiture dans le showroom
    if not hall._Hall__cars:
        print("Aucune voiture disponible dans le hall.")
        return
    
    # recherche de la voiture à vendre
    print("Choisissez une voiture à vendre (par son ID) :")
    for car in hall._Hall__cars:
        print(f"ID: {car.id}, {car}")
    
    car_id = int(input("Entrez l'ID de la voiture à vendre : "))
    selected_car = next((car for car in hall._Hall__cars if car.id == car_id), None)

    # instanciation de la vente et suppression de la voiture du showroom puis ajout au reporting
    if selected_car:

        price = float(input(f"Quel est le prix de vente de {selected_car.make} {selected_car.model} ? "))
        sale_date = input("Entrez la date de vente (YYYY-MM-DD) : ")

        sale = Sale(sale_date, price, selected_car)

        reporting.add_sale(sale)
        
        hall.delCar(selected_car)
        print(f"Vente effectuée: {sale}")
    else:
        print("Aucune voiture trouvée avec cet ID.")
