
from app.models.student import Student
from app.models.faculty import Faculty
from app.models.course import Course


class ModelFactory:

    @staticmethod
    def create_object(object_type, *args):
        object_type = object_type.lower()

        if object_type == "student":
            return Student(*args)

        elif object_type == "faculty":
            return Faculty(*args)

        elif object_type == "course":
            return Course(*args)

        else:
            raise ValueError("Invalid object type!")
