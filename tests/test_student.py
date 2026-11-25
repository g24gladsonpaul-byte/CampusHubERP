
from types import SimpleNamespace

from app.services import student_service
from app.services.student_service import StudentService


def test_add_student(monkeypatch):
    service = StudentService()
    student = SimpleNamespace(
        student_id=501,
        name="Test Student",
        age=20,
        email="test501@example.com",
        department="Computer Science"
    )

    result = {}

    def mock_add_student(*args):
        result["data"] = args

    monkeypatch.setattr(
        student_service,
        "db_add_student",
        mock_add_student
    )

    service.add_student(student)

    assert result["data"] == (
        501,
        "Test Student",
        20,
        "test501@example.com",
        "Computer Science"
    )


def test_update_student(monkeypatch):
    service = StudentService()

    result = {}

    def mock_update_student(student_id, **kwargs):
        result["student_id"] = student_id
        result["data"] = kwargs

    monkeypatch.setattr(
        student_service,
        "db_update_student",
        mock_update_student
    )

    service.update_student(
        501,
        name="Updated Student",
        department="Information Technology"
    )

    assert result["student_id"] == 501
    assert result["data"] == {
        "name": "Updated Student",
        "department": "Information Technology"
    }


def test_delete_student(monkeypatch):
    service = StudentService()

    result = {}

    def mock_delete_student(student_id):
        result["student_id"] = student_id

    monkeypatch.setattr(
        student_service,
        "db_delete_student",
        mock_delete_student
    )

    service.remove_student(501)

    assert result["student_id"] == 501


def test_search_student(monkeypatch):
    service = StudentService()

    students = [
        SimpleNamespace(student_id=501, name="Test Student"),
        SimpleNamespace(student_id=502, name="Rahul")
    ]

    monkeypatch.setattr(
        student_service,
        "get_students",
        lambda: students
    )

    result = service.get_student_by_id(501)

    assert result is not None
    assert result.student_id == 501
    assert result.name == "Test Student"


def test_search_student_not_found(monkeypatch):
    service = StudentService()

    monkeypatch.setattr(
        student_service,
        "get_students",
        lambda: []
    )

    result = service.get_student_by_id(999)

    assert result is None
