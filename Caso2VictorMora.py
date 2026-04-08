# Proyecto: Gestión de inventario - Caso 2

# Descripción: Programa para registrar productos, consultar inventario, realizar ventas y reabastecer.

# Variables globales
nombres:list[str] = []           # arreglo unidimensional: lista de nombres de productos
inventario:list[list[int|float]] = []       # arreglo bidimensional: cada elemento [cantidad, precio]

def registrar_productos():
    global nombre, inventario
    """Permite ingresar uno o varios productos al inventario"""
    print("\n--- Registrar productos ---")
    while True:
        nombre = input("Ingrese nombre del producto" + "\n------------- ")
        if nombre == "":
            print("El nombre no puede estar vacío. Intente de nuevo.")
            continue # Continua hasta que se coloque el nombre bien
        while True: # Leer cantidad
            cantidad = int(input("Ingrese cantidad disponible (entero >= 0)" + "\n------------- "))
            if cantidad < 0:
                print("La cantidad debe ser >= 0.\n")
                continue # Vuelve a iniciar este bucle
            elif cantidad > 0:
                print("Cantidad guardada\n")
                break
        while True: # Leer precio
            precio = float(input("Ingrese precio unitario (>= 0)"  + "\n------------- "))
            if precio < 0:
                print("El precio debe ser >= 0.")
                continue
            else: break
        nombres.append(nombre)
        inventario.append([cantidad, precio])
        print(f"Producto '{nombre}' registrado correctamente.")
        break   

def consultar_inventario():
    """Muestra el inventario completo con índices, nombres, cantidades y precios"""
    print("\n--- Inventario ---")
    if not nombres:
        print("El inventario está vacío\n")
        return
    print(f"{'Índice':<6} {'Producto':<20} {'Cantidad':<10} {'Precio':<10}") # Se realiza un pequeño espaciado para que los datos se puedan mostrar de mejor forma
    for i, nombre in enumerate(nombres):
        cantidad, precio = inventario[i]
        print(f"{i:<6} {nombre:<20} {cantidad:<10} ${precio:,.2f}") # Se utiliza el precio en dolares y se redondea a 2 decimales

def realizar_venta():
    """Realiza la venta de un producto si hay stock suficiente y actualiza el inventario."""
    global inventario
    print("\n--- Realizar venta ---")
    if not nombres:
        print("No hay productos registrados.")
        return

    consultar_inventario() # Seleccionar índice
    while True:
        
        idx = int(input("Ingrese el índice del producto a vender: "))
        if idx < 0 or idx >= len(nombres):
            print("Índice fuera de rango. Intente de nuevo.")
            continue
        else: break
    while True: # Cantidad a vender
        
        cantidad_vender = int(input("Ingrese la cantidad a vender: "))
        if cantidad_vender <= 0:
            print("La cantidad debe ser mayor que 0.")
            continue
        if cantidad_vender > inventario[idx][0]:
            print(f"Stock insuficiente. Stock disponible: {inventario[idx][0]}")
            return
        else: break
        
    total = calcular_total_venta(idx, cantidad_vender)
    inventario[idx][0] -= cantidad_vender # Actualizar inventario con el indice correspondiente
    print(f"Venta realizada: {cantidad_vender} x {nombres[idx]} a ${inventario[idx][1]:,.2f} c/u") # Redondea?
    print(f"Total a pagar: ${total:,.2f}")

def calcular_total_venta(indice:int, cantidad_vendida:int):
    """Calcula y retorna el total de la venta para un producto dado"""
    precio_unitario = inventario[indice][1]
    total = cantidad_vendida * precio_unitario
    return total

def reabastecer_inventario():
    """Añade stock a un producto existente"""
    global inventario
    print("\n--- Reabastecer inventario ---")
    if not nombres:
        print("No hay productos registrados.")
        return

    consultar_inventario() # Seleccionar índice
    while True:
        idx = int(input("Ingrese el índice del producto a reabastecer: "))
        if idx < 0 or idx >= len(nombres):
            print("Índice fuera de rango. Intente de nuevo.")
            continue
        else: break
    while True: # Cantidad a añadir
        cantidad_anadir = int(input("Ingrese la cantidad a añadir (entero > 0): "))
        if cantidad_anadir <= 0:
            print("La cantidad debe ser mayor que 0.")
            continue
        else: break
    inventario[idx][0] += cantidad_anadir
    print(f"Se añadieron {cantidad_anadir} unidades a '{nombres[idx]}'. Nuevo stock: {inventario[idx][0]}") # Muestra el producto y el stock con el añadido

def mostrar_menu():
    print("""\n==============================
Gestión de Inventario - Tienda Deportiva
==============================
1. Registrar productos
2. Consultar inventario
3. Realizar ventas
4. Reabastecer inventario
5. Salir
==============================""")

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

# - Programa - #

main() # Unicamente es necesario llamar a la función main para que se ejecute todo el programa