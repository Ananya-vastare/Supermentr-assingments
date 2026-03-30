students = {
    "A": 80,
    "B": 90,
    "C": 70,
    "D": 85,
    "E": 60
}

# Topper
topper = max(students, key=students.get)
print("Topper:", topper)

# Average
avg = sum(students.values()) / len(students)
print("Average:", avg)

# Grades
for s, m in students.items():
    if m >= 85:
        grade = "A"
    elif m >= 70:
        grade = "B"
    else:
        grade = "C"
    print(s, grade)