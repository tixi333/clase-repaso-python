
while True:
    edad = int(input("Ingrese su edad: "))
    if edad >= 3 and edad <= 12 :
        print("Su entrada cuesta: $10")
    elif edad > 12:
        print("Su entrada cuesta: $15")
    break