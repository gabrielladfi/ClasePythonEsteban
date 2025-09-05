class Carro:

    llantas = 4
    puertas = 4

    def __init__(self):
        self.color = "azul"
        pass
    
    def obtenerColor(self):
        print(self.color)


class Camioneta(Carro):

    tipo_llantas = "4x4"

    def obtenerTraccion(self):
        print(self.tipo_llantas)

class Ranger(Camioneta):
    def setColor(self, nombre_color):
        self.color = nombre_color

carro_de_esteban = Ranger()
carro_de_esteban.setColor("Rojo")
carro_de_esteban.obtenerColor()
carro_de_esteban.obtenerTraccion()
