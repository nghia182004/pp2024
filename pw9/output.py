import tkinter as tk

def clear_screen():
    root = tk.Tk()
    root.withdraw() 
    root.destroy()  

def wait_for_keypress():
    root = tk.Tk()
    root.withdraw() 


    label = tk.Label(root, text="Press any key to continue...")
    label.pack()


    root.bind("<KeyPress>", lambda event: root.quit())

    root.mainloop()
