# students.py

students = []


def add_student(student_id, name, course):
    student = {
        "id": student_id,
        "name": name,
        "course": course
    }
    students.append(student)
    print(f"Student {name} added successfully.")


def display_students():
    print("\nStudent List:")
    for student in students:
        print(
            f"ID: {student['id']}, "
            f"Name: {student['name']}, "
            f"Course: {student['course']}"
        )


# Sample data
add_student(101, "Ram Sharma", "BCA")
add_student(102, "Sita Thapa", "BCA")

display_students()