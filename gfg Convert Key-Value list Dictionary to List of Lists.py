# The original dictionary is : {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
# The converted list is : [['gfg', 1, 3, 4], ['is', 7, 6], ['best', 4, 5]]


dict_ =  {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}

res = []

for key, value in dict_.items():
    res.append([key] + value)
print(res)  ## [['gfg', 1, 3, 4], ['is', 7, 6], ['best', 4, 5]]

#   res.append(key + value)
#                ~~~~^~~~~~~
# TypeError: can only concatenate str (not "list") to str



# [['gfg', 1, 3, 4]]
# [['gfg', 1, 3, 4], ['is', 7, 6]]
# [['gfg', 1, 3, 4], ['is', 7, 6], ['best', 4, 5]]

