
def password(contraseña):
    contraseña
    right_pass = "right_password"
    if contraseña == right_pass:
        return("La contraseña es correcta")
    else:
        return("La contraseña es incorrecta")

contraseña = input("Ingresa la contraseña: ")
print(password(contraseña))
    
        