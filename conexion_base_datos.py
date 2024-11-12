import re
import sqlite3

# Funcion para crear la base de datos
# Crea las tablas: citas, usuarios y medicos
def crear_base_de_datos():
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()

    # tabla citas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS citas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        medico INTERGER NOT NULL,
        usuario_rut TEXT NOT NULL,
        fecha TEXT NOT NULL,
        motivo TEXT,
        estado TEXT NOT NULL
    )
    ''')

    # tabla usuarios
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        rut INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        correo TEXT,
        edad INTERGER NOT NULL,
        numero_telefonico INTERGER NOT NULL
    )
    ''')

    # tabla medicos
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

    # tabla agendas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS agendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        medico TEXT NOT NULL,
        fecha DATETIME NOT NULL
    )
    ''')

    conn.commit()
    conn.close()


# Funcion para ingresar una cita a la tabla citas
# @param medico Id del medico
# @param usuario_rut Rut del usuario
# @param fecha Fecha de la cita
# @param motivo Motivo de la cita

def ingresar_cita(id_medico, usuario_rut, fecha, motivo):
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()

    rut_num = re.sub('[^0-9]','', usuario_rut) # elimina caracteres no numericos
    fecha_str = str(fecha) 
    
    cursor.execute("INSERT INTO citas VALUES(NULL, ?, ?, ?, ?, ?)", (id_medico, rut_num, fecha_str, motivo, "false"))

    conn.commit()
    conn.close()

# Funcion para ingresar un usuario a la tabla usuarios
# @param id Id del usuario
# @param nombre Nombre del usuario
# @param email Email del usuario
# @param numero_telefonico Numero telefonico del usuario
def ingresar_usuario(rut, nombre, email, numero_telefonico):
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()
    rut_num = re.sub('[^0-9]','', rut)
    cursor.execute("INSERT INTO usuarios VALUES(?, ?, ?)", (rut_num, nombre, email, numero_telefonico))
    conn.commit()
    conn.close()

def ingresar_medico(rut, nombre, sexo, correo, especialidad, descripcion, estudios, ciudad):
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO medicos VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)", (rut, nombre, sexo, correo, especialidad, descripcion, estudios, ciudad))
    conn.commit()
    conn.close()

def ingresar_hora_agenda(medico, fecha):
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO agendas VALUES(NULL, ?, ?)", (medico, fecha))
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

# revisar
def eliminar_cita(medico, usuario_rut, fecha):
    pass

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

crear_base_de_datos()
# resetear_base_de_datos()