# ##########  28th Oct

test_dict = {'gfg' : 4, 'best' : 9}
test_list = [8, 2]

def dic_list(L, dic):
    # Create an empty dictionary to hold the result
    my_dict = {}
    
    # Check if both lists are of the same length
    if len(dic) == len(L):
        # Loop over both list and dictionary items using zip
        for key, (dict_key, dict_value) in zip(L, dic.items()):
            # Create a nested dictionary with capitalized key
            my_dict[key] = {dict_key.capitalize(): dict_value}
    
    return my_dict

print(dic_list(test_list, test_dict))   ## {8: {'Gfg': 4}, 2: {'Best': 9}}




# *The `zip()` function in Python is used to combine two or more iterables (e.g., lists, tuples, etc.) into a single iterable of tuples, where each tuple contains elements from the corresponding positions in the input iterables.*

### Syntax:
# ```python
# zip(iterable1, iterable2, ...)
# ```

# ### Example:
# ```python
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']

# zipped = zip(list1, list2)
# print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
# ```

# In this example:
# - The first elements from both lists (`1` and `'a'`) are combined into a tuple.
# - The second elements (`2` and `'b'`) are combined into another tuple, and so on.

# ### Key Points:
# 1. **Shortest Length**: The `zip()` function stops when the shortest input iterable is exhausted. If the iterables have different lengths, the extra elements from the longer iterables will be ignored.
#    ```python
#    list1 = [1, 2, 3]
#    list2 = ['a', 'b']
   
#    zipped = zip(list1, list2)
#    print(list(zipped))  # Output: [(1, 'a'), (2, 'b')]
#    ```

# 2. **Unzipping**: You can "unzip" a zipped object by using the `*` operator:
#    ```python
#    zipped = zip([1, 2, 3], ['a', 'b', 'c'])
#    list1, list2 = zip(*zipped)
#    print(list1)  # Output: (1, 2, 3)
#    print(list2)  # Output: ('a', 'b', 'c')
#    ```

# 3. **Common Uses**:
#    - To iterate over multiple sequences in parallel.
#    - To create pairs of elements from multiple lists.

# ### Example of Iterating Over Two Lists Simultaneously:
# ```python
# list1 = [10, 20, 30]
# list2 = ['a', 'b', 'c']

# for num, letter in zip(list1, list2):
#     print(f"Number: {num}, Letter: {letter}")
# ```
# **Output**:
# ```
# Number: 10, Letter: a
# Number: 20, Letter: b
# Number: 30, Letter: c
# ```

# This makes `zip()` very useful when you need to process elements from multiple iterables together.
