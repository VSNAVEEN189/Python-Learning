# if- else

# if condition:
#     # block of codeto be excuted when the condition is true
# else:
#     # block of code to be executed when the condition is false

# age = float(input("What is your age? "))
#
# if age >= 18:   #True
#     print("Congrats! you can cast your vote")
# else:  #If condition is false it will check else block
#     print("A few more years before you can vote")
#
# print("Rest of the program")

#          Q2
# Write a program if a number is odd or even
# even - when the number is divisible by 2. reminder is 0
# odd - the number is not divisible by 2. reminder is not 0

# % using modulus operator
# print(9 % 2)
# print(8 % 2)
#
num = int(input("Enter an integer: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


#  Write if a number is negative or positive

num = int(input("Enter an integer: "))
if num > 0:
    print("The number is positive")
else:
    print("The number is negative")