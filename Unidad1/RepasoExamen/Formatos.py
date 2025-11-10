# Ejercicio 1: Pide un sueldo por teclado y te lo muestra con 2 decimales
sueldo = float(input("Introduce un sueldo: "))
print(f"El sueldo es de: {sueldo:.2f}")

# Ejercicio 2: Mostrar un numero muy grande con separador de millas (,)
num = 1234567890
print(f"{num:,}")

# Ejercicio 3: Mostrar un numero con 5 "0" a la izquierda
num = 34
print(f"{num:0>7}")
print(f"{num:07d}")

# Ejercicio 4: Mostrar 3 notas con 3 "0" a la izquierda
nota1 = 7
nota2 = 4
nota3 = 5

print(f"{nota1:04d}")
print(f"{nota2:04d}")
print(f"{nota3:04d}")

# Ejercicio 5: Pide nombre por teclado y crea una ficha multilinea

nombre = input("Introduce un nombre: ")

print(
    f"""
    Ficha del alumno
    -----------
    Nombre = {nombre}
    """)

# Ejercicio 6: Usa condiciones dentro del f-String: Si el numero es par que muestre par y si es impar que muestre impar

num = int(input("Introduce un numero: "))
print(f"{"El numero es par" if num%2 == 0 else "El numero es impar"}")

# Ejercicio 7: Mostrar un numero 0.x con 3 decimales como porcentaje

num = float(input("Introduce un numero entre 0 y 1: "))
if 0 > num or num >= 1:
    print("Numero introducido no valido")
else:
    print(f"El porcentaje es: {num:.2%}")

# Ejercicio 8: Tienes una edad, muestrala justificada en centro, izquierda y derecha

edad = 19

print(f"Izquierda: {edad:<16}")
print(f"Centro   : {edad:^16}")
print(f"Derecha  : {edad:>16}")

# Ejercicio 9: Construye un f-String que imprima el valor de una lista usando {lista = } para ver su inspeccion tal y como tienes en el ejemplo
lista = [1,2,3,4,5,6,7,8,9,10]
print(f"{lista = }")

# Ejercicio 10: Haz una funcion que devuelva un nombre completo y usa esa funcion en un f-String

def funcion():
    return "Hola kevin"
print(f"{funcion() = }")

