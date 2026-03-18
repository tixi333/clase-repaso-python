def enviar_mensaje(menaje,lita):
    while menaje:
        m = menaje.pop()
        lita.append(m)
    
    print(menaje)
    print(lita)
        

lita = []
mensaje = ["bola","hola","zucchini","marmota","lllama"]

enviar_mensaje(mensaje[:],lita)
print(mensaje)