# They are mutable data types which are sets, list, dict.
l1 = [1,2.5, [10,20,30], "Python"]
# Using copy module
import copy

# Shallow copy
l2 = copy.copy(l1)    #gets new memory address
# print(l2)
l1[0] = 5
print(f"l1 -> {l1}")
print(f"l2 -> {l2}")

d1= {'id': 1111, 'name': 'John', 'marks': {'eng': 71.5, 'maths': 91.5, 'bio': 80.0}}
#deep copy
d2 = copy.deepcopy(d1)
d1['name'] = 'Dan'
d1['marks']['maths'] = 92.5
print(f"d1 -> {d1}", id(d1))
print(f"d2 -> {d2}", id(d2))