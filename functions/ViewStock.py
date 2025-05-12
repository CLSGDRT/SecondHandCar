from model.Car import *
from shop.stock.Garage import *
from shop.stock.Hall import *


def viewStock(stock, showroom):

    # affichage des stocks suivant le stockage renseigné
    if stock == "garage":

        print("Stock du garage : ")
        print(showroom)
    
    elif stock == "hall":
        
        print("Stock du showroom : ")
        print(showroom)  