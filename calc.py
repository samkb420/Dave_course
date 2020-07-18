def add(a,b):
	c = a + b
	return c

def sub(a,b):
	c = a - b
	return c

def mult(a,b):
	c = a * b
	return c

def div(a,b):
	c = a / b
	return c

menu = '''
		Simple calc made by Dave

		01. Add \n
		02. Subtract \n
		03. Multiply \n
		04. Divide 

	'''

print(menu)
# inputs
num1 = int(input('Enter a number:'))
num2 = int(input('Enter a number 2:'))

# get values from the func 
added = add(num1,num2)
subtracted = sub(num1,num2)
multplied = mult(num1,num2)
division = div(num1,num2)

# print outout

print(f"The sum of {num1} and {num2} is {added}")
print(f"The diffrence of {num1} and {num2} is {subtracted}")
print(f"The mutiple of {num1} and {num2} is {multplied}")
print(f"The Quotient of {num1} and {num2} is {division}")



# operaters

''' maths
addation +
sub -
division /
mult *

-----------------
logical oparetors
And  &&
Or   ||
Not !=


'''

# condations

# if 
# else
#elif


dave_age = 16
sam_age = 21

if sam_age < 18:
	print('You are under age')
else:
	print("You are an adult")


