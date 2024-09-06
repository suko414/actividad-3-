def crear_tabla_pitagoras(n):
    tabla = [[(i+1) * (j+1) for j in range(n)] for i in range(n)]
    return tabla
def mostrar_tabla(tabla):
    for fila in tabla:
        for valor in fila:
            print(f"{valor:3}", end=" ")
        print()  
def multiplicar(tabla, num1, num2):
    return tabla[num1-1][num2-1]
def main():
    tabla = crear_tabla_pitagoras(10)
    print("Tabla de Pitágoras:")
    mostrar_tabla(tabla)
    num1 = int(input("Ingresa el primer número (1-10): "))
    num2 = int(input("Ingresa el segundo número (1-10): "))
    if 1 <= num1 <= 10 and 1 <= num2 <= 10:
        resultado = multiplicar(tabla, num1, num2)
        print(f"\nEl resultado de multiplicar {num1} x {num2} es: {resultado}")
    else:
        print("Por favor, ingresa números dentro del rango 1-10.")
if __name__ == "__main__":
    main()