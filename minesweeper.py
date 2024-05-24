import tkinter as tk
import random

class Minesweeper(tk.Tk):
    def __init__(self, columns=16, rows=20, num_bombs=20):
        super().__init__()
        self.columns = columns
        self.rows = rows
        self.num_bombs = num_bombs
        self.cells = {}

        self.create_widgets()
        self.create_grid()
        self.create_bombs()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=self.columns * 30, height=self.rows * 30)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.left_click)
        self.canvas.bind("<Button-3>", self.right_click)

    def create_grid(self):
        for i in range(self.columns):
            for j in range(self.rows):
                cell_id = (i, j)
                x1, y1 = i * 30, j * 30
                x2, y2 = x1 + 30, y1 + 30
                self.cells[cell_id] = {'bomb': False, 'revealed': False, 'flagged': False}
                self.canvas.create_rectangle(x1, y1, x2, y2, fill='lightgreen', tags='cell')

    def create_bombs(self):
        bomb_positions = random.sample(list(self.cells.keys()), self.num_bombs)
        for pos in bomb_positions:
            self.cells[pos]['bomb'] = True

    def left_click(self, event):
        cell_id = (event.x // 30, event.y // 30)
        self.reveal_cell(cell_id)

    def right_click(self, event):
        cell_id = (event.x // 30, event.y // 30)
        if not self.cells[cell_id]['revealed']:
            self.cells[cell_id]['flagged'] = not self.cells[cell_id]['flagged']
            self.draw_flag(cell_id)

    def draw_flag(self, cell_id):
        x, y = cell_id
        if self.cells[cell_id]['flagged']:
            self.canvas.create_text(x * 30 + 15, y * 30 + 15, text='P', fill='blue', tags='flag')
        else:
            self.canvas.delete('flag')

    def reveal_cell(self, cell_id):
        if not self.cells[cell_id]['revealed']:
            if self.cells[cell_id]['bomb']:
                self.game_over()
            else:
                self.cells[cell_id]['revealed'] = True
                surrounding_bombs = self.count_surrounding_bombs(cell_id)
                if surrounding_bombs:
                    self.canvas.create_text(cell_id[0] * 30 + 15, cell_id[1] * 30 + 15, text=str(surrounding_bombs), tags='number')
                else:
                    self.reveal_empty_cells(cell_id)

    def count_surrounding_bombs(self, cell_id):
        x, y = cell_id
        surrounding_bombs = sum(self.cells.get((i, j), {}).get('bomb', False) for i in range(x - 1, x + 2) for j in range(y - 1, y + 2))
        return surrounding_bombs

    def reveal_empty_cells(self, cell_id):
        queue = [cell_id]
        while queue:
            current_cell = queue.pop(0)
            x, y = current_cell
            surrounding_bombs = self.count_surrounding_bombs(current_cell)
            if not surrounding_bombs:
                for i in range(x - 1, x + 2):
                    for j in range(y - 1, y + 2):
                        if (i, j) not in queue and 0 <= i < self.columns and 0 <= j < self.rows:
                            queue.append((i, j))
                            self.cells[(i, j)]['revealed'] = True
                            if not self.cells[(i, j)]['bomb']:
                                self.canvas.create_rectangle(i * 30, j * 30, (i + 1) * 30, (j + 1) * 30, fill='brown', tags='cell')
            else:
                self.canvas.create_text(x * 30 + 15, y * 30 + 15, text=str(surrounding_bombs), tags='number')

    def game_over(self):
        for cell_id, cell_info in self.cells.items():
            if cell_info['bomb']:
                x, y = cell_id
                self.canvas.create_text(x * 30 + 15, y * 30 + 15, text='*', fill='red', tags='number')
        print('Game Over')

if __name__ == "__main__":
    app = Minesweeper()
    app.mainloop()
