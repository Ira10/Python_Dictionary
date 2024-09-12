### 12th Sep

# Python code to demonstrate Dictionary and
# missing value error
d = { 'a' : 1 , 'b' : 2 }

# trying to output value of absent key 
print ("The value associated with 'c' is : ")
print (d['c'])   # KeyError: 'c'


ele = {'a': 5, 'c': 8, 'e': 2}
if "q" in ele:
	print(ele["d"])
else:
	print("Key not found")


country_code = {'India': '0091',
				'Australia': '0025',
				'Nepal': '00977'}

try:
	print(country_code['India'])
	print(country_code['USA'])
except KeyError:
	print('Not Found')
	
#     0091
# Not Found


