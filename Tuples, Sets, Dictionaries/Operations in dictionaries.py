marks = {"maths" : 80.5, "eng": 76.0, "phy": 89.0}
print(marks)
# Fetch the marks for "phy"
print(marks["phy"])

# Get()
print(marks.get("chem"))
print(marks.get("phy"))
emp1 = {'id' : 1001, 'name' : 'John', 'salary' : 10000}
print(emp1.get('phone', 98774635590))

#membership operator not-in\ in
print(1000 in emp1)
print('name' in emp1)
sem1_marks = {'maths' :78.5, 'eng' :71.0, 'phy': 86.5}
sem2_marks = {'chem' :81.5, 'bio' :90.5}
# Update   - Updates the key value pair in another dictionary inside existing dictionary
sem1_marks.update(sem2_marks)
print(sem1_marks)
groceries_1 = {'milk': 60, 'biscuits': 20, 'rice' : 100}
groceries_2 = {'rice' :110, 'bread': 30}
groceries_1.update(groceries_2)
print(groceries_1)

# pop -Deleting the key
groceries_1.pop('milk')
print(groceries_1)
# Keys cannot be duplicated in a dict