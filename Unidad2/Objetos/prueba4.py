class ClaseA:
    def __init__(self):
        self.nombre = "Clase A"
        self.codigo = 55

    def queSoy(self):
        print("Soy clase A")



class ClaseB():
    def __init__(self):
        self.nombre = "Clase B"

    def queSoy(self):
        print("Soy clase B")

# Cuando un metodo aparece en 2 clases, siempre se le da preferencia a la clase que esta a la izquierda cuando definimos la nueva clase:
class ClaseC(ClaseA, ClaseB):
    pass

class ClaseD(ClaseB, ClaseA):
    pass

objetoa = ClaseA()
objetob = ClaseB()
objetoc = ClaseC()
objetod = ClaseD()


print(objetoa.nombre)
print(objetob.nombre)

print(objetoc.nombre)
print(objetoc.codigo)

print(objetod.nombre)
# print(objetod.codigo)

objetoc.queSoy()
objetod.queSoy()