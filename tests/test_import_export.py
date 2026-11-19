
from app.models.student import Student
from app.models.faculty import Faculty
from app.models.course import Course

from app.utils.serializers import export_data, import_data


# Sample Application Data
students = [
    Student(101, "Gladson", 20, "gladson@example.com", "Computer Science"),
    Student(102, "Rahul", 21, "rahul@example.com", "Information Technology")
]

faculties = [
    Faculty(201, "Amit", 35, "amit@example.com", "Computer Science")
]

courses = [
    Course("CS101", "Python Programming", 5),
    Course("CS102", "Database Management", 3)
]

enrollments = [
    {
        "student": students[0],
        "course": courses[0]
    }
]


# Export Data
print("\n===== EXPORT DATA =====")

export_data(students, faculties, courses, enrollments)


# Import Data
print("\n===== IMPORT DATA =====")

loaded_students, loaded_faculties, loaded_courses, loaded_enrollments = import_data()


# Display Imported Data
print("\nImported Students:")
for student in loaded_students:
    student.display_details()

print("\nImported Faculty:")
for faculty in loaded_faculties:
    faculty.display_details()

print("\nImported Courses:")
for course in loaded_courses:
    course.display_details()

print("\nImported Enrollments:")
for enrollment in loaded_enrollments:
    print("Student:", enrollment["student"].name)
    print("Course:", enrollment["course"].course_name)

print("\nImport and Export Completed Successfully!")
