nombre = "Jose María"
edad = 57
sueldo = 1200.567
print("Mi nombre es",nombre,"tengo",edad,"años y cobro",sueldo,"euros")

# Salida como printf:
print()
print("Mi nombre es %s tengo %d años y cobro %.2f euros" %(nombre, edad, sueldo))

# F-String:
print()
print(f"Mi nombre es {nombre} tengo {edad} años y cobro {sueldo:.2f} euros")

print()
promedio = 0.86754
print(f"El porcentaje de aprobados es de {promedio:.2%}")

print()
poblacion = 1234567890
print(f"La poblacion del pais es de {poblacion:,} habitantes")

print()
n1 = 23
n2 = 456
n3 = 1
lista  = [1, 2, 3]
print(f"Números: \n{n1:04d}\n{n2:04d}\n{n3:04d}")
print(f"Justificado a la izquierda: ***{n1:<20}***")
print(f"Justificado al centro     : ***{n1:^20}***")
print(f"Justificado a la derecha  : ***{n1:>20}***")

print()
print(f"Inspeccionando variables {n1=}, {n2=} y {lista=}")

print()
def devuelveMiNombre():
    return "Jose Maria"

print(f"Mi nombre es: {devuelveMiNombre()}")

print()
ficha = f"""
Ficha del profesor:
==========================
Nombre: {nombre}
Edad: {edad}
Sueldo: {sueldo:.2f} euros
==========================
"""
print(ficha)

# Se puede usar F mayuscula y no cambia nada:
print(f"¿n1 es par? {True if n1%2==0 else False}")
print(F"¿n2 es par? {'Sì' if n2%2==0 else 'No'}")


print()
nota = 7
print(f"Nota: {'Nota no reconocida' if nota > 10 or nota < 0 else 'Excelente' if nota > 8  else 'Notable' if (6 < nota < 9) else 'Bien' if (6 >= nota > 5) else 'Suficiente' if nota >= 5 else 'Suspenso'}")