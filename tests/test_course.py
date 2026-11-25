
from types import SimpleNamespace

from app.services import course_service
from app.services.course_service import CourseService


def test_add_course(monkeypatch):
    service = CourseService()

    course = SimpleNamespace(
        course_code="TEST501",
        course_name="Python Testing",
        credits=4
    )

    result = {}

    def mock_add_course(*args):
        result["data"] = args

    monkeypatch.setattr(
        course_service,
        "db_add_course",
        mock_add_course
    )

    service.add_course(course)

    assert result["data"] == (
        "TEST501",
        "Python Testing",
        4
    )


def test_update_course(monkeypatch):
    service = CourseService()

    result = {}

    def mock_update_course(course_code, **kwargs):
        result["course_code"] = course_code
        result["data"] = kwargs

    monkeypatch.setattr(
        course_service,
        "db_update_course",
        mock_update_course
    )

    service.update_course(
        "TEST501",
        course_name="Updated Python",
        credits=5
    )

    assert result["course_code"] == "TEST501"
    assert result["data"] == {
        "course_name": "Updated Python",
        "credits": 5
    }


def test_delete_course(monkeypatch):
    service = CourseService()

    result = {}

    def mock_delete_course(course_code):
        result["course_code"] = course_code

    monkeypatch.setattr(
        course_service,
        "db_delete_course",
        mock_delete_course
    )

    service.remove_course("TEST501")

    assert result["course_code"] == "TEST501"


def test_search_course(monkeypatch):
    service = CourseService()

    courses = [
        SimpleNamespace(
            course_code="TEST501",
            course_name="Python Testing"
        ),
        SimpleNamespace(
            course_code="TEST502",
            course_name="Database Management"
        )
    ]

    monkeypatch.setattr(
        course_service,
        "get_courses",
        lambda: courses
    )

    result = service.get_course_by_code("TEST501")

    assert result is not None
    assert result.course_code == "TEST501"
    assert result.course_name == "Python Testing"


def test_search_course_not_found(monkeypatch):
    service = CourseService()

    monkeypatch.setattr(
        course_service,
        "get_courses",
        lambda: []
    )

    result = service.get_course_by_code("UNKNOWN")

    assert result is None
