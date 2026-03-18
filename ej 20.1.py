pedidos_sandwiches = ["1","2","3","pastron","pastron","pastron"]
sandwiches_teminados = []
print("nohaypastron")
for e in pedidos_sandwiches:
    while "pastron" in pedidos_sandwiches:
        pedidos_sandwiches.remove("pastron")
    print(f"prepare tu sanguche de {e} ")
    sandwiches_teminados.append(e)


print(sandwiches_teminados)