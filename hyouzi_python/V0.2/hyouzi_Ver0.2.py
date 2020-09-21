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
    print("NoSectionError /n or /n inifile not found", err.section)
    messagebox.showerror('error', err)
except configparser.NoOptionError as err:
    flag = False
    print("NoOptionError", err.option, err.section)
    messagebox.showerror('NoOptionError', err)
if hyouzi =='':
    flag = False
    messagebox.showerror('NoOptionError', 'Not entered in the DEFAULTPASS')


#hyouzi.txt read
while flag == True:
    dt_now = datetime.datetime.now()
    try:
        with open(hyouzi, 'r', encoding='UTF-8') as f:
            data = f.read()
    except FileNotFoundError:
        flag = False
        messagebox.showerror('error', 'Textfile not found')
    except Exception as err:
        flag = False
        messagebox.showerror('error', err)
    
    if flag == True:
        if not data:
            messagebox.showerror('error', 'There is no data in \n hyouzi.txt')
            flag = False
        else:
            messagebox.showinfo(dt_now.strftime('%m/%d %H:%M:%S'), data)
            flag = messagebox.askyesno('update', 'Do you want to update?')

#end
messagebox.showinfo('end','The end of the program')
root.destroy()
