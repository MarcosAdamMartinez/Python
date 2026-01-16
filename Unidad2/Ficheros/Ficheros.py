"""try:
    fichero = open("ElPozoDeLaAscension.txt", "rt")
    linea = fichero.readline(5) #lee de 5 en 5 caracteres
    while linea != "":
        print(linea)
        linea = fichero.readline(5)
    fichero.close()
except:
    print("El fichero no existe")"""

try:
    fichero = open("ElPozoDeLaAscension.txt", "wt")
    fichero.write("Escribo estas palabras \n")
    fichero.write("en acero porque todo lo \n")
    fichero.write("que no esté grabado en metal \n")
    fichero.write("es indigno de confianza. \n")
    fichero.close()
except:
    print("El fichero no existe")

try:
    fichero = open("ElPozoDeLaAscension.txt", "at")
    nuevaLinea = "Siempre hay otro secreto.\n"
    fichero.write(nuevaLinea)
    fichero.close()
except:
    print("El fichero no existe")

try:
    with open("ElPozoDeLaAscension.txt", "at") as fichero:
        fichero.write("Mientras me tenga en pie esta guerra no habrá acabado.\n")
        fichero.write("No confundas mi silencio con falta de duelo, llora a tu manera que yo lo haré a la mía.\n")
        fichero.close()
except:
    print("El fichero no existe")


