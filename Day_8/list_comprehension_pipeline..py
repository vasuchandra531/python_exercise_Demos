# Task 1: List Concatenation vs. Augmented Assignment Memory Test
list1 = [2, 3]
print("List1 Initial ID:", id(list1))
list1 = list1 + [4, 5] # Creates NEW memory location
print("List1 Post-'+' ID (New Address):", id(list1))
list2 = [2, 3]
print("\nList2 Initial ID:", id(list2))
list2 += [4, 5] # Modifies IN-PLACE (Same Address)
print("List2 Post-'+=' ID (Same Address):", id(list2))


# Task 2: For Loop Iteration & Membership Search
ip_list = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4"]
target_ips = ["10.0.0.2", "10.0.0.5"]
print("\n--- Membership Search Results ---")
for ip in target_ips:
    if ip in ip_list:
        print(f"IP {ip} found in network list.")
    else:
        print(f"IP {ip} NOT found in network list.")


# Task 3: Shared References vs. Shallow Copying
list_a = [1, 2, 6]
list_b = list_a # Shared reference (Deep copy behavior)
list_b.append(4)
print("\n--- Shared Reference Assignment ---")
print("List A:", list_a, "| ID:", id(list_a))
print("List B:", list_b, "| ID:", id(list_b))
list_c = list_a.copy() # Shallow copy (Isolated reference)
list_c.append(99)
print("\n--- Shallow Copy (.copy()) ---")
print("List A:", list_a, "| ID:", id(list_a))
print("List C:", list_c, "| ID:", id(list_c))

# Task 4: List Comprehensions
numbers = [1-11] # Numerical Filtering (Divisible by 7)
div_by_7 = [num for num in numbers if num % 7 == 0]
print("\n--- List Comprehension Results ---")
print("Numbers Divisible by 7:", div_by_7)
# String Normalization
contributors = ["alice", "BOB", "charlie"]
capitalized = [name.capitalize() for name in contributors]
print("Capitalized Contributors:", capitalized)
# Common Elements Across Lists
ai_team = ["Alice", "Bob", "Charlie", "David"]
data_team = ["Alice", "Charlie", "Eve", "Frank"]
common_members = [name for name in ai_team if name in data_team]
print("Common Team Members:", common_members)



