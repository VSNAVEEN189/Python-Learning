for num in range(10):
   if num % 3 == 0:  # if the number is divisible by 3
       continue    # It skips the below code and run again to for loop
#    # the number which reminder is not 0 is printed below
   print(num)

print("---------")

for num in range(1, 10):
    if num % 3 == 0:    #if the number is divisible by 3
        break        #Makes the control out of the loop\terminates the loop
    print(num)