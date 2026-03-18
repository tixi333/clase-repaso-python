class restaurante:
    def __init__(self,nombre_restaurante, tipo_cocina, clientes):
        self.restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.clientes_atendidos = 0
        self.clientes = clientes
    
    def describir_restaurante(self):
        print(f"el restaurante {self.restaurante} se dedica a la cocina {self.tipo_cocina}")

    def abrir_restaurante(self):
        print(f"el restaurante {self.restaurante} esta abierto")

    def establecer_clientes_atendidos(self):
        self.clientes_atendidos = self.clientes
        print(self.clientes_atendidos)

    def incrementar_clientes_atendidos(self):
        self.clientes_atendidos += self.clientes
        print(self.clientes_atendidos)

class PuestoDeHelados(restaurante):
    
    def __init__(self, nombre_restaurante, tipo_cocina, clientes,sabores):
        super().__init__(nombre_restaurante, tipo_cocina, clientes)
        self.sabores = sabores

    def mostrar_sabores(self):
        for e in self.sabores:
            print(e)

sabores= ["menta","tramontana"]
h= PuestoDeHelados("heladeria","helado",0,sabores)
h.mostrar_sabores()