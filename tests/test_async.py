import asyncio
from app.services.async_service import load_all_data

asyncio.run(load_all_data())



from app.models.student import Student
from app.models.faculty import Faculty
from app.models.course import Course

from app.services.async_service import generate_all_reports


students = [
    Student(101, "Gladson", 20, "gladson@example.com", "Computer Science"),
    Student(102, "Rahul", 21, "rahul@example.com", "Information Technology"),
    Student(103, "Priya", 19, "priya@example.com", "Computer Science")
]

faculties = [
    Faculty(201, "Rahul", 35, "rahul@example.com", "Computer Science")
]

courses = [
    Course("CS101", "Python Programming", 5)
]


asyncio.run(generate_all_reports(students, faculties, courses))
