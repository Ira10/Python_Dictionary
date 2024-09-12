### 12th Sep

dict = {'indrani':24,
        'ira':24,
        'puchu':16}

print(dict['indrani']) # 24

############                ############################               ############################
# Now taking input from user


####################################################################################
# Using 'for' loop 

user_dict = {}

num_entries = int(input("Enter the number of entries you want to add: "))

for i in range(num_entries):
	key = input("Enter key: ")
	value = input("Enter value: ")
	user_dict[key] = value

print("Dictionary after adding user input:", user_dict)


####################################################################################
## Using dictionary comprehension

num_entries = int(input("Enter the number of entries you want to add: "))

user_dict = {input(f"Enter key {i+1}: "): input(f"Enter value {i+1}: ") for i in range(num_entries)}

print("Dictionary after adding user input:", user_dict)

# Enter the number of entries you want to add: 2
# Enter key 1: ir
# Enter value 1: 23
# Enter key 2: pu
# Enter value 2: 22
# Dictionary after adding user input: {'ir': '23', 'pu': '22'}


####################################################################################
### using update method 

user_dict = {}

num_entries = int(input("Enter the number of entries you want to add: "))

for i in range(num_entries):
	key = input("Enter key: ")
	value = input("Enter value: ")
	user_dict.update({key: value})

print("Dictionary after adding user input:", user_dict)


# Enter the number of entries you want to add: 2
# Enter key: ku
# Enter value: 6
# Enter key: ko
# Enter value: 6
# Dictionary after adding user input: {'ku': '6', 'ko': '6'}