import curses
import math
import numpy as np


def prompt_user_for_input(win, prompt):
    win.addstr(prompt)
    win.refresh()
    curses.echo()
    input_str = win.getstr().decode()
    curses.noecho()
    return input_str


def menu(win, menu_items):
    win.clear()
    win.addstr("Please select an option:\n")
    for i, item in enumerate(menu_items, 1):
        win.addstr(f"{i}. {item}\n")
    win.refresh()
    option = prompt_user_for_input(win, "Enter the number of your choice: ")
    return int(option)

class Student:
    def __init__(self, student_number, existing_ids, win):
        while True:
            id = prompt_user_for_input(win, f"Enter student {student_number} ID: ")
            if id not in existing_ids:
                self.id = id
                break
            else:
                win.addstr("This ID is already taken. Please enter a different ID.\n")
        self.name = prompt_user_for_input(win, f"Enter student {student_number} name: ")
        self.dob = prompt_user_for_input(win, f"Enter student {student_number} date of birth: ")
        self.marks = {}
        self.gpa = 0 

    def calculate_gpa(self):
      
        grades = [self.convert_mark_to_grade(mark) for mark in self.marks.values()]
        self.gpa = np.mean(grades) if grades else 0

    @staticmethod
    def convert_mark_to_grade(mark):

        return (float(mark) / 20) * 4

class Course:
    def __init__(self, course_number, existing_ids, win):
        while True:
            id = prompt_user_for_input(win, f"Enter course {course_number} ID: ")
            if id not in existing_ids:
                self.id = id
                break
            else:
                win.addstr("This ID is already taken. Please enter a different ID.\n")
        self.name = prompt_user_for_input(win, f"Enter course {course_number} name: ")

class School:
    def __init__(self, win):
        self.win = win
        self.students = []
        self.courses = []

    def input_students(self, n):
        existing_ids = [student.id for student in self.students]
        for i in range(n):
            self.students.append(Student(i+1, existing_ids, self.win))
            existing_ids.append(self.students[-1].id)

    def input_courses(self, m):
        existing_ids = [course.id for course in self.courses]
        for i in range(m):
            self.courses.append(Course(i+1, existing_ids, self.win))
            existing_ids.append(self.courses[-1].id)

    def input_mark(self):
        select_course = prompt_user_for_input(self.win, "Select a course id: ")
        for course in self.courses:
            if course.id == select_course:
                for student in self.students:
                    mark = prompt_user_for_input(self.win, f"Enter the mark for student: {student.name} - {student.id} : ")
                    
                    student.marks[course.id] = math.floor(float(mark) * 10) / 10
                return
        self.win.addstr("Course not found\n")

    def list_courses(self):
        self.win.clear()
        if not self.courses:
            self.win.addstr("No courses available.\n")
        else:
            self.win.addstr("\nList of Courses:\n")
            for course in self.courses:
                self.win.addstr(f"Course ID: {course.id} - Course Name: {course.name}\n")
        self.win.refresh()
        self.win.getch()  

    def list_students(self):
        self.win.clear()
        if not self.students:
            self.win.addstr("No students available.\n")
        else:
            self.win.addstr("\nList of Students:\n")
            for student in self.students:
                self.win.addstr(f"Student ID: {student.id} - Name: {student.name} - DOB: {student.dob}\n")
        self.win.refresh()
        self.win.getch() 

    def list_marks(self):
        self.win.clear()
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
        self.win.getch() 

    def sort_students_by_gpa(self):
        self.win.clear()
        
        for student in self.students:
            student.calculate_gpa()

        self.students.sort(key=lambda x: x.gpa, reverse=True)

        self.win.addstr("\nStudents sorted by GPA (Descending):\n")
        for student in self.students:
            self.win.addstr(f"Student ID: {student.id} - Name: {student.name} - GPA: {student.gpa:.1f}\n")
        self.win.refresh()
        self.win.getch()  
def main(stdscr):
   
    curses.curs_set(0)  
    stdscr.clear()  
    stdscr.refresh()

    
    height, width = stdscr.getmaxyx()
    win = curses.newwin(height, width, 0, 0)

    school = School(win)
    n = 0
    m = 0

   
    menu_items = [
        "Input number of students",
        "Input student information",
        "Input number of courses",
        "Input course information",
        "Input marks for a course",
        "List courses",
        "List students",
        "Show student marks for a course",
        "Sort students by GPA",
        "Exit"
    ]

    while True:
        choice = menu(win, menu_items)
        if choice == 1:
            n = int(prompt_user_for_input(win, "Enter the number of students: "))
        elif choice == 2:
            school.input_students(n)
        elif choice == 3:
            m = int(prompt_user_for_input(win, "Enter the number of courses: "))
        elif choice == 4:
            school.input_courses(m)
        elif choice == 5:
            school.input_mark()
        elif choice == 6:
            school.list_courses()
        elif choice == 7:
            school.list_students()
        elif choice == 8:
            school.list_marks()
        elif choice == 9:
            school.sort_students_by_gpa()
        elif choice == 10:
            break

   
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()


curses.wrapper(main)

