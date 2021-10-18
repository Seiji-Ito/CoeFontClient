
import tkinter as tk
from tkinter import ttk

class save_frame(ttk.Frame):
    def __init__(self, row, col, master=None):
        super().__init__(master)
        self.master = master
        self.frame_grid(row, col)
        self.create_widgets()

    def create_widgets(self):
        # 再生ボタン
        self.play_button = ttk.Button(self)
        self.play_button["text"]="再生"
        self.play_button.pack()

        # 保存ボタン
        self.save_button = ttk.Button(self)
        self.save_button["text"]="保存"
        self.save_button.pack()

    def frame_grid(self, row, col):
        self.grid(row=row, column=col)