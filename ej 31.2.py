from random import choice

numeros = [1,2,3,4,5,6,7,8,9,10, "A", "B", "C", "D", "E"]

class Loteria:
    def __init__(self,numeros,cantidad):
        self.numeros = numeros
        self.cantidad = cantidad
    
    def sortear(self):
        n1 = choice(self.numeros)
        n2 = choice(self.numeros)
        if n2 == n1:
            while n2 == n1:
                 n2 = choice(self.numeros)
        n3 = choice(self.numeros)
        if n3 == n1 or n3 == n2:
            while n3 == n1 or n3 == n2:
                 n3 = choice(self.numeros)
                 
        n4 = choice(self.numeros)
        if n4 == n1 or n4 == n2 or n4 == n3:
            while n4 == n1 or n4 == n2 or n4 == n3:
                 n4 = choice(self.numeros)
        print(f"Los numeros sorteados son: {n1}, {n2}, {n3}, {n4}")

loteria = Loteria(numeros,4)
loteria.sortear()

