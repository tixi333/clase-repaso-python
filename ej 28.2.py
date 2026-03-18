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

r = restaurante("1","2",4)
r.describir_restaurante()
r.abrir_restaurante()

r.establecer_clientes_atendidos()
r.incrementar_clientes_atendidos()