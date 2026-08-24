#String Reversal via Slicing
message="john paul"
print(message[::-1])
#String Slicing Reversal & F-String Formatting vs. Concatenation
#normal Concatenation
model_name= 'GPT'
version=4
msg= 'Hello'
print(msg+' from '+model_name+' '+'version '+str(version))

#F-String Formatting
print(f'{msg} from {model_name} -{version}!')

#Floating-Point Formatting with F-Strings
#Floating-Point Formatting with F-Strings (:.4f)
total_cost = 0.12345678
print(f'Total cost: {total_cost:.4f}')
#Floating-Point Formatting with F-Strings (:.6f)
print(f'Total cost: {total_cost:.6f}')

#List Initialization, Data Types, & Utility Inspection (type(), len(), id())
sample_list=["GPT4", True, 10, 10.20, "Gemini"]

#perform empty list
empty_list1=[]
print(empty_list1)
print(sample_list)

#perform  Data Types, & Utility Inspection (type(), len(), id())
print(type(sample_list))
print(type(empty_list1))
print(len(sample_list))
print(len(empty_list1))
print(id(sample_list))
print(id(empty_list1))

#List Indexing, Reverse Indexing, & Index Error Handling
# list Indexing
print(sample_list[0])
print(sample_list[0:4])

#Reverse indexing
print(sample_list[-1])
print(sample_list[-2])

#index error handling
#print(sample_list[5])

#List Mutability Verification & Memory Address Tracking (id())
print(id(sample_list))

sample_list[1]=False
print(sample_list)
print(id(sample_list))


#Nested Lists (Matrices) & Chained Indexing
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,[9,10,11]]
]

print(matrix[1][2])
print(matrix[2][2][1])

#List Deletion Methods — .pop() and .clear()
list2=[10,20,30,40]
element_val=list2.pop()
print(list2)
print(element_val)

#remove specific number from the list
element_val1=list2.pop(1)
print(list2)
print(element_val1)

#remove the last element from the list
element_val2=list2.pop(-1)
print(list2)
print(element_val2)

#clear entire list
list2.clear()
print(len(list2))







