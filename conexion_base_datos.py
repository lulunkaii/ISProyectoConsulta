import re
import sqlite3

# Función para crear la base de datos
def crear_base_de_datos():
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()

    # Crear tabla citas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS citas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        medico INTEGER NOT NULL,
        usuario_rut TEXT NOT NULL,
        fecha TEXT NOT NULL,
        motivo TEXT,
        estado TEXT NOT NULL
    )
    ''')

    # Crear tabla usuarios
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        rut INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        correo TEXT,
        edad INTEGER NOT NULL,
        numero_telefonico INTEGER NOT NULL
    )
    ''')

    # Crear tabla medicos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS medicos (
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

    # Crear tabla agendas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS agendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        medico_id INTEGER NOT NULL,
        fecha TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

# Función para ingresar una cita a la tabla citas
def ingresar_cita(id_medico, usuario_rut, fecha, motivo):
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()

    rut_num = re.sub('[^0-9]', '', usuario_rut)  # Elimina caracteres no numéricos
    fecha_str = str(fecha)

    cursor.execute("INSERT INTO citas (medico, usuario_rut, fecha, motivo, estado) VALUES (?, ?, ?, ?, ?)", 
                   (id_medico, rut_num, fecha_str, motivo, "false"))

    conn.commit()
    conn.close()

# Función para obtener datos de la base de datos
def fetch_data_from_db(table_name):
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()
    data = cursor.execute(f"SELECT * FROM {table_name}").fetchall()
    conn.close()
    return data

# Funcion para ingresar un usuario a la tabla usuarios
# @param id Id del usuario
# @param nombre Nombre del usuario
# @param email Email del usuario
# @param numero_telefonico Numero telefonico del usuario
def ingresar_usuario(rut, nombre, email, edad,numero_telefonico):
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()
    rut_num = re.sub('[^0-9]','', rut)
    cursor.execute("INSERT INTO usuarios VALUES(?, ?, ?, ?, ?)", (rut_num, nombre, email, edad, numero_telefonico))
    conn.commit()
    conn.close()

def ingresar_medico(rut, nombre, sexo, correo, especialidad, descripcion, estudios, ciudad):

    rut_num = int(re.sub('[^0-9]','', rut))

    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO medicos VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?)", (rut_num, nombre, sexo, correo, especialidad, descripcion, estudios, ciudad))
    conn.commit()

    lista = cursor.execute("SELECT * FROM medicos").fetchall()

    conn.close()

def ingresar_hora_agenda(medico_id, fecha):
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()

    fecha = str(fecha)

    cursor.execute("INSERT INTO agendas VALUES(NULL, ?, ?)", (medico_id, fecha))
    conn.commit()
    conn.close()

def modificar_cita(medico, usuario_rut, fecha_antigua, fecha_nueva, motivo_nuevo):
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()

    rut_num = re.sub('[^0-9]','', usuario_rut)
    cita_id = cursor.execute("SELECT id FROM citas WHERE usuario_rut = ? AND medico = ? AND fecha = ?", (rut_num, medico, fecha_antigua)).fetchone()

    fecha_antigua = str(fecha_antigua)
    fecha_nueva_str = str(fecha_nueva) 
   
    if motivo_nuevo != None:
        cursor.execute("UPDATE citas SET fecha = ?, motivo = ? WHERE id = ?", (fecha_nueva, motivo_nuevo, cita_id[0]))

    else: 
        cursor.execute("UPDATE citas SET fecha = ? WHERE id = ?", (fecha_nueva_str, int(cita_id[0])))

    conn.commit()
    conn.close()

# revisar
def modificar_usuario(rut, nombre, correo, edad, numero_telefonico):
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE usuarios SET nombre = ?, correo = ?, edad = ?, numero_telefonico = ? WHERE rut = ?", (nombre, correo, edad, numero_telefonico, rut))
    conn.commit()
    conn.close()

# revisar
def modificar_medico(rut, nombre, sexo, correo, especialidad, descripcion, estudios, ciudad):
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()

    id_medico = cursor.execute("SELECT id FROM medicos WHERE rut = ?", rut).fetchone()

    cursor.execute("UPDATE medicos SET rut = ?, nombre = ?, sexo = ?, correo = ?, especialidad = ?, descripcion = ?, estudios = ?, ciudad = ? WHERE id = ?", (rut, nombre, sexo, correo, especialidad, descripcion, estudios, ciudad, id_medico))
    conn.commit()
    conn.close()

# Por verificar
def eliminar_cita(medico, usuario_rut, fecha):
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()

    rut_num = re.sub('[^0-9]','', usuario_rut)
    cursor.execute("DELETE FROM citas WHERE usuario_rut = ? AND medico = ? AND fecha = ?", (rut_num, medico, fecha))
    conn.commit()
    conn.close()

def eliminar_usuario(rut):
    pass

def eliminar_medico(id):
    pass

def resetear_base_de_datos():
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS citas")
    cursor.execute("DROP TABLE IF EXISTS medicos")
    cursor.execute("DROP TABLE IF EXISTS agendas")
    cursor.execute("DROP TABLE IF EXISTS usuarios")
    conn.commit()
    conn.close()


def imprimir_base_de_datos():

    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()

    print("Tabla citas")
    print(cursor.execute("SELECT * FROM citas").fetchall())
    print("Tabla medicos")
    print(cursor.execute("SELECT * FROM medicos").fetchall())
    print("Tabla agendas")
    print(cursor.execute("SELECT * FROM agendas").fetchall())
    print("Tabla usuarios")
    print(cursor.execute("SELECT * FROM usuarios").fetchall())

    conn.close()