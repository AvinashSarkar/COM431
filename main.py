from student import Student

students = []

for i in range(5):
    print(f"\nEntering details for student {i+1}")

    studentid = input("Student ID: ")
    name = input("Name: ")
    course = input("Course: ")

    while True:
        try:
            mark = float(input("Mark: "))
            if 0 <= mark <= 100:
                break
            else:
                print("Please enter a valid mark")
        except ValueError:
            print("Please enter a numerical value")

    student = Student(studentid, name, course, mark)
    students.append(student)

print("\nStudents Details: ")
for Student in students:
    Student.print_details()




