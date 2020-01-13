"""
 _     _     _   _               
| |   (_)___| |_| |__   _____  __
| |   | / __| __| '_ \ / _ \ \/ /
| |___| \__ \ |_| |_) | (_) >  < 
|_____|_|___/\__|_.__/ \___/_/\_\
                   
@author: Jonathan Wang
@coding: utf-8   
@environment: Manjaro 18.1.5 Juhraya + Python3.8.1
@date: 13th Jan., 2020

"""

import tkinter as tk

def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)

window = tk.Tk()

window.title('My Window')
window.geometry('500x300')

var1 = tk.StringVar()
lab = tk.Label(window, bg='green', fg='yellow', font=('Arial', 12), width=10, textvariable=var1)
lab.pack()

bu = tk.Button(window, text='Print Selection', width=10, height=2, command=print_selection)
bu.pack()

var2 = tk.StringVar()
var2.set((1, 2, 3, 4))

lb = tk.Listbox(window, listvariable=var2)

list_items = [11,22,33,44]
for item in list_items:
    lb.insert('end', item)  # insert since last position
lb.insert(1, 'first')   # insert 'fisrt' at position 1
lb.insert(2, 'second')   # insert 'second' at position 2
lb.delete(2)            # delete item at position2
lb.pack()
lb.insert(3, 'third')   # also can insert items after pack

window.mainloop()
