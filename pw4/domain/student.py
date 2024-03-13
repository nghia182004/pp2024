from input import prompt_user_for_input
import numpy as np
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

