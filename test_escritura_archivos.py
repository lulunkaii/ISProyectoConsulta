import datetime
import unittest



# importing
from funciones_escritura import escribir_a_archivo



class TestEscrituraArchivos(unittest.TestCase):

    def test_escribir_a_archivo(self):


        nombre1 = "Juan"
        correo1 = "jp@udec.cl"
        fecha1 = datetime.datetime(2020,9,1,12)
        rut1 = "12345678-1"
        motivo1 = "control"

        nombre2 = "Pedro"
        correo2 = "pg@udec.cl"
        fecha2 = datetime.datetime(2022,9,1,12,35)
        rut2 = "12345678-2"
        motivo2 = "resfrio"

        nombre3 = "Maria"
        correo3 = "maria_3223@yahoo.net"
        fecha3 = datetime.datetime(2021,9,1,12)
        rut3 = "12345678-3"
        motivo3 = "infeccion"

        medico = "00001"

        with open(f"./src/medicos/{medico}/citas.csv", "w") as file:
            file.write("") # limpiar archivo

        escribir_a_archivo(medico, nombre1, correo1, fecha1, rut1, motivo1)
        escribir_a_archivo(medico, nombre2, correo2, fecha2, rut2, motivo2)
        escribir_a_archivo(medico, nombre3, correo3, fecha3, rut3, motivo3)

        with open(f"./src/medicos/{medico}/citas.csv", "r") as file:
            lines = file.readlines()

        
            self.assertEqual(lines[0], f"{fecha1.strftime('%Y-%m-%d %H:%M')};{nombre1};{correo1};{rut1};{motivo1}\n") # juan
            self.assertEqual(lines[1], f"{fecha3.strftime('%Y-%m-%d %H:%M')};{nombre3};{correo3};{rut3};{motivo3}\n") # maria
            self.assertEqual(lines[2], f"{fecha2.strftime('%Y-%m-%d %H:%M')};{nombre2};{correo2};{rut2};{motivo2}\n") # pedro   



if __name__ == '__main__':
    unittest.main()
