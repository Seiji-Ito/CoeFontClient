import tkinter as tk
from tkinter import ttk
from tkinter.constants import HORIZONTAL

class detaile_frame(ttk.Frame):
    def __init__(self, row, col, master=None):
        super().__init__(master)
        self.master = master
        self.frame_grid(row, col)
        self.create_widgets()

    def create_widgets(self):
        #音量スライド
        self.volume_scale = tk.Scale(self, from_=0, to=100, label="音量", orient=tk.HORIZONTAL)
        #self.volume_scale = ttk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        self.volume_scale.grid(row=0, column=0)

        #声の高さ
        self.pitch_scale = tk.Scale(self, from_=0, to=100, label="声の高さ", orient=tk.HORIZONTAL)
        #self.pitch_scale = ttk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        self.pitch_scale.grid(row=1, column=0)

        #声のスピード
        self.speed_scale = tk.Scale(self, from_=0, to=20, label="声のスピード", orient=tk.HORIZONTAL)
        #self.speed_scale = ttk.Scale(self, from_=0, to=20, orient=tk.HORIZONTAL)
        self.speed_scale.grid(row=0, column=1)

        #声の抑揚
        self.speed_scale = tk.Scale(self, from_=0, to=8, label="声の抑揚", orient=tk.HORIZONTAL)
        #self.speed_scale = ttk.Scale(self, from_=0, to=8, orient=tk.HORIZONTAL)
        self.speed_scale.grid(row=1, column=1)

    def frame_grid(self, row, col):
        self.grid(row=row, column=col)