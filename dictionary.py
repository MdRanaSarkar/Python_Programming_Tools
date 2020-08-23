"""
Dictionaries
A dictionary is a data type similar to arrays, but works with keys and values instead of indexes.
 Each value stored in a dictionary can be accessed using a key,
which is any type of object (a string, a number, a list, etc.) instead of using its index to address it
"""
"""
#Type 01
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)
"""
"""
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)
"""

#Type 02

#Type 03:
"""
Iterating over dictionaries
Dictionaries can be iterated over, just like a list. However, a dictionary,
unlike a list, does not keep the order of the values stored in it. To iterate over key value pairs, 
use the following syntax:

phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
"""

#Type 04
"""Removing a value
To remove a specified index, use either one of the following notations:"""



phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
phonebook.pop('Jill')
print(phonebook)







"""

Exercise
Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# write your code here


# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")
"""