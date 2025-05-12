class Customer:
    __id_counter = 1

    def __init__(self, cars):
        self.__id = Customer.__id_counter
        Customer.__id_counter += 1
        self.__cars = cars  # list of Car

    @property
    def id(self):
        return self.__id
    
    @property
    def cars(self):
        return self.__cars

    @cars.setter
    def cars(self, value):
        self.__cars = value

    def addCar(self, car):
            self.__cars.append(car)
    
    def __str__(self):
         return f"Client : {self.__id}, \nSes voitures : {self.__cars}"