import sqlite3
import re

'''
Funciones para poder leer datos de un médico 
'''
def get_medico_id(id):
    '''
    Devuelve un médico (todos sus datos) según su id
    '''
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicos WHERE id = ?", (id,))
    medico = cursor.fetchone()
    conn.close()
    return medico

def get_dato_medico_id(id, dato):
    '''
    Devuelve un dato específico de un médico según su id. Los datos válidos son: id, rut, nombre,
    sexo, correo, especialidad, descripcion, estudios, ciudad
    '''
    valid_datos = ['id', 'rut', 'nombre', 'sexo', 'correo', 'especialidad', 'descripcion', 'estudios', 'ciudad']
    
    if dato not in valid_datos:
        return {"error": "Dato no válido"}

    try:
        conn = sqlite3.connect('centro_medico.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT {dato} FROM medicos WHERE id = ?", (id,))
        medico = cursor.fetchone()
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

def get_medicos_rut(rut):
    '''
    Devuelve un médico según su rut. Evite usar esta función, ya que el rut no es un identificador único
    '''
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicos WHERE rut = ?", (rut,))
    medico = cursor.fetchone()
    conn.close()
    return medico

def get_medicos_nombre(nombre):
    '''
    Devuelve un médico según su nombre. Considere que esto puede devolver más de un médico
    '''
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicos WHERE nombre = ?", (nombre,))
    medico = cursor.fetchone()
    conn.close()
    return medico

def get_medicos_especialidad(especialidad):
    '''
    Devuelve todos los médicos según su especialidad
    '''
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicos WHERE especialidad = ?", (especialidad,))
    medicos = cursor.fetchall()
    conn.close()
    return medicos

def get_medicos_ciudad(ciudad):
    '''
    Devuelve todos los médicos según su ciudad
    '''
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicos WHERE ciudad = ?", (ciudad,))
    medicos = cursor.fetchall()
    conn.close()
    return medicos

def get_medicos_sexo(sexo):
    '''
    Devuelve todos los médicos según su sexo
    '''
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicos WHERE sexo = ?", (sexo,))
    medicos = cursor.fetchall()
    conn.close()
    return medicos

