"""
Use of Lambda Function in python
We use lambda functions when we require a nameless function for a short period of time.

In Python, we generally use it as an argument to a higher-order function (a function that takes in other functions as arguments).
Lambda functions are used along with built-in functions like filter(), map() etc.
The filter() function in Python takes in a function and a list as arguments.
The map() function in Python takes in a function and a list.
"""


"""
TYPE :01
# Program to filter out only the even items from a list
"""

list_data=[3,5,4,2,5,6,2,5,33,67,7,45,3,4534]
even_data=list(filter(lambda a:(a%2==0),list_data))
print(even_data)
"""
TYPE :02
# Program to double each item in a list using map()
"""

list_data=[3,5,4,2,5,6,2,5,33,67,7,45,3,4534]
even_data=list(map(lambda a:a*2,list_data))
print(even_data)