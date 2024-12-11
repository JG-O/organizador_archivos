import tkinter
import app
import db
from tkinter import messagebox, ttk

#Crear pantalla inicial
pantalla = tkinter.Tk()
pantalla.title("Organizador de archivos")
pantalla.geometry("800x400")
pantalla.config(bg = 'black')

def enviar():
    r1 = ruta_o_dato.get()
    r2 = ruta_d_dato.get()
    mensaje = app.iniciar(r1, r2) 
    if type(mensaje) == list:
        mensaje_formateado = "\n-".join(mensaje)
        messagebox.showerror(title="Finalizo la ejecucion", message = f"los siguientes archivos no se pudieron ordenar:\n {mensaje_formateado}")
    else:
        messagebox.showinfo(title="Finalizo la ejecucion", message="Todo salio bien")

def mostrar_datos():
    datos = db.mostrar_historial()

    for dato in datos:
        tabla.insert("", "end", values=dato)

def historial():
    ventana_historial.deiconify()
    # Cargar los datos
    mostrar_datos()
    pantalla.withdraw()

def volver():
    pantalla.deiconify()      
    ventana_historial.withdraw()

def cerrar_programa_o():
    pantalla.quit()

def cerrar_programa_h():
    ventana_historial.quit()

box = tkinter.Frame(pantalla, bg='black')

#Texto
titulo = tkinter.Label(box, text="Organizador de archivos", bg='black', fg='white', font = ("Helvetica", 24))
explicacion = tkinter.Label(box, text="""Por favor, ingresa en el Campo 1(ruta 1) la ruta donde se encuentran los archivos que deseas organizar. En el Campo 2(ruta 2), ingresa la ruta de destino donde quieres mover y organizar los archivos. Si no introduces ninguna ruta en el Campo 2(ruta 2), los archivos se organizarán dentro de la misma carpeta especificada en el Campo 1(ruta 1).""",
                            wraplength = 700, justify="left", bg='black', fg='white', font = ("Times New Roman", 14))
ruta_o_texto = tkinter.Label(box, text="Ruta 1: ", bg='black', fg='white', font = ("Verdana", 18))
ruta_o_dato =  tkinter.Entry(box, width = 60, font = ("Courier", 14))
ruta_d_texto = tkinter.Label(box, text="Ruta 2: ", bg='black', fg='white', font = ("Verdana", 18))
ruta_d_dato =  tkinter.Entry(box, width = 60, font = ("Courier", 14))
boton = tkinter.Button(box, text="Organizar", bg='black', fg='white', font = ("Helvetica", 16), command=enviar)
boton_historial = tkinter.Button(box, text = "Historial", bg='black', fg='white', font = ("Helvetica", 16), command=historial)

titulo.grid(row = 0, column = 3, sticky="nsew", padx=20, pady = 30)
explicacion.grid(row = 1, column = 0, columnspan = 4)
ruta_o_texto.grid(row = 2, column = 2, pady = 15)
ruta_o_dato.grid(row = 2, column = 3, pady = 15)
ruta_d_texto.grid(row = 3, column = 2, pady = 15)
ruta_d_dato.grid(row = 3, column = 3, pady = 15)
boton.grid(row = 4, column = 3, columnspan = 2, sticky="e", pady = 15)
boton_historial.grid(row = 4, column = 1, columnspan = 2, sticky="e", pady = 15)

#ventana historial
ventana_historial = tkinter.Tk()
ventana_historial.title("Historial")
ventana_historial.geometry("1200x600")
ventana_historial.config(bg = 'black')
titulo = tkinter.Label(ventana_historial, text="Historial", bg='black', fg='white', font = ("Helvetica", 24), padx=20, pady = 30)
titulo.pack()

tabla = ttk.Treeview(ventana_historial, columns=("ID", "Ruta origen", "ruta destino", "archivo", "fecha"), show="headings")

# Configurar las columnas
tabla.heading("ID", text="ID")
tabla.heading("Ruta origen", text="Ruta origen")
tabla.heading("ruta destino", text="ruta destino")
tabla.heading("archivo", text="archivo")
tabla.heading("fecha", text="fecha")

# Configurar el tamaño de las columnas
tabla.column("ID", width=100, anchor="center")
tabla.column("Ruta origen", width=350, anchor="center")
tabla.column("ruta destino", width=350, anchor="center")
tabla.column("archivo", width=200, anchor="center")
tabla.column("fecha", width=100, anchor="center")

# Colocar el Treeview en la ventana
tabla.pack(padx=10, pady=10)
 
boton = tkinter.Button(ventana_historial, text = "Volver", bg='black', fg='white', font = ("Helvetica", 16), command = volver)
boton.pack()  
box.pack()

#cerrar programa
pantalla.protocol("WM_DELETE_WINDOW", cerrar_programa_o)
ventana_historial.protocol("WM_DELETE_WINDOW", cerrar_programa_h)

ventana_historial.withdraw()
pantalla.mainloop()