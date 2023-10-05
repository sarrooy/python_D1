from tkinter import *
import tkinter

marquito = Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()

def EnableAll():
    i=0
    if  (  C3['state'] == NORMAL ):
        C3['state'] = DISABLED
    else:
        C3['state'] = NORMAL



C1 = Checkbutton(marquito, text = "Music", variable = CheckVar1, \
   onvalue = 1, offvalue = 0, height=5, \
   width = 20, command=lambda:EnableAll())
C2 = Checkbutton(marquito, text = "Video", variable = CheckVar2, \
   onvalue = 1, offvalue = 0, height=5, \
   width = 20)
C3 = Button(marquito, text = "me controlan", height=2, width=15, state=NORMAL)

C1.grid(row=1, column=0, sticky=W, padx=2, pady=2)
C2.grid(row=2, column=0, sticky=W, padx=2, pady=2)
C3.grid(row=3, column=0, padx=2, pady=2)
marquito.mainloop()