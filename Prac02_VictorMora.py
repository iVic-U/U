"""
Programa: Gestión de notas de estudiantes
Descripción: Registrar estudiantes y 3 notas por estudiante, calcular promedios y determinar estado (Aprobado si promedio >= 70). 
Menú interactivo.

Análisis:

Entradas:
    - Nombres de estudiantes (tipo str, almacenados en un arreglo unidimensional estudiantes).
    - Notas de 3 exámenes por estudiante (tipo int, almacenadas en un arreglo bidimensional notas, donde cada fila corresponde a un estudiante y cada columna a un examen).
    - Opciones del menú (tipo int, seleccionadas por el usuario para decidir la acción a realizar).

Operaciones:
    - Registrar estudiantes y notas
    - Validar que el nombre no esté repetido.
    - Validar que cada nota esté en el rango 0 - 100.
    - Guardar nombre y notas en los arreglos globales.
    - Calcular promedios
    - Recorrer cada fila de notas.
    - Sumar las 3 notas y dividir entre 3.
    - Guardar el promedio en el arreglo promedios.
    - Determinar estado (Aprobado/Reprobado)
    - Comparar cada promedio con el umbral (70).
    - Asignar estado "Aprobado" si promedio ≥ 70, "Reprobado" si promedio < 70.
    - Mostrar todos los registros
    - Desplegar nombre, notas y promedio (si ya fue calculado).
    - Menú interactivo
    - Controlar el flujo del programa con while y if.
    - Permitir al usuario elegir entre registrar, calcular, determinar estado, mostrar registros o salir.

Salidas:
    - Mensajes de confirmación al registrar estudiantes y notas.
    - Promedios calculados correctamente.
    - Listado de estudiantes con su promedio y estado (Aprobado/Reprobado).
    - Visualización completa de todos los registros (nombres, notas y promedios).
    - Mensajes de error o advertencia en caso de entradas inválidas (ejemplo: nota fuera de rango, opción de menú incorrecta).
    - Mensaje final de salida del programa
"""

# Variables globales
estudiantes: list[str] = [] # arreglo unidimensional para nombres
notas: list[list[int]] = [] # arreglo bidimensional para notas (cada fila = 3 notas)
promedios: list[float] = [] # arreglo para almacenar promedios calculados
notas_est: list[int] = [] # arreglo temporal para las 3 notas de cada estudiante

def registrar_estudiantes(estudiantes:list[str], notas:list[list[int]], notas_est:list[int]): # Función: registrar estudiantes y sus 3 notas
    """
    Permite ingresar uno o varios estudiantes con sus 3 notas
    Usa variables locales para la entrada temporal
    """
    while True:
        nombre = str(input("\nIngrese el nombre del estudiante"+"\n------------ "))
        if nombre == "":
            break
        if nombre in estudiantes: # Validar que no se repita el nombre
            print("Ese nombre ya existe. Si desea actualizar notas, elimine y vuelva a registrar o use otro nombre.")
            continue
        notas_est = []  # reiniciar notas_est para cada estudiante y leer 3 notas con validación
        for i in range(1, 4):
            while True:
                entrada = int(input(f"Ingrese la nota del examen {i} (0-100) para {nombre}"+"\n------------ "))
                valor = entrada
                if 0 <= valor <= 100:
                    notas_est.append(valor)
                    break
                else: print("La nota debe estar entre 0 y 100.")      
        # Guardar en arreglos globales
        estudiantes.append(nombre)
        notas.append(notas_est)
        print(f"Estudiante '{nombre}' registrado con notas: {notas_est}")
        break

def calcular_promedios(estudiantes:list[str], notas:list[list[int]], promedios:list[float]): # Función: calcular promedio por estudiante
    """
    Calcula el promedio de las 3 notas para cada estudiante y lo guarda en 'promedios'
    """
    if len(estudiantes) == 0:
        print("\nNo hay estudiantes registrados. Primero registre estudiantes.")
        return
    promedios.clear()  # reiniciar promedios antes de calcular
    for fila in notas:
        suma = 0
        for n in fila:
            suma += n
        promedio = round(suma / len(fila),2)
        promedios.append(promedio)
    print("\nPromedios calculados correctamente.")
    

# Función: determinar estado (Aprobado/Reprobado) según promedio
def determinar_estado(estudiantes:list[str], notas:list[list[int]], promedios:list[float]):
    """
    Muestra el promedio y el estado (Aprobado si promedio >= 70) de cada estudiante.
    Si no se han calculado promedios, solicita calcularlos primero.
    """
    if len(estudiantes) == 0:
        print("\nNo hay estudiantes registrados.")
        return
    if len(promedios) != len(estudiantes):
        print("\nNo se han calculado los promedios o están desactualizados. Calculando ahora...")
        calcular_promedios(estudiantes, notas, promedios)
    print("\nResultados por estudiante:")
    for i in range(len(estudiantes)):
        nombre = estudiantes[i]
        promedio = promedios[i]
        estado = "Aprobado" if promedio >= 70 else "Reprobado"
        print(f"- {nombre}: Promedio = {promedio} -> {estado}")

# Función: mostrar todos los datos (nombres y notas)
def mostrar_todos(estudiantes:list[str], notas:list[list[int]], promedios:list[float]):
    if len(estudiantes) == 0:
        print("\nNo hay estudiantes registrados.")
        return
    print("\nListado completo de estudiantes y notas:")
    for i in range(len(estudiantes)):
        nombre = estudiantes[i]
        notas_est = notas[i]
        promedio = promedios[i] if i < len(promedios) else "No calculado"
        print(f"{i+1}. {nombre} | Notas: {notas_est} | Promedio: {promedio}")

def menu(): # Función: menú principal
    """
    Muestra el menú y permite al usuario elegir acciones hasta salir.
    Usa while para mantener el menú activo.
    """
    
    while True:
        print("""\nMenú
1 - Ingresar estudiantes y notas
2 - Calcular promedios
3 - Determinar estado (Aprobado/Reprobado) y mostrar promedios
4 - Mostrar todos los registros
5 - Salir\n""")
        opcion = int(input("Seleccione una opción (1-5)"+"\n------------ "))
    
        if opcion == 1:
            registrar_estudiantes(estudiantes, notas, notas_est)
        elif opcion == 2:
            calcular_promedios(estudiantes, notas, promedios)
        elif opcion == 3:
            determinar_estado(estudiantes, notas, promedios)
        elif opcion == 4:
            mostrar_todos(estudiantes, notas, promedios)
        elif opcion == 5:
            print("\nSaliendo del programa...\n")
            break
        else: print("Opción inválida. Por favor seleccione un número entre 1 y 5.")
                
# ------------------------------------------------------------------------------- #


# Punto de entrada

print("\n\tPrograma de gestión de notas")
menu()
