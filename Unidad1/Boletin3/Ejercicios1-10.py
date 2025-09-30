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
