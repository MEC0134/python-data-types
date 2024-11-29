"""

Python Data Types:

    1. Text Type:	str
    2. Numeric Types:	int, float, complex (Complex class - exmaple can algebraic expression)
    3. Sequence Types:	list, tuple, range
    4. Mapping Type:	dict
    5. Set Types:	set, frozenset
    6. Boolean Type:	bool
    7. Binary Types:	bytes, bytearray, memoryview
    8. None Type:	NoneType

"""

# Complex data type example
x = 3 + 4j

# The method below will output complex class as type
print(type(x))


""" 

    3. Sequence Data Types: are ordered collection of similar or different data types. Allows storing multiple values in an organized way
 
        3.1 - String: is a collection of one or more characters contained in b/w single, double or even triple quotes. There are no 
        character data type in python, it is simply a string with a length of one. We can also access characters within a string. 
        
        3.2 - List: the value types of the items in a list do not need to be of the same type. We have to use [] to declare a list. 
        We can declare and empty list and then initialize it or initialize it when declaring. 
        
        3.3 - Tuples: similar to lists, tuples are also a ordered collection of python objects. Main difference being that tuples are
        immutable, meaning they cannot be modified post-creation. We create them by placing a sequence of values separated by a comma 
        with or without the use of parentheses (). Like lists they can be declared without initialization. 
        
        3.4 - Range: ..........
        
 
 """


# 3.1 - Passing data type of String to the print function

string1 = 'Welcome to Python Data Types!'
print("This is a string with single quotes:", string1)
string2 = "Welcome to Python Data Types!"
print("This is a string with double quotes:", string2)

# 3.1 - Accessing elements of string data type using indexing

string3 = 'We will be using this string to demonstrate the usage of indexing in python'

# Below line will output the 1st character of our string, positive indexing
print(string3[0])

# Below line will output the last character of our string, negative indexing
print(string3[-1], "\n--------------------------")


# ---------------------------------------------------------------------------------------------

# 3.2 - Creating/declaring and initializing a list of same data types

car_list = ["Mini Cooper", "Toyota", "BMW"]
print(car_list, "\n")

# 3.2 - Creating/declaring and initializing a list of different data types
mixed_list = ['Hello', 3.0, 2]
print(mixed_list, "\n")

# 3.2 - Accessing list items
print("The 2nd element/item in our car list is:", car_list[1])
print("The last element/item in our car list is:", car_list[-1], "\n\n--------------------------\n")

# ---------------------------------------------------------------------------------------------

# 3.3 - Creating/declaring and initializing a tuple

countries_tuple = ('Mexico', 'Qatar', 'Norway', 'Lithuania')
print(countries_tuple, "\n")


# 3.3 - Converting a list into a tuple using tuple() method

numbers_list = [1, 2, 3, 4, 5]
print("Our numbers list converted to a tuple: ", tuple(numbers_list), "\n")


# 3.3 - Accessing tuple items, same as we do with lists using index operator []
print("My favorite trip to a foreign country was", countries_tuple[2], "and my least favorite was", countries_tuple[-1], "\n")


# 3.4 -



# -------------------------------------------------------------------------------

""" 

    4. Mapping Data Types - Dictionaries 
        
        - A mapping is a data structure with a key-value pair that allows us to retrieve values using keys which makes things simpler. 
        Dictionaries do not allow for duplicates. As of python 3.7 they are ordered. If we enter duplicates it will override. 
        
"""



