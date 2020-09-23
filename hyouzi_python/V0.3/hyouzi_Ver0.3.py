# -*- coding: utf-8 -*-
import configparser
import datetime
import tkinter as tk
from tkinter import messagebox

flag = True
root = tk.Tk()
root.withdraw()

#config.ini read
ini = configparser.ConfigParser()
try:
    ini.read('./config.ini', 'UTF-8')
    hyouzi = ini['DEFAULTPASS']['hyouzi']
except configparser.NoSectionError as err:
    flag = False
    messagebox.showerror('エラー', err)
except configparser.NoOptionError as err:
    flag = False
    messagebox.showerror('エラー', err)
if hyouzi =='':
    flag = False
    messagebox.showerror('エラー', 'iniファイルのhyouziパスが指定されていません')


#hyouzi.txt read
while flag == True:
    dt_now = datetime.datetime.now()
    try:
        with open(hyouzi, 'r', encoding='UTF-8') as f:
            data = f.read()
    except FileNotFoundError:
        flag = False
        messagebox.showerror('エラー', 'テキストファイルがありません')
    except Exception as err:
        flag = False
        messagebox.showerror('エラー', err)
    
    if flag == True:
        if not data:
            messagebox.showerror('エラー', 'txtファイルのデータがありません')
            flag = False
        else:
            messagebox.showinfo(dt_now.strftime('%m/%d %H:%M:%S'), data)
            flag = messagebox.askyesno('更新確認', 'メッセージボックスを更新しますか?')

#end
messagebox.showinfo('終了','プログラムを終了します')
root.destroy()
