
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.course_service import CourseService
from app.models.course import Course


router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)

# Create CourseService object
course_service = CourseService()


# Course Request Models
class CourseCreate(BaseModel):
    course_code: str
    course_name: str
    credits: int


class CourseUpdate(BaseModel):
    course_name: str
    credits: int


# Convert course object into dictionary
def course_to_dict(course):
    return {
        "course_code": course.course_code,
        "course_name": course.course_name,
        "credits": course.credits
    }


# GET - Display all courses
@router.get("")
def get_all_courses():

    courses = course_service.get_all_courses()

    return [
        course_to_dict(course)
        for course in courses
    ]


# GET - Display course by code
@router.get("/{course_code}")
def get_course(course_code: str):

    course = course_service.get_course_by_code(course_code)

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course_to_dict(course)


# POST - Add course
@router.post("")
def create_course(data: CourseCreate):

    existing = course_service.get_course_by_code(
        data.course_code
    )

    if existing is not None:
        raise HTTPException(
            status_code=400,
            detail="Course code already exists"
        )

    new_course = Course(
        data.course_code,
        data.course_name,
        data.credits
    )

    course_service.add_course(new_course)

    saved_course = course_service.get_course_by_code(
        data.course_code
    )

    if saved_course is None:
        raise HTTPException(
            status_code=500,
            detail="Unable to add course"
        )

    return {
        "message": "Course added successfully",
        "course": course_to_dict(saved_course)
    }


# PUT - Update course
@router.put("/{course_code}")
def update_course(course_code: str, data: CourseUpdate):

    existing = course_service.get_course_by_code(course_code)

    if existing is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    course_service.update_course(
        course_code,
        course_name=data.course_name,
        credits=data.credits
    )

    updated_course = course_service.get_course_by_code(
        course_code
    )

    if updated_course is None:
        raise HTTPException(
            status_code=500,
            detail="Unable to update course"
        )

    return {
        "message": "Course updated successfully",
        "course": course_to_dict(updated_course)
    }


# DELETE - Remove course
@router.delete("/{course_code}")
def delete_course(course_code: str):

    existing = course_service.get_course_by_code(course_code)

    if existing is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    course_service.remove_course(course_code)

    return {
        "message": "Course deleted successfully"
    }
