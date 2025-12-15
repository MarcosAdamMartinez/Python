# Crea un diccionario llamado estudiantes con:
# {
#     "Ana": [8, 9, 7],
#     "Luis": [6, 7, 8],
#     "Marta": [9, 10, 10]
# }
# Luego:
# Calcula la media de cada estudiante
# Crea un nuevo diccionario llamado medias donde la clave sea el nombre y el valor sea la media
# Imprime todas las medias en formato:
# Alumno: <nombre>, Media: <media>


estudiantes = {
    "Ana": [8, 9, 7],
    "Luis": [6, 7, 8],
    "Marta": [9, 10, 10]
}

medias = {
    nombre: round(sum(notas)/len(notas),1) for nombre, notas in estudiantes.items()
}

# mediaAna = round(sum(estudiantes["Ana"])/len(estudiantes["Ana"]),1)
# mediaLuis = round(sum(estudiantes["Luis"])/len(estudiantes["Luis"]),1)
# mediaMarta = round(sum(estudiantes["Marta"])/len(estudiantes["Marta"]),1)

# medias = {
#     "Ana": mediaAna,
#     "Luis": mediaLuis,
#     "Marta": mediaMarta
# }

for media in medias:
    print(f"Nombre: {media} | Media: {medias[media]}")






