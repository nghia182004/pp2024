class Student:
    def __init__(self, student_number, existing_ids):
        while True:
            id = input(f"Enter student {student_number} ID: ")
            if id not in existing_ids:
                self.id = id
                break
            else:
                print("This ID is already taken. Please enter a different ID.")
        self.name = input(f"Enter student {student_number} name: ")
        self.dob = input(f"Enter student {student_number} date of birth: ")
        self.marks = {}

class Course:
    def __init__(self, course_number, existing_ids):
        while True:
            id = input(f"Enter course {course_number} ID: ")
            if id not in existing_ids:
                self.id = id
                break
            else:
                print("This ID is already taken. Please enter a different ID.")
        self.name = input(f"Enter course {course_number} name: ")

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self, n):
        existing_ids = [student.id for student in self.students]
        for i in range(n):
            self.students.append(Student(i+1, existing_ids))
            existing_ids.append(self.students[-1].id)
    
    def input_courses(self, m):
        existing_ids = [course.id for course in self.courses]
        for i in range(m):
            self.courses.append(Course(i+1, existing_ids))
            existing_ids.append(self.courses[-1].id)
    
    def input_mark(self):
        select_course = input("Select a course id: ")
        for course in self.courses:
            if course.id == select_course:
                for student in self.students:
                    mark = input(f"Enter the mark for student: {student.name} - {student.id} : ")
                    student.marks[course.id] = mark
                return
        print("Course not found")
    
    def list_courses(self):
        print("\nList of Courses:")
        for course in self.courses:
            print(f"course id: {course.id} - course name: {course.name}")  

    def list_students(self, n):
        print("\nList of students:")
        if n>0:
         for student in self.students:
             print(f"id: {student.id} - student name: {student.name} - student dob: {student.dob}")
         return
        print("no student found")
    
    def list_marks(self):
        select_course = input("Enter a course to display: ")
        for course in self.courses:
            if course.id == select_course:
                for student in self.students:
                    print(f"id: {student.id} - student name: {student.name} - student mark: {student.marks.get(course.id, 'No mark yet')}")
                return
        print("Course not found")

def main():
    school = School()
    n = 0
    m = 0

    while True:
        print("\nOptions:")
        print("1. Input number of students")
        print("2. Input student information")
        print("3. Input number of courses")
        print("4. Input course information")
        print("5. Input marks for a course")
        print("6. List courses")
        print("7. List students")
        print("8. Show student marks for a course")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            n = int(input("Enter the number of students: "))
            
        elif choice == '2':
            school.input_students(n)
        elif choice == '3':
            m = int(input("Enter the number of courses: "))
            
        elif choice == '4':
            school.input_courses(m)
        elif choice == '5':
            school.input_mark()
        elif choice == '6':
            school.list_courses()
        elif choice == '7':
            school.list_students(n)
        elif choice == '8':
            school.list_marks()
        elif choice == '9':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()