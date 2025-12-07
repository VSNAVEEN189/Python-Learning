#SETS IN PYTHON
#Sets are non-sequential collection of items
#commma separated values enclosed within {}
set1 = {10, "Python", 2.5}
print(set1)
print(type(set1))

#Cannot have indexing with sets
#Length of the set
print(len(set1))

#Sets do not allow duplicate elements
s1 = {10, 2.5, 30}
print(s1, type(s1))

#Basic operations of set
nums_1 = {1, 3, 2, 0, -1}
#Membership operator - in, not in
print(0 in nums_1)
print(10 in nums_1)

#Repetation and concatenation is not allowed in sets
# #Creating sets using tuples or lists
weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")
weekdays = set(weekdays)
print(weekdays)
set1 = {2, 0, -1}
print(set1)

#add() function
set1.add(0)  #Assuming a bag of balls with 2,0,-1 adding randomly number 5
# If already present doesn't allow same elements
print(set1)

#remove() If element in the set is present, If not gives an error to us
set1.remove(0)
print(set1)

#discard  To avoid error use discard, We do not get error if element is not present in the set
# - gives error while in remove function
set1.discard(10)
print(set1)
