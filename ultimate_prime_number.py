def find_prime_num(random_num):
    if random_num < 2:
        return f"El numero {random_num} no cumple con la definicion de un numero primo, debe de ser mayor que 1 y ser divisible solamente entre ellos mismos y el 1"
    else:
        for i in range(2,random_num):
            if random_num % i == 0:
                return f"El numero {random_num} no es primo ya que se puede dividir entre el mismo, el 1 y otros"
        else:
            return f"El numero {random_num} si es primo ya que solamente se puede dividir entre el mismo y el 1"
        
random_num = int(input("Add any integer number: "))

print(find_prime_num(random_num))