from tkinter import *

def selecionar():
    cadena=""
    if(leche.get()):
        cadena+="Con leche"
    else:
        cadena += "Sin leche"

    if(azucar.get()):
        cadena += " y con azucar"
    else:
        cadena += " y sin azucar"
    monitor.config(text=cadena)

root = Tk()
root.config(bd=15)
leche = IntVar()
azucar= IntVar()

imagen = PhotoImage(file="giphy.gif")
Label(root, image=imagen).pack(side="left")

frame = Frame(root)
frame.pack(side="left")

Label(frame,text="¿como quieres el cafe?").pack(anchor="w")
Checkbutton(frame, text="Con leche", variable=leche, onvalue=1, offvalue=0, command=selecionar).pack(anchor="w")
Checkbutton(frame, text="Con azucar", variable=azucar, onvalue=1, offvalue=0, command=selecionar).pack(anchor="w")

monitor = Label(frame)
monitor.pack()

root.mainloop()