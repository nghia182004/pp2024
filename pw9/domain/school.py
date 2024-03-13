import tkinter as tk
from tkinter import simpledialog, messagebox
import threading
import os
import gzip
import pickle
from domain.student import Student
from domain.course import Course

class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.save_thread = None

        self.check_and_load_data()  

    def input_students(self, n):
        existing_ids = [student.id for student in self.students]
        for i in range(n):
            self.students.append(Student(i+1, existing_ids))
            existing_ids.append(self.students[-1].id)
        self.write_students_data()

    def input_courses(self, m):
        existing_ids = [course.id for course in self.courses]
        for i in range(m):
            self.courses.append(Course(i+1, existing_ids))
            existing_ids.append(self.courses[-1].id)
        self.write_courses_data()

    def input_mark(self):
        select_course = simpledialog.askstring("Input", "Select a course id:")
        for course in self.courses:
            if course.id == select_course:
                for student in self.students:
                    mark = simpledialog.askfloat("Input", f"Enter the mark for student: {student.name} - {student.id}:")
                    student.marks[course.id] = round(float(mark), 1)
                self.write_marks_data()
                return
        messagebox.showerror("Error", "Course not found")

    def list_courses(self):
        if not self.courses:
            messagebox.showinfo("Information", "No courses available.")
        else:
            course_info = "\nList of Courses:\n"
            for course in self.courses:
                course_info += f"Course ID: {course.id} - Course Name: {course.name}\n"
            messagebox.showinfo("Courses", course_info)

    def list_students(self):
        if not self.students:
            messagebox.showinfo("Information", "No students available.")
        else:
            student_info = "\nList of Students:\n"
            for student in self.students:
                student_info += f"Student ID: {student.id} - Name: {student.name} - DOB: {student.dob}\n"
            messagebox.showinfo("Students", student_info)

    def list_marks(self):
        select_course = simpledialog.askstring("Input", "Enter a course ID to display marks:")
        course_found = False
        for course in self.courses:
            if course.id == select_course:
                course_found = True
                marks_info = f"Marks for Course ID: {course.id} - {course.name}\n"
                for student in self.students:
                    mark = student.marks.get(course.id, 'No mark yet')
                    marks_info += f"Student ID: {student.id} - Name: {student.name} - Mark: {mark}\n"
                messagebox.showinfo("Marks", marks_info)
                break
        if not course_found:
            messagebox.showerror("Error", "Course not found")

    def sort_students_by_gpa(self):
        for student in self.students:
            student.calculate_gpa()
        self.students.sort(key=lambda x: x.gpa, reverse=True)
        sorted_info = "\nStudents sorted by GPA (Descending):\n"
        for student in self.students:
            sorted_info += f"Student ID: {student.id} - Name: {student.name} - GPA: {student.gpa:.1f}\n"
        messagebox.showinfo("Sorted Students", sorted_info)

    def write_students_data(self):
        if not self.save_thread or not self.save_thread.is_alive():
            self.save_thread = threading.Thread(target=self._write_students_data_thread)
            self.save_thread.start()

    def _write_students_data_thread(self):
        with gzip.open('students.pkl', 'wb') as f:
            pickle.dump(self.students, f)

    def write_courses_data(self):
        if not self.save_thread or not self.save_thread.is_alive():
            self.save_thread = threading.Thread(target=self._write_courses_data_thread)
            self.save_thread.start()

    def _write_courses_data_thread(self):
        with gzip.open('courses.pkl', 'wb') as f:
            pickle.dump(self.courses, f)

    def write_marks_data(self):
        if not self.save_thread or not self.save_thread.is_alive():
            self.save_thread = threading.Thread(target=self._write_marks_data_thread)
            self.save_thread.start()

    def _write_marks_data_thread(self):
        with gzip.open('marks.pkl', 'wb') as f:
            pickle.dump(self.students, f)

    def compress_data(self):
        compression_method = simpledialog.askstring("Input", "Select a compression method (gzip):")
        if compression_method and compression_method.lower() == 'gzip':
            with gzip.open('school_data.pkl.gz', 'wb') as f:
                pickle.dump((self.students, self.courses), f)
        else:
            messagebox.showerror("Error", "Invalid compression method. Data not compressed.")
        messagebox.showinfo("Information", "Data compressed successfully.")

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
