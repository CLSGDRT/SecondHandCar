from model.Car import *
from model.Customer import *


class Repare:
    __id_counter = 1
    
    def __init__(self, repare_date, price, car: Car):
        self.__id = Repare.__id_counter
        Repare.__id_counter += 1
        self.__repare_date = repare_date
        self.__price = price
        self.__car = car
    
    @property
    def id(self):
        return self.__id
    
    @property
    def repare_date(self):
        return self.__repare_date
    
    @repare_date.setter
    def repare_date(self, value):
        self.__repare_date = value
    
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
        return f"{self.__repare_date}, {self.__price}, {self.__car}"
