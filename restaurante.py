class restaurante:
    def __init__(self,nombre_restaurante, tipo_cocina):
        self.restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
    
    def describir_restaurante(self):
        print(f"el restaurante {self.restaurante} se dedica a la cocina {self.tipo_cocina}")

    def abrir_restaurante(self):
        print(f"el restaurante {self.restaurante} esta abierto")


#r = restaurante("1","2")
#r.describir_restaurante()
#r.abrir_restaurante()