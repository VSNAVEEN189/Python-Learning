print(" --------------------TASK 1------------------")

#            FOR ODD NUMBER
num = int(input("Enter a number: "))

if num % 2 == 0:
     print("even")
else:
     print("odd")

#            FOR EVEN NUMBER
num = int(input("Enter a number: "))
print("even") if num % 2 == 0 else print("odd")


print(" --------------------TASK 2--------------------")

total_sum = 0

for num in range(1, 51):
    total_sum += num

print("The sum of numbers from 1 to 50 is:", total_sum)