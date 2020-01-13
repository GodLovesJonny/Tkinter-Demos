"""
 ____           _ _       _           _   _              
|  _ \ __ _  __| (_) ___ | |__  _   _| |_| |_ ___  _ __  
| |_) / _` |/ _` | |/ _ \| '_ \| | | | __| __/ _ \| '_ \ 
|  _ < (_| | (_| | | (_) | |_) | |_| | |_| || (_) | | | |
|_| \_\__,_|\__,_|_|\___/|_.__/ \__,_|\__|\__\___/|_| |_|
                                                         
@author: Jonathan Wang
@coding: utf-8   
@environment: Manjaro 18.1.5 Juhraya + Python3.8.1
@date: 13th Jan., 2020

"""

import tkinter as tk

def print_selection():
    lab.config(text='You have selected ' + var.get())


window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

var = tk.StringVar()
lab = tk.Label(window, bg='yellow', width=20, text='empty')
lab.pack()

r1 = tk.Radiobutton(window, text='Option A', variable=var, value='A', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B', variable=var, value='B', command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='Option C', variable=var, value='C', command=print_selection)
r3.pack()


window.mainloop()
