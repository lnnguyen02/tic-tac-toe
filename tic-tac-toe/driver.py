'''
Created on Sep 28, 2021

@author: Leon
'''

from tkinter import *

window = Tk()

window.title("Tic Tac Toe GUI")

x = 625

y = 625

window.geometry("" + str(x) + "x" + str(y))

buttons = []

pixelVirtual = PhotoImage(width=1, height=1)

def clicked(x):
    print(str(x))
    #Button.configure(height = 100, width = 100)


for x in range(9):
    
    c = int(x % 3)
    
    r = int(x / 3)
    
    tempButton = Button(window,
                          text="" + str(x),
                          image=pixelVirtual,
                          width=200,
                          height=200,
                          compound="c",
                          command=clicked(x) )
    
    buttons.append(tempButton)
    
    buttons[x].grid(column=c , row=r)

window.mainloop()
