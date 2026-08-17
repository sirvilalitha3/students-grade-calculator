#student report card system
students=[]
num_students=int(input("enter no.of students:"))
for i in range(num_students):
    name=input(f'enter students {i+1} name:')
    subjects={}
    num_subjects=int(input("enter no.of subjects:"))

    for j in range(num_subjects):
        subject=input(f"enter subject {j+1}name:")
        marks=int(input(f'enter marks for {subject}:'))
        subjects[subject]=marks

        total=sum(subjects.values())
        avg=total / num_subjects

        if avg>=90:
             grade ="A"
        elif avg>=80:
             grade="A"
        elif avg>=70:
            grade="B+"
        elif avg>=60:
            grade="B" 
        elif avg>=30:
            grade="C"
        else:
            grade="F"


        student={
            "name":name,
            "subjects":subjects,
            "average":avg,
            "grade":grade
        }
        students.append(student)


print("\n=== Report Cards ===")
for student in students:
    print(f"\nName: {student['name']}")
    for subject, marks in student["subjects"].items():
        print(f"{subject}: {marks}")
    print(f"average: {student['average']:.2f}")
    print(f"grade: {student['grade']}")