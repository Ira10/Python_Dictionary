#####  2nd Oct

import sys

# sample Dictionaries
dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}

# print the sizes of sample Dictionaries
print("Size of dic1: " + str(sys.getsizeof(dic1)) + "bytes")
print("Size of dic2: " + str(sys.getsizeof(dic2)) + "bytes")
print("Size of dic3: " + str(sys.getsizeof(dic3)) + "bytes")

# Size of dic1: 232bytes
# Size of dic2: 232bytes
# Size of dic3: 232bytes

# sample Dictionaries
dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"} 


# print the sizes of sample Dictionaries
print("Size of dic1: " + str(dic1.__sizeof__()) + "bytes")
print("Size of dic2: " + str(dic2.__sizeof__()) + "bytes")
print("Size of dic3: " + str(dic3.__sizeof__()) + "bytes")


# Size of dic1: 216bytes
# Size of dic2: 216bytes
# Size of dic3: 216bytes


# 1. sys.getsizeof()
# Functionality: This function returns the total memory size of an object, including the size of its contents (like nested objects).
# Usage: It is more comprehensive and accounts for the overhead associated with the object itself and any additional space used by elements within it.
# 2. __sizeof__()
# Functionality: This method returns the size of the object itself, excluding any references to objects it contains.
# Usage: It provides a lower-level view of memory usage, focusing only on the object's immediate attributes.


# Expected Results
# You will likely see that:
# The sizes reported by sys.getsizeof() will be larger than those reported by __sizeof__(). This is because sys.getsizeof() includes the memory used by all elements contained in the dictionary.
# The difference in size can be significant depending on how many items are in each dictionary and their types.