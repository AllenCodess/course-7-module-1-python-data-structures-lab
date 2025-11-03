import student_data

def student_generator(student_list, major):
    """
    Generate student records filtered by major lazily for memory efficiency
    using a Python generator.
    """
    return (student for student in student_list if student[2].lower() == major.lower())

# Pass the major you want to filter
cs_students = student_generator(student_data.students, "Computer Science")

# To see the results, iterate over the generator
for student in cs_students:
    print(student)
