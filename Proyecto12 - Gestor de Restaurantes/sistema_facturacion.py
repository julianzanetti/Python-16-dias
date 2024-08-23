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

# Lista de Productos
lista_comidas = ['pollo', 'cordero', 'salmon', 'merluza', 'hamburguesa', 'pizza1', 'pizza2', 'pizza3']
lista_bebidas = ['agua', 'soda', 'cola', 'jugo', 'cerveza1', 'cerveza2', 'vino1', 'vino2']
lista_postres = ['helado', 'flan', 'tiramisu', 'brownie', 'lemon pie', 'mousse', 'budin', 'Torta']

# Generar el Item de comidas
variables_comida = []
contador = 0
for comida in lista_comidas:
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable=variables_comida[contador])
    comida.grid(row=contador, column=0, sticky=W)
    contador +=1

# Generar el Item de bebidas
variables_bebidas = []
contador = 0
for bebida in lista_bebidas:
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable=variables_bebidas[contador])
    bebida.grid(row=contador, column=0, sticky=W)
    contador +=1

# Generar el Item de postres
variables_postres = []
contador = 0
for postre in lista_postres:
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable=variables_postres[contador])
    postre.grid(row=contador, column=0, sticky=W)
    contador +=1


# Evitar que la pantalla se cierre
aplicacion.mainloop()
