"""
 ____        _   _              
| __ ) _   _| |_| |_ ___  _ __  
|  _ \| | | | __| __/ _ \| '_ \ 
| |_) | |_| | |_| || (_) | | | |
|____/ \__,_|\__|\__\___/|_| |_|
                                
@author: Jonathan Wang
@coding: utf-8   
@environment: Manjaro 18.1.5 Juhraya + Python3.8.1
@date: 13th Jan., 2020

"""

import tkinter as tk

def hit_me():
    global on_hit
    if not on_hit:
        on_hit = True
        var.set('You hit me!')
    else:
        on_hit = False
        var.set('')

window = tk.Tk()

window.title('My Window')
window.geometry('500x300')

var = tk.StringVar()

lab = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)

lab.pack()

on_hit = False

bu = tk.Button(window, text='Hit Me', font=('Arial', 12), width=10, height=1, command=hit_me)
bu.pack()

window.mainloop()
