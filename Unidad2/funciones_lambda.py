def cuadrado(x): return x**2
print(cuadrado(5))

cuadradoLambda = lambda x: x**2
print(cuadradoLambda(2))

elevarLambda = lambda x, y: x**y
print(elevarLambda(2,6))

media = lambda *lista: sum(lista)/len(lista)
print(media(10,9,8))

cuadradoMayorQue10 = lambda x: True if x**2 > 10 else False

print(cuadradoMayorQue10(10))