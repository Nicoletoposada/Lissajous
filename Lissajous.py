#Duvan Federico Sarmiento
#Nicolas Posada

import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox
import math
import turtle
from time import sleep

def dibujar():
    global f1,f2
    
    window = turtle.Screen()
    window.bgcolor('#0B0B3B')
    myPen=turtle.Turtle()
    myPen.speed(0)
    myPen.pensize(1)
    myPen.color('#00FFFF')
    myPen.penup()

    A=225
    B=225
    a=2*math.pi* float(f1.get())
    b=2*math.pi* float(f2.get())

    t=0
    for i in range(0,10000):
        t+=0.001
        x=A*math.sin(a*t+0)
        y=B*math.sin(b*t)

        myPen.goto(x,y)
        myPen.pendown()
        myPen.getscreen().update()
        
frame=tk.Tk()

tk.Label(frame,text='Dato A').grid(column=1,row=1, columnspan=2)
f1=tk.StringVar()
tk.Entry(frame,textvariable=f1).grid(column=3,row=1, columnspan=3)

tk.Label(frame,text='Dato B').grid(column=1,row=2, columnspan=2)
f2=tk.StringVar()
tk.Entry(frame,textvariable=f2).grid(column=3,row=2, columnspan=3)

tk.Button(frame,text='Ejecutar',command=dibujar).grid(column=1,row=9,columnspan=5)
frame.mainloop()