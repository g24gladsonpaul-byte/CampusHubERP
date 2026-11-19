
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.enrollment_service import EnrollmentService
from app.services.student_service import StudentService
from app.services.course_service import CourseService

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

enrollment_service = EnrollmentService()
student_service = StudentService()
course_service = CourseService()


# Request Models
class EnrollmentCreate(BaseModel):
    student_id: int
    course_code: str


class EnrollmentUpdate(BaseModel):
    student_id: int
    course_code: str


# Convert enrollment to dictionary
def enrollment_to_dict(enrollment):

    student = enrollment.student
    course = enrollment.course

    return {
        "enrollment_id": enrollment.enrollment_id,
        "student_id": enrollment.student_id,
        "student_name": student.name if student else None,
        "course_code": enrollment.course_code,
        "course_name": course.course_name if course else None
    }


# GET all enrollments
@router.get("")
def get_all_enrollments():

    enrollments = enrollment_service.get_all_enrollments()

    return [
        enrollment_to_dict(enrollment)
        for enrollment in enrollments
    ]


# GET enrollment by ID
@router.get("/{enrollment_id}")
def get_enrollment(enrollment_id: int):

    enrollment = enrollment_service.get_enrollment_by_id(
        enrollment_id
    )

    if not enrollment:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    return enrollment_to_dict(enrollment)


# CREATE enrollment
@router.post("")
def create_enrollment(data: EnrollmentCreate):

    student = student_service.get_student_by_id(data.student_id)

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    course = course_service.get_course_by_code(data.course_code)

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    enrollments = enrollment_service.get_all_enrollments()

    for enrollment in enrollments:

        if (enrollment.student_id == data.student_id and
                enrollment.course_code == data.course_code):

            raise HTTPException(
                status_code=400,
                detail="Student is already enrolled in this course"
            )

    enrollment_service.enroll_student(student, course)

    # Get the newly created enrollment
    updated_enrollments = enrollment_service.get_all_enrollments()

    for enrollment in updated_enrollments:

        if (enrollment.student_id == data.student_id and
                enrollment.course_code == data.course_code):

            return {
                "message": "Enrollment added successfully",
                "enrollment_id": enrollment.enrollment_id,
                "student_id": enrollment.student_id,
                "course_code": enrollment.course_code
            }

    raise HTTPException(
        status_code=500,
        detail="Unable to create enrollment"
    )


# UPDATE enrollment
@router.put("/{enrollment_id}")
def update_enrollment(enrollment_id: int, data: EnrollmentUpdate):

    enrollment = enrollment_service.get_enrollment_by_id(
        enrollment_id
    )

    if not enrollment:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    student = student_service.get_student_by_id(data.student_id)

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    course = course_service.get_course_by_code(data.course_code)

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    enrollments = enrollment_service.get_all_enrollments()

    for existing in enrollments:

        if (existing.student_id == data.student_id and
                existing.course_code == data.course_code and
                existing.enrollment_id != enrollment_id):

            raise HTTPException(
                status_code=400,
                detail="Student is already enrolled in this course"
            )

    enrollment_service.update_enrollment(
        enrollment_id,
        data.student_id,
        data.course_code
    )

    updated = enrollment_service.get_enrollment_by_id(enrollment_id)

    if not updated:
        raise HTTPException(
            status_code=500,
            detail="Unable to update enrollment"
        )

    return {
        "message": "Enrollment updated successfully",
        "enrollment_id": updated.enrollment_id,
        "student_id": updated.student_id,
        "course_code": updated.course_code
    }


# DELETE enrollment
@router.delete("/{enrollment_id}")
def delete_enrollment(enrollment_id: int):

    enrollment = enrollment_service.get_enrollment_by_id(
        enrollment_id
    )

    if not enrollment:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    enrollment_service.remove_enrollment(
        enrollment.student_id,
        enrollment.course_code
    )

    return {
        "message": "Enrollment deleted successfully"
    }
