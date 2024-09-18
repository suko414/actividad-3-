# Primero, creamos un archivo y escribimos algunas notas
with open('notas.txt', 'w') as file:
    file.write("Nota 1: Comprar leche\n")
    file.write("Nota 2: Terminar el proyecto\n")

# Ahora, vamos a añadir una nueva nota al final del archivo
with open('notas.txt', 'a') as file:
    file.write("Nota 3: Ir al gimnasio\n")

# Creamos una lista de nombres
nombres = ["Juan", "Ana", "Luis", "Maria"]

#Archivo para escribir los nombres
with open('nombres.txt', 'w') as file:
    for nombre in nombres:
        file.write(nombre + '\n') 
        import csv  

# Creamos una lista de diccionarios con productos
productos = [
    {"nombre": "Manzana", "precio": 0.5, "cantidad": 10},
    {"nombre": "Banana", "precio": 0.3, "cantidad": 20},
    {"nombre": "Naranja", "precio": 0.8, "cantidad": 15},
]

# Abrimos un archivo CSV para escribir
with open('productos.csv', 'w', newline='') as csvfile:
    fieldnames = ['nombre', 'precio', 'cantidad']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader() 
    for producto in productos:
        writer.writerow(producto)  

try:
    # Intentamos abrir un archivo para escribir
    with open('archivo_de_prueba.txt', 'w') as file:
        file.write("Este es un texto de prueba.\n")
except IOError as e:
    print(f"Ocurrió un error al intentar escribir en el archivo: {e}")
