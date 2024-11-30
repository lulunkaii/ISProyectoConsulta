import sqlite3
import re


# TODO
# Verificar si no se cambiará el formato de los archivos (primero las fechas) sino cambia el algoritmo
# Consultas adicionales 

'''
Funciones para poder leer datos de las citas de los médicos
'''

def get_citas_medico(medico_ID):
    '''
    Devuelve todas las citas de un medico según su id
    '''
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM citas WHERE medico = ?", (medico_ID,))
    citas = cursor.fetchall()
    conn.close()
    return citas


# Verificar si se usará esta función con la fecha y hora exactas
def get_cita_especifica(medico_ID, fecha):
    '''
    Devuelve una cita específica de un médico en una fecha específica
    '''
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM citas WHERE medico = ? AND fecha LIKE ?", (medico_ID, f"{fecha}%"))
    cita = cursor.fetchone()
    conn.close()
    return cita

def get_citas_dia(medico_ID, fecha):
    '''
    Devuelve todas las citas de un medico en especifico en un día en especifico (YYYY-MM-DD)
    '''
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM citas WHERE medico = ? AND fecha LIKE ?", (medico_ID, f"{fecha}%"))
    citas = cursor.fetchall()
    conn.close()
    return citas

def get_citas_rut(medico_ID, rut):
    '''
    Devuelve todas las citas de un medico en especifico de un paciente en especifico
    '''
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM citas WHERE medico = ? AND usuario_rut = ?", (medico_ID, rut))
    citas = cursor.fetchall()
    conn.close()
    return citas

def get_citas_estado(medico_ID, estado='confirmada'):
    '''
    Devuelve todas las citas de un medico en especifico con un estado en especifico,
    por defecto se buscan las citas confirmadas
    '''
    conn = sqlite3.connect('centro_medico.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM citas WHERE medico = ? AND estado = ?", (medico_ID, estado))
    citas = cursor.fetchall()
    conn.close()
    return citas

