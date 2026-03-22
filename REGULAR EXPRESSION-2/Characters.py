print("----------- * - Asterik--------------")
import re 

string="abbc"
pattern="ab*c"

if re.match(pattern,string):
    print('match found')
else:
    print('match not found')    


print("--------- + - Plus-----------") 

string="abbc"
pattern="ab+c"

if re.match(pattern,string):
    print('match found')
else:
    print('match not found')     


print("----------{...} - Curly braces---------")

string="abbbbc"
pattern="ab{3}"

if re.match(pattern,string):
    print('match found')
else:
    print('match not found')   


print("------------ . Notation--------------")

string="azb"
pattern=r"a.b"

if re.match(pattern,string):
    print('match found')
else:
    print('match not found')   
