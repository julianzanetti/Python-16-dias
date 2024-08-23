from tkinter import *

# Iniciar tkinter
aplicacion = Tk()

# Tamaño de la ventana
aplicacion.geometry('1250x650+0+0')

# Evitar maximizar
aplicacion.resizable(0,0)

# Titulo de la app
aplicacion.title("Sistema de Facturacion")

# Color del fondo
aplicacion.config(bg="burlywood")

# Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta del Titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturacion', fg='azure4', font=('Dosis', 58), bg='burlywood', width=27)
etiqueta_titulo.grid(row=0, column=0)

# Panel Izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel de costos
panel_costo = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costo.pack(side=BOTTOM)

# Panel de comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comidas', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# Panel de bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# Panel de postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# Panel derecho
panel_derecho = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecho.pack(side=RIGHT)

# Panel Calculadora
panel_calculadora = Frame(panel_derecho, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

# Panel Recibo
panel_recibo = Frame(panel_derecho, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# Panel Botones
panel_botones = Frame(panel_derecho, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

# Evitar que la pantalla se cierre
aplicacion.mainloop()
