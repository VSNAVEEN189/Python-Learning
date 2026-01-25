def func():
    """
    This is a doc string 
    we can write that the function does here.
    :return: None
    """
    return None

print(help(func))          #To see if the function has a doc string or not.


print("-------------DIVIDE FUNCTION WITH DOC STRING------------")


def divide(num1, num2):
    """
    num1: A number to be divided(Numerator)
    num2: A number to divide by(Denominator)
    :return: float
    """
    return num1 / num2
    return result

# print(help(divide))
print(divide(10, 4))           

print("---------------IN CASE OF DIVISION BY ZERO----------------")

def divide(num1, num2):
    """
    num1: A number to be divided(Numerator)
    num2: A number to divide by(Denominator)     #TO SHOW HOW TO WRITE ABOUT EXCEPTIONS IN DOC STRINGS  
    :return: float (if num2 is non-zero) or str(if num2 is 0)     should be the first thing in the function.
    """                                                            #To call it use help()
    if num2 == 0:
        return "Cannot divide as denominator is 0!"
    else:
         return num1 / num2
         return result

# print(help(divide))
print(divide(10, 0))
