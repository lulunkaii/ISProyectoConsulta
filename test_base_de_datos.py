import unittest
from conexion_base_datos import *
import datetime
import sqlite3

class TestBaseDeDatos(unittest.TestCase):

    
    def test_ingresar_citas(self):

        fecha1 = datetime.datetime(2027,12,25,18,25)
        rut1 = "12345678-1"
        motivo1 = "control"

        fecha2 = datetime.datetime(2022,9,1,12,35)
        rut2 = "12345678-2"
        motivo2 = "resfrio"

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
        
        assert(info[0][1] == 2)
        assert(info[0][2] == "123456781")
        assert(info[0][3] == "2027-12-25 18:25:00")
        assert(info[0][4] == "control")

        assert(info[1][1] == 2)
        assert(info[1][2] == "123456782")
        assert(info[1][3] == "2022-09-01 12:35:00")
        assert(info[1][4] == "resfrio")

        conn.close()

    def test_modificar_citas(self):

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

        assert(info[0][1] == 2)
        assert(info[1][1] == 2)

        assert(info[0][2] == "123456781")
        assert(info[1][2] == "123456782")

        assert(info[0][3] == "2024-09-01 12:45:00")
        assert(info[1][3] == "2025-10-05 22:00:00")

        assert(info[0][4] == "control")
        assert(info[1][4] == "no quiero ir al certamen")
        
        conn.close()

    def test_ingresar_usuario(self):
        rut1 = "12345678-1"
        nombre1 = "Juan"
        email1 = "jq@yahoo.com"
        edad1 = 58
        numero_telefonico1 = 8888888 

        ingresar_usuario(rut1, nombre1, email1, edad1, numero_telefonico1)

        conn = sqlite3.connect("./centro_medico.db")
        cursor = conn.cursor()

        info = cursor.execute("SELECT * FROM usuarios").fetchall()

        assert(info[0][0] == 123456781)
        assert(info[0][1] == "Juan")
        assert(info[0][2] == "jq@yahoo.com")
        assert(info[0][3] == 58)
        assert(info[0][4] == 8888888)

        conn.close()


    def test_ingresar_hora(self):
        medico = 2
        fecha = datetime.datetime(2021,9,1,12)

        medico2 = 1
        fecha2 = datetime.datetime(2021,9,1,12,30)

        ingresar_hora_agenda(medico, fecha)
        ingresar_hora_agenda(medico2, fecha2)

        conn = sqlite3.connect("./centro_medico.db")
        cursor = conn.cursor()

        info = cursor.execute("SELECT * FROM agendas").fetchall()

        assert(info[0][1] == 2)
        assert(info[0][2] == str(fecha))

        assert(info[1][1] == 1)
        assert(info[1][2] == str(fecha2))

        conn.close()
    
    def test_ingresar_medico(self):
        rut = "87654320-1"
        nombre = "Juan"
        sexo = "M"
        correo = "best_medico@icloud.com"
        especialidad = "cardiologia"
        descripcion = "cura corazones"
        estudios = "medicina en la chile"
        ciudad = "santiago"

        rut2 = "87654320-2"
        nombre2 = "Pedro P"
        sexo2 = "M"
        correo2 = None
        especialidad2 = "traumatologia"
        descripcion2 = "especialista en huesos"
        estudios2 = "medicina en la udec"
        ciudad2 = "concepcion"

        ingresar_medico(rut, nombre, sexo, correo, especialidad, descripcion, estudios, ciudad)

        ingresar_medico(rut2, nombre2, sexo2, correo2, especialidad2, descripcion2, estudios2, ciudad2)

        conn = sqlite3.connect("./centro_medico.db")
        cursor = conn.cursor()

        lista_medicos = cursor.execute("SELECT * FROM medicos").fetchall()

        assert(lista_medicos[0][1] == 876543201)
        assert(lista_medicos[0][2] == nombre)
        assert(lista_medicos[0][3] == sexo)
        assert(lista_medicos[0][4] == correo)
        assert(lista_medicos[0][5] == especialidad)
        assert(lista_medicos[0][6] == descripcion)
        assert(lista_medicos[0][7] == estudios)
        assert(lista_medicos[0][8] == ciudad)

        assert(lista_medicos[1][1] == 876543202)
        assert(lista_medicos[1][2] == nombre2)
        assert(lista_medicos[1][3] == sexo2)
        assert(lista_medicos[1][4] == correo2)
        assert(lista_medicos[1][5] == especialidad2)
        assert(lista_medicos[1][6] == descripcion2)
        assert(lista_medicos[1][7] == estudios2)
        assert(lista_medicos[1][8] == ciudad2)

        conn.close()     




if __name__ == '__main__':
    resetear_base_de_datos()
    crear_base_de_datos()
    unittest.main()

