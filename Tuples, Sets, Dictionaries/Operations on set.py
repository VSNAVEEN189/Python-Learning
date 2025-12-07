student1 = {"English", "Maths", "CS", "Chemistry", "Physics"}
student2 = {"English", "Biology", "Chemistry", "Physics"}


#Common subjects of student1 and student2 - Intersection
common_subjects = student1 & student2
print(common_subjects)

#All subject - Union
all_subjects = student1| student2
print(all_subjects)
#Empty set when there is no common element in the sets

days = {"mon", "tue", "wed", "thu", "fri", "sat", "sun"}
weekends = {"sat", "sun"}
#difference of sets
weekdays = days - weekends
print(weekdays)
s1 = {1,2,3,4,0}
s1.add(-1)
print(s1)

# Frozen sets - Immutable sets
fs1 = frozenset({10, 20, 30})
print(fs1, type(fs1))
fs2 = frozenset({10, 50, 100, 200})
print(fs2, type(fs2))
print(fs1&fs2)
print(fs1 | fs2)
print(fs2 - fs1)