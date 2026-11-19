
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.faculty_service import FacultyService
from app.models.faculty import Faculty


router = APIRouter(
    prefix="/faculty",
    tags=["Faculty"]
)

# Create FacultyService object
faculty_service = FacultyService()


# Faculty Request Model
class FacultyCreate(BaseModel):
    faculty_id: int
    name: str
    age: int
    email: str
    department: str


class FacultyUpdate(BaseModel):
    name: str
    age: int
    email: str
    department: str


# Convert faculty object into dictionary
def faculty_to_dict(faculty):
    return {
        "faculty_id": faculty.faculty_id,
        "name": faculty.name,
        "age": faculty.age,
        "email": faculty.email,
        "department": faculty.department
    }


# GET - Display all faculty
@router.get("")
def get_all_faculty():

    faculties = faculty_service.get_all_faculty()

    return [
        faculty_to_dict(faculty)
        for faculty in faculties
    ]


# GET - Display faculty by ID
@router.get("/{faculty_id}")
def get_faculty(faculty_id: int):

    faculty = faculty_service.get_faculty_by_id(faculty_id)

    if faculty is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty not found"
        )

    return faculty_to_dict(faculty)


# POST - Add faculty
@router.post("")
def create_faculty(data: FacultyCreate):

    existing = faculty_service.get_faculty_by_id(
        data.faculty_id
    )

    if existing is not None:
        raise HTTPException(
            status_code=400,
            detail="Faculty ID already exists"
        )

    new_faculty = Faculty(
        data.faculty_id,
        data.name,
        data.age,
        data.email,
        data.department
    )

    faculty_service.add_faculty(new_faculty)

    saved_faculty = faculty_service.get_faculty_by_id(
        data.faculty_id
    )

    if saved_faculty is None:
        raise HTTPException(
            status_code=500,
            detail="Unable to add faculty"
        )

    return {
        "message": "Faculty added successfully",
        "faculty": faculty_to_dict(saved_faculty)
    }


# PUT - Update faculty
@router.put("/{faculty_id}")
def update_faculty(faculty_id: int, data: FacultyUpdate):

    existing = faculty_service.get_faculty_by_id(faculty_id)

    if existing is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty not found"
        )

    faculty_service.update_faculty(
        faculty_id,
        name=data.name,
        age=data.age,
        email=data.email,
        department=data.department
    )

    updated_faculty = faculty_service.get_faculty_by_id(
        faculty_id
    )

    if updated_faculty is None:
        raise HTTPException(
            status_code=500,
            detail="Unable to update faculty"
        )

    return {
        "message": "Faculty updated successfully",
        "faculty": faculty_to_dict(updated_faculty)
    }


# DELETE - Remove faculty
@router.delete("/{faculty_id}")
def delete_faculty(faculty_id: int):

    existing = faculty_service.get_faculty_by_id(faculty_id)

    if existing is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty not found"
        )

    faculty_service.remove_faculty(faculty_id)

    return {
        "message": "Faculty deleted successfully"
    }
