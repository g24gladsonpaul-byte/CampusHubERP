
from app.utils.decorators import log_decorator, time_decorator
from app.utils.logger import logger

from app.database.repository import (
    add_enrollment as db_add_enrollment,
    get_enrollments,
    delete_enrollment as db_delete_enrollment,
    update_enrollment as db_update_enrollment
)


class EnrollmentService:

    def __init__(self):
        pass

    @log_decorator
    @time_decorator
    def enroll_student(self, student, course):

        try:
            db_add_enrollment(
                student.student_id,
                course.course_code
            )

            logger.info(
                f"Enrollment Created: Student {student.student_id}, "
                f"Course {course.course_code}"
            )

        except Exception as e:
            logger.error(f"Error creating enrollment: {e}")
            print(f"Unable to create enrollment: {e}")

    @log_decorator
    @time_decorator
    def remove_enrollment(self, student_id, course_code):

        try:
            enrollments = get_enrollments()

            found = False

            for enrollment in enrollments:

                if (enrollment.student_id == student_id and
                        enrollment.course_code == course_code):

                    db_delete_enrollment(enrollment.enrollment_id)
                    logger.info(
                        f"Enrollment Deleted: Student {student_id}, "
                        f"Course {course_code}"
                    )
                    found = True

            if not found:
                print("Enrollment not found")

        except Exception as e:
            logger.error(f"Error deleting enrollment: {e}")
            raise

    @log_decorator
    @time_decorator
    def list_enrollments(self):

        enrollments = get_enrollments()

        if not enrollments:
            print("No enrollments found")
            return

        for enrollment in enrollments:

            student = enrollment.student
            course = enrollment.course

            print("Student ID:", student.student_id)
            print("Student Name:", student.name)
            print("Course Code:", course.course_code)
            print("Course Name:", course.course_name)
            print()

    # Get all enrollments for FastAPI
    def get_all_enrollments(self):

        return get_enrollments()

    # Get enrollment by ID for FastAPI
    def get_enrollment_by_id(self, enrollment_id):

        enrollments = get_enrollments()

        for enrollment in enrollments:

            if enrollment.enrollment_id == enrollment_id:
                return enrollment

        return None

    # Update enrollment for FastAPI
    @log_decorator
    @time_decorator
    def update_enrollment(self, enrollment_id, student_id, course_code):

        try:
            db_update_enrollment(
                enrollment_id,
                student_id=student_id,
                course_code=course_code
            )

            logger.info(f"Enrollment Updated: {enrollment_id}")

        except Exception as e:
            logger.error(f"Error updating enrollment: {e}")
            raise
