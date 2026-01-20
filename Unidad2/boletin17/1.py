try:
    nombre = input("Introduce el nombre del primer fichero: ")
    nombre2 = input("Introduce el nombre del segundo fichero: ")

    fichero = open("ficheros/" + nombre, 'r+')
    fichero2 = open("ficheros/" + nombre2, 'r+')

    contenido = fichero.read()
    contenido2 = fichero2.read()

    if contenido == contenido2:
        print("El primer fichero es igual al segundo fichero.")
    else:
        print("El segundo fichero no es igual al primer fichero.")

    fichero.close()
    fichero2.close()
except Exception as excepcion:
    print(excepcion)