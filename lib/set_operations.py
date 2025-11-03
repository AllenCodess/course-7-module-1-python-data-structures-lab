# This module contains operations related to sets.
import student_data
def unique_majors(student_list):
    """
    Return a set of unique student majors using set comprehension.
    Extract the major field from each student record.
    """
    return {student[2] for student in student_list}
    pass
print(unique_majors(student_data.students))
