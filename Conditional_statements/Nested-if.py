"""
if marks >= 60, student is pass else student is fail
and the student is pass, then we print the grade
>=90 grade A
80 and 89 grade B
70 and 79, grade C
60 and 69, grade D
<60, grade F
"""

# Nested if means something inside something if inside

marks = float(input("Enter marks: "))

if marks >= 60:
    print("Congrats, you have passed the exam!")
    if marks>=90:
        print("You grade is A")
    elif 80 <= marks <= 90:
        print("You grade is B")
    elif 70 <= marks <= 79:
        print("You grade is C")
    else:
        print("You grade is D")
else:
    print("You have failed, study hard next time")