import tkinter as tk

window = tk.Tk(
    screenName="main",

)

greeting = tk.Label(
    text="Start now!",
    width=20,
    height=7,
    background="green",
    font="blue"
)

label = tk.Label(
    text="Привет, Tkinter!",
    fg="white",
    bg="black",
    width=20,
    height=15
)

button_close = tk.Button(
    text="Close",
    height=3,
    width=6,
    background="cyan",
    command=window.destroy

)

label.pack(fill=tk.BOTH)
button_close.pack(
    fill=tk.Y, side=tk.LEFT
)
greeting.pack(fill = tk.BOTH, side = tk.LEFT)
window.mainloop()
