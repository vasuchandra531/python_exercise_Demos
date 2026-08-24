#Arithmetic Operators, Division Types, & Powers
#1. Standard Division (/) vs. Floor Division (//):
# standard division
print(8/2) #Document that standard division always returns a float
print(38/2)
print(9/2)
# floor Division
print(9//2) #Document that floor division rounds down to the nearest whole number and returns an int.

#2. Exponentiation (**) & Modulus (%):
#Exponent
print(10**2)
#Modulus
print(7%2)

#Mixed Types
#adding int and float values
a=10
b=20.5
print(a+b)
#subtract
print(a-b)
#multiplying
print(a*b)

#Operator Precedence
print((2 + 4) * 2 ** 3 )

#Quote Consistency & Escape Characters (\):
message= 'Ai says ,I\'m here to assist you'
print(message)

#Multi-Line Strings & Newlines (\n, \t):
response="Capture terminal user inputs, \ndemonstrate default string behavior, \nand perform explicit type conversion for arithmetic operations"
print(response)

response="Capture terminal user inputs, \tdemonstrate default string behavior, \tand perform explicit type conversion for arithmetic operations"
print(response)

#1.	Default input() Behavior
training_hours=input("Enter your training hours:")
print(training_hours)
print(type(training_hours))

#2.Concatanation in input behavior
name=input("Enter your name:")
age=input("Enter your age:")
print(name+"is "+age+" years old.")

"""#1.	Handling Arithmetic without Type Casting (int()):
training_hours=input("Enter your training hours:")
print(training_hours)
print(type(training_hours))
iterations=input("Enter your number of iteterations:")
datasets=input("Enter your number of datasets:")
total = iterations*datasets
print(total)"""

#2.	Handling Arithmetic with Type Casting (int()):
training_hours=input("Enter your training hours:")
print(training_hours)
print(type(training_hours))
iterations=int(input("Enter your number of iteterations:"))
datasets=int(input("Enter your number of datasets:"))
total = iterations*datasets
print(total)











