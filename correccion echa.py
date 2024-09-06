numero = 10
mensaje = "Bienvenido al sistema de cálculo"
resultado = 0

valores = [2, 4, 6, 8, 10]

print(mensaje)  #corregi mensaj era mensaje

def cuadrado(n):
    return n**2

i = 0
while i < len(valores): #corregido: valore era valores
    valor_cuadrado = cuadrado(valores[i])  # Error corregido: "valor" debía ser "valores"
    print("El cuadrado de", valores[i], "es", valor_cuadrado)
    i += 1

if numero % 2 == 0:  #corregi = debía ser ==
    print("El número es par")
elif numero % 2 == 1:
    print("El número es impar")
else:
    print("Este caso no debería ocurrir")

suma = 0
for numero in valores:
    suma += numero
    if suma > 20:
        print("La suma ha superado 20")
        break
    else:

nueva_lista = [5, 7, 9, 11]
for x in nueva_lista:  #corregido lista_nueva debía ser nueva_lista
    print("Valor en nueva lista:", x)

numeros = [10, 20, 30, 40, 50]
total = 0
for n in numeros:
    total += n
promedio = total / len(numeros)
print("El promedio es", promedio)  #corregido promdio era promedio

contador = 0
while contador < 5:
    print("El contador es", contador)
    contador += 1
    if contador == 5:
        break
    else:
        print("Contador aún no ha llegado a 5")

edad = 20
if edad < 18:
    print("Eres menor de edad")
elif edad > 18:
    print("Eres mayor de edad")
else:
    print("Tienes exactamente 18 años")

def suma_numeros(a, b):  #corregido faltaba el segundo parámetro (b)
    return a + b

resultado_suma = suma_numeros(10, 5)  #corregi faltaba el segundo argumento en la llamada a la función
print("El resultado de la suma es", resultado_suma)

for i in range(10, 5):  #corregi range(10, 5) no generará ningún valor
    print("Valor de i:", i)

animales = ["gato", "perro", "conejo"]
if "tigre" in animales:  #corregi animal debía ser animales
    print("El tigre está en la lista")
else:
    print("El tigre no está en la lista")

try:
    print(animales[3])  # El índice 3 está fuera de rango pero el bloque try-except corregira el error
except IndexError:
    print("Error: índice fuera de rango")

contador2 = 10
while contador2 > 0:
    print("Contador2:", contador2)
    contador2 -= 2
    if contador2 == 5:
        print("Contador2 es igual a 5")
        continue
    else:
        print("Contador2 no es igual a 5")

def verificar_numero_en_lista(num, lista):
    if num in lista:
        return True
    else:
        return False  #corregi Falso era False

resultado_verificacion = verificar_numero_en_lista(10, numeros)
print("El número está en la lista:", resultado_verificacion)

duplicados = [1, 2, 2, 3, 4, 4, 5]
sin_duplicados = list(set(duplicados))
print("Lista sin duplicados:", sin_duplicados)  #corregi sin_duplicado debe ser "sin_duplicados"

texto = "Hola Mundo"
if len(texto) > 5:  #corregi "text" era texto
    print("El texto tiene más de 5 caracteres")
else:
    print("El texto tiene 5 o menos caracteres")

diccionario = {"nombre": "Carlos", "edad": 25}
for clave in diccionario:  # corregi "diccionarios" era diccionario porque solo es un diccionario
    print("Clave:", clave, "Valor:", diccionario[clave])

j = 0
while j < 10:
    if j == 5:
        print("Se alcanzó el valor de 5")
        break  #corregi "brake" era break
    else:
        j += 1
        continue  #corregi el "continúe" era continue no debe usar asentos

