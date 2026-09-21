# ================================================================
# TASK 1: LAMBDA, **KWARGS & GLOBAL
# ================================================================

print("\n =================================")
square = lambda x: x * x
print("Square:", square(5))

students = [("Vasu", 85), ("Ravi", 72), ("Anil", 91)]
students.sort(key=lambda x: x[1], reverse=True)
print("Sorted:", students)

def student_info(name, age, course):
    print(name, age, course)

student = {"name": "Vasu", "age": 23, "course": "Python"}
student_info(**student)

count = 10
def update():
    global count
    count += 5
update()
print("Global count:", count)


# ================================================================
# TASK 2: FILE CRUD OPERATIONS
# ================================================================

print("\n =================================")
file_name = "crud.txt"

# CREATE / WRITE
with open(file_name, "w") as f:
    f.write("First record\nSecond record\n")

# READ
with open(file_name, "r") as f:
    print("Read:", f.read())

# UPDATE / APPEND
with open(file_name, "a") as f:
    f.write("Third record\n")

# DELETE / OVERWRITE
with open(file_name, "w") as f:
    f.write("Fresh content\n")

with open(file_name, "r") as f:
    print("Final:", f.read())


# ================================================================
# TASK 3: TEXT, BINARY & FILE PATHS
# ================================================================

print("\n =================================")
import os

path = "./config.txt"

# TEXT FILE
with open(path, "w", encoding="utf-8") as f:
    f.write("Python File Handling\n")

print("Relative Path:", path)
print("Absolute Path:", os.path.abspath(path))

with open(path, "r", encoding="utf-8") as f:
    print("Text:", f.read())

# BINARY FILE
with open("./sample.bin", "wb") as f:
    f.write(b"Binary Data")

with open("./sample.bin", "rb") as f:
    print("Binary:", f.read())


# ================================================================
# TASK 4: read(n), tell() & seek()
# ================================================================

print("\n =================================")
with open("cursor.txt", "w") as f:
    f.write("Python file handling is easy and powerful. "
            "We can read, tell, and seek within a file.")

with open("cursor.txt", "r") as f:
    print("read(8):", f.read(8))
    print("Position:", f.tell())
    f.seek(50)
    print("After seek:", f.tell())
    print("Remaining:", f.read())


# ================================================================
# TASK 5: MANUAL CLOSE & CONTEXT MANAGER
# ================================================================

print("\n =================================")
with open("resource.txt", "w") as f:
    f.write("Resource management")

f = open("resource.txt", "r")
print("Manual:", f.read())
f.close()
print("Closed:", f.closed)

with open("resource.txt", "r") as f:
    print("Context:", f.read())

print("Auto Closed:", f.closed)


# ================================================================
# TASK 6: splitlines(), WRITE & APPEND
# ================================================================

print("\n =================================")
with open("logs.txt", "w") as f:
    f.write("Login successful\n")
    f.write("File opened\n")
    f.write("Data processed\n")

with open("logs.txt", "r") as f:
    lines = f.read().splitlines()

print("Lines:", lines)
print("First:", lines[0])

# WRITE = OVERWRITE
with open("logs.txt", "w") as f:
    f.write("Old content replaced\n")

# APPEND = PRESERVE + ADD
with open("logs.txt", "a") as f:
    f.write("New log 1\n")
    f.write("New log 2\n")

with open("logs.txt", "r") as f:
    print("Logs:\n", f.read())


# ================================================================
# TASK 7: CSV, next(), DICTIONARY & MAX TOKENS
# ================================================================

print("\n =================================")
import csv

with open("token_usage.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["date", "user", "request", "tokens"])
    writer.writerow(["2026-09-15", "Vasu", "Python", 1200])
    writer.writerow(["2026-09-16", "Vasu", "Files", 1800])
    writer.writerow(["2026-09-17", "Vasu", "CSV", 2500])
    writer.writerow(["2026-09-18", "Vasu", "Lambda", 2100])

with open("token_usage.csv", "r", newline="") as f:
    csv_reader = csv.reader(f)

    header = next(csv_reader)
    print("Header:", header)

    daywise_tokens = {
        row[0]: int(row[3])
        for row in csv_reader
    }

max_day = max(daywise_tokens, key=daywise_tokens.get)
print("Daywise:", daywise_tokens)
print("Maximum Date:", max_day)
print("Maximum Tokens:", daywise_tokens[max_day])