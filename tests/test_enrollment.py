
from types import SimpleNamespace

from app.services.enrollment_service import EnrollmentService


def test_add_enrollment(monkeypatch):

    service = EnrollmentService()
    called = {}

    def fake_add_enrollment(student_id, course_code):
        called["student_id"] = student_id
        called["course_code"] = course_code

    monkeypatch.setattr(
        "app.services.enrollment_service.db_add_enrollment",
        fake_add_enrollment
    )

    student = SimpleNamespace(student_id=101)
    course = SimpleNamespace(course_code="CS101")

    service.enroll_student(student, course)

    assert called["student_id"] == 101
    assert called["course_code"] == "CS101"


def test_update_enrollment(monkeypatch):

    service = EnrollmentService()
    called = {}

    def fake_update_enrollment(enrollment_id, **kwargs):
        called["enrollment_id"] = enrollment_id
        called.update(kwargs)

    monkeypatch.setattr(
        "app.services.enrollment_service.db_update_enrollment",
        fake_update_enrollment
    )

    service.update_enrollment(1, 102, "CS102")

    assert called["enrollment_id"] == 1
    assert called["student_id"] == 102
    assert called["course_code"] == "CS102"


def test_delete_enrollment(monkeypatch):

    service = EnrollmentService()
    deleted_ids = []

    enrollment = SimpleNamespace(
        enrollment_id=1,
        student_id=101,
        course_code="CS101"
    )

    monkeypatch.setattr(
        "app.services.enrollment_service.get_enrollments",
        lambda: [enrollment]
    )

    monkeypatch.setattr(
        "app.services.enrollment_service.db_delete_enrollment",
        lambda enrollment_id: deleted_ids.append(enrollment_id)
    )

    service.remove_enrollment(101, "CS101")

    assert deleted_ids == [1]


def test_search_enrollment(monkeypatch):

    service = EnrollmentService()

    enrollment = SimpleNamespace(
        enrollment_id=1,
        student_id=101,
        course_code="CS101"
    )

    monkeypatch.setattr(
        "app.services.enrollment_service.get_enrollments",
        lambda: [enrollment]
    )

    result = service.get_enrollment_by_id(1)

    assert result == enrollment


def test_search_enrollment_not_found(monkeypatch):

    service = EnrollmentService()

    monkeypatch.setattr(
        "app.services.enrollment_service.get_enrollments",
        lambda: []
    )

    result = service.get_enrollment_by_id(999)

    assert result is None
