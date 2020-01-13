"""
  ____ _               _    _           _   _              
 / ___| |__   ___  ___| | _| |__  _   _| |_| |_ ___  _ __  
| |   | '_ \ / _ \/ __| |/ / '_ \| | | | __| __/ _ \| '_ \ 
| |___| | | |  __/ (__|   <| |_) | |_| | |_| || (_) | | | |
 \____|_| |_|\___|\___|_|\_\_.__/ \__,_|\__|\__\___/|_| |_|
                                                           

@author: Jonathan Wang
@coding: utf-8   
@environment: Manjaro 18.1.5 Juhraya + Python3.8.1
@date: 13th Jan., 2020

"""

import tkinter as tk

def print_selection():
    if var1.get() == 1 and var2.get() == 0:
        lab.config(text='I use Python for MCM.')
    elif var1.get() == 0 and var2.get() == 1:
        lab.config(text='I use Matlab for MCM.')
    elif var1.get() == 0 and var2.get() == 0:
        lab.config(text='I cannot code for MCM.')
    else:
        lab.config(text='I use both for MCM.')

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

lab = tk.Label(window, bg='yellow', width=40, text='empty')
lab.pack()

var1 = tk.IntVar()
var2 = tk.IntVar()

c1 = tk.Checkbutton(window, text='Python',variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='Matlab',variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()

window.mainloop()
