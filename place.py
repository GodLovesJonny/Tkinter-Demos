"""
 ____  _                
|  _ \| | __ _  ___ ___ 
| |_) | |/ _` |/ __/ _ \
|  __/| | (_| | (_|  __/
|_|   |_|\__,_|\___\___|
                        
@author: Jonathan Wang
@coding: utf-8   
@environment: Manjaro 18.1.5 Juhraya + Python3.8.1
@date: 13th Jan., 2020

"""

import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

tk.Label(window, text='Pivot', font=('Arial', 20), ).place(x=50, y=100, anchor='nw')

window.mainloop()
