from model.Vehicle import Vehicle

class Car(Vehicle):
    __id_counter = 1

    def __init__(self, make, model, price, ecobonus, energy):
        super().__init__(make, model, price)
        self.__id = Car.__id_counter
        Car.__id_counter += 1
        self.__ecobonus = ecobonus
        self.__energy = energy

    @property
    def id(self):
        return self.__id
    
    @property    
    def ecobonus(self):
        return self.__ecobonus

    @ecobonus.setter
    def ecobonus(self, value):
        self.__ecobonus = value
    
    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        self.__energy = value

    def __str__(self):
        return f"Voiture : {self.__id}, {self.make}, {self.model}, {self.price}, {self.__ecobonus}, {self.__energy}"
    
    def __repr__(self):
        return f"{self.__id}, {self.make}, {self.model}, {self.price}, {self.__ecobonus}, {self.__energy}"

    @classmethod
    def createCar(cls):
        make = input("Marque de la voiture ? ")
        model = input("Modèle de la voiture ? ")
        price = float(input("Prix de la voiture ? "))
        ecobonus = float(input("Ecobonus de la voiture ? "))
        energy = input("Énergie de la voiture ? ")
        return cls(make, model, price, ecobonus, energy)