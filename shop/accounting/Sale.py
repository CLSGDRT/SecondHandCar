from model.Car import *
from model.Customer import *


class Sale:
    __id_counter = 1
    
    def __init__(self, sale_date, price, car: Car):
        self.__id = Sale.__id_counter
        Sale.__id_counter += 1
        self.__sale_date = sale_date
        self.__price = price
        self.__car = car
    
    @property
    def id(self):
        return self.__id
    
    @property
    def sale_date(self):
        return self.__sale_date
    
    @sale_date.setter
    def sale_date(self, value):
        self.__sale_date = value
    
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

    def __str__(self):
        return f"{self.__sale_date}, {self.__price}, {self.__car}"
