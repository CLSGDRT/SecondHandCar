from model.Vehicle import Vehicle

class Bike(Vehicle):
    __id_counter = 1

    def __init__(self, make, model, price, size):
        super().__init__(make, model, price)
        self.__id = Bike.__id_counter
        Bike.__id_counter += 1
        self.__size = size
    
    @property
    def id(self):
        return self.__id
    
    @property    
    def size(self):
        return self.__size

    @size.setter
    def ecobonus(self, value):
        self.__ecobonus = value