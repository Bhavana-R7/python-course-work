# main.py
from data import CoursePlatform

def menu():
    platform = CoursePlatform("Online Course Hub")

    while True:
        print("\n--- ONLINE COURSE MANAGEMENT ---")
        print("1. Register Student")
        print("2. Register Instructor")
        print("3. Create Course")
        print("4. Enroll Student in Course")
        print("5. Assign Instructor to Course")
        print("6. Display Student Info")
        print("7. Display Instructor Info")
        print("8. Display Course Info")
        print("9. Display Platform Report")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            platform.register_student(name, email)
            print("Student registered successfully!")

        elif choice == "2":
            name = input("Enter instructor name: ")
            email = input("Enter instructor email: ")
            platform.register_instructor(name, email)
            print("Instructor registered successfully!")

        elif choice == "3":
            title = input("Enter course title: ")
            fee = float(input("Enter course fee: "))
            platform.create_course(title, fee)
            print("Course created successfully!")

        elif choice == "4":
            if not platform.students or not platform.courses:
                print("Students or courses missing!")
                continue
            for i, s in enumerate(platform.students, 1):
                print(f"{i}. {s._name}")
            student_idx = int(input("Choose student: ")) - 1

            for i, c in enumerate(platform.courses, 1):
                print(f"{i}. {c.title}")
            course_idx = int(input("Choose course: ")) - 1

            platform.enroll_student_in_course(platform.students[student_idx], platform.courses[course_idx])
            print("Student enrolled successfully!")

        elif choice == "5":
            if not platform.instructors or not platform.courses:
                print("Instructors or courses missing!")
                continue
            for i, ins in enumerate(platform.instructors, 1):
                print(f"{i}. {ins._name}")
            instr_idx = int(input("Choose instructor: ")) - 1

            for i, c in enumerate(platform.courses, 1):
                print(f"{i}. {c.title}")
            course_idx = int(input("Choose course: ")) - 1

            platform.assign_instructor_to_course(platform.instructors[instr_idx], platform.courses[course_idx])
            print("Instructor assigned successfully!")

        elif choice == "6":
            for s in platform.students:
                s.display_info()

        elif choice == "7":
            for ins in platform.instructors:
                ins.display_info()

        elif choice == "8":
            for c in platform.courses:
                c.display_info()

        elif choice == "9":
            platform.display_report()

        elif choice == "0":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    menu()