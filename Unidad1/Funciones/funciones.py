def mifuncion():
    otroTexto = "Hola mundo cruel"
    texto = "Hola otra vez mundo"
    print("Desde dentro de la funcion:",texto)
    return otroTexto


texto = "Hola Mundo"
print("Desde fuera de la funcion:",texto)
print("Valor devuelto:",mifuncion())

print("\n\n\n")

def mifuncion2(texto, veces):
    print(texto)
    for i in range (1,veces):
        print(texto)
    otroTexto = "Hola otra vez mundo cruel"
    print(otroTexto)

otroTexto = "Hola mundo cruel"
mifuncion2("Hola mundo",3)

def mifuncion3(t, l, n):
    t = "Hola mundo cruel"
    n = 4.4
    l[0]= 111
    l.append(1)
    l.sort()

texto = "Hola mundo"
numero = 5.5
lista = [1,5,2,4,3]
mifuncion3(texto, lista, numero)
print(texto, "-", numero, "-", lista)


