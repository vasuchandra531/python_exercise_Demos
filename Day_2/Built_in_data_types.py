#Numeric Data Types & Operator Evaluation
from ipaddress import ip_address

age=25 #integer data type
temperature=12.3 #float data type
#perform assignment operator
print(age)
print(id(age))
print(temperature)
print(id(temperature))
#perform comparison operator
print(age==40) #comparison operator


#Perform arithmetic operations using augmented assignment operators
a=10
print(a)
print(id(a))

a+=5
print(a)
print(id(a))

a-=5
print(a)
print(id(a))

a*=5
print(a)
print(id(a))

#perform increment and decrement in python
a=10
a+=1 #increment
print(a)
print(id(a))

a-=1
print(a) #decrement
print(id(a))


#Strings & Utility Functions (len() and type())
model_name="oneplusnord5"
print(model_name)
print(id(model_name))
#implementing len() function
print(len(model_name))
print(id(len(model_name)))
#implementing type() function
print(type(model_name))
print(id(type(model_name)))
print(type(temperature))
print(id(type(temperature)))

#Collection Data Structures (Lists, Tuples, Sets, & Dictionaries)
#list[] function order mutable sequence
person=["RNS",13,"Rise n shine",13.5,True]# allows duplicate
print(person)
print(id(person))
#tuple() function order immutable sequence
person=("RNS",13,"Rise n shine",13.5,True,13)# allows duplicate
print(person)
print(id(person))
#sets {} mutable collections of unorder unique objects
ip_address={'1.0.0.3.4','13.34.53.','1.0.0.3.4'}#it removes duplicates
print(ip_address)
print(id(ip_address))
#Dictionary{} collection of unorder key-value pairs
employee= {"name":"rise","age":13,}
print(employee)
print(id(employee))
#override in dictionary
employee= {"name":"rise","age":13,"age":14}
print(employee)
print(id(employee))

#Mutability & Memory Address Analysis using id()
#Immutable Integer Test
x=10
print(x)
print(id(x))
x=20
print(id(x))
#Mutable List Test
numbers=[1,2,3,4,5]
print(numbers)
print(id(numbers))
numbers.append(6)
print(numbers)
print(id(numbers))
