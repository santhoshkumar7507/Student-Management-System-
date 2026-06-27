class Student:
    def __init__(self, student_id, name, marks):
        self.student_id=student_id
        self.name=name
        self.marks=marks

    def calculate_grade(self):
        if self.marks>=90: return "A+"
        elif self.marks>=80: return "A"
        elif self.marks>=70: return "B+"
        elif self.marks>=60: return "B"
        elif self.marks>=50: return "C"
        return "Fail"

    def display(self):
        print("-"*40)
        print(f"ID    : {self.student_id}")
        print(f"Name  : {self.name}")
        print(f"Marks : {self.marks}")
        print(f"Grade : {self.calculate_grade()}")

students=[]

def add_student():
    sid=int(input("Enter ID: "))
    name=input("Enter Name: ")
    marks=int(input("Enter Marks: "))
    students.append(Student(sid,name,marks))
    print("Student added.")

def display_students():
    if not students:
        print("No students found.")
    else:
        for s in students:
            s.display()

def search_student():
    sid=int(input("Enter ID to search: "))
    for s in students:
        if s.student_id==sid:
            s.display(); return
    print("Student not found.")

def update_marks():
    sid=int(input("Enter ID: "))
    for s in students:
        if s.student_id==sid:
            s.marks=int(input("New Marks: "))
            print("Updated."); return
    print("Student not found.")

def delete_student():
    sid=int(input("Enter ID: "))
    for s in students:
        if s.student_id==sid:
            students.remove(s); print("Deleted."); return
    print("Student not found.")

def topper():
    if students:
        max(students,key=lambda x:x.marks).display()
    else: print("No students.")

def statistics():
    if not students:
        print("No students."); return
    marks=[s.marks for s in students]
    print("Total:",len(students))
    print("Highest:",max(marks))
    print("Lowest:",min(marks))
    print("Average:",sum(marks)/len(marks))

def save():
    with open("students.txt","w") as f:
        for s in students:
            f.write(f"{s.student_id},{s.name},{s.marks},{s.calculate_grade()}\n")
    print("Saved to students.txt")

while True:
    print("\n1.Add 2.Display 3.Search 4.Update 5.Delete 6.Topper 7.Statistics 8.Save 9.Exit")
    ch=input("Choice: ")
    if ch=="1": add_student()
    elif ch=="2": display_students()
    elif ch=="3": search_student()
    elif ch=="4": update_marks()
    elif ch=="5": delete_student()
    elif ch=="6": topper()
    elif ch=="7": statistics()
    elif ch=="8": save()
    elif ch=="9": break
    else: print("Invalid choice")
