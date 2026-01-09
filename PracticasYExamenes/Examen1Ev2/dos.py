class Tareas():
    def __init__(self, identificador, titulo, prioridad):
        self.identificador = identificador
        self.titulo = titulo
        if prioridad in range(1,10):
            self.prioridad = prioridad
        self.realizada = False

class GestorTarea():
    def __init__(self):
        self.__tareas = {}

    @property
    def tareas(self):
        return self.__tareas

    def agregarTarea(self, tarea):
        try:
            if tarea.identificador not in self.tareas.keys():
                print(f"Tarea '{tarea.titulo}' (ID: {tarea.identificador}) añadida.")
                self.tareas[tarea.identificador] = tarea
            else:
                raise Exception(f"Error: ID {tarea.identificador} ya existente.")
        except Exception as e:
            print(e)
    def eliminarTarea(self, tarea):
        try:
            if tarea in self.tareas:
                self.tareas.pop(tarea)
                print(f"Tarea con ID ('{tarea}') eliminada.")
            else:
                raise Exception(f"Error: No se encontró una tarea con ID {tarea}.")
        except Exception as e:
            print(e)

    def realizarTarea(self, identificador):
        try:
            if identificador in self.tareas.keys():
                self.tareas[identificador].realizada = True
                print(f"Tarea ID {identificador} '{self.tareas[identificador].titulo}' marcada como completada.")
            else:
                raise Exception(f"Error: No se encontró una tarea con ID {tarea}.")
        except Exception as e:
            print(e)

    def mostrarTareasCompletadas(self):
        listaTareas = []
        listaTareasRealizadas = []
        for tarea in self.tareas:
            listaTareas.append(self.tareas[tarea])
        for tarea in listaTareas:
            if tarea.realizada:
                listaTareasRealizadas.append(tarea)
        print("- LISTADO DE TAREAS:")
        for tarea in listaTareasRealizadas:
            print(f"[{tarea.identificador}] {tarea.titulo} (Prioridad: {tarea.prioridad})")
        if listaTareasRealizadas == []:
            print("No hay tareas completadas")

    def mostrarTareasNoCompletadas(self):
        listaTareas = []
        listaTareasNoRealizadas = []
        for tarea in self.tareas:
            listaTareas.append(self.tareas[tarea])
        for tarea in listaTareas:
            if tarea.realizada == False:
                listaTareasNoRealizadas.append(tarea)
        print("- LISTADO DE TAREAS:")
        for tarea in listaTareasNoRealizadas:
            print(f"[{tarea.identificador}] {tarea.titulo} (Prioridad: {tarea.prioridad})")
        if listaTareasNoRealizadas == []:
            print("No hay no tareas completadas")

gestorTarea = GestorTarea()

tarea = Tareas("P10","Comprar billetes", 9)
tarea2 = Tareas("E25","Enviar email al jefe",5)
tarea3 = Tareas("P33","Aprender Python",2)
tarea4 = Tareas("F47","Revisar facturas",7)

gestorTarea.agregarTarea(tarea)
gestorTarea.agregarTarea(tarea)
gestorTarea.agregarTarea(tarea2)
gestorTarea.agregarTarea(tarea3)
gestorTarea.agregarTarea(tarea4)

print()
gestorTarea.realizarTarea("P33")
gestorTarea.realizarTarea("F47")

print()
gestorTarea.eliminarTarea("E25")
gestorTarea.eliminarTarea("E25")

print()
gestorTarea.mostrarTareasCompletadas()
print()
gestorTarea.mostrarTareasNoCompletadas()