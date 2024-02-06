import tkinter as tk
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('320x240')
root.title('My tk_app')
root['bg'] = '#551290'
def window_position(w, h):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = w
    window_height = h
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")


window_position(300, 200)

frame = Frame(root, bg='#de663e')
frame.pack()

label = LabelFrame(frame, bd=2, bg='green', text='Hello, motherfuckers')
label.pack()
button = Button(frame, text='close', height=1, width=3, anchor='se', bg='cyan', command=root.destroy)
button.pack()




root.mainloop()