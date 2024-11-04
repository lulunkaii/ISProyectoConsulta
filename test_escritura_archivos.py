import datetime
import unittest



# importing
from funciones import escribir_a_archivo



class TestEscrituraArchivos(unittest.TestCase):

    def test_escribir_a_archivo(self):
        nombre1 = "Juan"
        correo1 = "jp@udec.cl"
        fecha1 = datetime.datetime(2020,9,1,12)

        nombre2 = "Pedro"
        correo2 = "pg@udec.cl"
        fecha2 = datetime.datetime(2022,9,1,12,35)

        nombre3 = "Maria"
        correo3 = "maria_3223@yahoo.net"
        fecha3 = datetime.datetime(2021,9,1,12)
     

        escribir_a_archivo(nombre1, correo1, fecha1)
        escribir_a_archivo(nombre3, correo3, fecha3)
        escribir_a_archivo(nombre2, correo2, fecha2)

        with open("usuarios.csv", "r") as file:
            lines = file.readlines()
            self.assertEqual(lines[0], f"{fecha1.strftime('%Y-%m-%d %H:%M')};{nombre1};{correo1}\n") # juan
            self.assertEqual(lines[1], f"{fecha3.strftime('%Y-%m-%d %H:%M')};{nombre3};{correo3}\n") # maria
            self.assertEqual(lines[2], f"{fecha2.strftime('%Y-%m-%d %H:%M')};{nombre2};{correo2}\n") # pedro

if __name__ == '__main__':
    unittest.main()
