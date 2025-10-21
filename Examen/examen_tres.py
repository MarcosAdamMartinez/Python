texto = input("Escribe un texto: ")
contadorVoc = 0
contadorEsp = 0

for c in texto:
    if c in ["a","A","e","E","i","I","o","O","u","U"]:
        contadorVoc += 1
for c in texto:
    if c == " ":
        contadorEsp += 1

texto = texto.replace("a","")
texto = texto.replace("A","")
texto = texto.replace("e","")
texto = texto.replace("E","")
texto = texto.replace("i","")
texto = texto.replace("I","")
texto = texto.replace("o","")
texto = texto.replace("O","")
texto = texto.replace("u","")
texto = texto.replace("U","")
texto = texto.replace(" ","")
print("Sin vocales ni espacios:",texto)
print("Vocales suprimidas:",contadorVoc)
print("Espacios suprimidos:",contadorEsp)

