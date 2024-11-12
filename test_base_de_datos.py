import unittest
from conexion_base_datos import *
import datetime
import sqlite3

class TestBaseDeDatos(unittest.TestCase):

    def test_ingresar_citas(self):

        nombre1 = "Juan"
        correo1 = "jq@gmail.com"
        fecha1 = datetime.datetime(2027,12,25,18,25)
        rut1 = "12345678-1"
        motivo1 = "control"

        nombre2 = "Pedro"
        correo2 = "pg@gmail.com"
        fecha2 = datetime.datetime(2022,9,1,12,35)
        rut2 = "12345678-2"
        motivo2 = "resfrio"

        nombre3 = "Maria"
        correo3 = "maria_3223@yahoo.net"
        fecha3 = datetime.datetime(2021,9,1,12)
        rut3 = "12345678-3"
        motivo3 = "infeccion"
        medico = 2

        ingresar_cita(medico, rut1, fecha1, motivo1)
        ingresar_cita(medico, rut2, fecha2,  motivo2)
        ingresar_cita(medico, rut3, fecha3, motivo3)

    
        conn = sqlite3.connect("./centro_medico.db")
        cursor = conn.cursor()

        info = cursor.execute("SELECT * FROM citas").fetchall()
        
        for item in info:
            print(item)

    def test_modificar_citas(self):
        print("--------------------")

        rut1 = "12345678-1"
        fecha1 = datetime.datetime(2027,12,25,18, 25)
        fecha1nueva = datetime.datetime(2024,9,1,12,45)

        rut2 = "12345678-2"
        fecha2 = datetime.datetime(2022,9,1,12,35)
        fecha2nueva = datetime.datetime(2025,10,5,22)

        medico = 2
        
        modificar_cita(medico, rut1, fecha1, fecha1nueva, None)
        modificar_cita(medico, rut2, fecha2, fecha2nueva, "no quiero ir al certamen")

        conn = sqlite3.connect("./centro_medico.db")
        cursor = conn.cursor()
        
        info = cursor.execute("SELECT * FROM citas WHERE usuario_rut = ? OR usuario_rut = ?", (123456781, 123456782)).fetchall()
       
        for item in info:
            print(item)

        conn.close()
        assert(info[0][2] == "2024-09-01 12:45:00")
        assert(info[1][2] == "2025-10-05 22:00:00")

        assert(info[0][1] == 2)
        assert(info[1][1] == 2)

        assert(info[0][3] == "control")
        assert(info[1][3] == "no quiero ir al certamen")


if __name__ == '__main__':
    unittest.main()
