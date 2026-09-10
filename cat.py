from animal import *

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.fluffiness = 'high'
        self.color = "black"

    def comb(self):
        self.fluffiness = 'extreme'    