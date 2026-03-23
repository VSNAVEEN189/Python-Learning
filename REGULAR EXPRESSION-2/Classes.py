import re

print("----------- \d Character --------")

string="a8543"
pattern=r"\d{5}"                              # \d should consist only digits,

if re.match(pattern,string):
    print('match found')
else:
    print('match not found')  


print("-------------\D Character----------")

string="a8543"
pattern=r"\D"                                 # \D should match any non-digit character

if re.match(pattern,string):
    print('match found')
else:
    print('match not found')  


print("---------------\w Character---------------")

string="python99"
pattern=r"\w"                                # \w can match with any alpha numeric character

if re.match(pattern,string):
    print('match found')
else:
    print('match not found') 


print("-----------[] -------------")

string="python"
pattern=r"[a-zA-Z]ython"                                

if re.match(pattern,string):
    print('match found')
else:
    print('match not found') 

