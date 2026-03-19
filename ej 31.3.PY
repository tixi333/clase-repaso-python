from random import choice
boleto = 0
win = False
numeros = [1,2,3,4,5,6,7,8,9,10, "A", "B", "C", "D", "E"]
contador = 0

while win == False:
    winners = []
    contador += 1
    
    for i in range(4):
        n = choice(numeros)
        winners.append(n)

    boleto = choice(numeros)
    
    for e in winners:
        if boleto == e:
            win = True
            print("Ganaste")
            print(e)
    
print(f"Tuviste {contador} intentos hasta ganar")