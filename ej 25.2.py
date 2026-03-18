def construir_perfil(nombre,apellido,**info_user):
    info_user["nombre"] = nombre
    info_user["apellido"] = apellido
    print(info_user)
 
construir_perfil("tici","garin",hola = "1")