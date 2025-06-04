
contraseña = input("ingresa contraseña: ")

tiene_letra = False
tiene_numero = False

for caracter in contraseña:
    if caracter.isalpha():
        tiene_letra = True
    if caracter.isdigit():
        tiene_numero = True

pass_correcta = len(contraseña) >= 8  and tiene_letra and tiene_numero 

if pass_correcta == True:
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")