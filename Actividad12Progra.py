repartidores = {}
opcion = 0

def quick_sort(resultado):
    if len(resultado) <= 1:
        return resultado

    pivote = resultado[0]
    menores = [x for x in resultado[1:] if x < pivote]
    iguales = [x for x in resultado if x == pivote]
    mayores = [x for x in resultado[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)



print('Bienvenidos Actividad 12')
while opcion != 3:
    print('Bienvenido')
    print("1.- Registrar")
    print("2.- Mostrar")
    print("3.- Salir")
    opcion = int(input("Ingrese la opcion que desea: "))

    match opcion:
        case 1:
            participantes = int(input("Ingrese cuantos repartidores participaron"))
            for i in range (participantes):
                print(f"Ingrese los datos del participante {i+1}")
                nombre = input("Ingrese el nombre: ")
                repartidores[nombre] = {}
                repartidores[nombre]["Paquetes"] = int(input("Ingrese la cantidad de paquetes entregados"))
                repartidores[nombre]["Zona"] = input("Ingrese la zona donde fue asignad@")


        case 2:
            lista = list(repartidores.items())
            resultado = quick_sort(lista)
            print(resultado)



