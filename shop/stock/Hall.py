from model.Car import *

class Hall:
    __capacity = 50

    def __init__(self, name, cars):
        self.__name = name
        self.__cars = cars

    @classmethod
    def capacity(cls):
        return cls.__capacity
    
    def addCar(self, car):
        if len(self.__cars) < self.__capacity:
            self.__cars.append(car)
            self.__capacity -= 1
            print("Voiture ajouter au showroom.\nPlaces restantes : ", self.capacity())
        else:
            print("Hall plein, impossible d'ajouter une voiture.")

    def delCar(self, car):
        if car in self.__cars:
            self.__cars.remove(car)
            self.__capacity +=1
        else:
            print("Voiture non trouvée dans le hall.")

    def __str__(self):
        car_list = "\n  ".join(str(car) for car in self.__cars)
        return f"Hall: {self.__name}\nCars:\n  {car_list}"
    
    @property
    def cars(self):
        return self.__cars
    
    @cars.setter
    def cars(self, value):
        self.__cars = value