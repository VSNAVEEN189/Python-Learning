d1 = {True: 1, False : 0}
print(d1)

# Not allowed - list, Set, Dict
# Allowed keys - strings, Integers, Float, Boolean, Tuples
# Keys of a dictionary can only be mutable datatypes!!

# values can be any datatype
# fetch the keys only
# keys() - To fetch key only
print(d1.keys())
# values() - To fetch value only
print(d1.values())
# items() - To fetch key and value pair in a tuple format |Type will be dictionary only.
print(d1.items())