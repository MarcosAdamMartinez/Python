# Crea una clase Pedido con:
# Atributos:
# numero
# estado → puede ser: "pendiente", "enviado", "entregado"
# Reglas:
# Un pedido empieza siempre en "pendiente"
# Solo se puede pasar:
# de "pendiente" a "enviado"
# de "enviado" a "entregado"
# Cualquier otro cambio debe lanzar una excepción
# Métodos:
# enviar()
# entregar()
# __str__()
# Desde el programa principal:
# Crea un pedido
# Intenta entregarlo directamente (debe fallar)
# Envíalo
# Entrégalo
# Muestra el pedido final
# 👉 Esto es DAM 2 puro y duro (control de estado + excepciones).

class Pedido():
    def  __init__(self, numero):
        self.__numero = numero
        self.estado = "Pendiente"

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    def enviar(self):
        try:
            if self.estado == "Pendiente":
                self.estado = "Enviado"
            else:
                raise Exception("El estado no es Pendiente")
        except Exception as e:
            print(e)

    def entregar(self):
        try:
            if self.estado == "Enviado":
                self.estado = "Entregado"
            else:
                raise Exception("El pedido no se puede entregar porque no ha sido enviado")
        except Exception as e:
            print(e)

    def __str__(self):
        return f"Numero: {self.numero} | Estado: {self.estado}"

pedido = Pedido(1)

pedido.entregar()
pedido.enviar()
pedido.entregar()

print(pedido)

