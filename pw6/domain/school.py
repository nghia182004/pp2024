import pickle
import gzip
import os
import curses
from domain.student import Student
from domain.course import Course
from output import clear_screen, wait_for_keypress
from input import prompt_user_for_input


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
                    student.marks[course.id] = round(float(mark), 1)
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
        with gzip.open('students.pkl', 'wb') as f:
            pickle.dump(self.students, f)

    def write_courses_data(self):
        with gzip.open('courses.pkl', 'wb') as f:
            pickle.dump(self.courses, f)

    def write_marks_data(self):
        with gzip.open('marks.pkl', 'wb') as f:
            pickle.dump(self.students, f)

    def compress_data(self):
        compression_method = prompt_user_for_input(self.win, "Select a compression method (gzip): ")
        if compression_method.lower() == 'gzip':
            with gzip.open('school_data.pkl.gz', 'wb') as f:
                pickle.dump((self.students, self.courses), f)
        else:
            self.win.addstr("Invalid compression method. Data not compressed.\n")
        clear_screen(self.win)
        self.win.addstr("Data compressed successfully.\n")
        self.win.refresh()
        wait_for_keypress(self.win)

    def check_and_load_data(self):
        if os.path.exists('school_data.pkl.gz'):
            self.decompress_data()
            self.read_students_data()
            self.read_courses_data()

    def decompress_data(self):
        with gzip.open('school_data.pkl.gz', 'rb') as f:
            self.students, self.courses = pickle.load(f)

    def read_students_data(self):
        self.students = []
        with gzip.open('students.pkl', 'rb') as f:
            self.students = pickle.load(f)

    def read_courses_data(self):
        self.courses = []
        with gzip.open('courses.pkl', 'rb') as f:
            self.courses = pickle.load(f)

    def read_marks_data(self):
        with gzip.open('marks.pkl', 'rb') as f:
            self.students = pickle.load(f)





