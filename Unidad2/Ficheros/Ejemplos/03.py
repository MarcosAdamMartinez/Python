import pickle
from xxlimited_35 import Null


class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrarDatos(self):
        print("Nombre:", self.nombre,", Edad:", str(self.edad))

p1 = Persona("Pepe", 18)
p2 = Persona("Aitor", 24)
lista = [p1, p2]

try:
    fichero = open("persona.bin", 'wb')

    pickle.dump(p1, fichero)
    pickle.dump(p2, fichero)
    pickle.dump(lista, fichero)

    fichero.close()

    fichero = open("persona.bin", 'rb')

    p3 = pickle.load(fichero)
    p4 = pickle.load(fichero)
    lista2 = pickle.load(fichero)

    p3.mostrarDatos()
    p4.mostrarDatos()
    for p in lista2:
        p.mostrarDatos()

    fichero.close()
except:
    print("El fichero no existe")
