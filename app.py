import organizar

def iniciar(r1, r2):
    ruta_origen = r1
    ruta_destino = r2

    ruta_origen_m = ruta_origen.replace("\\", "/")
    ruta_destino_m = ruta_destino.replace("\\", "/")

    verificacion = organizar.las_rutas_existen(ruta_origen_m, ruta_destino_m)

    if verificacion[0] == True and verificacion[1] == False:
        ruta_destino_m += "/"
        ruta_origen_m += "/"
        mensaje = organizar.ejecucion(ruta_origen_m, ruta_destino_m)
        return mensaje
    elif verificacion[0] == True and verificacion[1] == True:
        ruta_origen_m += "/"
        ruta_destino_m = ruta_origen_m
        mensaje = organizar.ejecucion(ruta_origen_m, ruta_destino_m)
        return mensaje
    else:
        mensaje_error_2 = "la ruta origen o destino no existe"
        return mensaje_error_2