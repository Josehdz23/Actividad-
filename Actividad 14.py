from idlelib.autocomplete import TRY_A

participantes = {}
def menu():
    print("\n= = = = MENÚ DE OPCIONES = = = =\n1. Agregar participante\n2. Mostrar participantes ordenados por nombre\n3. Mostrar participantes ordenados por edad\n4. Salir")

def ingreso():
    while True:
        try:
            n = int(input("\n¿Cuántos participantes desea ingresar?: "))
            for i in range(n):
                print(f"\nPARTICIPANTE #{i+1}")
                while True:
                    try:
                        dorsal = int(input("Ingrese el dorsal del participante: "))
                        if dorsal > 0:
                            if dorsal in participantes:
                                print("El dorsal ya está en uso, pruebe otro")
                            else:
                                break
                    except Exception as ex:
                        print(f"Ha ocurrido un error: {ex}")
                while True:
                    nombre = input("Ingrese el nombre del participante: ")
                    if nombre or nombre.isspace():
                        break
                    else:
                        print("Nombre inválido, reintente")
                while True:
                    try:
                        edad = int(input("Ingrese la edad del participante (15 - 35): "))
                        if edad >= 15:
                            break
                        else:
                            print("La edad no es válida, reintente")
                    except Exception as ex:
                        print(f"Ha ocurrido un error: {ex}")
                while True:
                    categoria = input("Ingrese la categoría del participante (Juvenil, Adulto, Máster): ")
                    if categoria or categoria.isspace():
                        if ((categoria == "Juvenil") or (categoria == "Adulto") or (categoria == "Máster")):
                            break
                        else:
                            print("La categoría ingresada no es válida, reintente")
                    else:
                        print("Nombre inválido, reintente")
                participantes[nombre] = {
                    "dorsal": dorsal,
                    "edad": edad,
                    "categoria": categoria
                }
            break
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x[1] < pivote[1]]
        iguales = [x for x in lista if x[1] == pivote[1]]
        mayores = [x for x in lista[1:] if x[1] > pivote[1]]
        return quick_sort(menores) + iguales + quick_sort(mayores)

def main():
    while True:
        try:
            menu()
            opcion = int(input("Seleccione una opción: "))
            match opcion:
                case 1:
                    ingreso()
                case 2:
                    print("2")
                case 3:
                    print("3")
                case 4:
                    print("\nS A L I E N D O . . .")
                    break
                case _:
                    print("Opción inexistente, reintente")
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")
main()