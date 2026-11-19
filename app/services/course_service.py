from app.utils.decorators import log_decorator, time_decorator

from app.database.repository import (
    add_course as db_add_course,
    get_courses,
    update_course as db_update_course,
    delete_course as db_delete_course
)


class CourseService:

    def __init__(self):
        pass

    @log_decorator
    @time_decorator
    def add_course(self, course):

        db_add_course(
            course.course_code,
            course.course_name,
            course.credits
        )

    @log_decorator
    @time_decorator
    def remove_course(self, course_code):

        db_delete_course(course_code)

    @log_decorator
    @time_decorator
    def update_course(self, course_code, course_name=None, credits=None):

        update_data = {}

        if course_name is not None:
            update_data["course_name"] = course_name

        if credits is not None:
            update_data["credits"] = credits

        if update_data:
            db_update_course(course_code, **update_data)


    def get_all_courses(self):
        return get_courses()

    def get_course_by_code(self, course_code):
        courses = get_courses()

        for course in courses:
            if course.course_code == course_code:
                return course

        return None
    
    @log_decorator
    @time_decorator
    def list_courses(self):

        courses = get_courses()

        for course in courses:

            print("Course Code:", course.course_code)
            print("Course Name:", course.course_name)
            print("Credits:", course.credits)
            print()