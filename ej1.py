espacio = "-------------------------------"
invitados = ["gouarnalusse","alonso mazza yatra", "agus"]
for i in invitados:
    print(espacio)
    print(f"{i} veni a cenar ya")
print(espacio)
print("gornaluse: hola nu puedo ir")

invitados.remove("gouarnalusse")
print(espacio)
invitados.insert(0 ,"añañin")
print(f"{invitados[0]} veni a cenar ya")
print(espacio)
for i in invitados:
    print(f"hola {i} vamos a invitar a mas gente")
    print(espacio)
invitados.insert(0,"ciro")
tamaño = len(invitados)
invitados.insert(tamaño//2, "cande")
invitados.insert(tamaño+1, "alguien")


print("Invitados:")
for i in invitados:
    print(i)