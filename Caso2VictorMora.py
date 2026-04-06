# Caso2VictorApellido.py
# Proyecto: Gestión de inventario - Caso 2
# Autor: Victor Apellido
# Fecha: 2026-04-06
# Descripción: Programa para registrar productos, consultar inventario, realizar ventas y reabastecer.

# Variables globales
nombres = []          # arreglo unidimensional: lista de nombres de productos
inventario = []       # arreglo bidimensional: cada elemento [cantidad, precio]

def registrar_productos():
    """Permite ingresar uno o varios productos al inventario."""
    global nombres, inventario
    print("\n--- Registrar productos ---")
    while True:
        nombre = input("Ingrese nombre del producto: ").strip()
        if nombre == "":
            print("El nombre no puede estar vacío. Intente de nuevo.")
            continue

        # Leer cantidad
        while True:
            try:
                cantidad = int(input("Ingrese cantidad disponible (entero >= 0): "))
                if cantidad < 0:
                    print("La cantidad debe ser >= 0.")
                    continue
                break
            except ValueError:
                print("Entrada inválida. Ingrese un número entero.")

        # Leer precio
        while True:
            try:
                precio = float(input("Ingrese precio unitario (>= 0): "))
                if precio < 0:
                    print("El precio debe ser >= 0.")
                    continue
                break
            except ValueError:
                print("Entrada inválida. Ingrese un número (ej: 12.50).")

        nombres.append(nombre)
        inventario.append([cantidad, precio])
        print(f"Producto '{nombre}' registrado correctamente.")

        otro = input("¿Desea registrar otro producto? (s/n): ").strip().lower()
        if otro != 's':
            break

def consultar_inventario():
    """Muestra el inventario completo con índices, nombres, cantidades y precios."""
    print("\n--- Inventario ---")
    if not nombres:
        print("El inventario está vacío.")
        return
    print(f"{'Índice':<6} {'Producto':<20} {'Cantidad':<10} {'Precio':<10}")
    for i, nombre in enumerate(nombres):
        cantidad, precio = inventario[i]
        print(f"{i:<6} {nombre:<20} {cantidad:<10} ${precio:,.2f}")

def calcular_total_venta(indice, cantidad_vendida):
    """Calcula y retorna el total de la venta para un producto dado."""
    precio_unitario = inventario[indice][1]
    total = cantidad_vendida * precio_unitario
    return total

def realizar_venta():
    """Realiza la venta de un producto si hay stock suficiente y actualiza el inventario."""
    global inventario
    print("\n--- Realizar venta ---")
    if not nombres:
        print("No hay productos registrados.")
        return

    consultar_inventario()
    # Seleccionar índice
    while True:
        try:
            idx = int(input("Ingrese el índice del producto a vender: "))
            if idx < 0 or idx >= len(nombres):
                print("Índice fuera de rango. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

    # Cantidad a vender
    while True:
        try:
            cantidad_vender = int(input("Ingrese la cantidad a vender: "))
            if cantidad_vender <= 0:
                print("La cantidad debe ser mayor que 0.")
                continue
            if cantidad_vender > inventario[idx][0]:
                print(f"Stock insuficiente. Stock disponible: {inventario[idx][0]}")
                return
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

    total = calcular_total_venta(idx, cantidad_vender)
    # Actualizar inventario
    inventario[idx][0] -= cantidad_vender
    print(f"Venta realizada: {cantidad_vender} x {nombres[idx]} a ${inventario[idx][1]:,.2f} c/u")
    print(f"Total a pagar: ${total:,.2f}")

def reabastecer_inventario():
    """Añade stock a un producto existente."""
    global inventario
    print("\n--- Reabastecer inventario ---")
    if not nombres:
        print("No hay productos registrados.")
        return

    consultar_inventario()
    # Seleccionar índice
    while True:
        try:
            idx = int(input("Ingrese el índice del producto a reabastecer: "))
            if idx < 0 or idx >= len(nombres):
                print("Índice fuera de rango. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

    # Cantidad a añadir
    while True:
        try:
            cantidad_anadir = int(input("Ingrese la cantidad a añadir (entero > 0): "))
            if cantidad_anadir <= 0:
                print("La cantidad debe ser mayor que 0.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

    inventario[idx][0] += cantidad_anadir
    print(f"Se añadieron {cantidad_anadir} unidades a '{nombres[idx]}'. Nuevo stock: {inventario[idx][0]}")

def mostrar_menu():
    print("\n==============================")
    print(" Gestión de Inventario - Tienda Deportiva")
    print("==============================")
    print("1. Registrar productos")
    print("2. Consultar inventario")
    print("3. Realizar ventas")
    print("4. Reabastecer inventario")
    print("5. Salir")
    print("==============================")

def main():
    """Bucle principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()
        if opcion == '1':
            registrar_productos()
        elif opcion == '2':
            consultar_inventario()
        elif opcion == '3':
            realizar_venta()
        elif opcion == '4':
            reabastecer_inventario()
        elif opcion == '5':
            print("\nGracias por usar el sistema de inventario. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor seleccione una opción entre 1 y 5.")

