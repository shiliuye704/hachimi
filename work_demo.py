import tkinter as tk
from tkinter import messagebox


class Gobang:
    def __init__(self, root):
        self.root = root
        self.root.title("五子棋小游戏")

        self.size = 15
        self.cell = 40
        self.margin = 30

        self.canvas_size = self.margin * 2 + self.cell * (self.size - 1)

        self.canvas = tk.Canvas(
            root,
            width=self.canvas_size,
            height=self.canvas_size,
            bg="#DEB887"
        )
        self.canvas.pack()

        # 0表示空
        # 1表示黑棋
        # 2表示白棋
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]

        self.current_player = 1
        self.game_over = False

        self.draw_board()

        self.canvas.bind("<Button-1>", self.click)

        btn = tk.Button(root, text="重新开始", command=self.restart)
        btn.pack(pady=10)

    def draw_board(self):
        for i in range(self.size):
            x1 = self.margin
            y = self.margin + i * self.cell
            x2 = self.margin + (self.size - 1) * self.cell

            self.canvas.create_line(x1, y, x2, y)

        for i in range(self.size):
            x = self.margin + i * self.cell
            y1 = self.margin
            y2 = self.margin + (self.size - 1) * self.cell

            self.canvas.create_line(x, y1, x, y2)

    def click(self, event):
        if self.game_over:
            return

        col = round((event.x - self.margin) / self.cell)
        row = round((event.y - self.margin) / self.cell)

        if row < 0 or row >= self.size:
            return

        if col < 0 or col >= self.size:
            return

        if self.board[row][col] != 0:
            return

        self.board[row][col] = self.current_player

        self.draw_piece(row, col, self.current_player)

        if self.check_win(row, col):
            self.game_over = True

            if self.current_player == 1:
                winner = "黑棋"
            else:
                winner = "白棋"

            messagebox.showinfo("游戏结束", winner + "获胜！")
            return

        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

    def draw_piece(self, row, col, player):
        x = self.margin + col * self.cell
        y = self.margin + row * self.cell

        r = 15

        color = "black" if player == 1 else "white"

        self.canvas.create_oval(
            x - r,
            y - r,
            x + r,
            y + r,
            fill=color
        )

    def check_direction(self, row, col, dx, dy):
        player = self.board[row][col]

        count = 1

        r = row + dx
        c = col + dy

        while (0 <= r < self.size and
               0 <= c < self.size and
               self.board[r][c] == player):
            count += 1
            r += dx
            c += dy

        r = row - dx
        c = col - dy

        while (0 <= r < self.size and
               0 <= c < self.size and
               self.board[r][c] == player):
            count += 1
            r -= dx
            c -= dy

        return count

    def check_win(self, row, col):

        directions = [
            (1, 0),   # 竖直
            (0, 1),   # 水平
            (1, 1),   # 主对角线
            (1, -1)   # 副对角线
        ]

        for dx, dy in directions:
            if self.check_direction(row, col, dx, dy) >= 5:
                return True

        return False

    def restart(self):
        self.canvas.delete("all")

        self.board = [
            [0 for _ in range(self.size)]
            for _ in range(self.size)
        ]

        self.current_player = 1
        self.game_over = False

        self.draw_board()


if __name__ == "__main__":
    root = tk.Tk()

    game = Gobang(root)

    root.mainloop()