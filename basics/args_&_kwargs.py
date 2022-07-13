#args
from numpy import multiply


def add(*args):
    print(args[1])
    sum = 0
    for n in args:
        sum += n 
    return sum

# print(add(3,5,6,2,1,7,4,3))

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        self.make = kw.get("make")
        # self.model = kw["model"]
        self.model = kw.get("model")

# my_car = car(make="Nissan", model="GT-R")
my_car = car(make="Nissan")
print(my_car.model)

