# Modules are python files that have some python code written in it, or We can create are own modules writing
# some different codes saving as .py
# And using them in another file Using import keyword Which are not part of in-built.
import random

#random()- the random function is a function of random module that returns
# float between 0.0 and 1.0(excluded)
print("--------Random()-Return float between 0.0 and 1.0--------")
print(random.random())
print(random.random())

print("--------Randint()-Used to print integer value----------")
# randint(a, b) => Returns random int between a and b (both a and b are included)
print(random.randint(10,15))

print("--------Choice()-Gives random output from the given list-------")
nums = [10, 4, 1, 8, 4, 3]
fruits = ["apple", "banana", "cherry"]
# Choice(sequence) => takes sequence as an argument returns random item from the sequence
print(random.choice(nums))   #Gives output from the given list each time new output
print(random.choice(fruits))
print(nums)
print(fruits)

print("---------shuffle() -Shuffles the whole list----------")
# shuffle(sequence) => Returns the elements shuffled in random order
print(random.shuffle(nums))    #Use in card games and shuffle
print(random.shuffle(fruits))
print(nums)
print(fruits)
