import curses

def clear_screen(win):
    win.clear()
    win.refresh()

def wait_for_keypress(win):
    win.getch()

