"""1. Queremos implementar una clase para gestionar una aplicación de gestión de notas. Cada
nota tendrá cuatro elementos: título, descripción, color (debe de ser amarillo, verde, blanco o
cyan para una futura implementación en un entorno gráfico) y fecha de creación.
Necesitamos, además, añadir los siguientes métodos: crearNota, eliminarNota y listarNota
No hace falta que hagas entradas por teclado: crea los métodos y pruébalos llamándolos
directamente.
Trata de que la visualización de la nota sea lo mas agradable posible en pantalla usando
fstrings
2. Modifica el programa de forma que haya dos tipos de notas: una normal (como las descritas
anteriormente) y otra urgente que será siempre en rojo y que, cuando las listemos,
aparecerán siempre encima de las otras. Haz las modificaciones de forma que tengas una
clase abstracta de la que deriven los dos tipos de notas. Las notas urgentes, además,
pediran confirmación por teclado cuando tratemos de eliminarlas y se visualizaran con algún
detalle que las distinga de las normales."""

"""1"""
from datetime import datetime

# ===============================
# Clase Nota
# ===============================
class Nota:
    COLORES_VALIDOS = ["amarillo", "verde", "blanco", "cyan"]

    def __init__(self, titulo, descripcion, color, fecha=None):
        self.titulo = titulo
        self.descripcion = descripcion
        if color.lower() in Nota.COLORES_VALIDOS:
            self.color = color.lower()
        else:
            self.color = "blanco"  # default
        if fecha is None:
            self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            self.fecha = fecha

    def mostrar(self):
        print(f"==============================")
        print(f"TÍTULO: {self.titulo}")
        print(f"Descripción: {self.descripcion}")
        print(f"Color: {self.color}")
        print(f"Fecha: {self.fecha}")
        print(f"==============================\n")

# ===============================
# Clase GestorNotas
# ===============================
class GestorNotas:
    def __init__(self):
        self.notas = []

    def crearNota(self, nota):
        self.notas.append(nota)

    def eliminarNota(self, titulo):
        for i, nota in enumerate(self.notas):
            if nota.titulo == titulo:
                del self.notas[i]
                print(f"Nota '{titulo}' eliminada.")
                return
        print(f"No se encontró la nota '{titulo}'.")

    def listarNotas(self):
        if not self.notas:
            print("No hay notas.")
            return
        for nota in self.notas:
            nota.mostrar()

# ===============================
# PRUEBA
# ===============================
gestor = GestorNotas()

nota1 = Nota("Comprar pan", "Ir a la panadería a comprar pan integral", "amarillo")
nota2 = Nota("Estudiar POO", "Repasar herencia y diccionarios", "verde")

gestor.crearNota(nota1)
gestor.crearNota(nota2)

gestor.listarNotas()

gestor.eliminarNota("Comprar pan")
gestor.listarNotas()


"""2"""
# ===============================
# Clase abstracta NotaBase
# ===============================
class NotaBase:
    def __init__(self, titulo, descripcion, fecha=None):
        self.titulo = titulo
        self.descripcion = descripcion
        if fecha is None:
            self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            self.fecha = fecha

    def mostrar(self):
        pass  # Se implementará en subclases

# ===============================
# Nota normal
# ===============================
class NotaNormal(NotaBase):
    COLORES_VALIDOS = ["amarillo", "verde", "blanco", "cyan"]

    def __init__(self, titulo, descripcion, color, fecha=None):
        super().__init__(titulo, descripcion, fecha)
        if color.lower() in NotaNormal.COLORES_VALIDOS:
            self.color = color.lower()
        else:
            self.color = "blanco"

    def mostrar(self):
        print(f"--- Nota Normal ---")
        print(f"TÍTULO: {self.titulo}")
        print(f"Descripción: {self.descripcion}")
        print(f"Color: {self.color}")
        print(f"Fecha: {self.fecha}\n")

# ===============================
# Nota urgente
# ===============================
class NotaUrgente(NotaBase):
    def __init__(self, titulo, descripcion, fecha=None):
        super().__init__(titulo, descripcion, fecha)
        self.color = "rojo"

    def mostrar(self):
        print(f"*** NOTA URGENTE ***")
        print(f"TÍTULO: {self.titulo}")
        print(f"Descripción: {self.descripcion}")
        print(f"Color: {self.color}")
        print(f"Fecha: {self.fecha}\n")

# ===============================
# Gestor de notas actualizado
# ===============================
class GestorNotas2:
    def __init__(self):
        self.notas = []

    def crearNota(self, nota):
        self.notas.append(nota)

    def eliminarNota(self, titulo):
        for i, nota in enumerate(self.notas):
            if nota.titulo == titulo:
                if isinstance(nota, NotaUrgente):
                    respuesta = input(f"Esta nota es urgente. ¿Seguro que quieres eliminarla? (s/n): ")
                    if respuesta.lower() != "s":
                        print("Eliminación cancelada.")
                        return
                del self.notas[i]
                print(f"Nota '{titulo}' eliminada.")
                return
        print(f"No se encontró la nota '{titulo}'.")

    def listarNotas(self):
        # Primero notas urgentes
        print("=== LISTADO DE NOTAS ===")
        for nota in self.notas:
            if isinstance(nota, NotaUrgente):
                nota.mostrar()
        for nota in self.notas:
            if isinstance(nota, NotaNormal):
                nota.mostrar()

# ===============================
# PRUEBA
# ===============================
gestor2 = GestorNotas2()

n1 = NotaNormal("Comprar pan", "Ir a la panadería a comprar pan integral", "amarillo")
n2 = NotaNormal("Estudiar POO", "Repasar herencia y diccionarios", "verde")
n3 = NotaUrgente("Pagar factura", "La factura vence hoy!")

gestor2.crearNota(n1)
gestor2.crearNota(n2)
gestor2.crearNota(n3)

gestor2.listarNotas()

# Eliminar una nota urgente
# gestor2.eliminarNota("Pagar factura")  # Descomentar para probar confirmación
