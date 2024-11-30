import unittest
import sqlite3
from lectura_medico import *

class TestLecturaMedico(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Crear una base de datos en memoria local para pruebas
        cls.conn = sqlite3.connect(':memory:')
        cls.cursor = cls.conn.cursor()
        cls.cursor.execute('''
            CREATE TABLE medicos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rut INTEGER NOT NULL,
                nombre TEXT NOT NULL,
                sexo TEXT,
                correo TEXT,
                especialidad TEXT NOT NULL,
                descripcion TEXT,
                estudios TEXT,
                ciudad TEXT
            )
        ''')
        # Insertar datos de prueba
        cls.cursor.execute('''
            INSERT INTO medicos (rut, nombre, sexo, correo, especialidad, descripcion, estudios, ciudad)
            VALUES (12345678, 'Dr. Juan Perez', 'M', 'juan.perez@example.com', 'Cardiología', 'Especialista en cardiología', 'Universidad X', 'Ciudad Y')
        ''')
        cls.cursor.execute('''
            INSERT INTO medicos (rut, nombre, sexo, correo, especialidad, descripcion, estudios, ciudad)
            VALUES (87654321, 'Dra. Maria Lopez', 'F', 'maria.lopez@example.com', 'Pediatría', 'Especialista en pediatría', 'Universidad Y', 'Ciudad Y')
        ''')
        cls.conn.commit()

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()

    def test_get_medico_id(self):
        medico = get_medico_id(1, conn=self.conn)
        self.assertIsNotNone(medico)
        self.assertEqual(medico[1], 12345678)
        self.assertEqual(medico[2], 'Dr. Juan Perez')

    def test_get_dato_medico_id(self):
        nombre = get_dato_medico_id(1, 'nombre', conn=self.conn)
        self.assertEqual(nombre['nombre'], 'Dr. Juan Perez')

        correo = get_dato_medico_id(1, 'correo', conn=self.conn)
        self.assertEqual(correo['correo'], 'juan.perez@example.com')

        error = get_dato_medico_id(1, 'dato_invalido', conn=self.conn)
        self.assertEqual(error['error'], 'Dato no válido')
    
    def test_get_medicos_especialidad(self):
        medicos = get_medicos_especialidad('Cardiología', conn=self.conn)
        self.assertEqual(len(medicos), 1)
        self.assertEqual(medicos[0][2], 'Dr. Juan Perez')
    
    def test_get_medicos_ciudad(self):
        medicos = get_medicos_ciudad('Ciudad Y', conn=self.conn)
        self.assertEqual(len(medicos), 2)
        self.assertEqual(medicos[0][2], 'Dr. Juan Perez', 'Dra. Maria Lopez')

if __name__ == '__main__':
    unittest.main()