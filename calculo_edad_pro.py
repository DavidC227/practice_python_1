from datetime import date

año_nacimiento = int(input("Ingresa tu año de nacimiento"))
mes_nacimiento = int(input("Ingresa el numero del mes de nacimiento"))

fehca_actual = date.today()
año_actual = date.today().year
mes_actual = date.today().month


if mes_nacimiento == mes_actual:
    print(f" Este mes tienes  {año_actual - año_nacimiento} años")
elif mes_nacimiento > mes_actual:
    print(f" tienes  {(año_actual - año_nacimiento) -1} años y te faltan {abs(mes_actual - mes_nacimiento)} meses para cumplir {año_actual - año_nacimiento} años")
else:
    print(f" tienes  {(año_actual - año_nacimiento)} años con {abs(mes_actual - mes_nacimiento)} meses")