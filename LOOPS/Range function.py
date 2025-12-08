# """range() built in function used to generate sequence of integers in a given interval"""
# range(start, stop, step) step parameter decide in which step we want to generate integer

# range(start, stop, step): stop is not included in output generation
# range(start, stop): Step is by default
# range(stop):  0 to stop-1 with a step of 1, start value is 0 by default


# for i in range(start, stop, step):
    #statements

#   It won't include 10 in output
for i in range(1, 11, 1):           # for including 10 in output add 11 in stop
    print(i)                   #One by one will be generate due to for-loop

#Generate even numbers between 1 and 10 excluding 10
for i in range(2, 10, 2):
    print(i)
#Generate odd numbers between 1 and 10 excluding 10
for i in range(1, 10, 2):
    print(i)

    # Generate number in reverse order 20 to 10 (excluding 10) only even
for i in range(20, 10, -2):    #20, 18, 16, 14, 12 for descending order step should be in negative
    print(i)


# # Count down from 10 to 1 1 included
for i in range(10, 0, -1):    #For ascending go with positive step
    print(i)
print("Happy New Year!!!!")

# ------------------   2  --------------
#  range(start,stop) => step is 1 by default
for i in range(1, 5):   #Step = 1
    print(i)
# ------------------  3  ---------------
# range(stop) => start is 0 by default
for i in range(5):   #output won't include 5
    print(i)



#                            USE CASES
groceries = ['salt', 'milk', 'sugar']
for index in range(len(groceries)):    #range(3)=> 0, 1, 2
    print(index)

profits = [9, 11, 6, 10]
# print profit quarter wise     Using index
for index in range(len(profits)):
    q = index + 1    #By adding the value to index
    print(f"Profit for quarter{q} is {profits[index]}")