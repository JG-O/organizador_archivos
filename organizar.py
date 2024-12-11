import tipo_archivos
import shutil
import os
import db
"""
print(os.getcwd()) # Muestra la ruta actual del archivo
print(os.listdir()) # Muestra los archivos que estan en una carpeta

lista = os.listdir() # Guarda los archivos de una carpeta dentro de una lista

os.chdir("") # Cambiar de directorio/carpeta

os.mkdir("") # Crear una carpeta 

os.remove("") # Borrar una carpeta/archivo que esta dentro de un directorio

os.path.exists("") # Comprobar si una carpeta/archivo existe
"""
def nuevas_carpetas(extenciones_archivos, ruta_destino):
    for i in tipo_archivos.formatos.keys():
        for k in extenciones_archivos:
            if k in tipo_archivos.formatos[i] and not os.path.exists(ruta_destino + i):
                os.mkdir(ruta_destino + i)

def ordenar_archivos(ruta_origen, ruta_destino, archivo, extenciones_archivos):
    for i in tipo_archivos.formatos.keys():
        if extenciones_archivos in tipo_archivos.formatos[i]:
            try:
                db.guardar_historial(ruta_origen, ruta_destino, archivo)
                shutil.move(ruta_origen + archivo, ruta_destino + i)
            except:
                print("Algo salio mal")

def saber_extenciones(ruta_origen):
    extenciones_archivos = []
    for i in os.listdir(ruta_origen):
        extenciones = os.path.splitext(i)[1]
        if extenciones not in extenciones_archivos  and extenciones !="":                
            extenciones_archivos.append(extenciones)         

    return extenciones_archivos

def saber_archivo_invalido(ruta_origen):
    error = []
    for j in os.listdir(ruta_origen):
        verificar = False
        for i in tipo_archivos.formatos.keys():
            for k in tipo_archivos.formatos[i]:
                exts = os.path.splitext(j)[1]
                if exts == k:
                    verificar = True

        if verificar == False:
            error.append(j)

    return error

def ejecucion(ruta_origen, ruta_destino):
    extenciones_archivos= saber_extenciones(ruta_origen)
    error = saber_archivo_invalido(ruta_origen)
    nuevas_carpetas(extenciones_archivos, ruta_destino)
    for archivos in os.listdir(ruta_origen):
        extenciones_nueva = os.path.splitext(archivos)[1]
        ordenar_archivos(ruta_origen, ruta_destino, archivos, extenciones_nueva)

    if error:
        return error
    else:
        mensaje_p = "Todo salio bien"
        return mensaje_p

def las_rutas_existen(ruta_origen, ruta_destino):
    if os.path.exists(ruta_origen) and os.path.exists(ruta_destino):
        comparacion = True
        ruta = False
        return comparacion, ruta
    elif os.path.exists(ruta_origen) and ruta_destino == "":
        comparacion = True
        ruta = True
        return comparacion, ruta
    else:
        comparacion = False
        ruta = False
        return comparacion