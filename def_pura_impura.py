#funcion pura:
def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)
print(pure_function(10,5))

#funcion impura:
some_list = []

def impure(arg):
  some_list.append(arg)
  return some_list
print(impure(5))