
import re


# Validate Email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        return True
    else:
        return False


# Validate Student ID
def validate_student_id(student_id):
    pattern = r'^ST\d{3}$'

    if re.match(pattern, student_id):
        return True
    else:
        return False


# Validate Faculty ID
def validate_faculty_id(faculty_id):
    pattern = r'^FC\d{3}$'

    if re.match(pattern, faculty_id):
        return True
    else:
        return False


# Validate Course Code
def validate_course_code(course_code):
    pattern = r'^CS\d{3}$'

    if re.match(pattern, course_code):
        return True
    else:
        return False
