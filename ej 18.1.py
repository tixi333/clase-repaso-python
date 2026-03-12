while True:
    try:
        cant_grupo = int(input("Ingrese la cantidad de personas que contiene el grupo: "))
    except ValueError:
        pass
    else:
        if cant_grupo > 8:
            print("no hay mesa")
        elif cant_grupo >= 1 and cant_grupo <= 8:
            print("hay mesa")
        break