from Electrodomestico import Electrodomestico


class Television(Electrodomestico):
    def __init__(self, precioB=100, color="blanco", consumo='F', peso=5, resolucion=20, fourK=False):
        Electrodomestico.__init__(self, precioB=precioB, color=color, consumo=consumo, peso=peso)
        self.resolucion = resolucion
        self.fourK = fourK

    def precioFinal(self):
        Electrodomestico.precioFinal(self)
        if self.resolucion > 40:
            self.precioB = self.precioB*1.3
        if self.fourK == True:
            self.precioB = self.precioB+50