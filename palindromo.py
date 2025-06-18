print()
def palindromo(palabra):
    palabra = palabra.lower() 
    x = palabra[::-1]

    if palabra == x:
        return("es un palindromo")
    else:
        return("No es un palindromo")

print(palindromo(input("Ingresa una palabra: ")))
print()

