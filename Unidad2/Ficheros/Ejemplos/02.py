try:
    # fichero = open("quijote.txt",'r')
    # print("Posicion:",fichero.tell())
    # print(fichero.readline())
    # print("Posicion:", fichero.tell())
    # print(fichero.readline())
    # fichero.seek(0, 2)
    # print("Posicion:", fichero.tell())
    # print(fichero.readline())
    # fichero.close()

    # fichero = open("quijote.txt",'a+')
    # fichero.write("\nNueva linea")
    # fichero.seek(0)
    # print(fichero.read())

    fichero = open("quijote.txt", 'r+')
    fichero.seek(0)
    fichero.write("\nNueva linea Mancha ")
    print(fichero.tell())
    fichero.seek(0,2)
    fichero.write("\n123")
    fichero.seek(0,0)
    print(fichero.read())

except:
    print("El fichero no existe")