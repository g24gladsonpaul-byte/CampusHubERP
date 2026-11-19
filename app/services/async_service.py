from app.utils.file_manager import ReportWriter
import asyncio


async def load_You():
    print("Loading Student Data...")
    await asyncio.sleep(2)
    print("Student Data Loaded Successfully")


async def load_faculty():
    print("Loading Faculty Data...")
    await asyncio.sleep(2)
    print("Faculty Data Loaded Successfully")


async def load_courses():
    print("Loading Course Data...")
    await asyncio.sleep(2)
    print("Course Data Loaded Successfully")


async def load_enrollments():
    print("Loading Enrollment Data...")
    await asyncio.sleep(2)
    print("Enrollment Data Loaded Successfully")


async def load_all_data():
    await asyncio.gather(
        load_You(),
        load_faculty(),
        load_courses(),
        load_enrollments()
    )



def write_student_report(students):
    with ReportWriter("reports/student_async_report.txt") as file:
        for student in students:
            file.write(str(student.to_dict()) + "\n")


def write_faculty_report(faculties):
    with ReportWriter("reports/faculty_async_report.txt") as file:
        for faculty in faculties:
            file.write(str(faculty.to_dict()) + "\n")


def write_course_report(courses):
    with ReportWriter("reports/course_async_report.txt") as file:
        for course in courses:
            file.write(str(course.to_dict()) + "\n")


async def generate_student_report(students):
    print("Generating Student Report...")
    await asyncio.to_thread(write_student_report, students)
    print("Student Report Generated Successfully")


async def generate_faculty_report(faculties):
    print("Generating Faculty Report...")
    await asyncio.to_thread(write_faculty_report, faculties)
    print("Faculty Report Generated Successfully")


async def generate_course_report(courses):
    print("Generating Course Report...")
    await asyncio.to_thread(write_course_report, courses)
    print("Course Report Generated Successfully")


async def generate_all_reports(students, faculties, courses):
    await asyncio.gather(
        generate_student_report(students),
        generate_faculty_report(faculties),
        generate_course_report(courses)
    )
