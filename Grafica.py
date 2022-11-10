import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox
import math
import turtle
from time import sleep

delta=0
def changeDelta0():
    global delta
    delta=0

def changeDelta1():
    global delta
    delta=math.pi/4

def changeDelta2():
    global delta
    delta=math.pi/2

def changeDelta3():
    global delta
    delta=3*math.pi/4
    
def changeDelta4():
    global delta    
    delta=math.pi

def dibujar():
    global f1,f2,delta
    messagebox.showinfo(message=f'Frecuencia 1: {f1.get()}, Frecuencia 2: {f2.get()}, Fase: {delta}', title="Variables")
    
    window = turtle.Screen()
    window.bgcolor('#000000')
    myPen=turtle.Turtle()
    myPen.speed(0)
    myPen.pensize(3)
    myPen.color('#FFFFFF')
    myPen.penup()

    A=100
    B=100
    a=2*math.pi* float(f1.get())
    b=2*math.pi* float(f2.get())

    messagebox.showinfo(message=f'wa: {a}, wb: {b}, Fase: {delta}', title="Variables")
    t=0
    for i in range(0,1000):
        t+=0.01
        x=A*math.sin(a*t+delta)
        y=B*math.sin(b*t)

        myPen.goto(x,y)
        myPen.pendown()
        myPen.getscreen().update()
        
frame=tk.Tk()

tk.Label(frame,text='Frecuencia #1').grid(column=1,row=1, columnspan=2)
f1=tk.StringVar()
tk.Entry(frame,textvariable=f1).grid(column=3,row=1, columnspan=3)

tk.Label(frame,text='Frecuencia #2').grid(column=1,row=2, columnspan=2)
f2=tk.StringVar()
tk.Entry(frame,textvariable=f2).grid(column=3,row=2, columnspan=3)

tk.Button(frame,text='0',command=changeDelta0).grid(column=1,row=3)
tk.Button(frame,text='pi/4',command=changeDelta1).grid(column=2,row=3)
tk.Button(frame,text='pi/2',command=changeDelta2).grid(column=3,row=3)
tk.Button(frame,text='3pi/4',command=changeDelta3).grid(column=4,row=3)
tk.Button(frame,text='pi',command=changeDelta4).grid(column=5,row=3)

tk.Button(frame,text='Ejecutar',command=dibujar).grid(column=1,row=9,columnspan=5)
frame.mainloop()