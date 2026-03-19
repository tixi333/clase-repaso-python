class Usuario:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.intentos_login = 0

    def describir_usuario(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
    
    def saludo_personalizado(self):
        print(f"{self.nombre} bienvenido/a")
    
    def incrementar_intentos_login(self):
        self.intentos_login += 1
        print(self.intentos_login)

    def reiniciar_intentos_login(self):
        self.intentos_login = 0
        print(self.intentos_login)

class Administrador(Usuario):
    def __init__(self, nombre, apellido, edad,privilegios):
        super().__init__(nombre, apellido, edad)
        self.privilegios = Privilegios(privilegios)
    
    def mostrar_privilegios(self):
        self.privilegios.mostrar_privilegios()

class Privilegios:
    def __init__(self,privilegios):
        self.privilegios = privilegios
    
    def mostrar_privilegios(self):
        for e in self.privilegios:
            print(e)

privilegios = ["puede agregar publicaciones", "puede eliminar publicaciones", "puede bloquear usuarios"]

admin = Administrador("tici","garin","16",privilegios)
admin.mostrar_privilegios()