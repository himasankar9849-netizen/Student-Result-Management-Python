students = {}

def calculate_grade(marks):
    if marks >= 90: return "A+"
    elif marks >= 75: return "A"
    elif marks >= 60: return "B"
    elif marks >= 40: return "C"
    else: return "Fail"

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    grade = calculate_grade(marks)
    students[roll] = {"name": name, "marks": marks, "grade": grade}
    print(f"Added {name} - Grade {grade}")

def view_students():
    for r, s in students.items():
        print(f"{r} | {s['name']} | {s['marks']} | {s['grade']}")

def search_student():
    r = input("Enter Roll to search: ")
    if r in students:
        print(students[r])
    else:
        print("Not Found")

while True:
    print("\n1.Add 2.View 3.Search 4.Exit")
    ch = input("Choice: ")
    if ch == '1': add_student()
    elif ch == '2': view_students()
    elif ch == '3': search_student()
    elif ch == '4': break
