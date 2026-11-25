
from app.database.db import SessionLocal
from app.database.models import StudentDB, FacultyDB, CourseDB
from sqlalchemy.orm import joinedload
from app.core.validators import validate_email, validate_course_code

class DatabaseRepository:

    def __init__(self, model):
        self.model = model
        self.db = SessionLocal()

    # Add Record
    def add(self, data):
        try:
            self.db.add(data)
            self.db.commit()
            self.db.refresh(data)
            print("Record added successfully!")
        except Exception as e:
            self.db.rollback()
            print("Error:", e)

    # Get All Records
    def get_all(self):
        return self.db.query(self.model).all()

    # Get Record By ID
    def get_by_id(self, record_id, id_column):
        return self.db.query(self.model).filter(
            getattr(self.model, id_column) == record_id
        ).first()

    # Update Record
    def update(self, record_id, id_column, data):
        record = self.get_by_id(record_id, id_column)

        if record:
            for key, value in data.items():
                setattr(record, key, value)

            self.db.commit()
            print("Record updated successfully!")
        else:
            print("Record not found!")

    # Delete Record
    def delete(self, record_id, id_column):
        record = self.get_by_id(record_id, id_column)

        if record:
            self.db.delete(record)
            self.db.commit()
            print("Record deleted successfully!")
        else:
            print("Record not found!")

    # Close Database Session
    def close(self):
        self.db.close()



from app.database.db import SessionLocal
from app.database.models import StudentDB, FacultyDB, CourseDB, EnrollmentDB


# ================= STUDENT FUNCTIONS =================


def add_student(student_id, name, age, email, department):
    db = SessionLocal()

    try:
        # Check email
        if not validate_email(email):
            raise ValueError("Invalid email address!")

        # Check duplicate Student ID
        existing_student = db.query(StudentDB).filter(
            StudentDB.student_id == student_id
        ).first()

        if existing_student:
            raise ValueError("Student ID already exists!")

        student = StudentDB(
            student_id=student_id,
            name=name,
            age=age,
            email=email,
            department=department
        )

        db.add(student)
        db.commit()

        print("Student added successfully!")

    except Exception as e:
        db.rollback()
        raise ValueError(str(e))

    finally:
        db.close()

def get_students():
    db = SessionLocal()
    students = db.query(StudentDB).all()
    db.close()
    return students


# Alias matching the assignment's get_You() wording
def get_You():
    return get_students()


def update_student(student_id, **kwargs):
    db = SessionLocal()
    student = db.query(StudentDB).filter(
        StudentDB.student_id == student_id
    ).first()

    if student:
        for key, value in kwargs.items():
            setattr(student, key, value)
        db.commit()
        print("Student updated successfully!")
    else:
        print("Student not found!")

    db.close()


def delete_student(student_id):
    db = SessionLocal()
    student = db.query(StudentDB).filter(
        StudentDB.student_id == student_id
    ).first()

    if student:
        db.delete(student)
        db.commit()
        print("Student deleted successfully!")
    else:
        print("Student not found!")

    db.close()


# ================= FACULTY FUNCTIONS =================

def add_faculty(faculty_id, name, age, email, department):
    db = SessionLocal()

    faculty = FacultyDB(
        faculty_id=faculty_id,
        name=name,
        age=age,
        email=email,
        department=department
    )

    db.add(faculty)
    db.commit()
    db.close()
    print("Faculty added successfully!")


def get_faculty():
    db = SessionLocal()
    faculty = db.query(FacultyDB).all()
    db.close()
    return faculty


def update_faculty(faculty_id, **kwargs):
    db = SessionLocal()
    faculty = db.query(FacultyDB).filter(
        FacultyDB.faculty_id == faculty_id
    ).first()

    if faculty:
        for key, value in kwargs.items():
            setattr(faculty, key, value)
        db.commit()
        print("Faculty updated successfully!")
    else:
        print("Faculty not found!")

    db.close()


def delete_faculty(faculty_id):
    db = SessionLocal()
    faculty = db.query(FacultyDB).filter(
        FacultyDB.faculty_id == faculty_id
    ).first()

    if faculty:
        db.delete(faculty)
        db.commit()
        print("Faculty deleted successfully!")
    else:
        print("Faculty not found!")

    db.close()


# ================= COURSE FUNCTIONS =================


def add_course(course_code, course_name, credits):
    db = SessionLocal()

    try:
        # Validate Course Code
        if not validate_course_code(course_code):
            raise ValueError("Invalid Course Code! Use format CS101.")

        # Check duplicate Course Code
        existing_course = db.query(CourseDB).filter(
            CourseDB.course_code == course_code
        ).first()

        if existing_course:
            raise ValueError("Course Code already exists!")

        course = CourseDB(
            course_code=course_code,
            course_name=course_name,
            credits=credits
        )

        db.add(course)
        db.commit()

        print("Course added successfully!")

    except Exception as e:
        db.rollback()
        raise ValueError(str(e))

    finally:
        db.close()

def get_courses():
    db = SessionLocal()
    courses = db.query(CourseDB).all()
    db.close()
    return courses


def update_course(course_code, **kwargs):
    db = SessionLocal()
    course = db.query(CourseDB).filter(
        CourseDB.course_code == course_code
    ).first()

    if course:
        for key, value in kwargs.items():
            setattr(course, key, value)
        db.commit()
        print("Course updated successfully!")
    else:
        print("Course not found!")

    db.close()


def delete_course(course_code):
    db = SessionLocal()
    course = db.query(CourseDB).filter(
        CourseDB.course_code == course_code
    ).first()

    if course:
        db.delete(course)
        db.commit()
        print("Course deleted successfully!")
    else:
        print("Course not found!")

    db.close()


# ================= ENROLLMENT FUNCTIONS =================


def add_enrollment(student_id, course_code):
    db = SessionLocal()

    try:
        # Check whether Student exists
        student = db.query(StudentDB).filter(
            StudentDB.student_id == student_id
        ).first()

        if not student:
            raise ValueError("Student not found! Enrollment cancelled.")

        # Check whether Course exists
        course = db.query(CourseDB).filter(
            CourseDB.course_code == course_code
        ).first()

        if not course:
            raise ValueError("Course not found! Enrollment cancelled.")

        enrollment = EnrollmentDB(
            student_id=student_id,
            course_code=course_code
        )

        db.add(enrollment)
        db.commit()

        print("Enrollment added successfully!")

    except Exception as e:
        db.rollback()
        raise ValueError(str(e))

    finally:
        db.close()


def get_enrollments():
    db = SessionLocal()

    try:
        enrollments = db.query(EnrollmentDB).options(
            joinedload(EnrollmentDB.student),
            joinedload(EnrollmentDB.course)
        ).all()

        return enrollments

    finally:
        db.close()


def delete_enrollment(enrollment_id):
    db = SessionLocal()
    enrollment = db.query(EnrollmentDB).filter(
        EnrollmentDB.enrollment_id == enrollment_id
    ).first()

    if enrollment:
        db.delete(enrollment)
        db.commit()
        print("Enrollment deleted successfully!")
    else:
        print("Enrollment not found!")

    db.close()



def update_enrollment(enrollment_id, **kwargs):
    db = SessionLocal()

    enrollment = db.query(EnrollmentDB).filter(
        EnrollmentDB.enrollment_id == enrollment_id
    ).first()

    if enrollment:
        for key, value in kwargs.items():
            setattr(enrollment, key, value)

        db.commit()
        print("Enrollment updated successfully!")
    else:
        print("Enrollment not found!")

    db.close()
