# Crea una clase Animal que tenga:
# Un atributo nombre
# Un métodito hablar() que muestre:
# El animal hace un sonido
#
# Luego crea una clase Perro que herede de Animal y:
# Sobrescriba el métodito hablar() para mostrar:
# El perro <nombre> dice: Guau
# Desde el programa principal:
# Crea un objeto Animal
# Crea un objeto Perro
# Llama al métodito hablar() de ambos

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

animal1 = Animal("Michy")
perro1 = Perro("Lassy")

animal1.hablar()
perro1.hablar()
