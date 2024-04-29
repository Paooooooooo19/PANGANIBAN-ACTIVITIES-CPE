# Using + Concatenate Strings in Python using 4 variables concatenate them with spaces
a = "John"
b = "Paolo"
c = "D."
d = "Panganiban"

pao = a + " " + b + " " + c + " " + d

print(pao)

# Using + Concatenate Strings in Python get two strings from user input and concatenate them
fstr= input("Enter the first string: ")
sstr = input("Enter the second string: ")

output = fstr + " " + sstr

print(output)

# Using + Concatenate in Python using your name and your age in a paragraph
name = "Pao"
age = 21

paragraph = "My name is " + name + " and I am " + str(age)

print(paragraph)

# Create a Python program to perform Addition Subtraction Multiplication and Division using two numbers

print("please enter a value to perform an Addition, Subtraction, Multiplication & Addition")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

add = num1 + num2
sub = num1 - num2
multipli = num1 * num2
divide = num1 / num2
divi = num1 // num2 

print("sum: ", add)
print("difference: ", sub)
print("product: ", multipli)
print("quotient: " + str(divide) + " Without Decimal: " + str(divi))