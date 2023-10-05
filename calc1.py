from tkinter import*
#from tkinter import Tk

window = Tk()
window.title("Calculadora Basica")

#definicion del area de trabajo
espacio = Entry(window, background='gray', font=("Calibri 20"))
window['bg']='green'
espacio.grid(row=0, column=0, columnspan=4, padx=50, pady=5)

boton0 = Button(window, text="0", width=13, height=2)
boton1 = Button(window, text="1", width=5, height=2)
boton2 = Button(window, text="2", width=5, height=2)
boton3 = Button(window, text="3", width=5, height=2)
boton4 = Button(window, text="4", width=5, height=2)
boton5 = Button(window, text="5", width=5, height=2)
boton6 = Button(window, text="6", width=5, height=2)
boton7 = Button(window, text="7", width=5, height=2)
boton8 = Button(window, text="8", width=5, height=2)
boton9 = Button(window, text="9", width=5, height=2)

boton_clr = Button(window, text="AC", width=5, height=2)
boton_par1 = Button(window, text="(", width=5, height=2)
boton_par2 = Button(window, text=")", width=5, height=2)
boton_dot = Button(window, text=".", width=5, height=2)

boton_ADD = Button(window, text="+", width=5, height=2)
boton_SUB = Button(window, text="-", width=5, height=2)
boton_MULT = Button(window, text="*", width=5, height=2)
boton_DIV = Button(window, text="/", width=5, height=2)
boton_EQU = Button(window, text="=", width=5, height=2)

# agregamos elementos a la ventana mediante un arreglo


window.mainloop()