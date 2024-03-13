import curses

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
