import tkinter as tk 
from tkinter import messagebox


def saludo_bienvenido:


ventana = tk.Tk()
ventana.title("Ventana insanidad")#title es para el titulo de la ventana
ventana.geometry("800x700")


#Fuente
letra=("Rockwell,24")
etiqueta = tk.Label(ventana,text = "Ingreses tu nombre : ",font=letra)
etiqueta.pack(pady=15)#pady me sirve para distanciar mis objetos 

boton = tk.Button(ventana,text="Saludos",command=saludo_bienvenido)
boton.pack(pady=15)
































ventana.mainloop()
