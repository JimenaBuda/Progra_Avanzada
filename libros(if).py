#Pide al usuario que escriba un numero, segun el número que ingrese se le recomendarán 3 libros del género seleccionado

#Se inicia el ciclo para si se quiere, volver a ejecutar todo el programa

while True:

    #Mostramos las opciones
    print("Bienvenido")
    print("=============================")
    print("Selecciona el género de tu interés:\n1:Romance\n2:Terror\n3:Novela Gótica\n4:Ciencia Ficción")
    print("=============================")
    opcion=int(input("Opción: "))

    if (opcion == 1):
        print("1.- Yo antes de ti\n2.- Orgullo y prejuicio\n3.- El cuaderno de Noah")
        
    elif (opcion == 2):
        print("1.- El Resplandor\n2.- La semilla del diablo\n3.- El exorcista")
        
    elif (opcion == 3):
        print("1.- El castillo de Otranto\n2.- Los Misterios de Udolfo\n3.- Abadía de Northanger")
        
    elif (opcion == 4):
        print("1.- Fahrenheit 451\n2.- En las montañas de la locura\n3.- La máquina del tiempo")
        
    #Mostramos el mensaje de error en caso de ser necesario
    else:
        print("No ha ingresado una opción / Opción NO válida")
            

    print("Deseas continuar?")

    # Le preguntamos al usuario si desea continuar o no
    respuesta = input("Escribe 's' para continuar o 'n' para salir: ")

    # Si la respuesta es 'n', detenemos el bucle
    if (respuesta == "n"):
        break
        
    elif (respuesta == "s"):
        continue