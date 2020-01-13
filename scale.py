"""
 ____            _      
/ ___|  ___ __ _| | ___ 
\___ \ / __/ _` | |/ _ \
 ___) | (_| (_| | |  __/
|____/ \___\__,_|_|\___|

@author: Jonathan Wang
@coding: utf-8   
@environment: Manjaro 18.1.5 Juhraya + Python3.8.1
@date: 13th Jan., 2020

"""

import tkinter as tk

def print_selection(value):
    lab.config(text='You have selected ' + value)

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

lab = tk.Label(window, bg='green', fg='white', width=30, text='empty')
lab.pack()

s = tk.Scale(window, label='Try Me!', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)
s.pack()

window.mainloop()
