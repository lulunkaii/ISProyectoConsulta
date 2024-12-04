from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
from html_interface import CentroMedicoInterface
from conexion_base_datos import ingresar_cita, ingresar_hora_agenda, eliminar_cita, ingresar_medico, eliminar_hora_agenda

app = Flask(__name__) # Crear la aplicación Flask
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}}) # Permitir CORS (Reemplazar con la URL de la aplicación web)

centro_medico = CentroMedicoInterface()

@app.route('/obtener_horas_ocupadas', methods=['GET']) # Endpoint para obtener las horas ocupadas
def obtener_horas_ocupadas():
    fecha = request.args.get('fecha') # Obtener la fecha de la solicitud

    # Convertir la fecha solicitada a un objeto datetime
    fecha_datetime = datetime.strptime(fecha, '%Y-%m-%d')

    # Calcular el inicio y el fin de la semana
    start_of_week = fecha_datetime - timedelta(days=fecha_datetime.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    horas_ocupadas = centro_medico.obtener_horas_agendadas() # Obtener todas las horas ocupadas

    # Filtrar las horas ocupadas dentro del rango de la semana
    horas_filtradas = [hora for hora in horas_ocupadas if start_of_week <= datetime.strptime(hora['fecha'], '%Y-%m-%d') <= end_of_week]

    return jsonify(horas_filtradas) # Devolver las horas ocupadas en la semana

@app.route('/obtener_agenda_medico', methods=['GET']) # Endpoint para obtener la agenda de un médico
def obtener_agenda_medico():
    id_medico = request.args.get('id_medico') # Obtener el ID del médico de la solicitud
    fecha = request.args.get('fecha') # Obtener la fecha de la solicitud

    # Convertir la fecha solicitada a un objeto datetime
    fecha_datetime = datetime.strptime(fecha, '%Y-%m-%d')

    # Calcular el inicio y el fin de la semana
    start_of_week = fecha_datetime - timedelta(days=fecha_datetime.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    agenda_medico = centro_medico.obtener_agenda_medico(id_medico) # Obtener la agenda del médico

    # Filtrar las horas de la agenda dentro del rango de la semana
    agenda_filtrada = [hora for hora in agenda_medico if start_of_week <= datetime.strptime(hora['fecha'].split('T')[0], '%Y-%m-%d') <= end_of_week]

    return jsonify(agenda_filtrada) # Devolver la agenda del médico en la semana

# Por verificar
@app.route('/obtener_medicos', methods=['GET']) # Endpoint para obtener la lista de médicos
def obtener_medicos():
    medicos = centro_medico.obtener_medicos() # Obtener la lista de médicos

    return jsonify(medicos) # Devolver la lista de médicos

@app.route('/ingresar_cita', methods=['POST']) # Endpoint para ingresar una cita
def ingresar_cita_endpoint():
    try:
        data = request.get_json() # Obtener los datos de la solicitud
        id_medico = data['id_medico']
        usuario_rut = data['usuario_rut']
        fecha = data['fecha']
        motivo = data['motivo']
        
        # Llama a la función para ingresar la cita
        ingresar_cita(id_medico, usuario_rut, fecha, motivo)        
        return jsonify({'status': 'success'}), 200 # Devuelve un mensaje de éxito
    except Exception as e: # Manejar errores
        print("Error:", e)
        return jsonify({'status': 'error', 'message': str(e)}), 500
    
# Por verificar
@app.route('/cancelar_cita', methods=['POST']) # Endpoint para cancelar una cita
def cancelar_cita_endpoint():
    try:
        data = request.get_json() # Obtener los datos de la solicitud
        id_cita = data['id_cita']
        
        # Llama a la función para cancelar la cita
        eliminar_cita(id_cita)        
        return jsonify({'status': 'success'}), 200 # Devuelve un mensaje de éxito
    except Exception as e: # Manejar errores
        print("Error:", e)
        return jsonify({'status': 'error', 'message': str(e)}), 500
    
@app.route('/ingresar_agenda', methods=['POST']) # Endpoint para ingresar una agenda
def ingresar_agenda_endpoint():
    try:
        data = request.get_json() # Obtener los datos de la solicitud
        id_medico = data['id_medico']
        horas = data['horas']

        for fecha in horas:
            ingresar_hora_agenda(id_medico, fecha)

        return jsonify({'status': 'success'}), 200 # Devuelve un mensaje de éxito
    except Exception as e: # Manejar errores
        print("Error:", e)
        return jsonify({'status': 'error', 'message': str(e)}), 500
    
@app.route('/eliminar_hora_agenda', methods=['POST']) # Endpoint para eliminar una hora de la agenda
def eliminar_hora_agenda_endpoint():
    try:
        data = request.get_json() # Obtener los datos de la solicitud
        id_medico = data['id_medico']
        fecha = data['fecha']

        eliminar_hora_agenda(id_medico, fecha) # Llama a la función para eliminar la hora
        print(f"Hora {fecha} eliminada como disponible para el médico {id_medico}")

        return jsonify({'status': 'success'}), 200 # Devuelve un mensaje de éxito
    except Exception as e: # Manejar errores
        print("Error:", e)
        return jsonify({'status': 'error', 'message': str(e)}), 500
    
# Por verificar
@app.route('/ingresar_medico', methods=['POST']) # Endpoint para ingresar un médico
def ingresar_medico_endpoint():
    try:
        data = request.get_json() # Obtener los datos de la solicitud
        id = data['id']
        rut = data['rut']
        nombre = data['nombre']
        sexo = data['sexo']
        correo = data['correo']
        especialidad = data['especialidad']
        descripcion = data['descripcion']
        estudios = data['estudios']
        ciudad = data['ciudad']
        telefono = data['telefono']
        
        # Llama a la función para ingresar el médico
        ingresar_medico(id, rut, nombre, sexo, correo, especialidad, descripcion, estudios, ciudad, telefono)        
        return jsonify({'status': 'success'}), 200 # Devuelve un mensaje de éxito
    except Exception as e: # Manejar errores
        print("Error:", e)
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)