class Perro:
    numperros = 0

    def __init__(self, nombre = "Bobby"):
        self.nombre = nombre
        Perro.numperros += 1

    def llamar(self):
        return "Ey "+self.nombre+" Ven aqui!"

    @classmethod
    def cuantosPerros(cls):
        return cls.numperros

    @staticmethod
    def ladrar():
        return "Guau"

    def sorecargada(self, atributo):
        if isinstance(atributo,int):
            print("Estoy trabajando con un entero")
        elif isinstance(atributo, float):
            print("Estoy trabajando con un float")
        elif isinstance(atributo, str):
            print("Estoy trabajando con un string")
        elif isinstance(atributo, list):
            print("Estoy trabajando con una lista")
        else:
            print("Estoy trabajando con otra cosa")

    def sobrecargada2(self, *atributos):
        if len(atributos) == 1:
            print("Recibo un parametro")
        elif len(atributos) == 2:
            print("Recibo dos parametros")
        else:
            print("Recibo tres o mas parametros")



mascota1 = Perro()
mascota2 = Perro("Sultan")
mascota3 = Perro("Tobby")

print(mascota1.nombre)
print(mascota2.nombre)
print(mascota3.nombre)

print(Perro.cuantosPerros())
print(Perro.ladrar())
print(mascota1.ladrar())

mascota3.sorecargada(3)
mascota3.sorecargada(3.5)
mascota3.sorecargada("Hola")
mascota3.sorecargada([1,2,3])

mascota3.sobrecargada2(1,[4,8],2)
