# ============================================================
# PYTHON FILE OPERATIONS, CSV, JSON & API TASKS
# ============================================================

import csv
import json
import os


# ============================================================
# TASK 1: FILE CRUD OPERATIONS & CSV READER
# ============================================================

print("\n" + "=" * 60)
print("TASK 1: FILE CRUD OPERATIONS & CSV READER")
print("=" * 60)

# CREATE / WRITE
with open("task1.txt", "w") as file:
    file.write("Python File Operations\n")
    file.write("CSV and JSON Practice\n")

# READ
with open("task1.txt", "r") as file:
    content = file.read()

print("READ OUTPUT:")
print(content)

# UPDATE / APPEND
with open("task1.txt", "a") as file:
    file.write("File updated using append mode.\n")

# READ UPDATED FILE
with open("task1.txt", "r") as file:
    updated_content = file.read()

print("UPDATED FILE:")
print(updated_content)

# CSV READER
with open("task1.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "score"])
    writer.writerow(["Vasu", 90])
    writer.writerow(["Rahul", 85])

print("CSV DATA AFTER SKIPPING HEADER:")

with open("task1.csv", "r", newline="") as file:
    csv_reader = csv.reader(file)

    # Skip header
    next(csv_reader)

    for row in csv_reader:
        print(row)


# ============================================================
# TASK 2: CSV WRITER, WRITEROW() & newline=''
# ============================================================

print("\n" + "=" * 60)
print("TASK 2: CSV WRITER & WRITEROW()")
print("=" * 60)

with open("task2.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Header
    writer.writerow(["day", "tokens_used"])

    # Data rows
    writer.writerow(["Monday", 1200])
    writer.writerow(["Tuesday", 1500])
    writer.writerow(["Wednesday", 1800])

print("CSV FILE CREATED SUCCESSFULLY.")

with open("task2.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

print("newline='' prevents unwanted blank lines in CSV files.")


# ============================================================
# TASK 3: BATCH CSV WRITING & TEXT-TO-CSV CONVERSION
# ============================================================

print("\n" + "=" * 60)
print("TASK 3: WRITEROWS() & TEXT-TO-CSV CONVERSION")
print("=" * 60)

# 2D list containing multiple records
model_data = [
    ["model", "accuracy", "response_time", "tokens"],
    ["GPT", 0.95, 1.2, 1200],
    ["BERT", 0.91, 1.5, 1500],
    ["Llama", 0.93, 1.3, 1300]
]

# Batch writing using writerows()
with open("model_performance.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(model_data)

print("MODEL PERFORMANCE CSV:")

with open("model_performance.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# ------------------------------------------------------------
# TEXT-TO-CSV CONVERSION
# ------------------------------------------------------------

# Create comma-separated text file
with open("input.txt", "w") as file:
    file.write("Python,95,1.2\n")
    file.write("Java,90,1.5\n")
    file.write("C++,88,1.7\n")

# Convert text file to CSV
with open("input.txt", "r") as input_file:
    with open("converted.csv", "w", newline="") as output_file:

        writer = csv.writer(output_file)

        for line in input_file:
            values = line.strip().split(",")
            writer.writerow(values)

print("\nTEXT-TO-CSV CONVERSION:")

with open("converted.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# ============================================================
# TASK 4: JSON DATA ARCHITECTURE & json.load()
# ============================================================

print("\n" + "=" * 60)
print("TASK 4: JSON DATA ARCHITECTURE & JSON.LOAD()")
print("=" * 60)

# Create JSON configuration file
config_data = {
    "default_parameters": {
        "temperature": 0.7,
        "max_tokens": 1000
    },
    "user_prompts": {
        "welcome_message": "Welcome to Python!",
        "farewell_message": "Thank you for using the application."
    }
}

with open("config.json", "w") as file:
    json.dump(config_data, file, indent=4)

# Load JSON file
with open("config.json", "r") as file:
    config = json.load(file)

print("Type of config:")
print(type(config))

# Nested key lookups
temperature = config["default_parameters"]["temperature"]
farewell_message = config["user_prompts"]["farewell_message"]

print("Temperature:", temperature)
print("Farewell Message:", farewell_message)


# ============================================================
# TASK 5: WEB API REQUESTS & RESPONSE PARSING
# ============================================================
"""
print("\n" + "=" * 60)
print("TASK 5: WEB API REQUESTS & RESPONSE PARSING")
print("=" * 60)

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

print("HTTP Status Code:", response.status_code)

# ------------------------------------------------------------
# METHOD A: json.loads(response.text)
# ------------------------------------------------------------

data_method_a = json.loads(response.text)

print("\nMETHOD A: json.loads(response.text)")
print("Data Type:", type(data_method_a))
print("First Post ID:", data_method_a[0]["id"])
print("First Post Title:", data_method_a[0]["title"])


# ------------------------------------------------------------
# METHOD B: response.json()
# ------------------------------------------------------------

data_method_b = response.json()

print("\nMETHOD B: response.json()")
print("Data Type:", type(data_method_b))
print("First Post ID:", data_method_b[0]["id"])
print("First Post Title:", data_method_b[0]["title"])
"""

# ============================================================
# TASK 6: HTTP STATUS CODE CATEGORIZATION
# ============================================================

print("\n" + "=" * 60)
print("TASK 6: HTTP STATUS CODE CATEGORIZATION")
print("=" * 60)

status_codes = {
    200: "OK - Request succeeded",
    201: "Created - Resource successfully created",
    204: "No Content - Request succeeded without response data",

    301: "Moved Permanently - Resource permanently moved",
    302: "Found - Temporary redirection",

    400: "Bad Request - Invalid or malformed request",
    401: "Unauthorized - Authentication required",
    403: "Forbidden - Permission denied",
    404: "Not Found - Resource does not exist",
    405: "Method Not Allowed - HTTP method is not allowed",
    429: "Too Many Requests - Rate limit exceeded",

    500: "Internal Server Error - Server encountered an error",
    502: "Bad Gateway - Invalid upstream response",
    503: "Service Unavailable - Server temporarily unavailable"
}

for code, description in status_codes.items():
    if 200 <= code <= 299:
        category = "2xx SUCCESS"
    elif 300 <= code <= 399:
        category = "3xx REDIRECTION"
    elif 400 <= code <= 499:
        category = "4xx CLIENT ERROR"
    elif 500 <= code <= 599:
        category = "5xx SERVER ERROR"
    else:
        category = "UNKNOWN"

    print(f"{code}: {category} -> {description}")


# ============================================================
# END OF PROGRAM
# ============================================================

print("\n" + "=" * 60)
print("ALL 6 TASKS COMPLETED SUCCESSFULLY")
print("=" * 60)