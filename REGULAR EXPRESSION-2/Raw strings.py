# print(r"hello \n world")

print(" ---------MATCHES ---------") 
import re 
string="abc"
pattern="a"

if re.match(pattern,string):
    print('match found')                       # matches the a when in first position
else:
    print('match not found')             
 

print("---------SEARCH--------")
import re 
string="babc"
pattern="a"

if re.search(pattern,string):
    print('match found')                       # search the a when in first position
else:
    print('match not found')   