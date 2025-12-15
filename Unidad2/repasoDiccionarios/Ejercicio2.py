# Crea un diccionario llamado notas con los siguientes alumnos y sus notas:
# "Ana": 8
# "Luis": 6
# "Marta": 9
# Luego:
# Imprime la nota de "Luis"
# Cambia la nota de "Ana" a 10
# Imprime todas las notas en formato:
# Alumno: <nombre>, Nota: <nota>

notas = {
    "Ana": 8,
    "Luis": 6,
    "Marta": 9
}

print(notas["Luis"])

notas["Ana"] = 10

for nota in notas:
    print(f"Nombre: {nota} | Nota: {notas[nota]}")