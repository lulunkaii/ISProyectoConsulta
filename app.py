from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
from html_interface import CentroMedicoInterface
from conexion_base_datos import ingresar_cita

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

if __name__ == '__main__':
    app.run(debug=True)