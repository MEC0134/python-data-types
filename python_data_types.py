"""

Python Data Types:

    1. Text Type:	str (There are a lot of built-in-methods to use with strings)
    2. Numeric Types:	int, float, complex (Complex class - exmaple can algebraic expression)
    3. Sequence Types:	list, tuple, range
    4. Mapping Type:	dict
    5. Set Types:	set, frozenset
    6. Boolean Type:	bool
    7. Binary Types:	bytes, bytearray, memoryview
    8. None Type:	NoneType

"""

""" Strings: are arrays in python, therefor can be treated as such. To define characters we have to use string type as well.  """

# 1- Multiline strings stored in a variable

print("------------------------------------PYTHON STRINGS------------------------------------\n")

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a, "\n")
#
# # Accessing characters from a string
# print(a[0], "\n")
#
# # Looping a string
# for x in "Apple":
#     print(x)
# print()
#
# # Membership testing for strings using in keyword
# my_str = "Life is worth fighting for!"
# print("is" in my_str, "\n")
#
# # Using if statement for membership testing
# my_str1 = "Another string to test!"
# if "test" in my_str1:
#     print("test is here", "\n")
#
# # Using not in keyword for membership testing
# my_str2 = "Enough with these membership tests!"
# print("more" not in my_str2, "\n")
#
# # Using not in keyword with if statement for membership testing
# my_str2 = "Enough with these membership tests! Never mind one more :("
# if "one more" not in my_str2:
#     print("Where did it go!", "\n")
# else:
#     print("I am here", "\n")
#
# # Slicing strings
# x = " Hello World! "
# print(x[1:5], "\n")
#
# # Modify strings - Make all characters in string upper-case
# print(x.upper(), "\n")
#
# # Modify strings - Make all characters in string lower-case
# print(x.lower(), "\n")
#
# # Modify strings - Remove whitespaces from string (Can be useful for form validation)
# print(x.strip(), "\n")
#
# # Modify strings - Replace characters using the replace() method
# print(x.replace("H", "K"), "\n")
#
# #Modify strings - Split string into sub-strings using split() method, case-sensitive and will only work for existing characters
# print(x.split("W"), "\n")
#
# """ We cannot normally combine string type and numbers using + or , but we can do it w/F-strings and format() method """
#
# # Combining numbers and strings using F-Strings, notice the f pre-string initialization
# age = 28
# my_str3 = f'My name is Enes, and I am {age}'
# print(my_str3, "\n")
#
# # We can use {} as a placeholder in general and perform even arithmetics within it
# print(f"Your total will be ${7 * 14:.2f} sir")



# Complex data type example
# x = 3 + 4j
#
# # The method below will output complex class as type
# print(type(x))


"""

    3. Sequence Data Types: are ordered collection of similar or different data types. Allows storing multiple values in an organized way

        3.2 - List: the value types of the items in a list do not need to be of the same type. We have to use [] to declare a list.
        We can declare and empty list and then initialize it or initialize it when declaring. Items added later will go to the end of
        the list. Duplicates are allowed.

        3.3 - Tuples: similar to lists, tuples are also a ordered collection of python objects. Main difference being that tuples are
        immutable, meaning they cannot be modified post-creation. We create them by placing a sequence of values separated by a comma
        with or without the use of parentheses (). Like lists they can be declared without initialization.

        3.4 - Range: range() function returns a sequence of numbers between a range specified in the method parameters. Common usage
        is for iteration. range(start[optional], stop, step[optional]). The method will only accept integers and not floats or any other.

 """

print("------------------------------------PYTHON LISTS------------------------------------\n")


# 3.2 - Creating/declaring and initializing a list of same data types

car_list = ["Mini Cooper", "Toyota", "BMW", "Mercedes", "Volvo"]
print(car_list, "\n")

# 3.2 - Creating/declaring and initializing a list of different data types
mixed_list = ['Hello', 3.0, 2]
print(mixed_list, "\n")

# 3.2 - Range of Indexes
print(car_list[1:4], "\n")

# Membership test using if statement and in keyword
if "BMW" in car_list:
    print("Yes sir, we have a 330i in our inventory!", "\n")

