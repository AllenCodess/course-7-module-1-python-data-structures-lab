# This module contains functions for filtering student data.
import student_data

def filter_students_by_major(student_list, major):
    filter_students_by_major = [x for x in student_data.students if major.lower() in x[2].lower()]
    return filter_students_by_major

    """
    Return a filtered list of students by major using a list comprehension.
    The function should:
    - Check if a student's major matches the given major (case insensitive).
    - Return a new list containing only students that match.
    """
    pass


cs_students = filter_students_by_major(student_data.students, "Computer Science")
print(cs_students)