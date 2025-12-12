# # user deifned
# def function_name(can have zero or more arguments):
#     statements can have one or more statements    
#     statements1
#     statements2.

def greeting_someone(name):
    print(f"Hello {name}, Good morning!")       #Gets in the memory
    print("It's a beutiful day")

# calling a function    
greeting_someone("Mark")                     
greeting_someone("Carol")  
greeting_someone("John")  

def even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_odd(10)
even_odd(11)
even_odd(99)
even_odd(100)

# Reusability is main thing to use function and neat

def add(num1, num2):
    result = num1 + num2
    print(f"Result: {result}")

add(10, 3)
add(9, -4)    
