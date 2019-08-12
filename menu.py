from tkinter import *

root = Tk()

menubar=Menu(root)
root.config(menu=menubar)

filemenu= Menu(menubar, tearoff=0)
filemenu.add_command(label="nuevo")
filemenu.add_command(label="abrir")
filemenu.add_command(label="guardar")
filemenu.add_command(label="cerrar")
filemenu.add_separator()
filemenu.add_command(label="salir",command=root.quit)

editmenu= Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")

helpmenu= Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de ...")

menubar.add_cascade(label="Archivo",menu=filemenu)
menubar.add_cascade(label="Editar",menu=editmenu)
menubar.add_cascade(label="Ayuda",menu=helpmenu)

root.mainloop()

