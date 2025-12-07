"""
>=90 grade A
80 and 89 grade B
70 and 79, grade C
60 and 69, grade D
<60, grade F
"""
# if - elif - else  first if then all other elif none of them is true its else
marks = float(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif 80 <= marks < 90:     #Chained more standard way
    print("Grade B")
elif marks >= 70 and marks < 80:
    print("Grade C")
elif marks >= 60 and marks < 70:
    print("Grade D")
else:
    print("Grade F")