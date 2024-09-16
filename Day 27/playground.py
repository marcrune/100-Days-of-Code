def add(*args):
    # args is a tuple
    total = 0
    for arg in args:
        total += arg
    return total
    
print(add(3, 4, 5, 10, 20, 40))

def calculate(n, **kwargs):
    # kwargs is a dictionary
    print(kwargs)
    # for key, value in kwargs.items():
        # print(key)
        # print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    
    def __init__(self, **kwargs):
        # If we don't specify these values when creating the class, it will crash. For it to not crash we need to use kwargs.get(), which will return None if the argument isn't specified
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)