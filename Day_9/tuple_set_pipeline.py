#1.Tuple Definition, Immutability Enforcement, & Single-Element Syntax
from Day_6.list_pipeline import matrix, empty_list1

location=(37.7749, -122.4194)
print(location)
#3.	Single-Element Trailing Comma Rule:
sig_val1=10
print(type(sig_val1))
sig_val2=10,
print(type(sig_val2))
#2.try to immutable test
#location[1] = -122.5000
#print(location)

#Explicit Type Casting (tuple() ↔ list()) & Data Freezing
score_list=[1,2,3,4,5]
print(score_list)
print(type(score_list))
immutable_scores = tuple(score_list)
print(immutable_scores)
print(type(immutable_scores))
#immutable_scores.append(6)
#bidirectional cast tuple into list
immutable_scores=list(score_list)
print(immutable_scores)
print(type(immutable_scores))

#Tuple Unpacking & Multi-Dimensional Nested Tuple (Matrix) Access
#tuple unpacking
location=(37.7749, -122.4194)
latitude, longitude = location
print(location)
#multi-dimensional nested tuple matrix
matrix=((1,2,3),
        (4,5,6),
        (7,8,9))
print(matrix[1][1])
print(matrix[2][1])

# Set Fundamentals, Unordered Behavior, & Empty Set Declaration Rules
unique_val= {1, 2, 3, 3, "A", "B", 4}
print(type(unique_val))
print(len(unique_val))
print(unique_val)

#empty Set rule
empty_list1={}
print(type(empty_list1))

empty_list2=set()
print(type(empty_list2))

# One-Line List Deduplication & Set Methods (.add(), .remove(), .update())
duplicate_log = ["hello", "world", "hello", "python", "world"]
clean_log = list(set(duplicate_log))
print(clean_log)
print(type(clean_log))
#Set Modification Methods:
unique_val.add(5) #add element
print(unique_val)

unique_val.remove(3) #remove element
print(unique_val)

unique_val.update(['a', 'b', 'c'])
print(unique_val)

#3.	Item Assignment Rejection
unique_val= {1, 2, 3, 3, "A", "B", 4}
unique_val=99
print(unique_val)
"""Item Assignment Rejection: Attempt unique_ids = 99.
Document that sets do not support index-based assignment and raise
 TypeError: 'set' object does not support item assignment. But not Shows the error
 it overrides the previous value with new value. """

#: Immutable Set Management using frozenset()
frozen_set_exmaple=frozenset({1, 2, 3})
print(frozen_set_exmaple)
print(type(frozen_set_exmaple))
#frozen_set_exmaple.add(4)#because frozen set is immutable we cannot add elements
#print(frozen_set_exmaple)

#Tuple Slicing, Sequence Reversal ([::-1]), & Tuple Comprehension
data_tuple=(1,2,3,4,5)
print(data_tuple)
print(data_tuple[1:4:])
print(data_tuple[::-1])
even_tuple=tuple(num for num in data_tuple if num%2==0)
print(even_tuple)

