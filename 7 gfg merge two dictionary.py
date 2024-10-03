# ######  3rd Oct

dict1 = {'a':10, 'b':8}
dict2 = {'d':6, 'd':12}

print(dict1.update(dict2))     ### None

###  1. 'update' function

# # By using the method update() in Python, one dictionary can be merged into another. But in this, the second dictionary is merged into the first dictionary and no new list is created. It returns None. In this example, we are using the update function to merge two dictionaries.

# # Python code to merge dict using update() method
def Merge_(dict1, dict2):
    return(dict2.update(dict1))


# # Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# This returns None
print(Merge_(dict1, dict2))    ### None

# changes made in dict2
print(dict2)    ### {'d': 6, 'c': 4, 'a': 10, 'b': 8}


######    2. Python unpacking operator


def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res
    
# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = Merge(dict1, dict2)
print(dict3)  # {'a': 10, 'b': 8, 'd': 6, 'c': 4}


# ######   3. Using  '|'


def Merge(dict1, dict2): 
    res = dict1 | dict2
    return res 
      
# Driver code 
dict1 = {'x': 10, 'y': 8} 
dict2 = {'a': 6, 'b': 4} 
dict3 = Merge(dict1, dict2) 
print(dict3)   # {'x': 10, 'y': 8, 'a': 6, 'b': 4}


########   4. merge


def Merge(dict1, dict2):
    for i in dict2.keys():
        print(i)
        print(dict2[i])
        dict1[i]=dict2[i]
        print(dict1[i])
    return dict1

# a
# 6
# 6
# b
# 4
# 4
    
# Driver code
dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}
dict3 = Merge(dict1, dict2)
print(dict3)   # {'x': 10, 'y': 8, 'a': 6, 'b': 4}




