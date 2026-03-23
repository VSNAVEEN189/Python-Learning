
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
