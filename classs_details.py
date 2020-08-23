"""
Classes and Objects
Objects are an encapsulation of variables and functions into a single entity. Objects get their variables and functions
 from classes. Classes are essentially a template to create your objects.
"""


"""
Type 01:
The simplest form of class definition looks like this:

class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
"""

"""
class MYclas:
    print("Okay")
"""

"""

Type 02:
Accessing Object Variables
To access the variable inside of the newly created object 
"""

"""
class MYclass:
    variable = "Its all right"
    print("Okay")


obj = MYclass()
print(obj.variable)
"""
"""
Type 02:
Many classes like to create objects with instances customized to a specific initial state


def __init__(self):
    self.data = []
example shown video
"""
"""

class Myclass:
    def __init__(self, realpart, complex_part):
        self.a = realpart
        self.b = complex_part


obj = Myclass(3, -4.947)

print(obj.a, obj.b)
"""
"""
Type 03:
You can create multiple different objects that are of
 the same class(have the same variables and functions defined).
"""

"""
class MYclass:
    variable = "Its all right"
    print("Okay")


obj = MYclass()
obj.variable2 = "Thanks"
print(obj.variable)
print(obj.variable2)
"""

"""
Type 04:
Accessing Object Functions
To access a function inside of an object you use notation similar to accessing a variable:
"""
"""

class Myclass:
    def rect(self, x, y):
        self.a = x
        self.b = y
        return self.a*self.b


obj = Myclass()
print(obj.rect(4, 6))

"""
"""
Exercise
We have a class defined for vehicles. Create two new vehicles called car1 and car2. Set car1 to be a red convertible 
worth $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.
"""

"""
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())
"""
