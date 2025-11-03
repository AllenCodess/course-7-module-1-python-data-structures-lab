# data_processing.py
import student_data

def format_student_data(student):
    """
    Format student data for display.
    The function should return a formatted string containing:
    - Student ID
    - Student Name
    - Major
    such as: "ID: 10 | Name: Louis Medina | Major: Computer Science"
    """
    student_id = student[0]
    name = student[1]
    major = student[2]

    return f"ID: {student_id} | Name: {name} | Major: {major}"


def display_students(student_list):
    """
    Display all student records.
    Loop through the student_list and print each student using format_student_data().
    """
    for student in student_list:
        print(format_student_data(student))


# ✅ Call the display function with the actual list inside the module
display_students(student_data.students)
