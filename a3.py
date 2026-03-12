import tkinter as tk
import random

GRID_SIZE = 4
CELL_SIZE = 100
PADDING = 10

BG_COLOR = "#bbada0"
EMPTY_COLOR = "#cdc1b4"

TILE_COLORS = {
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e",
}

class Game2048:
    def __init__(self, root):
        self.root = root
        self.root.title("2048")

        self.board = [[0]*GRID_SIZE for _ in range(GRID_SIZE)]

        self.frame = tk.Frame(root, bg=BG_COLOR)
        self.frame.pack()

        self.cells = []
        for r in range(GRID_SIZE):
            row = []
            for c in range(GRID_SIZE):
                cell = tk.Frame(
                    self.frame,
                    bg=EMPTY_COLOR,
                    width=CELL_SIZE,
                    height=CELL_SIZE
                )
                cell.grid(row=r, column=c, padx=PADDING, pady=PADDING)
                label = tk.Label(self.frame, text="", font=("Helvetica", 24, "bold"),
                                 width=4, height=2, bg=EMPTY_COLOR)
                label.grid(row=r, column=c)
                row.append(label)
            self.cells.append(row)

        self.root.bind("<Key>", self.handle_key)

        self.spawn_tile()
        self.spawn_tile()
        self.update_ui()

    def spawn_tile(self):
        empty = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if self.board[r][c] == 0]
        if empty:
            r, c = random.choice(empty)
            self.board[r][c] = 2 if random.random() < 0.9 else 4

    def update_ui(self):
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                value = self.board[r][c]
                label = self.cells[r][c]
                if value == 0:
                    label.config(text="", bg=EMPTY_COLOR)
                else:
                    label.config(
                        text=str(value),
                        bg=TILE_COLORS.get(value, "#3c3a32"),
                        fg="#776e65" if value <= 4 else "white"
                    )

    def compress(self, row):
        new_row = [i for i in row if i != 0]
        new_row += [0] * (GRID_SIZE - len(new_row))
        return new_row

    def merge(self, row):
        for i in range(GRID_SIZE-1):
            if row[i] == row[i+1] and row[i] != 0:
                row[i] *= 2
                row[i+1] = 0
        return row

    def move_left(self):
        new_board = []
        for row in self.board:
            row = self.compress(row)
            row = self.merge(row)
            row = self.compress(row)
            new_board.append(row)
        self.board = new_board

    def move_right(self):
        self.board = [row[::-1] for row in self.board]
        self.move_left()
        self.board = [row[::-1] for row in self.board]

    def transpose(self):
        self.board = [list(row) for row in zip(*self.board)]

    def move_up(self):
        self.transpose()
        self.move_left()
        self.transpose()

    def move_down(self):
        self.transpose()
        self.move_right()
        self.transpose()

    def handle_key(self, event):
        key = event.keysym

        if key == "Left":
            self.move_left()
        elif key == "Right":
            self.move_right()
        elif key == "Up":
            self.move_up()
        elif key == "Down":
            self.move_down()
        else:
            return

        self.spawn_tile()
        self.update_ui()

root = tk.Tk()
game = Game2048(root)
root.mainloop()