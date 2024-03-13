import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from domain.school import School

def main():
    global n, m 
    root = tk.Tk()
    root.title("School Management System")
    n = 0
    m = 0
    school = School()

    def input_students():
        global n  
        n = simpledialog.askinteger("Input", "Enter the number of students:")
        
    def input_student_info():
        if n is not None:
            school.input_students(n)
    
    def input_courses():
        global m  
        m = simpledialog.askinteger("Input", "Enter the number of courses:")
        
    def input_course_info():
        if m is not None:
            school.input_courses(m)

    def input_marks():
        school.input_mark()

    def list_courses():
        school.list_courses()

    def list_students():
        school.list_students()

    def show_student_marks():
        school.list_marks()

    def sort_students_by_gpa():
        school.sort_students_by_gpa()

    def compress_data():
        school.compress_data()
        root.quit()

    menu_items = [
        ("Input number of students", input_students),
        ("Input student information", input_student_info),
        ("Input number of courses", input_courses),
        ("Input course information", input_course_info),
        ("Input marks for a course", input_marks),
        ("List courses", list_courses),
        ("List students", list_students),
        ("Show student marks for a course", show_student_marks),
        ("Sort students by GPA", sort_students_by_gpa),
        ("Exit", compress_data)
    ]

    menu_frame = tk.Frame(root)
    menu_frame.pack()

    for item, command in menu_items:
        button = tk.Button(menu_frame, text=item, command=command)
        button.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)

    root.mainloop()

if __name__ == "__main__":
    main()
