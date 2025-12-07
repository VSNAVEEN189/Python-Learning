t1 = ("Python", 10, 1.5, True, [1, 2, 3], [10,20])
print(t1)
print(len(t1))#

#Accessing item of a tuple- Using index
print(t1[0])
print(t1[-1])

# #To create a tuple
t1 = 10, 20, 30, 40
print(t1)
print(type(t1))

#Type-casting a list to tuple
l1 = [1, 2, 3]
print(l1, type(l1))
t1 = tuple(l1)
print(t1, type(t1))

# Tuple to a list
fruits= "Mango", "Orange", "Apple"
print(fruits, type(fruits))
fruits = list(fruits)
print(fruits)

#Basic operations on tuples
"""
concatenation, repetition, membership
count, index
min, max, sum
"""
student_detail1 = (1001, "john")
student_detail2 = (78.5, 91.0, 83.5, 79.5)

#  +
#  student_detail = student_detail1 + student_detail2
print(student_detail)

# *
t1 = ("Class 5", 5000)
print(t1 * 3)

# Membership operation
#in, not in
print(91.0 in student_detail2)
print(99.0 in student_detail2)
print(91.0 not in student_detail2)
print(99.0 not in student_detail2)

# Major differences in tuple and list that it cannot be re-modified
# count
t1 = (10, 4, 1, 9, 0, 3, 1)

#tuple.count(element)
print(t1.count(1))

# index
# print(t1.index(1)) # What is the index of 4 in a tuple t1?
print(f"Smallest number is: {min(t1)}")
print(f"Biggest number is: {max(t1)}")
print(f"Total number is {sum(t1)}")

