
from app.database.repository import DatabaseRepository
from app.database.models import StudentDB


# Create Student Repository
student_repo = DatabaseRepository(StudentDB)

# Add Student
student = StudentDB(
    student_id=999,
    name="Gladson",
    age=20,
    email="gladson@test.com",
    department="Computer Science"
)

student_repo.add(student)

# Display All Students
print("\n===== ALL STUDENTS =====")

students = student_repo.get_all()

for s in students:
    print(s.student_id, s.name, s.email, s.department)

# Search Student
print("\n===== SEARCH STUDENT =====")

result = student_repo.get_by_id(999, "student_id")

if result:
    print(result.name)

# Update Student
print("\n===== UPDATE STUDENT =====")

student_repo.update(
    999,
    "student_id",
    {"department": "Information Technology"}
)

# Delete Student
print("\n===== DELETE STUDENT =====")

student_repo.delete(999, "student_id")

# Close Database
student_repo.close()

print("\nDatabase testing completed!")
