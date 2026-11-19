
def id_generator(prefix):
    count = 0

    def generate_id():
        nonlocal count
        count += 1
        return f"{prefix}{count:03d}"

    return generate_id


def student_report(students):
    for student in students:
        yield student


def faculty_report(faculties):
    for faculty in faculties:
        yield faculty


def course_report(courses):
    for course in courses:
        yield course


class StudentIterator:
    def __init__(self, students):
        self.students = students
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration

        student = self.students[self.index]
        self.index += 1
        return student


# Testing code runs only when this file is executed directly
if __name__ == "__main__":

    # Student ID generator
    student_id = id_generator("ST")

    # Faculty ID generator
    faculty_id = id_generator("FC")

    # Course ID generator
    course_id = id_generator("CS")

    print("Student IDs:")
    print(student_id())
    print(student_id())
    print(student_id())

    print("\nFaculty IDs:")
    print(faculty_id())
    print(faculty_id())

    print("\nCourse IDs:")
    print(course_id())
    print(course_id())

    # Test report generators
    students = [
        {"student_id": 101, "name": "Gladson"},
        {"student_id": 102, "name": "Rahul"}
    ]

    faculties = [
        {"faculty_id": 201, "name": "Amit"}
    ]

    courses = [
        {"course_code": "CS001", "course_name": "Python"},
        {"course_code": "CS002", "course_name": "Database"}
    ]

    print("\nStudent Report:")
    for student in student_report(students):
        print(student)

    print("\nFaculty Report:")
    for faculty in faculty_report(faculties):
        print(faculty)

    print("\nCourse Report:")
    for course in course_report(courses):
        print(course)

    # Test StudentIterator
    print("\nTesting StudentIterator:")
    iterator = StudentIterator(["Gladson", "Rahul", "Priya"])

    for student in iterator:
        print(student)
