class StockingArea:
    def __init__(self, name, capacity):
        self.__name = name
        self.__capacity = capacity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    
    