# Changing Item values in a list simply using = operator

car_list[1] = "Audi"
print(car_list, "\n")

# Changing a range of items in a list
car_list[0:1] = ["BYD", "Tesla"]
print("Updated list:", car_list, "\n")

# We can also change a few items with only one
car_list[0:2] = ["Hyundai"]
print("Updated list:", car_list, "\n")

# Insert new items using insert() method, 1st param is for index and 2nd for item value
car_list.insert(0, "Ford")
print(car_list, "\n")

# append() method will insert an item to the end of the list

# extend() - add items/elements from another list to the end of current list, we can use this for any iterable not just lists
aeroplanes_list = {"Airbus", "Boeing", "Bombardier"}
# Append set to list
car_list.extend(aeroplanes_list)
print("Extended list:", car_list, "\n")

# remove() - removes specified item, if duplicates exist, it will remove the 1st occurrence
car_list.remove("Ford")
print(car_list, "\n")

# pop() - use if we want to remove using index , if index not mentioned, will remove last item (Syntax: del list_name[index])

# del keyword - can be used to delete the whole list or an item using index []

# clear() - will clear list items but not delete the list from memory

# Looping lists - using a for loop
for x in car_list:
    print(x)
print()

print(range(len(car_list)))


# ---------------------------------------------------------------------------------------------

# 3.3 - Creating/declaring and initializing a tuple

# countries_tuple = ('Mexico', 'Qatar', 'Norway', 'Lithuania')

# print(countries_tuple, "\n")

# # 3.3 - Converting a list into a tuple using tuple() method
#
# numbers_list = [1, 2, 3, 4, 5]
# print("Our numbers list converted to a tuple: ", tuple(numbers_list), "\n")
#
#
# # 3.3 - Accessing tuple items, same as we do with lists using index operator []
# print("My favorite trip to a foreign country was", countries_tuple[2], "and my least favorite was", countries_tuple[-1], "\n")
#
# # -------------------------------------------------------------------------------
#
#
# # 3.4 - Example of using range() method within a for loop using step parameter as well to only print odd numbers
#
# for i in range(0, 10, 2):
#     print(i, end=" ")
# print("\n")
#
#
# # 3.4 - we can also decrement using the step parameter of the range() method
#
# for i in range(20, 1, -2):
#     print(i, end=" ")
# print("\n")
#
#
# # -------------------------------------------------------------------------------
#
# """
#
#     4. Mapping Data Types - Dictionaries
#
#         - A mapping is a data structure with a key-value pair that allows us to retrieve values using keys which makes things simpler.
#         Dictionaries do not allow for duplicate keys. As of python 3.7 they are ordered. If we enter duplicates it will override. Note
#         that keys are case sensitive.
#
# """
#
#
# # 4 - Examples of a basic dictionary
#
# my_dict = {1: "One", 2: "Two", 3: "Three"}
# print(my_dict, "\n")
#
#
# # 4 - Dictionary with mixed keys and a tuple as a value for one of the keys
#
# my_dict2 = {"Name": "Enes", 1: [1,2,3,4,5]}
# print(my_dict2, "\n")
#
# # 4 - Creating a dictionary using the dict() constructor
#
# my_dict3 = dict({"Ellen": 91, "George": 85})
# print(my_dict3, "\n")
#
#
# #------------------------------------------------------------------------
#
#
# """
#
#     5. Set Types: set, frozenset
#
#         5.1 - Set: an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries.
#         Set objects also support mathematical operations like union, intersection, difference, and symmetric difference. We can use the set()
#         function to create one. Sets, unlike lists or tuples, cannot have multiple occurrences of the same element and store unordered values.
#
#             Membership testing: checking if a collection of items contains a specific item.
#
# """
#
# # Creating an empty set
# empty_set = set()
#
#
# # Notice the duplicate will not be output when printing
# fruits_set = {'Apple', 'Banana', 'Kiwi', 'Mango', 'Apple'}
# print(fruits_set,"\n")
#
# # Get length of set
# print("Fruits set contains", len(fruits_set), "elements/items")

