# ============================================================
# PYTHON FUNCTIONS, LAMBDA & SCOPE - TASKS 1 TO 6
# ============================================================


# ============================================================
# TASK 1: FUNCTION ARGUMENT TYPES & RETURN UNPACKING
# ============================================================

print("\n========== TASK 1 ==========")


# 1. Positional Arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)


student("Vasu", 23)


# 2. Keyword Arguments
student(age=23, name="Vasu")


# 3. Default Arguments
def greet(name="Vasu"):
    print("Hello", name)


greet()
greet("Rahul")


# 4. Arbitrary Positional Arguments (*args)
def add_numbers(*args):
    print("args:", args)
    print("Type:", type(args))
    print("Sum:", sum(args))


add_numbers(10, 20, 30, 40)


# 5. Arbitrary Keyword Arguments (**kwargs)
def display_data(**kwargs):
    print("kwargs:", kwargs)
    print("Type:", type(kwargs))


display_data(name="Vasu", age=23, role="AI Engineer")


# Return Statement & Tuple Unpacking
def get_student():
    name = "Vasu"
    age = 23
    role = "AI Engineer"

    return name, age, role


name, age, role = get_student()

print("Name:", name)
print("Age:", age)
print("Role:", role)


# ============================================================
# TASK 2: LAMBDA FUNCTIONS & SINGLE-LINE EXECUTION
# ============================================================

print("\n========== TASK 2 ==========")


# Inline Lambda Function
result = (lambda a, b, c: a + b + c)(1, 2, 3)

print("Sum:", result)


# Lambda Assigned to a Variable
square = lambda x=10: x ** 2

print("Default square:", square())
print("Square of 5:", square(5))


# ============================================================
# TASK 3: CUSTOM COLLECTION SORTING USING LAMBDA
# ============================================================

print("\n========== TASK 3 ==========")


friends = [
    ("Alice", 25),
    ("Bob", 22),
    ("Charlie", 30)
]


# Sort by Age (Index 1)
friends.sort(key=lambda x: x[1])

print("Sorted by age:")
print(friends)


# Reset the List
friends = [
    ("Alice", 25),
    ("Bob", 22),
    ("Charlie", 30)
]


# Sort by Person Name Length
friends.sort(key=lambda person: len(person[0]))

print("Sorted by name length:")
print(friends)


# ============================================================
# TASK 4: DICTIONARY PACKING (**kwargs)
#          & DICTIONARY UNPACKING (**dictionary)
# ============================================================

print("\n========== TASK 4 ==========")


# Dictionary Packing using **kwargs
def receive_user_data(**kwargs):
    print("User data:", kwargs)
    print("Type:", type(kwargs))


receive_user_data(
    name="Vasu",
    age=23,
    role="AI Engineer"
)


# Standard Server Connection Function
def connect_to_server(ip, port, username, password):
    print("Connecting to server...")
    print("IP:", ip)
    print("Port:", port)
    print("Username:", username)
    print("Password:", password)


# Server Configuration Dictionary
server_info = {
    "ip": "192.168.0.1",
    "port": 22,
    "username": "admin",
    "password": "xyz"
}


# Dictionary Unpacking
connect_to_server(**server_info)


# ============================================================
# TASK 5: VARIABLE SCOPES, NAMESPACES & LOCAL VARIABLES
# ============================================================

print("\n========== TASK 5 ==========")


# Global Variables
scores = 100
accuracy = 0.95


# Function with Local Variable
def count_tokens(text):
    token_count = len(text.split())
    return token_count


# Calling the Function
result = count_tokens("sample text")

print("Token count:", result)


# NOTE:
# token_count is a local variable.
# Therefore, it cannot be accessed outside the function.
#
# If the following line is uncommented, it will produce:
# NameError: name 'token_count' is not defined

# print(token_count)


# ============================================================
# TASK 6: MODIFYING GLOBAL STATE USING global KEYWORD
# ============================================================

print("\n========== TASK 6 ==========")


# Global Variable
accuracy = 0.85


# Function to Modify Global Variable
def update_accuracy():
    global accuracy

    accuracy = 0.90


print("Before update:", accuracy)

update_accuracy()

print("After update:", accuracy)


# ============================================================
# END OF ALL TASKS
# ============================================================

print("\n========== ALL TASKS COMPLETED ==========")