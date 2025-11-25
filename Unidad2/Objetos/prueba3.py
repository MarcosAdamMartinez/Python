class ClaseA:
    def __init__(self):
        self.nombre = "Clase A"
        self.codigo = 55


    # No se pueden usar decoradores (@property) para heredar a otras clases:
    def getNombre(self):
        return self.nombre

    # Creamos una funcion que se heredara y no se modificara en la ClaseB:
    def cambiarNombre(self, nuevoNombre):
        self.nombre = nuevoNombre


class ClaseB(ClaseA):
    def __init__(self):
        super().__init__()
        self.nombre = self.getNombre()+" -> Clase B"

    # Funcion que no esta en la ClaseA:
    def incrementaCodigo(self):
        self.codigo += 1



objetoa = ClaseA()
objetob = ClaseB()

print(objetoa.getNombre())
print(objetob.getNombre())

objetoa.cambiarNombre("ClaseA 2")
print(objetoa.getNombre())

objetob.cambiarNombre("Paco")
print(objetob.getNombre())

print(objetob.codigo)
objetob.incrementaCodigo()
print(objetob.codigo)