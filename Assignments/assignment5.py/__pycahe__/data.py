#data.py
# data.py
from abc import ABC, abstractmethod

# ---------- Base Class ----------
class Person(ABC):
    def __init__(self, name, email):
        self._name = name   # encapsulated attributes
        self._email = email

    @abstractmethod
    def display_info(self):
        pass


# ---------- Subclasses ----------
class Student(Person):
    student_count = 0

    def __init__(self, name, email):
        super().__init__(name, email)
        self.courses = []
        Student.student_count += 1

    def enroll(self, course):
        self.courses.append(course)

    def display_info(self):
        print(f"Student: {self._name}, Email: {self._email}")
        print("Enrolled Courses:", [c.title for c in self.courses] or "None")


class Instructor(Person):
    instructor_count = 0

    def __init__(self, name, email):
        super().__init__(name, email)
        self.courses = []
        Instructor.instructor_count += 1

    def assign_course(self, course):
        self.courses.append(course)

    def display_info(self):
        print(f"Instructor: {self._name}, Email: {self._email}")
        print("Teaching Courses:", [c.title for c in self.courses] or "None")


# ---------- Supporting Class ----------
class Course:
    course_count = 0

    def __init__(self, title, fee):
        self.title = title
        self.fee = fee
        self.students = []
        self.instructor = None
        Course.course_count += 1

    def add_student(self, student):
        self.students.append(student)

    def assign_instructor(self, instructor):
        self.instructor = instructor

    def display_info(self):
        print(f"Course: {self.title}, Fee: {self.fee}")
        print(f"Instructor: {self.instructor._name if self.instructor else 'None'}")
        print("Students:", [s._name for s in self.students] or "None")


# ---------- Controller / Manager Class ----------
class CoursePlatform:
    revenue = 0

    def __init__(self, name):
        self.name = name
        self.students = []
        self.instructors = []
        self.courses = []

    def register_student(self, name, email):
        student = Student(name, email)
        self.students.append(student)
        return student

    def register_instructor(self, name, email):
        instructor = Instructor(name, email)
        self.instructors.append(instructor)
        return instructor

    def create_course(self, title, fee):
        course = Course(title, fee)
        self.courses.append(course)
        return course

    def enroll_student_in_course(self, student, course):
        student.enroll(course)
        course.add_student(student)
        CoursePlatform.revenue += course.fee

    def assign_instructor_to_course(self, instructor, course):
        instructor.assign_course(course)
        course.assign_instructor(instructor)

    def display_report(self):
        print(f"--- {self.name} Report ---")
        print(f"Total Students: {len(self.students)}")
        print(f"Total Instructors: {len(self.instructors)}")
        print(f"Total Courses: {len(self.courses)}")
        print(f"Total Revenue: {CoursePlatform.revenue}")