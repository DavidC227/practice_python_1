

def right_password(contraseña):

    tiene_letra = False
    tiene_numero = False

    for caracter in contraseña:
        if caracter.isalpha():
            tiene_letra = True
        if caracter.isdigit():
            tiene_numero = True
    return len(contraseña) >= 8 and tiene_numero and tiene_letra

ingresar_contraseña = right_password(input("Ingresa contraseña"))

if ingresar_contraseña == True:
    print("La contraseña es valida")
else:
    print("La contraseña no es valida")




