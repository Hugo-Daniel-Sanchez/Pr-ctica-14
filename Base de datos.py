from os import system
system("cls")

print("Programa realizado por: Sánchez Vázquez Hugo Daniel y Olvera Martinez Maximiliano")

CONTRASENA = "2090"

telefonos = []

print("Bienvenido. Por favor, ingresa la contraseña:")
while True:
    contrasena_ingresada = input("Contraseña: ")
    if contrasena_ingresada == CONTRASENA:
        print("Contraseña correcta. Acceso concedido.")
        break
    else:
        print("Contraseña incorrecta. Inténtalo nuevamente.")

def capturar_telefono():
    telefono = {}
    telefono["Marca"] = input("Indique la marca del teléfono: ")
    telefono["Modelo"] = input("Indique el modelo del teléfono: ")
    telefono["Procesador"] = input("Indique el procesador del teléfono: ")
    telefono["RAM"] = input("Indique la cantidad de RAM (en GB): ")
    telefono["ROM"] = input("Indique la capacidad de almacenamiento interno ROM (en GB): ")
    telefono["Pantalla"] = input("Indique el tamaño de la pantalla (en pulgadas): ")
    telefono["Batería"] = input("Indique la capacidad de la batería: ")
    telefono["Resolución"] = input("Indique la resolución de la pantalla (Ejemplo = 1080x2400): ")
    telefono["Cámara trasera"] = input("Indique la calidad de la cámara trasera: ")
    telefono["Cámara frontal"] = input("Indique la calidad de la cámara frontal: ")
    telefono["Carga rápida"] = input("Indique la potencia de carga soportada: ")
    telefono["Precio"] = input("Indique el precio del teléfono (en MXN): ")
    return telefono

def agregar():
    if len(telefonos) < 10:
        print("\n--- Agregar nuevo teléfono ---")
        nuevo_telefono = capturar_telefono()
        telefonos.append(nuevo_telefono)
        print("Teléfono agregado exitosamente.")
    else:
        print("No se pueden agregar más teléfonos. El límite es de 10.")

def consultar():
    if telefonos:
        print("\n--- Lista de teléfonos almacenados ---")
        for i, telefono in enumerate(telefonos, start=1):
            print(f"\nTeléfono {i}:")
            for clave, valor in telefono.items():
                print(f"  {clave}: {valor}")
    else:
        print("No hay teléfonos insertados en la base de datos.")

def modificar():
    consultar()
    if telefonos:
        try:
            indice = int(input("\nIngrese el número del teléfono que desea modificar: ")) - 1
            if 0 <= indice < len(telefonos):
                print("\n--- Modificar teléfono ---")
                print("Deje en blanco los campos que no desea modificar.")
                telefono = telefonos[indice]
                for clave in telefono.keys():
                    nuevo_valor = input(f"{clave} actual ({telefono[clave]}): ")
                    if nuevo_valor:
                        telefono[clave] = nuevo_valor
                print("Teléfono modificado exitosamente.")
            else:
                print("Índice fuera de rango.")
        except ValueError:
            print("Entrada inválida.")

def eliminar():
    consultar()
    if telefonos:
        try:
            indice = int(input("\nIngrese el número del teléfono que desea eliminar: ")) - 1
            if 0 <= indice < len(telefonos):
                telefonos.pop(indice)
                print("Teléfono eliminado exitosamente.")
            else:
                print("Índice fuera de rango.")
        except ValueError:
            print("Entrada inválida.")

# Menú principal
while True:
    print("\n--- Menú ---")
    print("1. Agregar teléfono")
    print("2. Consultar teléfonos")
    print("3. Modificar teléfono")
    print("4. Eliminar teléfono")
    print("5. Salir")
    
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            agregar()
        elif opcion == 2:
            consultar()
        elif opcion == 3:
            modificar()
        elif opcion == 4:
            eliminar()
        elif opcion == 5:
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")