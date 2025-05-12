class Vehicle:
    def __init__(self, make, model, price):
       self.__make = make
       self.__model = model 
       self.__price = price
    
    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, value):
        self.__make = value
    
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value
    
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value
    