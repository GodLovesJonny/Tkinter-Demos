"""
  ____      _     _ 
 / ___|_ __(_) __| |
| |  _| '__| |/ _` |
| |_| | |  | | (_| |
 \____|_|  |_|\__,_|
                    
@author: Jonathan Wang
@coding: utf-8   
@environment: Manjaro 18.1.5 Juhraya + Python3.8.1
@date: 13th Jan., 2020

"""

import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

for i in range(3):
    for j in range(3):
        tk.Label(window, text=3*i+j+1).grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)

window.mainloop()
