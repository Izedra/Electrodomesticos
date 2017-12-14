from Electrodomestico import Electrodomestico
from Lavadora import Lavadora
from Television import Television

electro = ()
electro = list(electro)

electro.insert(-1, Electrodomestico(consumo="A", peso=15))
electro.insert(-1, Electrodomestico(consumo="A", peso=30))
electro.insert(-1, Electrodomestico(consumo="A", peso=60))
electro.insert(-1, Electrodomestico(consumo="A", peso=90))

electro.insert(-1, Lavadora(consumo="E", peso=50, carga=30))
electro.insert(-1, Lavadora(consumo="A", peso=50, carga=60))

electro.insert(-1, Television(peso=20, resolucion=30))
electro.insert(-1, Television(peso=20, resolucion=50))

tv,lava,electro = 0,0,0
i = 0
for ele in electro:
    i+=1
    ele.precioFinal()

    if isinstance(ele,Television):
        tv += ele.precioBase
    elif isinstance(ele,Lavadora):
        lava += ele.precioBase
    else:
        electro += ele.precioBase

print("Total de televisores: " + repr(tv))
print("Total de lavadoras: " + repr(lava))
print("Total de electrodomésticos: " + repr(electro))

print("Total: " + repr(tv+lava+electro))