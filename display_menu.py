import random 

opcion = " "

while opcion != "3":
    print("\n=====Menu=====\n")
    print("1. Saludar")
    print("2. Mostrar un numero aleatorio del 1 al 100")
    print("3. Despedirse")

    opcion = input("\nIngresar una opcion del 1 al 3: ")

    if opcion == "1":
        print("\nHola programador espero que estes al 100")
    elif opcion == "2": 
        print("\nEl número aleatorio es: ", random.randint(1,100))
    elif opcion == "3":
        print("\nNos vemos programador")
    else:
        print("\nNecesitas agregar una de las siguientes opciones: 1, 2 o 3")
