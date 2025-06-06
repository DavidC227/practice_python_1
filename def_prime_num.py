
def prime_number(numero):
    for i in range (2,numero):
        if numero % i == 0:
            return False
    return True

write_numero = int(input("escribe un numero entero: "))

if prime_number(write_numero) is True:
    print("Es un numero primo")
else:
    print("no es un numero primo")