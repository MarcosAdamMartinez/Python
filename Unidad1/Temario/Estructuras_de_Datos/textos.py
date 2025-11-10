texto = "Hola mundo"

#Longitud del texto:
print(len(texto))

# for c in texto:
#     print(c)

# for i in range(0,len(texto)):
#     #Posicion de cada caracter:
#     print(i,"-",texto[i])

#Posicion 3 a 8
print(texto[3:8])

#Devuelve hasta 8
print(texto[:8])

#Devuelve desde 3
print(texto[3:])

#Devuelve numeros pares
print(texto[1::2])

#Dar la vuelta al texto
print(texto[::-1])

#COnvertir numero a cadena(String):
cadenaNumerica = str(3456.5)
print(cadenaNumerica)

#CONVERIR MAYUSCULAS, MINUSCULAS O INTERCAMBIARLAS:
print(texto.upper())
print(texto.lower())
print(texto.swapcase())

#Devuelve la primera posicion en la que aparece la letra (si no aparece -1):
print(texto.find("o"))
print(texto[2:].find("o"))

#Devuelve el numero de veces que aparece:
print(texto.count("o"))

#Sustituye el primer valor por el segundo:
print(texto.replace("o","x"))

#Sustituye solo el numero de veces que aparezca en el count:
print(texto.replace("o","x",1))

