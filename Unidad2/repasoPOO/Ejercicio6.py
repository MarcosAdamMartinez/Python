# Crea una función llamada hacer_hablar(animal) que:
# Reciba un objeto de tipo Animal
# Llame a su métodito hablar()
#
# Luego:
# Crea una lista con varios animales (Animal, Perro, y al menos otra clase que tú inventes, por ejemplo Gato)
# Recorre la lista y llama a hacer_hablar() con cada uno
# 👉 Cada animal debe “hablar” según su clase.

class Animal():
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    def hablar(self):
        print("El animal",self.nombre,"hace un sonido")

class Perro(Animal):
    def hablar(self):
        print("El perro",self.nombre,"dice: Guau")

class Gato(Animal):
    def hablar(self):
        print("El gato",self.nombre,"dice: Miau")

class Pajaro(Animal):
    def hablar(self):
        print("El pajaro",self.nombre,"dice: Pio")

def hacer_hablar(animal):
    animal.hablar()

animal1 = Animal("Cocodrilo")
animal2 = Animal("Leon")
animal3 = Animal("Hiena")
perro1 = Perro("Lassy")
perro2 = Perro("Tobby")
gato1 = Gato("Michi")
pajaro1 = Pajaro("Federico Garcia Lorca")

listaAnimales = [animal1, pajaro1, animal3, perro1, animal2, perro2, gato1]

for animal in listaAnimales:
    hacer_hablar(animal)
