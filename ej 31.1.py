import random

class Dado:
    def __init__(self,sides = 20):
        self.sides = sides
    
    def roll_die(self):
        cant = 10
        while cant > 0:
            n = random.randint(1,self.sides)
            cant-=1
            print(n)

dado = Dado()
dado.roll_die()