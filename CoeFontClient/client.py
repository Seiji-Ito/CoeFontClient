
# -*- coding: utf-8 -*-
from download_frame import download_frame
import tkinter as tk
from tkinter import ttk
from tkinter.constants import X
import text_frame
import save_frame
import detaile_frame

"""
------メニューに必要なもの------
[account_menu]
アカウントの設定を行う

[voice_sample]
設定ボイスを選ぶ　※デフォルトではミリアル

------画面上に必要なもの------
[text_frame]
テキストボックス　※一度フォーカスを外れて再度フォーカスされた時に
                  テキストを全て選択する

[save_frame]
再生ボタン
保存ボタン

[detail_frame]
声の高さ
声の抑揚
声のスピード
音量　※数値で指定できる必要がある

[download_frame]
音声ファイルのダウンロード先をリストで選べる
"""

def testmessage(send_text):
    print(send_text)

def window_main():
    root = tk.Tk()

    #テキストボックスフレーム
    tf = text_frame.text_frame(0, 0, master=root)

    #再生、保存ボタンフレーム
    sf = save_frame.save_frame(0, 1, master=root)

    #声の詳細フレーム
    detf = detaile_frame.detaile_frame(1, 0, master=root)

    #ダウンロード先フレーム
    #dwnf = download_frame(1, 1, master=root)

    #window表示
    root.geometry("500x300")
    root.mainloop()

if __name__ == "__main__":
    window_main()