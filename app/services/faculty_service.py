from app.utils.decorators import log_decorator, time_decorator

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

        db_add_faculty(
            faculty.faculty_id,
            faculty.name,
            faculty.age,
            faculty.email,
            faculty.department
        )

    @log_decorator
    @time_decorator
    def remove_faculty(self, faculty_id):

        db_delete_faculty(faculty_id)

    @log_decorator
    @time_decorator
    def update_faculty(self, faculty_id, name=None, age=None,
                       email=None, department=None):

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