d1 = {}
d2 = dict()
d3 = { "Nombre":"Sara", "Edad" : 57, "Solterx":True, "Edad" : 33 }
d4 = dict(Primero = 'Uno', Tercero = 'Tres', Edad = 44)
d4["Segundo"] = "Dos"

# Metodos que devuelven: Claves, Valores, Conjuntos de clave - valor:
print(d3)
print(d3.keys())
print(d3.values())
print(d3.items())

# Devuelve valor auxiliar si no se encuentra el pedido:
print(d3.get("Titulo", False))

# Devuelve el valor escogidoy lo elimina:
print(d3.pop("Edad"))

# Elimina el ultimo valor insertado, su clave y devuelve en forma de tupla su clave - valor:
print(d3.popitem())
print(d3)

# Si hay algun elemento en d4 que no tenga d3 lo añade a d3, si estan duplicados, los ignora:
d3.update(d4)
print(d3)