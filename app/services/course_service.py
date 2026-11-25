
from app.utils.decorators import log_decorator, time_decorator
from app.utils.logger import logger

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

        try:
            db_add_course(
                course.course_code,
                course.course_name,
                course.credits
            )

            logger.info(f"Course Added: {course.course_code}")

        except Exception as e:
            logger.error(f"Error adding course: {e}")
            print(f"Unable to add course: {e}")

    @log_decorator
    @time_decorator
    def remove_course(self, course_code):

        try:
            db_delete_course(course_code)
            logger.info(f"Course Deleted: {course_code}")

        except Exception as e:
            logger.error(f"Error deleting course: {e}")
            raise

    @log_decorator
    @time_decorator
    def update_course(self, course_code, course_name=None, credits=None):

        try:
            update_data = {}

            if course_name is not None:
                update_data["course_name"] = course_name

            if credits is not None:
                update_data["credits"] = credits

            if update_data:
                db_update_course(course_code, **update_data)
                logger.info(f"Course Updated: {course_code}")

        except Exception as e:
            logger.error(f"Error updating course: {e}")
            raise

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
