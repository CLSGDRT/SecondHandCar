from model.Car import *
from model.Customer import *
from shop.accounting.Purchase import Purchase
from shop.accounting.Repare import Repare
from shop.accounting.Sale import Sale

class Reporting:
    def __init__(self):
        self.__repairs = []
        self.__purchases = []
        self.__sales = []
    
    def add_repair(self, repair: Repare):
        self.__repairs.append(repair)
    
    def add_purchase(self, purchase: Purchase):
        self.__purchases.append(purchase)
    
    def add_sale(self, sale: Sale):
        self.__sales.append(sale)
    
    def display_repairs(self):
        print("Repairs:")
        for repair in self.__repairs:
            print(f"ID: {repair.id}, Date: {repair.repare_date}, Car: {repair.car}, Price: {repair.price}")
            with open("data/carOutput.csv", 'a') as file :
                file.write(f"ID: {repair.id}, Date: {repair.repare_date}, Car: {repair.car}, Price: {repair.price}\n")
    
    def display_purchases(self):
        print("Purchases:")
        for purchase in self.__purchases:
            print(f"ID: {purchase.id}, Date: {purchase.purchase_date}, Car: {purchase.car}, Customer: {purchase.customer}, Price: {purchase.price} euros")
            with open("data/carOutput.csv", 'a') as file :
                file.write(f"ID: {purchase.id}, Date: {purchase.purchase_date}, Car: {purchase.car}, Customer: {purchase.customer}, Price: {purchase.price} euros\n")
    
    def display_sales(self):
        print("Sales:")
        for sale in self.__sales:
            print(f"ID: {sale.id}, Date: {sale.sale_date}, Car: {sale.car}, Price: {sale.price}")
            with open("data/carOutput.csv", 'a') as file :
                file.write(f"ID: {sale.id}, Date: {sale.sale_date}, Car: {sale.car}, Price: {sale.price}\n")
            
    
    def display_all(self):
        with open("data/carOutput.csv", 'w') as file :
            file.write("")
        self.display_repairs()
        self.display_purchases()
        self.display_sales()
