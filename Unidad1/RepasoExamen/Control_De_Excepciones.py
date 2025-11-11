# Ejercicio 1: Pide dos números y divide el primero entre el segundo
# Maneja ValueError y ZeroDivisionError

try:
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    print(num1/num2)
except ValueError:
    print("Algo de lo que has metido ta mal manin")
except ZeroDivisionError:
    print("Dime donde te enseñaron a dividir para no ir bro")


# Ejercicio 2: Pide la edad de una persona y conviértela a entero
# Si no es un número, lanza ValueError
# Si la edad es menor que 0, lanza Exception personalizada

try:
    edad = int(input("Introduce una edad:"))
    if edad < 0:
        # raise Exception("Eres un negrata")  # Si lo dejo asi y sin ningun except sale el mensaje de error rojo
        raise Exception("hola") # Si lo dejas asi y le metes un except personalizas mejor
    elif edad > 10:
        raise Exception("adios")
except ValueError as nigga:
    print("Algo de lo que has metido ta mal manin 2")
except Exception as e:
    if str(e) == "hola":
        print("Eres un negrata")
    elif str(e) == "adios":
        print("No eres un negrata")



# Ejercicio 3: Pide una lista de números separados por comas
# Convierte cada elemento a entero
# Usa try/except para manejar valores que no sean números

try:
    lista = input("Pasame una lista de numeros separados por \",\": ")
    lista.replace(" ","")
    nums = lista.split(",")
    numeros = list()
    for num in nums:
        numeros.append(int(num))
    print(numeros)
except ValueError:
    print("Tu ta loooco")

# Ejercicio 4: Crea una lista con 5 elementos
# Pide al usuario un índice y muestra el elemento
# Captura IndexError si el índice no existe

lista = [1,2,3,4,5,6,7,8]
try:
    indice = int(input("Introduce un indice para buscar en la lista (Empezando por 0): "))
    print(lista[indice])
except ValueError:
    print("Tu ta locoo x2")
except IndexError:
    print("Me cago en tus muelas, no se puede buscar algo que no existe")


# Ejercicio 5: Pide dos números y suma
# Si alguno no es número, lanza ValueError
# Usa else para imprimir el resultado si no hubo excepción

try:
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
except ValueError:
    print("Tu ta loooco x3")
else:
    print("El resultado de sumar",num1,"con",num2,"es:",num1+num2)



# Ejercicio 6: Pide un número entre 1 y 10
# si está fuera de rango
# lanza un ValueError con tu propio mensaje personalizado
try:
    num = int(input("Introduce un numero entre 1-10: "))
    if 1 > num < 10:
        raise ValueError("Tas cagao bro")
except ValueError:
    print("Miau")
else:
    print("Ta bien👍")


# Ejercicio 7: Haz un programa que convierta un input a float
# si meten algo que no se pueda convertir → ValueError
# en el else imprime “el número es flotante”

try:
    numDec = float(input("Introduce un numero decimal: "))
except ValueError:
    print("Quevedo con el Linton maai")
else:
    print("El numero decimal es:",numDec)


# Ejercicio 8: Haz una función dividir(a, b) que internamente tenga el try/except
# y que si algo falla, levante una tuya:
# raise Exception("operación no válida")
# y llámala desde main 2 veces:
# una vez que funcione y otra que falle

def funcion(a, b):
    try:
        print("Funcion: ")
        if b == 0:
            raise Exception("0")
        elif b < 0:
            raise Exception("si")
        else:
            print(a / b)

    except Exception as e:
        if str(e) == "0":
            print("Chupalo")
        elif str(e) == "si":
            print("Mamame el webo")
funcion(10,2)
funcion(1,0)
funcion(1,-1)

# Ejercicio 9: Pide un denominador y divide 100/denominador
# si es 0 captura ZeroDivisionError
# y en finally imprime “cerrando operación”

try:
    deno = int(input("Introduce un denominador: "))
    print(100 / deno)
except ValueError:
    print("Tu ta looooco x4")
except ZeroDivisionError:
    print("Si tu novio te deja soola 😈")
finally:
    print("Cerrando operación")

# Ejercicio 10: Pide una palabra
# Si la palabra es "Python", lanza Exception con mensaje "Palabra prohibida"
# Captura la excepción y muestra un mensaje personalizado

palabraProhibida = input("Introduce una palabra para banearla: ")
if len(palabraProhibida.split(" ")) == 1 :
    try:
        frase = input("Introduce una frase: ")
        listaPalabras = frase.split(" ")
        fraseRecon = ""
        incorrecto = False

        if  listaPalabras.count(palabraProhibida) != 0:
            for palabra in listaPalabras:
                if palabra != palabraProhibida:
                    fraseRecon += palabra+" "
                    for c in fraseRecon:
                        if c in ["'","[","]",","]:
                            fraseRecon = fraseRecon.replace(c,"")
                else:
                    fraseRecon = fraseRecon + "\""+palabra+"\" "
                    incorrecto = True

            if incorrecto:
                listaPalabras2 = fraseRecon.split(" ")
                listaPalabras2.insert(0,"Frase incorrecta: ")
                fraseRecon2 = str(listaPalabras2)
                for c in [",","'","[","]"]:
                    fraseRecon2 = fraseRecon2.replace(c, "")
                print(fraseRecon2)
                raise Exception()

        else:
            print("Frase correcta:",frase)
    except Exception:
        print("Ayer me besaste y no podias parar 😘💕")
else:
    print("Has introducido mas de una palabra a banear")
