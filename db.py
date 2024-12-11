import pymysql
from datetime import date

Host = 'localhost'
Port = 3305
User = 'root'
Password = #Aqui va la contraseña de tu xammp
Database = 'seminario'

try:
    conexion = pymysql.connect(
    host = Host,
    user = User,
    password = Password,
    database = Database,
    port = Port
    )

    cursor = conexion.cursor()

    print("conexion exitosa")
except:
    print("Conexion a base de datos fallida")


def guardar_historial(ruta_origen, ruta_destino, nom_archivo):
    r1 = ruta_origen
    r2 = ruta_destino
    archivo = nom_archivo
    fecha = date.today()

    solicitud = 'INSERT INTO historial (ruta_origen, ruta_destino, archivo, fecha) VALUES (%s, %s, %s, %s)'
    
    cursor.execute(solicitud, (r1, r2, archivo, fecha))
    conexion.commit()
    
    return print("Bien")

def mostrar_historial():
    cursor.execute('SELECT * FROM historial')
    resultado = cursor.fetchall()

    return resultado
