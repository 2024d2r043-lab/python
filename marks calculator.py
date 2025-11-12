marks = [float(input(f"Enter marks of subject {i+1}: ")) for i in range(5)]
total = sum(marks)
percent = total / 5
print(f"\nTotal = {total}\nPercentage = {percent}%")

if percent >= 90: grade = "A+"
elif percent >= 80: grade = "A"
elif percent >= 70: grade = "B"
elif percent >= 60: grade = "C"
elif percent >= 50: grade = "D"
else: grade = "F"

print("Grade =", grade)
