
# Imports
from app.models import student
from app.models.student import Student
from app.models.faculty import Faculty
from app.models.course import Course

from app.services.student_service import StudentService
from app.services.faculty_service import FacultyService
from app.services.course_service import CourseService
from app.services.enrollment_service import EnrollmentService

from app.database.repository import (
    get_students,
    get_faculty,
    get_courses,
    get_enrollments
)

from app.utils.file_manager import ReportWriter
from app.utils.generators import StudentIterator

import threading
import multiprocessing
import asyncio

from app.utils.serializers import (
    save_You_json,
    save_faculty_json,
    save_courses_json,
    save_enrollments_json
)

from app.services.async_service import (
    load_all_data,
    generate_all_reports
)


# Student Report
def generate_student_report(students):
    print("Generating Student Report...")

    with ReportWriter("reports/student_report.txt") as file:
        for student in students:
            report = str(student.to_dict())
            file.write(report + "\n")
            print(report)


# Faculty Report
def generate_faculty_report(faculties):
    print("Generating Faculty Report...")

    with ReportWriter("reports/faculty_report.txt") as file:
        for faculty in faculties:
            report = str(faculty.to_dict())
            file.write(report + "\n")
            print(report)


# Course Report
def generate_course_report(courses):
    print("Generating Course Report...")

    with ReportWriter("reports/course_report.txt") as file:
        for course in courses:
            report = str(course.to_dict())
            file.write(report + "\n")
            print(report)


# Multiprocessing Summary
def calculate_summary(total_students, total_faculty,
                      total_courses, total_enrollments):

    print("\n===== CampusHubERP Summary =====")
    print("Total Students:", total_students)
    print("Total Faculty:", total_faculty)
    print("Total Courses:", total_courses)
    print("Total Enrollments:", total_enrollments)
    print("================================")


# Asynchronous Tasks
async def run_async_tasks(students, faculties, courses):

    print("\nLoading Data...")

    await load_all_data()

    print("All data loaded successfully.")

    print("\nGenerating Reports...")

    await generate_all_reports(
        students,
        faculties,
        courses
    )

    print("All Reports Generated Successfully.")


# Main Function
def main():

    # Creating Student, Faculty and Course Objects
    s1 = Student(
        101, "Gladson", 20,
        "gladson@example.com", "Computer Science"
    )

    f1 = Faculty(
        201, "Rahul", 35,
        "rahul@example.com", "Computer Science"
    )

    c1 = Course(
        "CS101", "Python Programming", 4
    )

    print("Student Details:")
    s1.display_details()

    print("\nFaculty Details:")
    f1.display_details()

    print("\nCourse Details:")
    c1.display_details()


    # Student Management
    service = StudentService()

    s2 = Student(
        102, "Rahul", 21,
        "rahul@example.com", "Information Technology"
    )

    s3 = Student(
        103, "Priya", 19,
        "priya@example.com", "Computer Science"
    )

# Check existing students before adding
    existing_student_ids = {
        student.student_id for student in get_students()
    }

    if s1.student_id not in existing_student_ids:
        service.add_student(s1)

    if s2.student_id not in existing_student_ids:
        service.add_student(s2)

    if s3.student_id not in existing_student_ids:
        service.add_student(s3)

    print("\nAll Students (Sorted by Name):")
    service.list_students()

    print("\nStudents in Computer Science:")
    service.filter_by_department("Computer Science")


    # Faculty Management
    faculty_service = FacultyService()

    existing_faculty_ids = {
        faculty.faculty_id for faculty in get_faculty()
    }

    if f1.faculty_id not in existing_faculty_ids:
        faculty_service.add_faculty(f1)

    print("\nAll Faculty:")
    faculty_service.list_faculty()


    # Course Management
    course_service = CourseService()

    c2 = Course(
        "CS102", "Database Management", 3
    )

    existing_course_codes = {
        course.course_code for course in get_courses()
    }

    if c1.course_code not in existing_course_codes:
        course_service.add_course(c1)

    if c2.course_code not in existing_course_codes:
        course_service.add_course(c2)

    print("\nAll Courses:")
    course_service.list_courses()

    print("\nUpdating Course:")
    course_service.update_course("CS101", credits=5)

    print("\nRemoving Course:")
    course_service.remove_course("CS102")

    print("\nRemaining Courses:")
    course_service.list_courses()


    # Get Records from SQLite Database
    students = get_students()
    faculties = get_faculty()
    courses = get_courses()

    print("\nAll Students (Sorted by Name):")
    service.list_students()

    print("\nStudents in Computer Science:")
    service.filter_by_department("Computer Science")


    # Asynchronous Programming
    asyncio.run(
        run_async_tasks(
            students,
            faculties,
            courses
        )
    )


    # Saving Reports using Context Manager
    with ReportWriter("reports/You.txt") as report:
        report.write("Student Report\n")
        report.write("Name: Gladson\n")

    with ReportWriter("reports/faculty.txt") as report:
        report.write("Faculty Report\n")

    with ReportWriter("reports/courses.txt") as report:
        report.write("Course Report\n")


    # Student Iterator
    print("\nTesting StudentIterator:")

    for student in StudentIterator(students):
        print(student.name)


    # Enrollment Management
    enrollment_service = EnrollmentService()

    student = next(
        (s for s in students if s.student_id == 101),
        students[0]
    )

    course = next(
        (c for c in courses if c.course_code == "CS101"),
        courses[0]
    )    
    print("\nEnrolling Student:")

    existing_enrollments = get_enrollments()

    already_enrolled = any(
        e.student_id == student.student_id and
        e.course_code == course.course_code
        for e in existing_enrollments
    )

    if not already_enrolled:
        enrollment_service.enroll_student(student, course)
    else:
        print("Student is already enrolled in this course!")

    print("\nAll Enrollments:")
    enrollment_service.list_enrollments()

    print("\nRemoving Enrollment:")
    enrollment_service.remove_enrollment(
        student.student_id,
        course.course_code
    )

    print("\nRemaining Enrollments:")
    enrollment_service.list_enrollments()


    # Refresh Data from Database
    students = get_students()
    faculties = get_faculty()
    courses = get_courses()
    enrollments = get_enrollments()


    # Saving All Application Data
    print("\nSaving Application Data...")

    save_You_json(students)
    save_faculty_json(faculties)
    save_courses_json(courses)
    save_enrollments_json(enrollments)

    print("All Application Data Saved Successfully.")


    # Threading - Generate Multiple Reports
    print("\nGenerating Reports...")

    student_thread = threading.Thread(
        target=generate_student_report,
        args=(students,)
    )

    faculty_thread = threading.Thread(
        target=generate_faculty_report,
        args=(faculties,)
    )

    course_thread = threading.Thread(
        target=generate_course_report,
        args=(courses,)
    )

    student_thread.start()
    faculty_thread.start()
    course_thread.start()

    student_thread.join()
    faculty_thread.join()
    course_thread.join()

    print("All reports generated successfully!")
    print("Done.")


    # Multiprocessing - Calculate Summary
    summary_process = multiprocessing.Process(
        target=calculate_summary,
        args=(
            len(students),
            len(faculties),
            len(courses),
            len(enrollments)
        )
    )

    summary_process.start()
    summary_process.join()

    print("Summary process completed")


# Main Execution
if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
