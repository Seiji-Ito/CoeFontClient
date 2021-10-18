
import tkinter as tk
from tkinter import ttk
"""
class text_frame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

    def create_widgets(self):
        self.voice_text = tk.Text(self, width=50, height=5)
        self.voice_text.pack()

    def frame_grid(self, row, col):
        self.grid(row=row, column=col)
        """

class text_frame(ttk.Frame):
    def __init__(self, row, col, master=None):
        super().__init__(master)
        self.master = master
        self.frame_grid(row, col)
        self.create_widgets()

    def create_widgets(self):
        self.voice_text = tk.Text(self, width=50, height=5)
        self.voice_text.pack()

    def frame_grid(self, row, col):
        self.grid(row=row, column=col)