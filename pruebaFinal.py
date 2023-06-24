import numpy as np

registroCiudadano = []
nif    = ""
nombre = ""
edad   = ""

def registro(nombre, nif, edad): #Definicion de registros
    print("\tPor favor complete lo siguiente:\n")
    while True:  # NIF
        try:
            nif = int(input("\tIngrese los  primeros 8 digitos de su NIF: "))
            if nif > 10000000 and nif < 999999999:
                print("\tNIF ha sido registrado")
                break
            else:
                print("\tNIF mal ingresado, por favor vuelva a intentarlo")
        except ValueError:
            print("\tERROR!NIF mal ingresado! Intente nuevamente")

    while True:  # Nombre 
        try:
            nombre= str(input("\tIngrese nombre: ").title())
            print("\tEl nombre ha sido registrado")
            break
        except ValueError:
            print("\tNombre mal ingresado")
    while True:  # Edad
        try:
            edad = int(input("\tIngrese edad: "))
            if edad > 0 or edad < 150:
                print("\tLa ha sido Edad bien registrada ")
                break
            else:
                print("\tedad mal ingresada, por favor vuelva a intentarlo")
        except ValueError:
            print("\t¡ERROR! Edad mal ingresada!")

    datos = (nombre, nif, edad)
    registroCiudadano.append(datos)

    return nombre, nif, edad, 

def buscadorNif(buscarNif):
    for i in range(len(registroCiudadano)):
        if str(registroCiudadano[i][1]) == buscarNif:  
            return i
    return -1        
                                                    
print("\nBienvenidos a Registros\n\nSeleccione una opción")
print("\t1.- Grabar registro\n\t2.- Buscar registro\n\t"
      "3.- Imprimir Certificados\n\t4.- Salir")
opc = int(input())

while opc != 4:

    if opc == 1:
        while True:
            print("\n\t\tGRABAR REGISTRO\n")
            nombre, nif , edad= registro(nombre, nif, edad)
            print("\tDatos bien ingresados")
            break     
    elif opc == 2:
        while True:
            print("BUSCAR REGISTRO")
            buscadorNif = input("Ingrese el NIF desea buscar: ")
            ciudadano = buscadorNif(buscadorNif)
            if ciudadano != -1:
                print("Nombre:", registro[ciudadano][0])
                print("Rut:", registro[ciudadano][1])
                print("Edad:", registro[ciudadano][2])
            else:
                print("¡NIF no encontrada!")
