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

user = Usuario("tici","garin","16")
user.describir_usuario()
user.saludo_personalizado()
user.incrementar_intentos_login()
user.incrementar_intentos_login()
user.incrementar_intentos_login()
user.reiniciar_intentos_login()