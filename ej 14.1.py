usuarios = ["admin", "topo1", "topo2", "topo3", "topo4"]
if usuarios:
    for i in usuarios:
        if i == "admin":
            print("Hola admin, ¿querés ver un informe de estado?")
        else:
            print(f"Hola {i}, gracias por volver a iniciar sesión.")
else:
    print("Necesitamos encontrar algunos usuarios")