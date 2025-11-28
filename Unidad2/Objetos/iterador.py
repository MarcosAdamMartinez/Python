# profesores = ["Agustin", "Natalia", "Javier"]
# iterador = iter(profesores)
# print(next(iterador, "NO HAY MAS PROFES"))
# print(next(iterador, "NO HAY MAS PROFES"))
# print(next(iterador, "NO HAY MAS PROFES"))
# print(next(iterador, "NO HAY MAS PROFES"))

class DiasDeLaSemana:
    def __init__(self, dia):
        self.dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
        self.indice = dia

    def mostrar(self):
        print(self.dias[self.indice])

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice >= len(self.dias):
            raise StopIteration
        dia_actual = self.dias[self.indice]
        self.indice += 1
        return dia_actual


dia = DiasDeLaSemana(2)
dia.mostrar()

iterador = iter(dia)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

class DiasDeLaSemana2:
    def __init__(self, dia):
        self.dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
        self.indice = dia

    def mostrar(self):
        print(self.dias[self.indice])

    def __iter__(self):
        return self

    def __next__(self):
        dia_actual = self.dias[self.indice]
        if self.indice == len(self.dias)-1:
            self.indice = 0
        else:
            self.indice += 1
        return dia_actual

dia2 = DiasDeLaSemana2(2)
print()
iterador2 = iter(dia2)
print(next(iterador2))
print(next(iterador2))
print(next(iterador2))
print(next(iterador2))
print(next(iterador2))
print(next(iterador2))
print(next(iterador2))
print(next(iterador2))
print(next(iterador2))
print(next(iterador2))