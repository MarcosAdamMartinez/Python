# Crea un diccionario llamado inventario que contenga productos y sus cantidades:
# "manzanas": 10
# "naranjas": 5
# "peras": 8
# Luego:
# Añade "plátanos" con cantidad 12
# Reduce "manzanas" en 3
# Muestra todos los productos con su cantidad en formato:
# Producto: <producto>, Cantidad: <cantidad>

inventario = {
    'manzanas': 10,
    'naranjas': 5,
    'peras': 8
}

inventario['platanos'] = 12

inventario['manzanas'] -= 3

for producto in inventario:
    print(f"Producto: {producto} | Cantidad: {inventario[producto]}")