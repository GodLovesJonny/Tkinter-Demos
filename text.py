"""
 _____         _   
|_   _|____  _| |_ 
  | |/ _ \ \/ / __|
  | |  __/>  <| |_ 
  |_|\___/_/\_\\__|
                   
@author: Jonathan Wang
@coding: utf-8   
@environment: Manjaro 18.1.5 Juhraya + Python3.8.1
@date: 13th Jan., 2020

"""

import tkinter as tk

def insert_point():     # insert at cursor position
    var = e.get()
    tx.insert('insert', var)

def insert_end():       # insert at the end of text
    var = e.get()
    tx.insert('end', var)


window = tk.Tk()

window.title('My Window')
window.geometry('500x300')

e = tk.Entry(window, show=None)
e.pack()

bu1 = tk.Button(window, text='Insert Point', width=10, height=2, command=insert_point)
bu2 = tk.Button(window, text='Insert End', width=10, height=2, command=insert_end)
bu1.pack()
bu2.pack()

tx = tk.Text(window, height=3)
tx.pack()

window.mainloop()
