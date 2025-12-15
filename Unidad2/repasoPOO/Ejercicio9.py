# Crea una clase Motor con:
# Atributo potencia
# Crea una clase Vehiculo que tenga:
# marca
# motor (objeto de tipo Motor)
# Métodos:
# __str__() →
# Marca: <marca>, Potencia: <potencia> CV
#
# Luego crea una clase Coche que:
# Herede de Vehiculo
# Añada puertas
# Sobrescriba __str__() para mostrar también las puertas
# Desde el programa principal:
# Crea varios motores
# Crea varios coches con distintos motores
# Imprime los coches
# 👉 OJO: aquí no hay herencia entre Motor y Vehiculo, es composición (muy preguntado en examen).

class Motor():
    def __init__(self, potencia):
        self.__potencia = potencia

    @property
    def potencia(self):
        return self.__potencia

    @potencia.setter
    def potencia(self, nuevaPotencia):
        self.__potencia = nuevaPotencia

class Vehiculo():
    def __init__(self, marca, motor):
        self.__marca = marca
        self.__motor = motor

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, nuevaMarca):
        self.__marca = nuevaMarca

    @property
    def motor(self):
        return self.__motor

    @motor.setter
    def motor(self, nuevoMotor):
        self.__motor = nuevoMotor

    def __str__(self):
        return f"Marca: {self.marca} | Potencia: {self.motor.potencia} CV"

class Coche(Vehiculo):
    def __init__(self, marca, motor, puertas):
        super().__init__(marca, motor)
        self.__puertas = puertas

    @property
    def puertas(self):
        return self.__puertas

    @puertas.setter
    def puertas(self, nuevoPuertas):
        self.__puertas = nuevoPuertas

    def __str__(self):
        return f"Marca: {self.marca} | Potencia: {self.motor.potencia} CV | Puertas: {self.puertas}"

motor1 = Motor(100)
motor2 = Motor(300)
motor3 = Motor(700)

coche1 = Coche("Toyota", motor1, 5)
coche2 = Coche("Cupra", motor2, 5)
coche3 = Coche("Ferrari", motor3, 2)

listaCoches = [coche1, coche2, coche3]

for coche in listaCoches:
    print(coche)