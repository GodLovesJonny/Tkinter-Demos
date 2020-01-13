"""
 ____            _    
|  _ \ __ _  ___| | __
| |_) / _` |/ __| |/ /
|  __/ (_| | (__|   < 
|_|   \__,_|\___|_|\_\
                      
@author: Jonathan Wang
@coding: utf-8   
@environment: Manjaro 18.1.5 Juhraya + Python3.8.1
@date: 13th Jan., 2020

"""

import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

tk.Label(window, text='N', fg='red').pack(side='top')
tk.Label(window, text='S', fg='red').pack(side='bottom')
tk.Label(window, text='W', fg='red').pack(side='left')
tk.Label(window, text='E', fg='red').pack(side='right')

window.mainloop()
