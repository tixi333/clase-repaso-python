while True:
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))

        if num2 == 0:
            raise ZeroDivisionError("No se puede dividir por cero.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue
    except ZeroDivisionError as e:
        print(e)
        continue
    else:
        resultado = num1 / num2
        print(f"El resultado de {num1} dividido por {num2} es: {resultado}")
        
    break