
from app.core.validators import (
    validate_email,
    validate_student_id,
    validate_faculty_id,
    validate_course_code
)

print("Email Validation:")
print(validate_email("gladson@gmail.com"))

print("\nStudent ID Validation:")
print(validate_student_id("ST001"))

print("\nFaculty ID Validation:")
print(validate_faculty_id("FC001"))

print("\nCourse Code Validation:")
print(validate_course_code("CS101"))
