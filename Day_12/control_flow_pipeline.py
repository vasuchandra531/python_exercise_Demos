# Task 1: Dictionary Comprehension, Boolean Values,
# and Logical Operators

# Dictionary
student_marks = {
    "Krishna": 75,
    "Vasu": 85,
    "Ravi": 65,
    "Arun": 55
}

# Dictionary comprehension using .items()
passed_students = {
    name: marks
    for name, marks in student_marks.items()
    if marks >= 70
}

print("Original Dictionary:")
print(student_marks)

print("\nStudents who scored 70 or above:")
print(passed_students)


# Boolean values
print("\nBoolean Integer Mapping:")
print("True == 1:", True == 1)
print("False == 0:", False == 0)

print("Integer value of True:", int(True))
print("Integer value of False:", int(False))


# String truthiness
empty_string = ""
non_empty_string = "Python"

print("\nString Truthiness:")

if empty_string:
    print("Empty string is True")
else:
    print("Empty string is False")

if non_empty_string:
    print("Non-empty string is True")
else:
    print("Non-empty string is False")


# Logical operators
age = 23
has_id = True

print("\nLogical Operators:")

print("age >= 18 and has_id:", age >= 18 and has_id)
print("age < 18 or has_id:", age < 18 or has_id)
print("not has_id:", not has_id)


# Task 2: Student Grading Program

mark = 75

print("Student Mark:", mark)

if mark >= 40:
    print("Result: Passed")

    if mark >= 90:
        print("Grade: A")
    elif mark >= 75:
        print("Grade: B")
    elif mark >= 60:
        print("Grade: C")
    else:
        print("Grade: D")

else:
    print("Result: Failed")

# Task 2: Temperature Alert System

temperature = 28

print("Temperature:", temperature, "°C")

if temperature < 0:
    print("Alert: Freezing")
elif temperature <= 14:
    print("Alert: Cold")
elif temperature <= 24:
    print("Alert: Mild")
else:
    print("Alert: Hot")


# Task 3: Tweet Keyword Filtering

tweets = [
    "Exploring AI applications",
    "Machine learning is the future",
    "Having lunch",
    "New GenAI advances"
]

print("Tweets related to AI or Machine Learning:\n")

for tweet in tweets:
    tweet_lower = tweet.lower()

    if "ai" in tweet_lower or "machine learning" in tweet_lower:
        print(tweet)

# Task 3: Case-Sensitive vs Case-Insensitive Search

comments = [
    "Great service",
    "Excellent response time",
    "Had to wait",
    "Excellent support"
]

print("Searching without lower():\n")

for comment in comments:
    if "excellent" in comment:
        print(comment)

print("\nSearching with lower():\n")

for comment in comments:
    if "excellent" in comment.lower():
        print(comment)


# Task 3: Temperature Threshold Monitoring

temperatures = [72, 85, 78, 92, 81, 65, 88]

threshold = 80

print("Temperature Monitoring\n")

for temperature in temperatures:
    if temperature > threshold:
        print("WARNING:", temperature, "degrees exceeds the threshold.")
    else:
        print("Normal:", temperature, "degrees.")

# Task 4: Single Argument range()

print("Numbers generated using range(5):")

for number in range(5):
    print(number)

# Task 4: range(start, stop)

print("Numbers from 1 to 100:")

for number in range(1, 101):
    print(number)

# Task 4: List Casting

numbers = list(range(1, 11))

print("List of numbers:")
print(numbers)

# Task 4: Even Numbers using Step

even_numbers = list(range(2, 101, 2))

print("Even numbers from 2 to 100:")
print(even_numbers)

# Task 4: Multiples of 10

multiples_of_10 = list(range(10, 101, 10))

print("Multiples of 10:")
print(multiples_of_10)

# Task 5: Ignoring the Loop Variable

print("Using a normal loop variable:")

for i in range(5):
    print("Analyzing data...")


print("\nUsing underscore for an unused variable:")

for _ in range(5):
    print("Analyzing data...")