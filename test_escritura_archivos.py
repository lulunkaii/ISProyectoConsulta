import datetime
import os
import unittest



# importing
from funciones_escritura import escribir_a_archivo



class TestEscrituraArchivos(unittest.TestCase):

    # ADVERTENCIA correr esta funcion borrara el contenido de archivo log.txt, /00001/citas.csv
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
        
        with open(f"./src/base_de_datos/medicos/{medico}/citas.csv", "w") as file:
            file.write("") # limpiar archivo

        escribir_a_archivo(medico, nombre1, correo1, fecha1, rut1, motivo1)
        escribir_a_archivo(medico, nombre2, correo2, fecha2, rut2, motivo2)
        escribir_a_archivo(medico, nombre3, correo3, fecha3, rut3, motivo3)

        with open(f"./src/base_de_datos/medicos/{medico}/citas.csv", "r") as file:
            lines = file.readlines()

        
            self.assertEqual(lines[0], f"{fecha1.strftime('%Y-%m-%d %H:%M')};{nombre1};{correo1};{rut1};{motivo1};False\n") # juan
            self.assertEqual(lines[1], f"{fecha3.strftime('%Y-%m-%d %H:%M')};{nombre3};{correo3};{rut3};{motivo3};False\n") # maria
            self.assertEqual(lines[2], f"{fecha2.strftime('%Y-%m-%d %H:%M')};{nombre2};{correo2};{rut2};{motivo2};False\n") # pedro   


    # ADVERTENCIA correr esta funcion borrara el contenido de los archivos log.txt, /00002/citas.csv
    def test_formato_incorrecto(self):

        
        nombre1 = "Pablo"
        correo1 = "juan_pablo@udec.cl"
        fecha1 = datetime.datetime(2020,9,1,12,22)
        rut1 = "1234.78-1"
        motivo1 = "control"
        medico1 = "00002"

        nombre2 = "Oscar"
        correo2 = "oscar@udec.cl"
        fecha2 = "2022-09-01"
        rut2 = "12345678-2"
        motivo2 = "resfrio"
        medico2 = "00002"

        nombre3 = "Javiera"
        correo3 = "javiera-ddd@yahoo.net"
        fecha3 = datetime.datetime(2021,9,1,12)
        rut3 = "12345678-3"
        motivo3 = "infeccion"
        medico3 = "00003"

        for medico in [medico1, medico2, medico3]:

            if os.path.exists(f"./src/base_de_datos/medicos/{medico}/citas.csv"):
                with open(f"./src/base_de_datos/medicos/{medico}/citas.csv", "w") as file:
                    file.write("")

       
        with open(f"./src/log.txt", "w") as file:
            file.write("")
        
        escribir_a_archivo(medico1, nombre1, correo1, fecha1, rut1, motivo1)
        escribir_a_archivo(medico2, nombre2, correo2, fecha2, rut2, motivo2)
        escribir_a_archivo(medico3, nombre3, correo3, fecha3, rut3, motivo3)

        
        with open(f"./src/log.txt", "r") as file:
            lines = file.readlines()

            error_lines = list(map(lambda x: x.split("> ")[1], lines))
            self.assertEqual(error_lines[0], 'Error. Formato de rut incorrecto.\n')
            self.assertEqual(error_lines[1], 'Error. Formato de fecha incorrecto.\n')
            self.assertEqual(error_lines[2], 'Error. La ID de medico no existe.\n')

        


if __name__ == '__main__':
    unittest.main()
