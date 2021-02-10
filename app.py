from tkinter import *

# Aqui empiezan las funciones:


def hola():
    print("Hola!")


ventana1 = Tk()
ventana1.geometry("500x200")
ventana1.resizable(0, False)
# ventana1.config()
fondo1 = PhotoImage(file="Fondo1.gif")
etiqueta_fondo1 = Label(ventana1, image=fondo1).place(x=0, y=0)
Label(ventana1, text="Usted ya esta registrado?").grid(
    row=1, column=0, sticky=E, padx=175
)
boton = Button(ventana1, text="Iniciar sesion", command=hola).grid(row=2, column=0)
Label(ventana1, text="Usted no esta registrado?").grid(row=3, column=0)
boton = Button(ventana1, text="Registrarse", command=hola).grid(row=4, column=0)
ventana1.mainloop()
"""
ventana2 = Tk()
ventana2.geometry("500x200")
ventana2.resizable(0, False)
ventana2.mainloop()

ventana3 = Tk()
ventana3.geometry("500x200")
ventana3.resizable(0, False)
ventana3.mainloop()

ventana4 = Tk()
ventana4.geometry("500x200")
ventana4.resizable(0, False)
ventana4.mainloop()
"""