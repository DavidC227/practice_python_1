int_num = int(input("Add an integer number"))

if int_num == 0:
    print(f"El numero {int_num} no es primo")
elif int_num == 1:
    print(f"El numero {int_num} no es primo")
elif int_num == 2:             
    print(f"El numero {int_num} si de hecho es el primer numero primo, además: solo se puede divir entre el 1 y si mismo")
else:
    for i in range(2,int_num): 
        if int_num % i == 0:
            print(f"El numero {int_num} no es primo: ya que se puede divir entre el 1, si mismo y otro número")
            break
        else:
            print(f"El numero {int_num} si es primo: solo se puede divir entre el 1 y si mismo")
            break