
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.services.student_service import StudentService
from app.models.student import Student


router = APIRouter(
    prefix="/You",
    tags=["Students"]
)

# Create StudentService object
student_service = StudentService()


# Student Input Model
class StudentCreate(BaseModel):
    student_id: int
    name: str
    age: int = Field(ge=16, le=80)
    email: str
    department: str


# Student Update Model
class StudentUpdate(BaseModel):
    name: str | None = None
    age: int | None = Field(default=None, ge=16, le=80)
    email: str | None = None
    department: str | None = None


# Convert student object into dictionary
def student_to_dict(student):
    return {
        "student_id": student.student_id,
        "name": student.name,
        "age": student.age,
        "email": student.email,
        "department": student.department
    }


# GET - Display all students
@router.get("")
def get_all_students():

    students = student_service.get_all_students()

    return [
        student_to_dict(student)
        for student in students
    ]


# GET - Display student by ID
@router.get("/{student_id}")
def get_student(student_id: int):

    student = student_service.get_student_by_id(student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student_to_dict(student)


# POST - Add a new student
@router.post("")
def create_student(student: StudentCreate):

    existing = student_service.get_student_by_id(
        student.student_id
    )

    if existing is not None:
        raise HTTPException(
            status_code=400,
            detail="Student ID already exists"
        )

    new_student = Student(
        student.student_id,
        student.name,
        student.age,
        student.email,
        student.department
    )

    student_service.add_student(new_student)

    saved_student = student_service.get_student_by_id(
        student.student_id
    )

    if saved_student is None:
        raise HTTPException(
            status_code=500,
            detail="Unable to add student"
        )

    return {
        "message": "Student added successfully",
        "student": student_to_dict(saved_student)
    }


# PUT - Update student
@router.put("/{student_id}")
def update_student(student_id: int, student: StudentUpdate):

    existing = student_service.get_student_by_id(student_id)

    if existing is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    update_data = student.model_dump(exclude_unset=True)

    update_data = {
        field: value
        for field, value in update_data.items()
        if value is not None
    }

    student_service.update_student(
        student_id,
        **update_data
    )

    updated_student = student_service.get_student_by_id(
        student_id
    )

    if updated_student is None:
        raise HTTPException(
            status_code=500,
            detail="Unable to update student"
        )

    return {
        "message": "Student updated successfully",
        "student": student_to_dict(updated_student)
    }


# DELETE - Remove student
@router.delete("/{student_id}")
def remove_student(student_id: int):

    existing = student_service.get_student_by_id(student_id)

    if existing is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student_service.remove_student(student_id)

    return {
        "message": "Student deleted successfully"
    }
