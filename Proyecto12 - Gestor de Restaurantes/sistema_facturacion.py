from tkinter import *

# Iniciar tkinter
aplicaion = Tk()

# Tamaño de la ventana
aplicaion.geometry('1020x630+0+0')

# Evitar maximizar
aplicaion.resizable(0,0)

# Titulo de la app
aplicaion.title("Sistema de Facturacion")

# Color del fondo
aplicaion.config(bg="burlywood")

# Evitar que la pantalla se cierre
aplicaion.mainloop()
