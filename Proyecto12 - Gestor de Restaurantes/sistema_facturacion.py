from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''

def revisar_check():
    x=0
    for c in lista_comidas:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x +=1

    x=0
    for c in lista_bebidas:
        if variables_bebidas[x].get() == 1:
            cuadros_bebidas[x].config(state=NORMAL)
            if cuadros_bebidas[x].get() == '0':
                cuadros_bebidas[x].delete(0, END)
            cuadros_bebidas[x].focus()
        else:
            cuadros_bebidas[x].config(state=DISABLED)
            texto_bebidas[x].set('0')
        x +=1

    x=0
    for c in lista_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x +=1


def total():
    sub_total_comida = 0
    p = 0
    for cant in texto_comida:
        sub_total_comida = sub_total_comida + (float(cant.get()) * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cant in texto_bebidas:
        sub_total_bebida = sub_total_bebida + (float(cant.get()) * precios_bebida[p])
        p += 1

    sub_total_postre = 0
    p = 0
    for cant in texto_postres:
        sub_total_postre = sub_total_postre + (float(cant.get()) * precios_postres[p])
        p += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set(f'$ {round(sub_total_comida, 2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida, 2)}')
    var_costo_postre.set(f'$ {round(sub_total_postre, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuestos.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')


def recibo():
    texto_recibo.delete(1.0, END)
    nro_recibo = f"N# - {random.randint(1000,9999)}"
    fecha = datetime.datetime.now()
    fecha_recibo = f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.second}"
    texto_recibo.insert(END, f"Datos:\t{nro_recibo}\t\t{fecha_recibo}\n")
    texto_recibo.insert(END, f"*" * 76 + "\n")
    texto_recibo.insert(END, f"Items\t\tCant.\tCosto Items\n")
    texto_recibo.insert(END, f"-" * 91 + "\n")

    x=0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f"{lista_comidas[x]}\t\t{comida.get()}\t${int(comida.get()) * precios_comida[x]}\n")
        x +=1

    x=0
    for bebida in texto_bebidas:
        if bebida.get() != '0':
            texto_recibo.insert(END, f"{lista_bebidas[x]}\t\t{bebida.get()}\t${int(bebida.get()) * precios_bebida[x]}\n")
        x +=1

    x=0
    for postre in texto_postres:
        if postre.get() != '0':
            texto_recibo.insert(END, f"{lista_postres[x]}\t\t{postre.get()}\t${int(postre.get()) * precios_postres[x]}\n")
        x +=1

    texto_recibo.insert(END, f"-" * 91 + "\n")
    texto_recibo.insert(END, f"Costo Comida: \t\t\t{var_costo_comida.get()}\n")
    texto_recibo.insert(END, f"Costo Bebida: \t\t\t{var_costo_comida.get()}\n")
    texto_recibo.insert(END, f"Costo Postre: \t\t\t{var_costo_comida.get()}\n")
    texto_recibo.insert(END, f"-" * 91 + "\n")
    texto_recibo.insert(END, f"Sub-Total: \t\t\t{var_subtotal.get()}\n")
    texto_recibo.insert(END, f"Impuestos: \t\t\t{var_impuestos.get()}\n")
    texto_recibo.insert(END, f"Total: \t\t\t{var_total.get()}\n")

    texto_recibo.insert(END, f"*" * 76 + "\n")
    texto_recibo.insert(END, f"Los Esperamos Pronto")


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')


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
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable=variables_comida[contador], command=revisar_check)
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
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable=variables_bebidas[contador], command=revisar_check)
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
    postre = Checkbutton(panel_postres, text=postre.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable=variables_postres[contador], command=revisar_check)
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
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones, text=boton.title(), font=('Dosis', 14, 'bold'), fg='white', bg='azure4', bd=1, width=9)
    boton.grid(row=0, column = columnas)
    botones_creados.append(boton)
    columnas +=1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)

# Recibo
texto_recibo = Text(panel_recibo, font=('Dosis', 12, 'bold'), bd=1, width=51, height=10)
texto_recibo.grid(row=0, column=0)

# Calculadora
visor_calculadora = Entry(panel_calculadora, font=('Dosis', 16, 'bold'), width=38, bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=4)

botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '*', '=', 'Borrar', '0', '/']
botones_guardados = []
fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora, text=boton.title(), font=('Dosis', 16, 'bold'), fg='white', bg='azure4', bd=1, width=8)
    boton.grid(row=fila, column=columna)
    botones_guardados.append(boton)
    if columna == 3:
        fila+=1

    columna +=1
    if columna == 4:
        columna=0

botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))


# Evitar que la pantalla se cierre
aplicacion.mainloop()
