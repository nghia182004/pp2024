import tkinter as tk
from tkinter import simpledialog

def prompt_user_for_input(prompt):
    root = tk.Tk()
    root.withdraw() 

    input_str = simpledialog.askstring("Input", prompt)
    root.destroy() 
    return input_str

def menu(menu_items):
    root = tk.Tk()
    root.title("Menu")

    selected_option = None

    def select_option(option):
        nonlocal selected_option
        selected_option = option
        root.quit()

    for i, item in enumerate(menu_items, 1):
        button = tk.Button(root, text=f"{i}. {item}", command=lambda item=item: select_option(item))
        button.pack()

    root.mainloop()
    return selected_option


