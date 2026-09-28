# TASK 4: TRY-EXCEPT

# Example 1: FileNotFoundError
try:
    file = open("data.txt", "r")
    print(file.read())
except FileNotFoundError as e:
    print("Error: The requested file was not found.")

# Example 2: ZeroDivisionError
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero.")

# Generic exception
try:
    number = int("abc")
except Exception as e:
    print("Error: An unexpected error occurred.")


#=================================================

# TASK 5: FINALLY

file = None

try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("Error: File not found.")

finally:
    print("Execution of try-except block is completed.")

#=======================================================

# TASK 6: ELSE + EXCEPTION ORDERING

try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("Error: File not found.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except Exception as e:
    print("Unexpected error:", e)

else:
    print("File operation completed successfully.")

finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("File closed.")