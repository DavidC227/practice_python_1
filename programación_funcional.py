def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))
print("\n")

def double_mult(function,argue):
    return function(function(argue))

def multiplication(num):
    product = num * num 
    return product

print(double_mult(multiplication,3))
print("\n")

def division_by_2(function,argument):
    return function(function(argument))

def funct_div(argue):
    return argue / 2

print(division_by_2(funct_div,20))