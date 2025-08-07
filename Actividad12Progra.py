repartidores = {}
opcion = 0

print('Bienvenidos Actividad 12')
while opcion != 3:
    print('Bienvenido')
    print("1.- Registrar")
    print("2.- Mostrar")
    print("3.- Salir")

    match opcion:
        case 1:
            participantes = int(input("Ingrese cuantos repartidores participaron"))
            for i in range (participantes):
                print(f"Ingrese los datos del participante {i+1}")
                nombre = input("Ingrese el nombre: ")
                repartidores[nombre] = {}
                repartidores[nombre]["Paquetes"] = int(input("Ingrese la cantidad de paquetes entregados"))
                repartidores[nombre]["Zona"] = input("Ingrese la zona donde fue asignad@")




