from tkinter import *
from tkinter import ttk

class Sketchpad(Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.color = "black"
        self.brush_size = 3

        self.bind("<Button-1>", self.save_posn)
        self.bind("<B1-Motion>", self.add_line)

    def save_posn(self, event):
        self.lastx, self.lasty = event.x, event.y

    def add_line(self, event):
        self.create_line(
            self.lastx, self.lasty, event.x, event.y,
            fill=self.color,
            width=self.brush_size,
            capstyle=ROUND,
            smooth=True
        )
        self.save_posn(event)

    def clear(self):
        self.delete("all")

    def set_color(self, new_color):
        self.color = new_color

    def set_brush_size(self, value):
        self.brush_size = int(value)


root = Tk()
root.title("Sketchpad")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = ttk.Frame(root)
frame.grid(column=0, row=0, sticky=(N, W, E, S))

frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

sketch = Sketchpad(frame, bg="white")
sketch.grid(row=0, column=0, columnspan=10, sticky=(N, W, E, S))

# 10 color buttons
colors = [
    "black", "red", "blue", "green", "yellow",
    "orange", "purple", "pink", "brown", "gray"
]

for i, c in enumerate(colors):
    btn = Button(frame, bg=c, width=3,
                 command=lambda col=c: sketch.set_color(col))
    btn.grid(row=1, column=i, padx=2, pady=2)

# Brush size slider
size_label = ttk.Label(frame, text="Brush Size")
size_label.grid(row=2, column=0, columnspan=2)

size_slider = Scale(frame, from_=1, to=20,
                    orient=HORIZONTAL,
                    command=sketch.set_brush_size)
size_slider.set(3)
size_slider.grid(row=2, column=2, columnspan=6, sticky=(E, W))

# Clear button
clear_button = ttk.Button(frame, text="Clear", command=sketch.clear)
clear_button.grid(row=2, column=8, columnspan=2, pady=5)

root.mainloop()