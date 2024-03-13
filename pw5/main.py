import curses
from input import menu
from input import prompt_user_for_input
from output import clear_screen, wait_for_keypress
from domain.school import School

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
            school.compress_data()
            break
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

curses.wrapper(main)