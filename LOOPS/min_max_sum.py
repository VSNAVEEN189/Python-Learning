scores = [2, 45, 102, 4, 9, 12, 45, 90, 1, 0, 1]
print("------------SUM--------------")
total = 0
for score in scores:
    total = total + score

total = sum(scores)
print(f"total runs scored is: {total}")
print("---------------------------Highest---------------------")
# Find the highest score
highest = scores[0]  #assume that the first value is highest
for score in scores:
    if highest < score:
        highest = score#

highest = max(scores)
print(f"The highest number is {highest}")

print("-----------------------------LOWEST---------------------")
# lowest\minimum

lowest = scores[0]  # assume that the first value is lowest

for score in scores:
   if lowest > score:
      lowest = score

lowest = min(scores)
print(f"The lowest number is {lowest}")