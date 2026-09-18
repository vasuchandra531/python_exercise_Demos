# ============================================================
# TASK 1: THREE PILLARS OF FUNCTION DESIGN
# ============================================================

print("TASK 1: FUNCTION DESIGN")
print("-" * 50)


# Task / Goal: Calculate square
# Input: number
# Output: square of number

def calculate_square(number):
    return number * number


result = calculate_square(5)

print("Square:", result)


# Built-in print()
print("Hello Python")
print(100)


# Built-in len()
name = "Python"
numbers = [10, 20, 30, 40]

print("Length of name:", len(name))
print("Length of list:", len(numbers))

print()


# ============================================================
# TASK 2: POSITIONAL ARGUMENTS
# ============================================================

print("TASK 2: POSITIONAL ARGUMENTS")
print("-" * 50)


def display_weather(temperature, humidity, wind_speed):
    print("Temperature:", temperature)
    print("Humidity:", humidity)
    print("Wind Speed:", wind_speed)


# Positional arguments
display_weather(22, 70, 30)

# Order:
# 22 -> temperature
# 70 -> humidity
# 30 -> wind_speed


# Missing argument example
# DO NOT RUN:
#
# display_weather()
#
# Output:
# TypeError: display_weather() missing 3 required positional arguments:
# 'temperature', 'humidity', and 'wind_speed'

print()


# ============================================================
# TASK 3: KEYWORD ARGUMENTS
# ============================================================

print("TASK 3: KEYWORD ARGUMENTS")
print("-" * 50)


# Keyword arguments
display_weather(
    humidity=80,
    wind_speed=40,
    temperature=30
)


# Order does not matter with keyword arguments.

print()


# Unexpected keyword example
# DO NOT RUN:
#
# display_weather(
#     temperature=30,
#     humidity1=80,
#     wind_speed=40
# )
#
# Output:
# TypeError: display_weather() got an unexpected keyword argument 'humidity1'


# Mixing positional and keyword arguments
display_weather(
    10,
    wind_speed=20,
    humidity=60
)


# Positional argument before keyword arguments is valid.

print()


# Invalid example
# DO NOT RUN:
#
# display_weather(wind_speed=20, 10, 60)
#
# Output:
# SyntaxError: positional argument follows keyword argument


# ============================================================
# TASK 4: DEFAULT ARGUMENTS
# ============================================================

print("TASK 4: DEFAULT ARGUMENTS")
print("-" * 50)


def adjust_lighting(
    room,
    brightness=75,
    color_temperature=4000
):
    print("Room:", room)
    print("Brightness:", brightness)
    print("Color Temperature:", color_temperature)


# Only mandatory argument
adjust_lighting("Living Room")

print()


# Override brightness
adjust_lighting(
    "Kitchen",
    brightness=50
)

print()


# ============================================================
# TASK 5: ARBITRARY POSITIONAL ARGUMENTS (*args)
# ============================================================

print("TASK 5: ARBITRARY POSITIONAL ARGUMENTS")
print("-" * 50)


def calculate_total_cost(base_cost, *items):

    print("Base Cost:", base_cost)
    print("Items:", items)
    print("Type of items:", type(items))

    total = base_cost + sum(items)

    print("Total Cost:", total)


# No dynamic arguments
calculate_total_cost(5)

print()


# Multiple dynamic arguments
calculate_total_cost(5, 10, 15, 20, 25)

print()


# ============================================================
# TASK 6: ARBITRARY KEYWORD ARGUMENTS (**kwargs)
# ============================================================

print("TASK 6: ARBITRARY KEYWORD ARGUMENTS")
print("-" * 50)


def display_user_info(**user_data):

    print("User Data:", user_data)
    print("Type of user_data:", type(user_data))


# Zero arguments
display_user_info()

print()


# Two keyword arguments
display_user_info(
    name="Alice",
    age=30
)

print()


# Three keyword arguments
display_user_info(
    name="Bob",
    age=25,
    membership="Premium"
)

print()


# ============================================================
# TASK 7: RETURN STATEMENT
# ============================================================

print("TASK 7: RETURN STATEMENT")
print("-" * 50)


def add(a, b):

    result = a + b

    return result

    # This statement will never execute
    print("This will not be printed.")


answer = add(10, 20)

print("Addition:", answer)

print()


# ============================================================
# TASK 7: MULTI-VALUE RETURN
# ============================================================


def get_metrics(base_val=10):

    return (
        base_val,
        base_val * 10,
        base_val * 100,
        base_val * 1000
    )


# Complete tuple
metrics = get_metrics(10)

print("Returned value:", metrics)
print("Type:", type(metrics))

print()


# Tuple unpacking
w, x, y, z = get_metrics(10)

print("w =", w)
print("x =", x)
print("y =", y)
print("z =", z)