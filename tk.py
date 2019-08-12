from tkinter import *

# Creamos la raíz
root = Tk()
root.title("Marc Guapo")

entry = Entry(root)
entry.grid(row=0, column=1,padx=5,pady=5)
entry.config(justify="right")

label = Label(root,text="Nombre muy largo")
label.grid(row=0, column=0,sticky="e",padx=5,pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1,padx=5,pady=5)
entry2.config(justify="center")

label2 = Label(root,text="Apellido")
label2.grid(row=1, column=0,sticky="e",padx=5,pady=5)

# Comenzamos el bucle de aplicación, es como un while True y va a bajo
root.mainloop()