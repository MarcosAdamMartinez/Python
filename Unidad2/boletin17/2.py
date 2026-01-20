
def contarPersonas():
    try:
        fichero = open("ficheros/estadisticas.txt", 'r+')

        sigue = True
        contadorAltura = 0
        contadorHombres = 0
        contadorMujeres = 0

        fichero.seek(0)

        while sigue:
            linea = fichero.readline()
            linea = linea.replace("\n", "")
            if linea == "Mujer":
                contadorMujeres = contadorMujeres + 1
            elif linea == "Hombre":
                contadorHombres = contadorHombres + 1
            elif linea == "":
                sigue = False
            else:
                contadorAltura += float(linea)

        print(f"Hombres: {contadorHombres}.\nMujeres: {contadorMujeres}.\nAltura media: {contadorAltura/(contadorHombres + contadorMujeres):.2f}.")

        fichero.close()

    except:
        print("Error al ejecutar.")

contarPersonas()