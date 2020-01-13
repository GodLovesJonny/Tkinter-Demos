"""
 __  __                  
|  \/  | ___ _ __  _   _ 
| |\/| |/ _ \ '_ \| | | |
| |  | |  __/ | | | |_| |
|_|  |_|\___|_| |_|\__,_|
                         
@author: Jonathan Wang
@coding: utf-8   
@environment: Manjaro 18.1.5 Juhraya + Python3.8.1
@date: 13th Jan., 2020

"""

import tkinter as tk

cnt = 0

def do_job():
    global cnt
    lab.config(text='do '+ str(cnt))
    cnt += 1

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

lab = tk.Label(window, text='       ', bg='green')
lab.pack()

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)

filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()
submenu = tk.Menu(filemenu, tearoff=0)
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
submenu.add_command(label='Submenu_1', command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)

editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)

window.config(menu=menubar)

window.mainloop()
