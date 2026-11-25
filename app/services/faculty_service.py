
from app.utils.decorators import log_decorator, time_decorator
from app.utils.logger import logger

from app.database.repository import (
    add_faculty as db_add_faculty,
    get_faculty,
    update_faculty as db_update_faculty,
    delete_faculty as db_delete_faculty
)


class FacultyService:

    def __init__(self):
        pass

    @log_decorator
    @time_decorator
    def add_faculty(self, faculty):

        try:
            db_add_faculty(
                faculty.faculty_id,
                faculty.name,
                faculty.age,
                faculty.email,
                faculty.department
            )

            logger.info(f"Faculty Added: {faculty.faculty_id}")

        except Exception as e:
            logger.error(f"Error adding faculty: {e}")
            raise

    @log_decorator
    @time_decorator
    def remove_faculty(self, faculty_id):

        try:
            db_delete_faculty(faculty_id)
            logger.info(f"Faculty Deleted: {faculty_id}")

        except Exception as e:
            logger.error(f"Error deleting faculty: {e}")
            raise

    @log_decorator
    @time_decorator
    def update_faculty(self, faculty_id, name=None, age=None,
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
                db_update_faculty(faculty_id, **update_data)
                logger.info(f"Faculty Updated: {faculty_id}")

        except Exception as e:
            logger.error(f"Error updating faculty: {e}")
            raise

    def get_all_faculty(self):
        return get_faculty()

    def get_faculty_by_id(self, faculty_id):
        faculties = get_faculty()

        for faculty in faculties:
            if faculty.faculty_id == faculty_id:
                return faculty

        return None

    @log_decorator
    @time_decorator
    def list_faculty(self):

        faculties = get_faculty()

        for faculty in faculties:

            print("Faculty ID:", faculty.faculty_id)
            print("Name:", faculty.name)
            print("Age:", faculty.age)
            print("Email:", faculty.email)
            print("Department:", faculty.department)
            print()
