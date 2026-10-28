""""#-------------------------------------
#Task1
#_________________________________
import sys
#print python version
print("python version", sys.version)

#print command line arguments
print("command line", sys.argv)

#now print command line arguments in terminal

#now read the arguments using command line
print("frist argument", sys.argv[0])
print("second argument", sys.argv[1])
print("third argument", sys.argv[2])

#now using sys.exit() to terminate the execution process
#sys.exit()
#for i in range(1, len(sys.argv)):
    #print(f"argument{i}: {sys.argv[i]}")"""
#-------------------------------------------------------
#Task 2
#-------------------------------------------------------
import os
current_directory = os.getcwd()
print(current_directory)
# Create a Directory(if it doesn't exit
new_directory = "rns"
if not os.path.exists(new_directory):
    os.mkdir(new_directory)
else:
    print(f"{new_directory} already exists")

#create  if a file exist
file_name="example.txt"
if os.path.exists(file_name):
    print(f"{file_name}  exists")
else:
    print(f"{file_name} does not exist")

#listing Directory contents
print("contents of the current directory")
for item  in os.listdir(current_directory):
    print(item)
print("contents of the current directory")

#4.changing the current Directory
new_directory = ("rns")
try:
    os.chdir(new_directory)
    print(f"changing directory to {os.getcwd()}")
except FileNotFoundError:
    print(f"Directory {new_directory} does not exist cannot change directory")

#example2
old_name="rns"
new_name="rns tech"
os.chdir("..")
if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"renamed {old_name} -> {new_name}")
else:
    print(f"{old_name} does not exist")

#task 4
from random import randint, choice

print(randint(1, 100))
print(choice(["Python", "Java", "AI"]))


import random as rnd
import os as operating_system

print(rnd.randint(1, 50))
print(operating_system.getcwd())

#task 5
import os

parent = os.getcwd()
source = os.path.join(parent, "audit_logs")
destination = os.path.join(parent, "audit_logs_archived")

try:
    if not os.path.isdir(source):
        print("Source directory not found.")
    elif os.path.exists(destination):
        print("Archive directory already exists.")
    else:
        os.chdir(source)
        print("Entered directory:", os.getcwd())

        os.chdir(parent)
        os.rename(source, destination)
        print("Directory renamed successfully.")

except FileNotFoundError as e:
    print("Directory not found:", e)
except PermissionError as e:
    print("Permission denied:", e)
except OSError as e:
    print("Operating system error:", e)
finally:
    try:
        os.chdir(parent)
    except OSError as e:
        print("Cleanup error:", e)
    print("Operation finished.")

