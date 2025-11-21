import random

d1 = dict(Sara = 33, Pepe = 55, Luis = 44, Manolo = 33, Eva = 22, Ines = 66)

print(d1)

def eliminaAzar(d1):
    # El metodo copy nos permite crear una copia de los valores, no de la referencia, asi podemos modificar tranquilamente:
    d2 = d1.copy()
    # lista = list()
    lista = list(d1.keys())
    # for clave in d2.keys():
    #     lista.append(clave)
    d2.pop(random.choice(lista))
    return d2

# Los diccionarios se pasan por referencia, si haces cambios en variables cuyo valor lleve a la direccion, se cambia la referencia:
print(eliminaAzar(d1))
print(d1)

texto = str(d1)
print("En texto:",texto)

# Metodo que devuelve el valor de una clave del diccionario: Si existe, no lo modifica y te muestra el valor, si no existe
# lo añade y te devuelve el valor nuevo:
print(d1.setdefault("Pepe"))
print(d1)
print(d1.setdefault("Antonio", 44))
print(d1)