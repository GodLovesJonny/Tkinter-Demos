"""
 __  __                                ____            
|  \/  | ___  ___ ___  __ _  __ _  ___| __ )  _____  __
| |\/| |/ _ \/ __/ __|/ _` |/ _` |/ _ \  _ \ / _ \ \/ /
| |  | |  __/\__ \__ \ (_| | (_| |  __/ |_) | (_) >  < 
|_|  |_|\___||___/___/\__,_|\__, |\___|____/ \___/_/\_\
                            |___/                      

@author: Jonathan Wang
@coding: utf-8   
@environment: Manjaro 18.1.5 Juhraya + Python3.8.1
@date: 13th Jan., 2020

"""

import tkinter as tk
import tkinter.messagebox   # is a must

def hit_me():
    tk.messagebox.showinfo(title='Hi', message='Hello!')
    tk.messagebox.showwarning(title='Hi', message='Warning!')
    tk.messagebox.showerror(title='Hi', message='Error!')
    print(tk.messagebox.askquestion(title='Hi', message='Hello!'))      # return 'yes' or 'no'
    print(tk.messagebox.askyesno(title='Hi', message='Hello!'))         # return 'True' or 'False'
    print(tk.messagebox.askokcancel(title='Hi', message='Hello!'))      # return 'True' or 'False'

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

tk.Button(window, text='Hit Me!', bg='green', font=('Arial', 14), command=hit_me).pack()

window.mainloop()
