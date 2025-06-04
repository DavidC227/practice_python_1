print()
from datetime import date

def edad_actual (año_nacimiento):
    año_actual = date.today().year
    edad = año_actual -año_nacimiento
    return edad

print("Tuedad es:",edad_actual(int(input("ingresa tu año de nacimiento: "))),"años")
print()