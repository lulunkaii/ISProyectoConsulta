import sqlite3

def crear_base_de_datos():
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS citas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        medico TEXT NOT NULL,
        usuario_rut TEXT NOT NULL,
        fecha TEXT NOT NULL,
        motivo TEXT,
        estado TEXT NOT NULL
    )
    ''')

    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS TABLE 
        usuarios (
        rut INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        correo TEXT,
        edad INTERGER NOT NULL,
        numero_telefonico INTERGER NOT NULL
    )
    ''')

    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS TABLE 
        medicos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rut INTEGER NOT NULL,       
        nombre TEXT NOT NULL,
        sexo TEXT,
        correo TEXT,
        especialidad TEXT NOT NULL
        descripcion TEXT,   
        estudios TEXT,
        ciudad TEXT,  
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS TABLE 
        agendas (
        medico TEXT NOT NULL,
        fecha DATETIME NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

def ingresar_cita(medico, usuario, fecha, motivo):
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO citas VALUES(?, ?, ?, ?, ?)", id, medico, usuario, fecha, motivo, "false")
    conn.commit()
    conn.close()

def ingresar_usuario(id, nombre, email, numero_telefonico):
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO usuarios VALUES(?, ?, ?)", id, nombre, email, numero_telefonico)
    conn.commit()
    conn.close()

def ingresar_medico(id, rut, nombre, sexo, correo, especialidad, descripcion, estudios, ciudad):
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()


    cursor.execute("INSERT INTO medicos VALUES(?, ?, ?, ?, ?, ?, ?, ?)", id, rut, nombre, sexo, correo, especialidad, descripcion, estudios, ciudad)
    conn.commit()
    conn.close()

def ingresar_hora_agenda(medico, fecha):
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO agendas VALUES(?, ?)", medico, fecha)
    conn.commit()
    conn.close()

def modificar_cita(medico, usuario_rut, fecha_antigua, fecha_nueva):
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()

    cita_id = cursor.execute("SELECT id FROM citas WHERE usuario_rut = ?, medico = ?, fecha = ?", usuario_rut, medico, fecha_antigua).fetchone()
    cursor.execute("UPDATE citas SET fecha = ? WHERE id = ?", fecha_nueva, cita_id[0])
    conn.commit()
    conn.close()

# revisar
def modificar_usuario(rut, nombre, correo, edad, numero_telefonico):
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE usuarios SET nombre = ?, correo = ?, edad = ?, numero_telefonico = ? WHERE rut = ?", nombre, correo, edad, numero_telefonico, rut)
    conn.commit()
    conn.close()

# revisar
def modificar_medico(id, rut, nombre, sexo, correo, especialidad, descripcion, estudios, ciudad):
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE medicos SET rut = ?, nombre = ?, sexo = ?, correo = ?, especialidad = ?, descripcion = ?, estudios = ?, ciudad = ? WHERE id = ?", rut, nombre, sexo, correo, especialidad, descripcion, estudios, ciudad, id)
    conn.commit()
    conn.close()

# revisar
def eliminar_cita(medico, usuario_rut, fecha):
    pass

def eliminar_usuario(rut):
    pass

def eliminar_medico(id):
    pass
