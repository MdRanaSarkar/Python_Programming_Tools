

"""
What are Lambda Functions?
In Python, we use the lambda keyword to declare an anonymous function, which is why we refer to them as "lambda functions".


lambda argument(s): expression

Why Use Lambda Functions?

This is commonly used when you want to pass a function as an argument to higher-order functions
"""


"""
Type 1:
A lambda function that adds 10 to the number passed in as an argument, and print the result:
"""
"""a=lambda b:b+10
print(a(10))

"""

"""
Type 02:
A lambda function that multiplies argument a with argument b and print the result:
"""
"""
e=lambda a, b: a*b
print(e(10,20))

"""
"""
Type 03:
function definition that takes one argument, and that argument will be multiplied with an unknown number:
"""

def power(a):
    return lambda b:b*a


d=power(20)
print(d(30))

"""
Type 04:
Exercise:
Create a lambda function that takes one parameter (a) and returns it.
"""
