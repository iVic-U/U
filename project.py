# Inventario y factiruacion de tienda electrónicos (Partes de PC)

# - Usuarios Admin - #

admin1 = "Victor"
passwordAdmin1 = "admin1234"
admin2 = "Sara"
passwordAdmin2 = "admin4321"

# - Funciones - # 
def login(user:str, password:str):
    """Función para verificar el usuario y contraseña"""
    if user == admin1: 
        if password == passwordAdmin1:
            return True
    elif user == admin2:
        if password == passwordAdmin2:
            return True
    else: return False

def createCustomer():
    """Función createCustomer, se encarga de recolectar la información del cliente para luego devolverlas"""
    print("\nRegistro del Cliente\t\n")
    customerName = str(input("\nNombre completo del Cliente:\n---------- "))
    customerID = int(input("\nIngrese la Cédula del Cliente:\n---------- "))
    customerPhoneNumber = int(input("\nIngrese el Número de Teléfono del Cliente:\n---------- "))
    customerEmail = str(input("\nIngrese el Email del Cliente:\n---------- "))
    customerAddress = str(input("\nIngrese la Dirección del Cliente:\n---------- "))
    return customerName, customerID, customerPhoneNumber, customerEmail, customerAddress

def showPackagesOption():
    """Muestra los paquetes a elegir y se escoge con el número correspondiente
    Unicamente se paga por el producto escogido, no puede escoger dos productos diferente"""
    packageOptionName = ""
    packageOption = int(input("""\n¿Qué Paquete le gustaría comprar?
1. Computadora de Escritorio + Monitor + Mouse + Teclado --> $800
2. Laptop + Audifonos --> $500
3. Laptop + Base de Refrigeración + Mouse Innalambrico --> $700
4. Computadora de Escritorio Gamer + Monitor + Teclado + Parlante + Mouse Innalambrico --> $1500
--------------------- """))
    if packageOption == 1: 
        packagePrice = 800
        packageOptionName = "Computadora de Escritorio + Monitor + Mouse + Teclado"
    elif packageOption == 2: 
        packagePrice = 500
        packageOptionName = "Laptop + Audifonos"
    elif packageOption == 3:   
        packagePrice = 700
        packageOptionName = "Laptop + Base de Refrigeración + Mouse Innalambrico"
    elif packageOption == 4: 
        packagePrice = 1500
        packageOptionName = "Computadora de Escritorio Gamer + Monitor + Teclado + Parlante + Mouse Innalambrico"
    else: packagePrice = 0
    return packageOption, packagePrice, packageOptionName

def cxPreferrredTime():
    """Muestra los tiempos de preferencia a elegir y se escoge con el número correspondiente"""
    preferredTime = int(input("""¿Cuál sería su horario de Preferencia para ser Atendido?
1. 7 am - 11 am 
2. 1 pm - 4 pm
3. 6 pm - 9 pm
--------------------- """))
    customerTimeSlot = ""
    if preferredTime == 1: customerTimeSlot = "7 am - 11 am"
    elif preferredTime == 2: customerTimeSlot = " 1 pm - 4 pm"
    elif preferredTime == 3: customerTimeSlot = "6 pm - 9 pm"
    return preferredTime, customerTimeSlot

def showProductOptions():
    """Muestra los productos disponibles a elegir y se escoge con el número correspondiente
    Unicamente se paga por el producto escogido, no puede escoger dos productos diferente"""
    productName = ""
    productOption = int(input("""\nElija el Producto que desea con el número correspodiente:
1. CPU --> $400
2. Tarjeta Madre --> $20
3. RAM 8gb --> $60
4. Fuente de Poder 600W --> $70
5. Disco de Almacenamiento SSD 512gb --> $120
--------------------- """))
    quantity = int(input("\n¿Cuántas unidades desea comprar?:\n---------- ")) # Añade el producto y la cantidad
    if productOption == 1: 
        productPrice = 400 * quantity
        productName = "CPU"
    elif productOption == 2: 
        productPrice = 20 * quantity
        productName = "Tarjeta Madre"
    elif productOption == 3: 
        productPrice = 60 * quantity
        productName = "RAM 8gb"
    elif productOption == 4: 
        productPrice = 70 * quantity
        productName = "Fuente de Poder 600W"
    elif productOption == 5: 
        productPrice = 120 * quantity
        productName = "Disco de Almacenamiento SSD 512gb"
    else: productPrice = 0
    return productOption, productPrice, productName

