list_ = ['apple','banana','watermelon','avocado']

dict_ = {}

for i in range(len(list_)):
    dict_[list_[i]] = len(list_[i])

print(dict_)  # {'apple': 5, 'banana': 6, 'watermelon': 10, 'avocado': 7}
    
