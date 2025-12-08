"""It is an iterator based loop which steps through the items of a
collection (lists, tuples, sets, dict, str), and executes a block
or code repeatedly for a number of times equal to the items/elements
of that collection. """

# ---------------------With string---------------------
s1 = "Hello World"

for char in s1:
    print(char)
print("End of loop")

# ---------------------With dictionary-----------------
employee = {'empid' : 1001, 'name' : "John Gray", "department" : "HR"}

for i in employee:
    print(i)
print("End of loop")
# If we run for-loop on dictionary it will give you key only
# To get the key-value pair
# To print each key-value pair in a tuple;
print(employee.items())

for i in employee.items():
    print(i)

for i in employee.items():
    print(i[1])      #To print values only
    print(i[0])      #To print keys only
    print(i[0], i[1])  #To print both the values