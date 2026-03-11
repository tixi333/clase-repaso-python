pizzas = ["Muzzarella", "Jamon", "Salame"]
for p in pizzas:
    print(f"me gusta la pizza de {p}")

print("que asco el salame")

pizzas_amigo = pizzas.copy()

pizzas.append("Cebolla")

pizzas_amigo.append("otra pizza")

print("mis pizzas favoritas son: ")
for i in pizzas:
    print(i)
print("_-------------------------------------------_")
print ("las pizzas favopritas de mi amigo son: ")
for i in pizzas_amigo:
    print(i)