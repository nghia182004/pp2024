import tkinter as tk
from tkinter import simpledialog

class Student:
    def __init__(self, student_number, existing_ids):
        self.id = self.prompt_for_unique_id(student_number, existing_ids)
        self.name = self.prompt_for_input(f"Enter student {student_number} name: ")
        self.dob = self.prompt_for_input(f"Enter student {student_number} date of birth: ")
        self.marks = {}
        self.gpa = 0 

    def prompt_for_unique_id(self, student_number, existing_ids):
        root = tk.Tk()
        root.withdraw() 

        id = simpledialog.askstring("Input", f"Enter student {student_number} ID: ")
        while id in existing_ids:
            id = simpledialog.askstring("Input", "This ID is already taken. Please enter a different ID:")
        root.destroy() 
        return id

    def prompt_for_input(self, prompt):
        root = tk.Tk()
        root.withdraw() 

        input_str = simpledialog.askstring("Input", prompt)
        root.destroy() 
        return input_str

    def calculate_gpa(self):
        grades = [self.convert_mark_to_grade(mark) for mark in self.marks.values()]
        self.gpa = sum(grades) / len(grades) if grades else 0

    @staticmethod
    def convert_mark_to_grade(mark):
        return (float(mark) / 20) * 4


