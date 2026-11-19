
from app.database.repository import (
    get_students,
    get_faculty,
    get_courses,
    get_enrollments
)

print("\n===== STUDENT TEST =====")
for student in get_students():
    print(student.to_dict())

print("\n===== FACULTY TEST =====")
for faculty in get_faculty():
    print(faculty.to_dict())

print("\n===== COURSE TEST =====")
for course in get_courses():
    print(course.to_dict())

print("\n===== ENROLLMENT TEST =====")
for enrollment in get_enrollments():
    print(enrollment.to_dict())

print("\nAll model dictionary tests completed!")
