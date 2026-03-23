import re

# print("----------- * - Asterik--------------")

# string="abbc"
# pattern="ab*c"

# if re.match(pattern,string):
#     print('match found')
# else:
#     print('match not found')    


# print("--------- + - Plus-----------") 

# string="abbc"
# pattern="ab+c"

# if re.match(pattern,string):
#     print('match found')
# else:
#     print('match not found')     


# print("----------{...} - Curly braces---------")

# string="abbbbc"
# pattern="ab{3}"

# if re.match(pattern,string):
#     print('match found')
# else:
#     print('match not found')   


# print("------------ . Notation--------------")

# string="azb"
# pattern=r"a.b"

# if re.match(pattern,string):
#     print('match found')
# else:
#     print('match not found')   


print("-----------? Optional-------------")

string="python-file"
pattern=r"python-?file"            # This states that - is optional

if re.match(pattern,string):
    print('match found')
else:
    print('match not found')   


print("----------- ^ - Caret---------")

string="912345677"
pattern=r"^91"            

if re.match(pattern,string):
    print('match found')
else:
    print('match not found')  


