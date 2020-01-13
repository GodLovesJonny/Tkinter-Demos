"""
 _____                         
|  ___| __ __ _ _ __ ___   ___ 
| |_ | '__/ _` | '_ ` _ \ / _ \
|  _|| | | (_| | | | | | |  __/
|_|  |_|  \__,_|_| |_| |_|\___|
                               
@author: Jonathan Wang
@coding: utf-8   
@environment: Manjaro 18.1.5 Juhraya + Python3.8.1
@date: 13th Jan., 2020

"""

import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

tk.Label(window, text='on the window', bg='red', font=('Arial', 16)).pack()

frame = tk.Frame(window)
frame.pack()

frame_l = tk.Frame(frame)
frame_r = tk.Frame(frame)
frame_l.pack(side='left')
frame_r.pack(side='right')

tk.Label(frame_l, text='on the frame_l1', bg='green').pack()
tk.Label(frame_l, text='on the frame_l2', bg='green').pack()
tk.Label(frame_l, text='on the frame_l3', bg='green').pack()
tk.Label(frame_r, text='on the frame_r1', bg='yellow').pack()
tk.Label(frame_r, text='on the frame_r2', bg='yellow').pack()
tk.Label(frame_r, text='on the frame_r3', bg='yellow').pack()

window.mainloop()
