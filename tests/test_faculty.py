
from types import SimpleNamespace

from app.services import faculty_service
from app.services.faculty_service import FacultyService


def test_add_faculty(monkeypatch):
    service = FacultyService()

    faculty = SimpleNamespace(
        faculty_id=501,
        name="Test Faculty",
        age=35,
        email="faculty501@example.com",
        department="Computer Science"
    )

    result = {}

    def mock_add_faculty(*args):
        result["data"] = args

    monkeypatch.setattr(
        faculty_service,
        "db_add_faculty",
        mock_add_faculty
    )

    service.add_faculty(faculty)

    assert result["data"] == (
        501,
        "Test Faculty",
        35,
        "faculty501@example.com",
        "Computer Science"
    )


def test_update_faculty(monkeypatch):
    service = FacultyService()

    result = {}

    def mock_update_faculty(faculty_id, **kwargs):
        result["faculty_id"] = faculty_id
        result["data"] = kwargs

    monkeypatch.setattr(
        faculty_service,
        "db_update_faculty",
        mock_update_faculty
    )

    service.update_faculty(
        501,
        name="Updated Faculty",
        department="Information Technology"
    )

    assert result["faculty_id"] == 501
    assert result["data"] == {
        "name": "Updated Faculty",
        "department": "Information Technology"
    }


def test_delete_faculty(monkeypatch):
    service = FacultyService()

    result = {}

    def mock_delete_faculty(faculty_id):
        result["faculty_id"] = faculty_id

    monkeypatch.setattr(
        faculty_service,
        "db_delete_faculty",
        mock_delete_faculty
    )

    service.remove_faculty(501)

    assert result["faculty_id"] == 501


def test_search_faculty(monkeypatch):
    service = FacultyService()

    faculties = [
        SimpleNamespace(faculty_id=501, name="Test Faculty"),
        SimpleNamespace(faculty_id=502, name="Rahul")
    ]

    monkeypatch.setattr(
        faculty_service,
        "get_faculty",
        lambda: faculties
    )

    result = service.get_faculty_by_id(501)

    assert result is not None
    assert result.faculty_id == 501
    assert result.name == "Test Faculty"


def test_search_faculty_not_found(monkeypatch):
    service = FacultyService()

    monkeypatch.setattr(
        faculty_service,
        "get_faculty",
        lambda: []
    )

    result = service.get_faculty_by_id(999)

    assert result is None
