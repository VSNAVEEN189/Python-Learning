# Day 2 Extend, remove, pop
# Extend
fruits = ["apple", "mango", "orange", "mango"]
print(fruits)
fruits.extend(["banana", "grapes"])
print(fruits)
print(len(fruits))
#remove
fruits.remove("mango")
print(fruits)
#pop
print(fruits)
fruits.pop()
print(fruits)
# reverse
# sort
# count
# Membership operation
days_of_week = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
print(days_of_week)
#reverse()
days_of_week.reverse()
print(days_of_week)
# Sort
nums = [4, 9, 0, 1, 2, 3]
print(nums)
nums.sort(reverse=True)
print(nums)
# count()
numbers = [0, 1, 3, 4, 1, 0, 5, 0, 0, 3, 0]
print(f"The list is: {numbers}")
item_to_count = int(input("Enter the number to be counted from the above list: "))
c = numbers.count(item_to_count)
print(f"Occurrence of {item_to_count} is {c} times")
# Membership operation
# in/not in
language = ["python","java","c++","python"]
print("python" not in language)
print("javascript" not in language)
print("python" in language)
print("javascript)" in language)