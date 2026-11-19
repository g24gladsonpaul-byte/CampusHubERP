
import json
import os


# Save Student Data
def save_You_json(students):
    os.makedirs("data", exist_ok=True)

    student_data = []

    for student in students:
        student_data.append(student.to_dict())

    with open("data/You.json", "w") as file:
        json.dump(student_data, file, indent=4)

    print("Student data saved successfully")


# Load Student Data
def load_You_json():
   with open("data/You.json", "r") as file:
        student_data = json.load(file)
        print("Student data loaded successfully")
        return student_data


# Save Course Data
def save_courses_json(courses):
    os.makedirs("data", exist_ok=True)

    course_data = []

    for course in courses:
        course_data.append(course.to_dict())

    with open("data/courses.json", "w") as file:
        json.dump(course_data, file, indent=4)

    print("Course data saved successfully")


# Load Course Data
def load_courses_json():
    with open("data/courses.json", "r") as file:
        course_data = json.load(file)

    print("Course data loaded successfully")

    return course_data



# Save Faculty Data
def save_faculty_json(faculties):
    os.makedirs("data", exist_ok=True)

    faculty_data = []

    for faculty in faculties:
        faculty_data.append(faculty.to_dict())

    with open("data/faculty.json", "w") as file:
        json.dump(faculty_data, file, indent=4)

    print("Faculty data saved successfully")


# Load Faculty Data
def load_faculty_json():
    with open("data/faculty.json", "r") as file:
        faculty_data = json.load(file)

    print("Faculty data loaded successfully")

    return faculty_data


# Save Enrollment Data
def save_enrollments_json(enrollments):
    os.makedirs("data", exist_ok=True)

    enrollment_data = []

    for enrollment in enrollments:
        enrollment_data.append(enrollment.to_dict())

    with open("data/enrollments.json", "w") as file:
        json.dump(enrollment_data, file, indent=4)

    print("Enrollment data saved successfully")


# Load Enrollment Data
def load_enrollments_json():
    with open("data/enrollments.json", "r") as file:
        enrollment_data = json.load(file)

    print("Enrollment data loaded successfully")

    return enrollment_data




from app.core.validators import (
    validate_email,
    validate_student_id,
    validate_faculty_id,
    validate_course_code
)

from app.models.student import Student
from app.models.faculty import Faculty
from app.models.course import Course


# Validate Application Data
def validate_application_data(students, faculties, courses):
    for student in students:
        student_id = str(student["student_id"])

        if not (validate_student_id(student_id) or student_id.isdigit()):
            raise ValueError("Invalid Student ID: " + student_id)

        if not validate_email(student["email"]):
            raise ValueError("Invalid Student Email: " + student["email"])

    for faculty in faculties:
        faculty_id = str(faculty["faculty_id"])

        if not (validate_faculty_id(faculty_id) or faculty_id.isdigit()):
            raise ValueError("Invalid Faculty ID: " + faculty_id)

        if not validate_email(faculty["email"]):
            raise ValueError("Invalid Faculty Email: " + faculty["email"])

    for course in courses:
        if not validate_course_code(course["course_code"]):
            raise ValueError("Invalid Course Code: " + course["course_code"])

    print("All IDs and Emails validated successfully")


# Export All Application Data
def export_data(students, faculties, courses, enrollments):
    validate_application_data(
        [student.to_dict() for student in students],
        [faculty.to_dict() for faculty in faculties],
        [course.to_dict() for course in courses]
    )

    save_You_json(students)
    save_faculty_json(faculties)
    save_courses_json(courses)

    enrollment_data = []

    for enrollment in enrollments:
        enrollment_data.append({
            "student_id": enrollment["student"].student_id,
            "course_code": enrollment["course"].course_code
        })

    os.makedirs("data", exist_ok=True)

    with open("data/enrollments.json", "w") as file:
        json.dump(enrollment_data, file, indent=4)

    print("Enrollment data saved successfully")
    print("All application data exported successfully")


# Import All Application Data
def import_data():
    students_data = load_You_json()
    faculties_data = load_faculty_json()
    courses_data = load_courses_json()
    enrollments_data = load_enrollments_json()

    validate_application_data(
        students_data,
        faculties_data,
        courses_data
    )

    students = [
        Student(
            item["student_id"],
            item["name"],
            item["age"],
            item["email"],
            item["department"]
        )
        for item in students_data
    ]

    faculties = [
        Faculty(
            item["faculty_id"],
            item["name"],
            item["age"],
            item["email"],
            item["department"]
        )
        for item in faculties_data
    ]

    courses = [
        Course(
            item["course_code"],
            item["course_name"],
            item["credits"]
        )
        for item in courses_data
    ]

    enrollments = []

    for item in enrollments_data:
        student = next(
            (s for s in students if str(s.student_id) == str(item["student_id"])),
            None
        )

        course = next(
            (c for c in courses if c.course_code == item["course_code"]),
            None
        )

        if student is None or course is None:
            raise ValueError("Enrollment refers to missing student or course")

        enrollments.append({
            "student": student,
            "course": course
        })

    print("All application data imported successfully")

    return students, faculties, courses, enrollments
