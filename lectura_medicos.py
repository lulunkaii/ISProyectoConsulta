import os
import datetime


# TODO
# Verificar si no se cambiará el formato de los archivos (primero las fechas) sino cambia el algoritmo
# Consultas adicionales 

'''
Funciones para poder leer datos de las citas de los médicos
'''

def leer_archivo(medico_ID):
    '''
    Lee un archivo de citas de un medico según su id
    '''
    path_archivo = f"./medicos/{medico_ID}/citas.csv"
    if not os.path.exists(path_archivo):
        return []
    with open(path_archivo, "r") as file:
        return file.readlines()


def get_citas_medico(medico_ID : int)-> list[str]:
    '''
    Devuelve todas las citas de un medico según su id
    '''
    return leer_archivo(medico_ID)

# Verificar si se usará esta función con la fecha y hora exactas
def get_cita_especifica(medico_ID : int, fecha_hora: datetime)-> str:
    '''
    Devuelve una cita en cierto dia y cierta hora de un medico en especifico (YYYY-MM-DD HH:MM)
    '''
    citas = leer_archivo(medico_ID)
    for cita in citas:
        if cita.startswith(fecha_hora):
            return cita
    return None

def get_citas_dia(medico_ID : int, fecha: str)-> list[str]:
    '''
    Devuelve todas las citas de un medico en especifico en un día en especifico (YYYY-MM-DD)
    '''
    citas = leer_archivo(medico_ID)
    citas_fecha = []
    for cita in citas:
        if cita.startswith(fecha):
            citas_fecha.append(cita)
    return citas_fecha

def get_citas_rut(medico_ID : int, rut: str)-> list[str]:
    '''
    Devuelve todas las citas de un medico en especifico de un paciente en especifico
    '''
    citas = leer_archivo(medico_ID)
    citas_rut = []
    for cita in citas:
        if cita.split(";")[3] == rut:
            citas_rut.append(cita)
    return citas_rut

# Pruebas
#print(get_citas_medico("00002"), end="\n")
#print(get_cita_especifica("00002", "2021-09-01 12:00"), end="\n")
#print(get_citas_dia("00002", "2021-09-01"))
#print(get_citas_rut("00002", "12345678-9"))
