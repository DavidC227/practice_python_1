opcion = ""

while opcion != "4":
    print("\n========MENÚ========\n")
    print("1.- Saludo de bienvenida")
    print("2.- ¿Cómo te llamas?")
    print("3.- ¡Otorgar un numero de asiento al azar!")
    print("4.- Despedida\n")

    opcion = input("Ingresa una opción del 1 al 4: ")

    if opcion == "1": 
        print("\nBienvenido programador")
    elif opcion == "2":
        nombre = input("\nIngresa tu nombre: ")
        print(f"\nMucho gusto {nombre}")
    elif opcion == "3":
        import random
        print("\nEl numero de asitento que obtiviste es: ",random.randint(1,100))
    elif opcion == "4":
        print("\nHasta pronto programador\n")
    else:
        print("\nElige una opción del 1 al 4\n")