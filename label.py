"""
 _          _          _ 
| |    __ _| |__   ___| |
| |   / _` | '_ \ / _ \ |
| |__| (_| | |_) |  __/ |
|_____\__,_|_.__/ \___|_|
                         
@author: Jonathan Wang
@coding: utf-8   
@environment: Manjaro 18.1.5 Juhraya + Python3.8.1
@date: 13th Jan., 2020

"""

import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

lab = tk.Label(window, text='Hello! This is Tkinter.', bg='green', font=('Arial', 12), width=30, height=2)

lab.pack()

window.mainloop()
