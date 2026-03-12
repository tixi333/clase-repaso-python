lugares_favoritos = {
    "juan" : ["lugar1", "puente", "lugar2"],
    "persona2" : ["lugar_lindo", "lugar6", "lugar"],
    "persona 5" : ["por ahi", "aca", "lugar 7"]
}

for e in lugares_favoritos:
    print(f"\nlugares favoritos de {e}: ")
    for lugar in lugares_favoritos[e]:
        print(f"\t{lugar}")