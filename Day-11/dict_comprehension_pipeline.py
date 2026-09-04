#Set Comprehensions & PEP 8 String Normalization
# Uncleaned contributor names
names = {"alice", "BOB", "charlie", "DAVID"}

# Single-line set comprehension
cleaned_names = {name.capitalize() for name in names}

print(cleaned_names)  # {'Alice', 'Bob', 'Charlie', 'David'}

#  Multi-line loop
cleaned_names = set()
for name in names:
    cleaned_names.add(name.capitalize())


#Dictionary Comprehensions — Transformation & Conditional Filtering
hyperparams = {"layers": 3, "units": 256, "dropout": 0.2}

scaled = {k: v * 2 for k, v in hyperparams.items()}
print(scaled)

filtered = {k.upper(): v for k, v in hyperparams.items() if v > 0.2}
print(filtered)

#Combining Parallel Datasets into Dictionaries using zip()
years = [2022, 2023, 2024]
dataset_sizes = [500, 800, 1200]

combined = dict(zip(years, dataset_sizes))
print(combined)

#Practical Financial Metrics Calculation with Dictionary Comprehensions
sales = {2022: 50000, 2023: 80000, 2024: 120000}
profits = {year: revenue * 0.15 for year, revenue in sales.items()}
print(profits)

# Internal Boolean Integer Representations & Arithmetic Operations
cardio_completed = True
strength_completed = False
bonus_points = cardio_completed + strength_completed
print(bonus_points)

if bonus_points > 0:
    print("Bonus awarded!")


#String Truthiness & Logical Operator Short-Circuiting (and, or, not)0
print(bool(""))       # Empty string
print(bool("hello"))  # Non-empty string

if "" and "next":
    print("Won’t run")

if "" or "fallback":
    print("Runs with fallback")

age = 16
has_consent = False
print(not (age >= 18 or has_consent))




