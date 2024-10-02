### Python program to find the sum of all items in a dictionary
###  2nd Oct

Input = {'a': 100, 'b':200, 'c':300}
sum_= 0
for i in Input:
    print(i, " : ", Input[i])
    sum_ += Input[i]

print(sum_)

# a  :  100
# b  :  200
# c  :  300
# 600


# #### 2. Using 'values'


def returnSum(dict):

	sum = 0
	for i in dict.values():
		sum = sum + i

	return sum


# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))    ## 600


############         3           ###########################
import functools

dic = {'a': 100, 'b': 200, 'c': 300}

sum_dic = functools.reduce(lambda ac,k: ac+dic[k], dic, 0)

# sum_dic = functools.reduce(lambda ac,k: ac+dic[k], dic, 3)


print("Sum :", sum_dic)   # Sum : 600 

# print("Sum :", sum_dic)   # Sum : 603 