"""
 _____       _              
| ____|_ __ | |_ _ __ _   _ 
|  _| | '_ \| __| '__| | | |
| |___| | | | |_| |  | |_| |
|_____|_| |_|\__|_|   \__, |
                      |___/ 

@author: Jonathan Wang
@coding: utf-8   
@environment: Manjaro 18.1.5 Juhraya + Python3.8.1
@date: 13th Jan., 2020

"""

import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

e1 = tk.Entry(window, show='*', font=('Arial', 14))         # show as password
e2 = tk.Entry(window, show=None, font=('Arial', 14))        # show as plain text
e1.pack()
e2.pack()

window.mainloop()
