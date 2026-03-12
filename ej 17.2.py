chimu = {
    "animal" : "gato",
    "dueño" : "desconocido"
}

luna = {
    "animal" : "gato",
    "dueño" : "desconocido"
}

aiko = {
    "animal" : "gato",
    "dueño" : "desconocido"
}

mascotas = [chimu,luna,aiko]
for p in mascotas:
    for e in p:
        print(f"{e}: {p[e]}")
