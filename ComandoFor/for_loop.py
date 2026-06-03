print("--- GENERADOR DE TABLAS DE MULTIPLICAR ---\n")

# Ingreso de datos esenciales vía teclado
numero = int(input("¿De qué número desea generar la tabla?: "))
limite = int(input("¿Hasta qué número desea multiplicar? (Ej. 12, 15, 20): "))

print(f"\nGenerando la tabla del {numero} hasta el {limite}:")
print("-" * 30)

# El bucle FOR utiliza el límite ingresado por el usuario (+1 para incluirlo)
for i in range(1, limite + 1):
    resultado = numero * i
    print(f" -> {numero} x {i} = {resultado}")

print("-" * 30)
print("Proceso de iteración finalizado con éxito.")
