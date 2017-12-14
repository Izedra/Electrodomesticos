from Electrodomestico import Electrodomestico


class Lavadora(Electrodomestico):
    def __init__(self, precioB=100, color="blanco", consumo='F', peso=5, carga=5):
        Electrodomestico.__init__(self, precioB=precioB, color=color, consumo=consumo, peso=peso)
        self.carga=carga

    def precioFinal(self):
        Electrodomestico.precioFinal(self)
        if self.carga > 30:
            self.precioB = self.precioB + 50