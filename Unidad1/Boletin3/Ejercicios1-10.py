#1. Escribir un programa que pida una contraseña por teclado (dos veces) y si no coinciden
#nos lo vuelva a pedir hasta que lo hagan
# contraseña = input("Introduce la contraseña:\n")
# confContra = input("Introduce la contraseña de nuevo:\n")
#
# while  not (contraseña == confContra):
#     print("Inicio de sesion incorrecto\n\n")
#     contraseña = input("Introduce la contraseña:\n")
#     confContra = input("Introduce la contraseña de nuevo:\n")
# print("Incio de sesion correcto")

#2. Modifica el programa anterior para que cuando coincidan ambas contraseñas nos
# informe del número de intentos inválidos

# contraseña = input("Introduce la contraseña:\n")
# confContra = input("Introduce la contraseña de nuevo:\n")
# cont = 0
#
# while  not (contraseña == confContra):
#     print("Inicio de sesion incorrecto\n\n")
#     contraseña = input("Introduce la contraseña:\n")
#     confContra = input("Introduce la contraseña de nuevo:\n")
#     cont = cont + 1
# print("Incio de sesion correcto, numero de intentos fallidos: ",cont)

#3. Escribir un programa que nos pida nuestro nombre y apellidos (dos peticiones diferentes
# hechas en ese orden) y nos lo escriba formateado de la siguiente forma:
# nombre = input("Introduce tu nombre: ")
# apellidos = input("Introduce tus apelidos: ")
#
# print(apellidos+", "+nombre)

#4. Escribir un programa que pida por teclado una cadena de texto y la escriba en sin
# espacios en blanco (si los hubiera). Además, nos debe de decir el número de espacios
# que ha encontrado y suprimido.
# texto = input("Introduce un texto: ")
# cont = 0
#
# for c in texto:
#     if (c == " "):
#         cont += 1
# print(texto.replace(" ",""),cont)

#5. Escribir un programa que pida por teclado una cadena de texto y la imprima escrita al
# reves (es decir, si el usuario escribe Hola Mundo el programa debería de escribir odnuM
# aloH)

# texto = input("Introduce un texto: ")
# textoReversa = ""
#
# for i in range(len(texto),0,-1):
#     textoReversa = textoReversa + texto[i-1]
# print(textoReversa)


#10. Validar DNI
# dni = input("Introduce un dni:")
# while len(dni) != 10:
#     dni = input("Introduce un dni valido:")
# if (dni[0:9].isdigit() and dni[9:].isalpha()):
#     print("El dni es valido")
# else:
#     print("El dni no es valido")



#11. Validar NIE Y DNI
# doc = input("Introduce un dni o nie:")
# while len(doc) != 10:
#     doc = input("Introduce un dni o nie valido:")
#
# if doc[0:9].isdigit() and doc[9:].isalpha():
#     print("El dni es valido")
# elif doc[0:1].isalpha() and doc[1:9].isdigit() and doc[9:].isalpha():
#     letra = doc[0:1]
#     if letra.upper() == "X" or letra.upper() == "Y" or letra.upper() == "Z":
#         print("El nie es valido")
#     else:
#         print("El nie no es valido")
# else:
#     print("El dni no es valido")

#12. Validar matricula
matr = input("Introduce una matricula:")
while len(matr) != 7:
    matr = input("Introduce una matricula valido:")
if matr[0:4].isdigit() and matr[4:].isalpha():
    letras = matr[4:]
    if "A" "E" "I" "O" "U" "Q" "Ñ" in letras.upper():
        print("La matricula no es valida")
    else:
        print("La matricula es valida")
else:
    print("La matricula no es valida")