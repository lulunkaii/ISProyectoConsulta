import sqlite3
import re

'''
Funciones para poder leer datos de un médico 
'''
def get_medico_id(id, conn=None):
    '''
    Devuelve un médico (todos sus datos) según su id
    '''
    if conn is None:
        conn = sqlite3.connect('centro_medico.db')
        close_conn = True
    else:
        close_conn = False

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicos WHERE id = ?", (id,))
    medico = cursor.fetchone()
    
    if close_conn:
        conn.close()
    return medico

def get_dato_medico_id(id, dato, conn=None):
    '''
    Devuelve un dato específico de un médico según su id.
    '''
    valid_datos = ['id', 'rut', 'nombre', 'sexo', 'correo', 'especialidad', 'descripcion', 'estudios', 'ciudad']
    
    if dato not in valid_datos:
        return {"error": "Dato no válido"}

    try:
        if conn is None:
            conn = sqlite3.connect('centro_medico.db')
            close_conn = True
        else:
            close_conn = False

        cursor = conn.cursor()
        cursor.execute(f"SELECT {dato} FROM medicos WHERE id = ?", (id,))
        medico = cursor.fetchone()
        
        if close_conn:
            conn.close()
        
        if medico:
            return {dato: medico[0]}
        else:
            return {"error": "Médico no encontrado"}
    except sqlite3.Error as e:
        return {"error": str(e)}


'''
Funciones para retornar todos los médicos según distintos criterios
'''

def get_medicos_rut(rut, conn=None):
    '''
    Devuelve un médico según su rut. Evite usar esta función, ya que el rut no es un identificador único
    a priori
    '''
    if conn is None:
        conn = sqlite3.connect('centro_medico.db')
        close_conn = True
    else:
        close_conn = False
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicos WHERE rut = ?", (rut,))
    medico = cursor.fetchone()

    if close_conn:
        conn.close()
    return medico

def get_medicos_nombre(nombre, conn=None):
    '''
    Devuelve un médico según su nombre. Considere que esto puede devolver más de un médico
    '''
    if conn is None:
        conn = sqlite3.connect('centro_medico.db')
        close_conn = True
    else:
        close_conn = False

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicos WHERE nombre = ?", (nombre,))
    medico = cursor.fetchone()

    if close_conn:
        conn.close()
    return medico

def get_medicos_especialidad(especialidad, conn=None):
    '''
    Devuelve todos los médicos según su especialidad
    '''
    if conn is None:
        conn = sqlite3.connect('centro_medico.db')
        close_conn = True
    else:
        close_conn = False
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicos WHERE especialidad = ?", (especialidad,))
    medicos = cursor.fetchall()

    if close_conn:
        conn.close()
    return medicos

def get_medicos_ciudad(ciudad, conn=None):
    '''
    Devuelve todos los médicos según su ciudad
    '''
    if conn is None:
        conn = sqlite3.connect('centro_medico.db')
        close_conn = True
    else:
        close_conn = False

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicos WHERE ciudad = ?", (ciudad,))
    medicos = cursor.fetchall()

    if close_conn:
        conn.close()
    return medicos

def get_medicos_sexo(sexo, conn=None):
    '''
    Devuelve todos los médicos según su sexo
    '''
    if conn is None:
        conn = sqlite3.connect('centro_medico.db')
        close_conn = True
    else:
        close_conn = False

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicos WHERE sexo = ?", (sexo,))
    medicos = cursor.fetchall()

    if close_conn:
        conn.close()
    return medicos

