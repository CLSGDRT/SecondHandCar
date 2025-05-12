from model.Car import *
from shop.accounting.Repare import *

class Garage:
    __capacity = 50

    def __init__(self, name, cars):
        self.__name = name
        self.__cars = cars
        self.__repares = []

    def addCar(self, car):
        if len(self._cars) < self.__capacity:
            self._cars.append(car)
        else:
            print("Garage plein, impossible d'ajouter une voiture.")


    def addCar(self, car):
        if len(self.__cars) < self.__capacity:
            self.__cars.append(car)
            self.__capacity -= 1
        else:
            print("Garage plein, impossible d'ajouter une voiture.")

    def delCar(self, car):
        if car in self.__cars:
            self.__cars.remove(car)
            self.__capacity += 1
        else:
            print("Voiture non trouvée dans le garage.")

    @property
    def cars(self):
        return self.__cars

    @cars.setter
    def cars(self, value):
        self.__cars = value
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        
    @property
    def repares(self):
        return self.__repares

    @repares.setter
    def repares(self, value):
        self.__repares = value

    @classmethod
    def capacity(cls):
        return cls.__capacity