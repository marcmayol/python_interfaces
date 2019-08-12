from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as Colorchooser
from tkinter import filedialog as Filedialog

root = Tk()
root.title("Marc Guapo")


def test():
    # MessageBox.showinfo("Hola","hola mundo")
    # MessageBox.showwarning("Alerta","sección para adultos")
    # MessageBox.showerror("Error","sección para adultos")
    # res= MessageBox.askquestion("Salir","¿estas seguro que quieres salir?")
    # if(res == "yes"):
    #     root.quit()
    # res = MessageBox.askokcancel("Salir", "¿estas seguro de sobreescribir el fichero?")
    #
    # res = MessageBox.askretrycancel("reintentar","no se puede conectar")
    # if (res):
    #     root.quit()
    # color=Colorchooser.askcolor(title="elige un color")
    # print(color)
    # fichero = Filedialog.askopenfilename(title="Abrir un fichero", initialdir="/",filetypes=(("Fixero de texto","txt"),("Fixero de texto","*.txt")))
    # print(fichero)
    fichero = Filedialog.asksaveasfile(title="Guaradar fichero", mode="w", defaultextension=".txt") #equivale a  open(ruta , formato write)
    print(fichero)

Button(root, text="clicame", command=test).pack()

root.mainloop()
