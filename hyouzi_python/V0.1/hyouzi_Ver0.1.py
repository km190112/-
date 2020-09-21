# -*- coding: utf-8 -*-
import configparser
import datetime
import tkinter as tk
from tkinter import messagebox

ini = configparser.ConfigParser()
ini.read('./config.ini', 'UTF-8')
hyouzi = ini['DEFAULTPASS']['hyouzi']

root = tk.Tk()
root.withdraw()

flag = True
while flag == True:
    dt_now = datetime.datetime.now()
    
    f = open(hyouzi, 'r', encoding='UTF-8')
    data = f.read()
    f.close()   
    
    if not data:
        messagebox.showerror('error', 'There is no data in \n hyouzi.txt')
        flag = False
    else:
        messagebox.showinfo(dt_now.strftime('%m/%d %H:%M:%S'), data)
        flag = messagebox.askyesno('update', 'Do you want to update?')
        
messagebox.showinfo('end','The end of the program')
root.destroy()
