
# -*- coding: utf-8 -*-
import tkinter as tk
import json

class download_frame(tk.Frame):
    def __init__(self, row, col, master=None):
        super().__init__(master)
        self.master = master
        self.frame_grid(row, col)
        self.create_widgets()

    def create_widgets(self):
        #スクロールバーの親フレームの中にリストボックスとスクロールバーを入れる
        self.scrollbar_frame = tk.Frame(self)
        self.scrollbar_frame.grid(row=0, column=0)

        #ダウンロード先のリストを読み込む
        json_open = open('./download_list.json', 'r')
        download_json = json.load(json_open)

        #リストボックス作成
        self.listbox = tk.Listbox(self.scrollbar_frame)
        for line in download_json["download"]:
            self.listbox.insert(tk.END, line)
        self.listbox.pack(side=tk.LEFT)

        #スクロールバー作成
        self.scroll_bar = tk.Scrollbar(self.scrollbar_frame, command=self.listbox.yview)
        self.scroll_bar.pack(side = tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=self.scroll_bar.set)

    def frame_grid(self, row, col):
        self.grid(row=row, column=col)