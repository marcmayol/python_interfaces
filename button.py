from tkinter import *


def sumar():
    n3.set(float(n1.get()) + float(n2.get()))
    borrar()
def resta():
    n3.set(float(n1.get()) - float(n2.get()))
    borrar()
def multi():
    n3.set(float(n1.get()) - float(n2.get()))
    borrar()


def borrar():
    n1.set("")
    n2.set("")


root = Tk()
root.config(bd=15)
n1 = StringVar()
n2 = StringVar()
n3 = StringVar()
Label(root, text="Número 1").pack()
Entry(root, justify="center", textvariable=n1).pack()  # 1
Label(root, text="Número 2").pack()
Entry(root, justify="center", textvariable=n2).pack()  # 2
Label(root, text=" ").pack()
Button(root, text="Sumar", command=sumar).pack()
Button(root, text="Resta", command=resta).pack()
Button(root, text="Producto", command=multi).pack()
Label(root, text="\nResultado").pack()
Entry(root, justify="center", textvariable=n3, state="disabled").pack()  # ressultado

root.mainloop()
