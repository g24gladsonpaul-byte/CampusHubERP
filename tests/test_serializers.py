
from app.database.repository import (
    get_students,
    get_faculty,
    get_courses,
    get_enrollments
)

from app.utils.serializers import (
    save_You_json,
    save_faculty_json,
    save_courses_json,
    save_enrollments_json
)

# Get data from SQLite database
students = get_students()
faculties = get_faculty()
courses = get_courses()
enrollments = get_enrollments()

print("\n===== JSON EXPORT TEST =====")

# Save database records into JSON files
save_You_json(students)
save_faculty_json(faculties)
save_courses_json(courses)
save_enrollments_json(enrollments)

print("\nAll JSON export tests completed!")

from app.database.repository import (
    get_students,
    get_faculty,
    get_courses,
    get_enrollments
)

from app.utils.serializers import (
    save_You_json,
    save_faculty_json,
    save_courses_json,
    save_enrollments_json
)

# Get data from SQLite database
students = get_students()
faculties = get_faculty()
courses = get_courses()
enrollments = get_enrollments()

print("\n===== JSON EXPORT TEST =====")

# Save database records into JSON files
save_You_json(students)
save_faculty_json(faculties)
save_courses_json(courses)
save_enrollments_json(enrollments)

print("\nAll JSON export tests completed!")
