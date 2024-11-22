from conexion_base_datos import (
    crear_base_de_datos,
    fetch_data_from_db,
)

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