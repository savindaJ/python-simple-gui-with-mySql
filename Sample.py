from Tk import *

window = Tk()

def close_window (root):
    root.destroy()

frame = Frame(window)
frame.pack()
button = Button (frame, text = "Good-bye.", command = close_window)
button.pack()

window.mainloop()