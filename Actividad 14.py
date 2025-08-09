def menu():
    print("\n= = = = MENÚ DE OPCIONES = = = =\n1. Agregar participante\n2. Mostrar participantes ordenados por nombre\n3. Mostrar participantes ordenados por edad\n4. Salir")

def main():
    while True:
        try:
            menu()
            opcion = int(input("Seleccione una opción: "))
            match opcion:
                case 1:
                    print("1")
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