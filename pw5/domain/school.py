from domain.student import Student
from domain.course import Course
from output import clear_screen, wait_for_keypress
from input import prompt_user_for_input
import math
import os

class School:
    def __init__(self, win):
        self.win = win
        self.students = []
        self.courses = []

        self.check_and_load_data()

    def input_students(self, n):
        existing_ids = [student.id for student in self.students]
        for i in range(n):
            self.students.append(Student(i+1, existing_ids, self.win))
            existing_ids.append(self.students[-1].id)
        self.write_students_data()

    def input_courses(self, m):
        existing_ids = [course.id for course in self.courses]
        for i in range(m):
            self.courses.append(Course(i+1, existing_ids, self.win))
            existing_ids.append(self.courses[-1].id)
        self.write_courses_data()

    def input_mark(self):
        select_course = prompt_user_for_input(self.win, "Select a course id: ")
        for course in self.courses:
            if course.id == select_course:
                for student in self.students:
                    mark = prompt_user_for_input(self.win, f"Enter the mark for student: {student.name} - {student.id} : ")
                    student.marks[course.id] = math.floor(float(mark) * 10) / 10
                self.write_marks_data()
                return
        self.win.addstr("Course not found\n")

    def list_courses(self):
        clear_screen(self.win)
        if not self.courses:
            self.win.addstr("No courses available.\n")
        else:
            self.win.addstr("\nList of Courses:\n")
            for course in self.courses:
                self.win.addstr(f"Course ID: {course.id} - Course Name: {course.name}\n")
        self.win.refresh()
        wait_for_keypress(self.win)

    def list_students(self):
        clear_screen(self.win)
        if not self.students:
            self.win.addstr("No students available.\n")
        else:
            self.win.addstr("\nList of Students:\n")
            for student in self.students:
                self.win.addstr(f"Student ID: {student.id} - Name: {student.name} - DOB: {student.dob}\n")
        self.win.refresh()
        wait_for_keypress(self.win) 

    def list_marks(self):
        clear_screen(self.win)
        select_course = prompt_user_for_input(self.win, "Enter a course ID to display marks: ")
        course_found = False
        for course in self.courses:
            if course.id == select_course:
                course_found = True
                self.win.addstr(f"Marks for Course ID: {course.id} - {course.name}\n")
                for student in self.students:
                    mark = student.marks.get(course.id, 'No mark yet')
                    self.win.addstr(f"Student ID: {student.id} - Name: {student.name} - Mark: {mark}\n")
                break
        if not course_found:
            self.win.addstr("Course not found.\n")
        self.win.refresh()
        wait_for_keypress(self.win)  

    def sort_students_by_gpa(self):
        clear_screen(self.win)
        for student in self.students:
            student.calculate_gpa()
        self.students.sort(key=lambda x: x.gpa, reverse=True)
        self.win.addstr("\nStudents sorted by GPA (Descending):\n")
        for student in self.students:
            self.win.addstr(f"Student ID: {student.id} - Name: {student.name} - GPA: {student.gpa:.1f}\n")
        self.win.refresh()
        wait_for_keypress(self.win)

    def write_students_data(self):
        with open('students.txt', 'w') as f:
            for student in self.students:
                f.write(f"{student.id},{student.name},{student.dob}\n")

    def write_courses_data(self):
        with open('courses.txt', 'w') as f:
            for course in self.courses:
                f.write(f"{course.id},{course.name}\n")

    def write_marks_data(self):
        with open('marks.txt', 'w') as f:
            for student in self.students:
                for course_id, mark in student.marks.items():
                    f.write(f"{student.id},{course_id},{mark}\n")

    def compress_data(self):
        compression_method = prompt_user_for_input(self.win, "Select a compression method (zip/tar): ")
        if compression_method.lower() == 'zip':
            import zipfile
            with zipfile.ZipFile('students.dat', 'w') as zipf:
                zipf.write('students.txt')
                zipf.write('courses.txt')
                zipf.write('marks.txt')
        elif compression_method.lower() == 'tar':
            import tarfile
            with tarfile.open('students.tar.gz', 'w:gz') as tarf:
                tarf.add('students.txt')
                tarf.add('courses.txt')
                tarf.add('marks.txt')
        else:
            self.win.addstr("Invalid compression method. Data not compressed.\n")
        clear_screen(self.win)
        self.win.addstr("Data compressed successfully.\n")
        self.win.refresh()
        wait_for_keypress(self.win)

    def check_and_load_data(self):
        if os.path.exists('students.dat'):
            self.decompress_data()
            self.read_students_data()
            self.read_courses_data()
            self.read_marks_data()

    def decompress_data(self):
        import zipfile
        with zipfile.ZipFile('students.dat', 'r') as zipf:
            zipf.extractall()

    def read_students_data(self):
        self.students = []
        with open('students.txt', 'r') as f:
            for line in f:
                student_data = line.strip().split(',')
                self.students.append(Student(student_data[0], [], None))
                self.students[-1].name = student_data[1]
                self.students[-1].dob = student_data[2]

    def read_courses_data(self):
        self.courses = []
        with open('courses.txt', 'r') as f:
            for line in f:
                course_data = line.strip().split(',')
                self.courses.append(Course(course_data[0], [], None))
                self.courses[-1].name = course_data[1]

    def read_marks_data(self):
        with open('marks.txt', 'r') as f:
            for line in f:
                mark_data = line.strip().split(',')
                for student in self.students:
                    if student.id == mark_data[0]:
                        student.marks[mark_data[1]] = float(mark_data[2])

