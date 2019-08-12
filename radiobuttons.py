from tkinter import *

root = Tk()
def selecionar():
   monitor.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    monitor.config(text="")

opcion = IntVar()
Radiobutton(root, text="opcion 1", variable=opcion, value=1, command=selecionar).pack()
Radiobutton(root, text="opcion 2", variable=opcion, value=2, command=selecionar).pack()
Radiobutton(root, text="opcion 3", variable=opcion, value=3, command=selecionar).pack()

monitor = Label(root)
monitor.pack()
Button(root, text="reiniciar", command=reset).pack()

root.mainloop()