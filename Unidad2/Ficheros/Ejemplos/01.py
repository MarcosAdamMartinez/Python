try:
    fichero = open("tlf.txt", "r")
    linea = fichero.readlines()
    while linea != "-":
        if len(linea) <= 9:
            print(linea)
    fichero.close()
except:
    print("El fichero no existe")