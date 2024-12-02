import sqlite3
from conexion_base_datos import (
    crear_base_de_datos
)
from lectura.lectura_medico import *

# Clase que implementa la interfaz de la aplicación web
class CentroMedicoInterface:
    def __init__(self):
        # Crear la base de datos si no existe
        crear_base_de_datos()
        
    def obtener_horas_agendadas(self):
        # Obtener todas las citas desde la base de datos y formatearlas
        citas = fetch_data_from_db("citas")
        horas_agendadas = []
        
        for row in citas:
            try:
                fecha = row[3] # La fecha está en la cuarta columna
                fecha_part = fecha.split("T")[0] # Separar la fecha de la hora
                hora_part = int(fecha.split("T")[1].split(":")[0]) # Obtener la hora
                horas_agendadas.append({"fecha": fecha_part, "hora": hora_part}) # Agregar a la lista
            except (IndexError, ValueError) as e: # Manejar errores de formato
                print(f"Error al procesar la fecha '{fecha}': {e}")
        
        # Devolver la lista de diccionarios directamente
        return horas_agendadas

    # Por verificar
    def obtener_agenda_medico(self, id_medico):
        # Obtener la agenda del médico desde la base de datos y formatearla
        agenda = fetch_data_from_db("agendas")
        agenda_medico = []
        
        for row in agenda:
            try:
                if row[0] == id_medico: # Comprobar si el ID del médico coincide
                    fecha = row[1] # La fecha está en la segunda columna
                    fecha_part = fecha.split("T")[0] # Separar la fecha de la hora
                    hora_part = int(fecha.split("T")[1].split(":")[0]) # Obtener la hora
                    agenda_medico.append({"fecha": fecha_part, "hora": hora_part}) # Agregar a la lista
            except (IndexError, ValueError) as e: # Manejar errores de formato
                print(f"Error al procesar la fecha '{fecha}': {e}")

        # Devolver la lista de diccionarios directamente
        return agenda_medico
    
    def obtener_campos_filtros(self):
        conn = sqlite3.connect('centro_medico.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Obtener especialidades, áreas y convenios disponibles
        cursor.execute('SELECT DISTINCT especialidad FROM medicos')
        especialidades = cursor.fetchall()
        
        cursor.execute('SELECT DISTINCT ciudad FROM medicos')
        areas = cursor.fetchall()
        
        # cursor.execute('SELECT DISTINCT convenio FROM medicos')
        # convenios = cursor.fetchall()

        convenios = [{"convenio":'Fonasa'}, {"convenio":'Isapre'}, {"convenio":'Particular'}]
        
        conn.close()

        # Retornar los filtros como un diccionario
        filtros = {
            'especialidades': [row['especialidad'] for row in especialidades],
            'areas': [row['ciudad'] for row in areas],
            'convenios': [row['convenio'] for row in convenios]
        }
        return filtros

    
    # Por verificar
    def obtener_medicos(self, especialidad, area, convenio, nombre):

        # Obtener la lista de médicos desde la base de datos y formatearla
        medicos = get_medico_multiples_filtros(especialidad, area, convenio, nombre)
        medicos_list = []
        
        for row in medicos:
            try:
                id_medico = row[0]
                rut = row[1]
                nombre = row[2]
                sexo = row[3]
                correo = row[4]
                especialidad = row[5]
                descripcion = row[6]
                estudios = row[7]
                ciudad = row[8]
                telefono = row[9]

                # Agregar a la lista de médicos
                medicos_list.append({
                    "id": id_medico, 
                    "rut": rut, 
                    "nombre": nombre, 
                    "sexo": sexo, 
                    "correo": correo, 
                    "especialidad": especialidad, 
                    "descripcion": descripcion, 
                    "estudios": estudios, 
                    "ciudad": ciudad, 
                    "telefono": telefono
                    }) 
                
            except (IndexError, ValueError) as e: # Manejar errores de formato
                print(f"Error al procesar el médico '{row}': {e}")
        
        # Devolver la lista de diccionarios directamente
        return medicos_list