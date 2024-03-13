import tkinter as tk
from tkinter import simpledialog

class Course:
    def __init__(self, course_number, existing_ids):
        self.id = self.prompt_for_unique_id(course_number, existing_ids)
        self.name = self.prompt_for_input(f"Enter course {course_number} name: ")

    def prompt_for_unique_id(self, course_number, existing_ids):
        root = tk.Tk()
        root.withdraw()  

        id = simpledialog.askstring("Input", f"Enter course {course_number} ID: ")
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

