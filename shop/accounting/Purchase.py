from model.Car import *
from model.Customer import *

class Purchase:
    __id_counter = 1
    
    def __init__(self, purchase_date, price, car: Car, customer: Customer):
        self.__id = Purchase.__id_counter
        Purchase.__id_counter += 1
        self.__purchase_date = purchase_date
        self.__price = price
        self.__car = car
        self.__customer = customer
    
    @property
    def id(self):
        return self.__id
    
    @property
    def purchase_date(self):
        return self.__purchase_date
    
    @purchase_date.setter
    def purchase_date(self, value):
        self.__purchase_date = value
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        self.__price = value
    
    @property
    def car(self):
        return self.__car
    
    @car.setter
    def car(self, value):
        self.__car = value
    
    @property
    def customer(self):
        return self.__customer
    
    @customer.setter
    def customer(self, value):
        self.__customer = value
    
    def __str__(self):
        return f"Infos d'achat : {self.id}, {self.__purchase_date}, {self.__price},\n{self.__car},\n {self.__customer}"
