
from app.database.repository import (
    add_student, get_students, get_You,
    update_student, delete_student,
    add_faculty, get_faculty,
    update_faculty, delete_faculty,
    add_course, get_courses,
    update_course, delete_course,
    add_enrollment, get_enrollments,
    delete_enrollment
)


# =====================================
# 1. STUDENT TESTING
# =====================================

print("\n========== STUDENT TESTING ==========")

add_student(
    9901, "Test Student", 20,
    "teststudent9901@gmail.com", "Computer Science"
)

print("\nAll Students:")

for student in get_students():
    print(student.student_id, student.name,
          student.email, student.department)

print("\nTesting get_You():")
print("Total students:", len(get_You()))

update_student(9901, department="Information Technology")

print("\nAfter Student Update:")

for student in get_students():
    if student.student_id == 9901:
        print(student.name, student.department)


# =====================================
# 2. FACULTY TESTING
# =====================================

print("\n========== FACULTY TESTING ==========")

add_faculty(
    9901, "Test Faculty", 35,
    "testfaculty9901@gmail.com", "Computer Science"
)

print("\nAll Faculty:")

for faculty in get_faculty():
    print(faculty.faculty_id, faculty.name,
          faculty.email, faculty.department)

update_faculty(9901, department="Information Technology")

print("\nAfter Faculty Update:")

for faculty in get_faculty():
    if faculty.faculty_id == 9901:
        print(faculty.name, faculty.department)


# =====================================
# 3. COURSE TESTING
# =====================================

print("\n========== COURSE TESTING ==========")

add_course("TEST9901", "Python Programming", 4)

print("\nAll Courses:")

for course in get_courses():
    print(course.course_code, course.course_name,
          course.credits)

update_course("TEST9901", credits=5)

print("\nAfter Course Update:")

for course in get_courses():
    if course.course_code == "TEST9901":
        print(course.course_name, course.credits)


# =====================================
# 4. ENROLLMENT TESTING
# =====================================

print("\n========== ENROLLMENT TESTING ==========")

add_enrollment(9901, "TEST9901")

print("\nAll Enrollments:")

for enrollment in get_enrollments():
    print(enrollment.enrollment_id,
          enrollment.student_id,
          enrollment.course_code)


# =====================================
# 5. DELETE TESTING
# =====================================

print("\n========== DELETE TESTING ==========")

# Delete enrollment first
enrollments = get_enrollments()

for enrollment in enrollments:
    if enrollment.student_id == 9901:
        delete_enrollment(enrollment.enrollment_id)

# Delete student
delete_student(9901)

# Delete faculty
delete_faculty(9901)

# Delete course
delete_course("TEST9901")


# =====================================
# 6. FINAL VERIFICATION
# =====================================

print("\n========== FINAL VERIFICATION ==========")

print("Student exists:",
      any(s.student_id == 9901 for s in get_students()))

print("Faculty exists:",
      any(f.faculty_id == 9901 for f in get_faculty()))

print("Course exists:",
      any(c.course_code == "TEST9901" for c in get_courses()))

print("Enrollment exists:",
      any(e.student_id == 9901 for e in get_enrollments()))

print("\nAll Repository Tests Completed!")
