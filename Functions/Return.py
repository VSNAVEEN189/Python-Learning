# Check if a number is even or odd
def even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

result = even_odd(9)
print(result)


print("-------------CREATING FUNCTION-----------")

# Simple addition function
def add(a, b):
    return a + b

n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))

sum_val = add(n1, n2)
print(f"Addition of {n1} and {n2} is {sum_val}")


print("--------------ADDITION FUNCTION----------------")

# Same addition function (kept for structure)
def add(a, b):
    return a + b

n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))

sum_val = add(n1, n2)
print(f"Addition of {n1} and {n2} is {sum_val}")


print("------------ARITHMETIC FUNCTION--------------")

# Perform basic arithmetic and return all results
def arithmetic(a, b):
    return a + b, a - b, a * b

n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))

add_res, sub_res, mul_res = arithmetic(n1, n2)

print(f"Addition of {n1} and {n2} is {add_res}")
print(f"Difference between {n1} and {n2} is {sub_res}")
print(f"Product of {n1} and {n2} is {mul_res}")
