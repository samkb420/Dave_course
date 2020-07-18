# this is a comment


# Simple hellow world program

print("hellow world")


name = "david njunguna"  # str

print(name)

number = 120  # int

number2 = 12.5 # float


print(type(number))
print(type(number2))


# Boolean ie. True or False

is_male = True

is_female = False


print(type(is_female))
print(type(is_male))

# list
fruits = ["banana","mango","apple"]

print(fruits[0])
print(fruits)

# dict

user = {
	'name':'David joe',
	'id':12345,
	'age':20,
}

print(user)

print(user.values())
print(user.keys())


# func

def add(a,b):
	c  = a + b
	return c

result = add(5,3)

print(result)

# inputs

username = input("Enter your name:")  # sring formating

print(f"Welcome {username} to our program ")


# loops 

# for loops
# create a list with valiable name nums with 0-9

nums = [0,1,2,3,4,5,6,7,8,9]

for i in nums:
	print(i)

######
######
######
######

# print('######')
# print('######')
# print('######')
# print('######')

for i in range(0,4):
	print('#'*4, end=' ')