def record(customerName:str, customerID:int, customerPhoneNumber:int, customerEmail:str, customerAddress:str, 
           packageOption: int, packageOptionName:str,
           preferredTime:int, customerTimeSlot:str,
           productOption:int, productName:str):
    """Muestra el historial que se ha obtenido hasta ahora con base a la inforrmación brindada"""
    print(f'''\nRegistro:
Cliente: {customerName}
Cédula: {customerID}
Número de Teléfono: {customerPhoneNumber}
Correo electrónico: {customerEmail}
Dirección: {customerAddress}''')
    if packageOption > 0 and packageOption <= 4: print(f"\nPaquete seleccionado: {packageOptionName}")
    else: print("\nNo se ha seleccionado un paquete aún...")
    if preferredTime > 0 and preferredTime <= 3: print(f"\nTiempo de preferencia seleccionado: {customerTimeSlot}")
    else: print("\nNo se ha seleccionado un tiempo de preferencia aún...")
    if productOption > 0 and productOption <= 5: print(f"\nProducto seleccionado: {productName}")
    else: print("\nNo se ha seleccionado un producto aún...")

def createInvoice(productPrice:int, packagePrice:int,
                  customerName:str, customerID:int, customerEmail:str):
    subtotal = (productPrice + packagePrice)
    iva = subtotal * 13 / 100
    print(f"""\nFactura a nombre de: {customerName}
Cédula: {customerID}
Email: {customerEmail}
El total a pagar sería: {(subtotal + iva)} con IVA incluido""")
    return False

# - Menu - #

def mainMenu():
    """Función mainMenu refleja el menú principal del programa"""
    menuOption = int(input("""\nQue desea realizar?
1. Selecciona un Paquete en Promocion
2. Seleccionar Horario de Atención de Preferencia
3. Ver los Productos
4. Historial de Consultas Realizadas
5. Facturar
6. Salir del Programa
                           
------------------------  """))
    return menuOption

# - Programa Principal - #

print("\nBienvenido al Programa de Ventas\t\n")
i=0
condition = True
while i < 3: # unicamente por 3 intentos    
    if condition == False:
        break
    elif condition == True:
        user = str(input("\nCual es su usario?:\n---------- "))
        password = str(input("Cual es su contraseña?:\n---------- "))
        if login(user,password): # Se inicia el login y se hace el break solo si selecciona salir del programa o si se realiza la factura
            print("\nBienvenido al Programa\t")
            customerName, customerID, customerPhoneNumber, customerEmail, customerAddress = createCustomer()
            # Se crean varias variables para su posterior uso de manera que ya esten inicializadas
            preferredTime = 0
            productOption = 0
            subtotal = 0
            packageOption = 0
            packageOptionName = ""
            productName = ""
            customerTimeSlot = ""
            iva = 0
            condition = True
            packagePrice = 0
            productPrice = 0
            print("\nCliente registrado...")
            while(condition):
                option = mainMenu() # Se optiene la opción a partir del menú y Realiza las funciones, guardando el retorno en las variables correspondientes
                if option == 1:
                    packageOption, packagePrice, packageOptionName = showPackagesOption()
                elif option == 2:
                    preferredTime, customerTimeSlot = cxPreferrredTime()
                elif option == 3:
                    productOption, productPrice, productName = showProductOptions()
                elif option == 4: # Muestra el Historial utilizando las variables correspondientes como parametros
                    record(customerName, customerID, customerPhoneNumber, customerEmail, customerAddress,
                        packageOption, packageOptionName,
                        preferredTime, customerTimeSlot,
                        productOption, productName)
                elif option == 5:
                    if productPrice > 0 or packagePrice > 0: # Valida que haya algun producto agregado para comprar
                        condition = createInvoice(productPrice, packagePrice, customerName, customerID, customerEmail)
                        break
                    else:
                        print("No se ha seleccionado nada para comprar")
                elif option == 6:
                    condition = False
                    break # Break point
                else:
                    print("No se ha seleccionado la opción correcta")
            if condition == False:
                print("\nMuchas gracias por usar nuestro servicio...\n")  
        else: 
            i = i+1 # Incrementa i
            print("Intento Fallido...")
            if i==3: print("\nSe han completado 3 intentos incorrectos, cerrando el programa...\n") # Si es igual a 3 intentos muestra el mensaje
