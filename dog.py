from animal import *

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        self.trained = False
        self.color =  "brown"

    def train(self):
        self.trained = True