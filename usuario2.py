
from usuario1 import Usuario

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