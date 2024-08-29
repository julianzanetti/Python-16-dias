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
panel_costo = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=100)
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
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:

    #Crear el chekbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable=variables_comida[contador])
    comida.grid(row=contador, column=0, sticky=W)

    #Crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED, textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador, column=1)

    contador += 1


# Generar el Item de bebidas
variables_bebidas = []
cuadros_bebidas = []
texto_bebidas = []
contador = 0
for bebida in lista_bebidas:

    # Crear el chekbutton
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable=variables_bebidas[contador])
    bebida.grid(row=contador, column=0, sticky=W)

    #Crear los cuadros de entrada
    cuadros_bebidas.append('')
    texto_bebidas.append('')
    texto_bebidas[contador] = StringVar()
    texto_bebidas[contador].set('0')
    cuadros_bebidas[contador] = Entry(panel_bebidas, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED, textvariable=texto_bebidas[contador])
    cuadros_bebidas[contador].grid(row=contador, column=1)

    contador += 1


# Generar el Item de postres
variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for postre in lista_postres:

    # Crear el chekbutton
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable=variables_postres[contador])
    postre.grid(row=contador, column=0, sticky=W)

    #Crear los cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED, textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador, column=1)

    contador += 1


# Variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()


# Etiqueta de costo y campos de entrada
# Comida
etiqueta_costo_comida = Label(panel_costo, text='Costo Comida', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_comida.grid(row=0, column=0)
texto_costo_comida = Entry(panel_costo, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

# Bebida
etiqueta_costo_bebida = Label(panel_costo, text='Costo Bebida', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)
texto_costo_bebida = Entry(panel_costo, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

# Postre
etiqueta_costo_postre = Label(panel_costo, text='Costo Postre', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_postre.grid(row=2, column=0)
texto_costo_postre = Entry(panel_costo, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)

# Subtotal
etiqueta_subtotal = Label(panel_costo, text='Subtotal', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_subtotal.grid(row=0, column=2)
texto_subtotal = Entry(panel_costo, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

# Impuestos
etiqueta_impuestos = Label(panel_costo, text='Impuestos', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_impuestos.grid(row=1, column=2)
texto_impuestos = Entry(panel_costo, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_impuestos)
texto_impuestos.grid(row=1, column=3, padx=41)

# Total
etiqueta_total = Label(panel_costo, text='Total', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_total.grid(row=2, column=2)
texto_total = Entry(panel_costo, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)


# Botones
botones = ['total', 'recibo', 'guardar', 'imprimir']
columnas = 0
for boton in botones:
    boton = Button(panel_botones, text=boton.title(), font=('Dosis', 14, 'bold'), fg='white', bg='azure4', bd=1, width=9)
    boton.grid(row=0, column = columnas)
    columnas +=1

# Recibo
texto_recibo = Text(panel_recibo, font=('Dosis', 12, 'bold'), bd=1, width=51, height=10)
texto_recibo.grid(row=0, column=0)

# Calculadora
visor_calculadora = Entry(panel_calculadora, font=('Dosis', 16, 'bold'), width=38, bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=4)

botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '*', '=', 'Borrar', '0', '/']
fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora, text=boton.title(), font=('Dosis', 16, 'bold'), fg='white', bg='azure4', bd=1, width=8)
    boton.grid(row=fila, column=columna)
    if columna == 3:
        fila+=1

    columna +=1
    if columna == 4:
        columna=0


# Evitar que la pantalla se cierre
aplicacion.mainloop()
