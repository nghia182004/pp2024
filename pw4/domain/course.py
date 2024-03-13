from input import prompt_user_for_input

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

