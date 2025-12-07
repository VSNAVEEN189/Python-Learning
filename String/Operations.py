"""

#Membership operation
s1 = "Python is fun"
print("z" in s1)
print("Java" in s1)
# not in
print("z" not in s1)
print("Java" not in s1)
print("Python" not in s1)

# Removing space from a string
s1 = "Python "
s2 = s1.strip()
print(s2)

#Replace
s1 = "We are learning Python"
print(s1)
print(s1.replace("Python", "Java"))
print(s1.replace("e", "E"))
print(s1.replace("e", "E", 1))
"""
####DAY 2 OPERATIONS #####
#Counting substring from a string
#count()
#string.count(substring)
s1 = "We are learning Python. Python is fun"
s2 = "Python"
print(s1.count(s2))
#Changing case of a string
#upper(), lower(), title(), capatilize()
#s1 = "Python"
s1 = "We are learning Python"
print(s1.upper())
print(s1.lower())
print(s1.title())
print(s1.capitalize())
#Starting and ending of a string
print(s1.startswith(""))
print(s1.endswith("Python"))
