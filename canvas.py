"""
  ____                          
 / ___|__ _ _ ____   ____ _ ___ 
| |   / _` | '_ \ \ / / _` / __|
| |__| (_| | | | \ V / (_| \__ \
 \____\__,_|_| |_|\_/ \__,_|___/
                                
@author: Jonathan Wang
@coding: utf-8   
@environment: Manjaro 18.1.5 Juhraya + Python3.8.1
@date: 13th Jan., 2020

"""

import tkinter as tk

def move_rect():
    canvas.move(rect, 2, 2)

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

canvas = tk.Canvas(window, bg='green', height=200, width=500)
img_file = tk.PhotoImage(file='./src/imgs/wolf.png')
img = canvas.create_image(250, 0, anchor='n', image=img_file)

x0, y0, x1, y1 = 100, 100, 150, 150
line = canvas.create_line(x0-50, y0-50, x1-50, y1-50)
oval = canvas.create_oval(x0+120, y0+50, x1+120, y1+50, fill='yellow')
arc = canvas.create_arc(x0, y0+50, x1, y1+50, start=0, extent=180)
rect = canvas.create_rectangle(330, 30, 330+20, 30+20)
canvas.pack()

bu = tk.Button(window, text='Move the Rect',command=move_rect).pack()

window.mainloop()
