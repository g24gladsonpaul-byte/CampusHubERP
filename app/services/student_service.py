
from app.utils.decorators import log_decorator, time_decorator
from app.utils.logger import logger

from app.database.repository import (
    add_student as db_add_student,
    get_students,
    update_student as db_update_student,
    delete_student as db_delete_student
)


class StudentService:

    def __init__(self):
        pass

    @log_decorator
    @time_decorator
    def add_student(self, student):
        try:
            db_add_student(
                student.student_id,
                student.name,
                student.age,
                student.email,
                student.department
            )
            logger.info(f"Student Added: {student.student_id}")

        except Exception as e:
            logger.error(f"Error adding student: {e}")
            print(f"Unable to add student: {e}")

    @log_decorator
    @time_decorator
    def remove_student(self, student_id):
        try:
            db_delete_student(student_id)
            logger.info(f"Student Deleted: {student_id}")

        except Exception as e:
            logger.error(f"Error deleting student: {e}")
            raise

    @log_decorator
    @time_decorator
    def update_student(self, student_id, name=None, age=None,
                       email=None, department=None):

        try:
            update_data = {}

            if name is not None:
                update_data["name"] = name

            if age is not None:
                update_data["age"] = age

            if email is not None:
                update_data["email"] = email

            if department is not None:
                update_data["department"] = department

            if update_data:
                db_update_student(student_id, **update_data)
                logger.info(f"Student Updated: {student_id}")

        except Exception as e:
            logger.error(f"Error updating student: {e}")
            raise

    def get_all_students(self):
        return get_students()

    def get_student_by_id(self, student_id):
        students = get_students()

        for student in students:
            if student.student_id == student_id:
                return student

        return None

    @log_decorator
    @time_decorator
    def list_students(self):

        students = get_students()

        sorted_students = sorted(
            students,
            key=lambda student: student.name.lower()
        )

        uppercase_names = map(
            lambda student: student.name.upper(),
            sorted_students
        )

        for student, name in zip(sorted_students, uppercase_names):
            print("Student ID:", student.student_id)
            print("Name:", name)
            print("Age:", student.age)
            print("Email:", student.email)
            print("Department:", student.department)
            print()

    @log_decorator
    @time_decorator
    def filter_by_department(self, department):

        students = get_students()

        department_students = filter(
            lambda student: student.department.lower() == department.lower(),
            students
        )

        found = False

        for student in department_students:
            found = True

            print("Student ID:", student.student_id)
            print("Name:", student.name)
            print("Age:", student.age)
            print("Email:", student.email)
            print("Department:", student.department)
            print()

        if not found:
            print("No students found in this department")
