"""
name="Vasu chandra" #String Data type

age=22 #integer data type

print("before concatenation " +name)

name="Domathoti"

print(age)


print("after concatenation " +name)

#we can assign multiple variables like this
temperature, user_age, a= 30,22,'a value'
print(temperature, user_age, a)
"""

"""# Demonstrating Case Sensitivity in Python

name= "vasu Chandra"
Name, age= "Domathoti", 22
print(Name, age)
print(name)

name= "vasu Chandra"
Name, age= "Domathoti", 22
print(name, age)
print(Name)
"""

"""
Module Summary:
This script demonstrates PEP 8 commenting standards.
It shows how to use single-line and multi-line comments to explain WHY logic exists,
rather than stating obvious syntax.
"""

# Good single-line comment: Explains WHY we do something
counter = 0
# Reset counter to zero at program start to ensure accurate tracking of user actions

# Example of a calculation
user_age = 20
# Apply age-based discount because users under 21 qualify for student pricing
discount = 0.15 if user_age < 21 else 0.05

#  Bad comment (obvious syntax)
# Increment counter by 1
counter += 1

#  Refactored good comment
# Increment counter to record a new login attempt for security monitoring

# Multi-line comment explaining a block of logic
"""
This block handles user account activation.
We check if the email has been verified before enabling access.
This prevents unauthorized users from bypassing the verification process.
"""
is_verified = True
is_active = False

if is_verified:
    # Good comment: WHY, not WHAT
    # Activate the user account only after successful email verification
    is_active = True

print("Counter:", counter)
print("Discount:", discount)
print("Account Active:", is_active)

#  Valid variable names (snake_case style)
max_value = 100
person_weight = 72.5
user_name = "Alex"

# Constants (ALL_CAPS style)
PI = 3.14159
DAYS_IN_A_YEAR = 365
MAX_CONNECTIONS = 100

# Invalid variable names (will cause errors)
# 1variable = "Invalid"   # Cannot start with a digit
# user-name = "Invalid"   #  Hyphens not allowed
# user name = "Invalid"   #  Spaces not allowed

#  Reserved keywords (invalid)
# if = "keyword"          #  'if' is reserved in Python

# ⚠️ Shadowing built-in names (discouraged)
list = [1, 2, 3]          # ⚠️ Avoid using 'list' as a variable name
string = "Hello"          # ⚠️ Avoid shadowing built-in types

# ✅ CamelCase is reserved for class names
class StudentProfile:
    def __init__(self, name, age):
        self.name = name
        self.age = age



