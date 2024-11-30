
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from datetime import datetime, timedelta
from html_interface import CentroMedicoInterface
from conexion_base_datos import ingresar_cita


app = Flask(__name__) # Crear la aplicación Flask
CORS(app, resources={r"/*": {"origins": "*"}}) # Permitir CORS (Reemplazar con la URL de la aplicación web)

centro_medico = CentroMedicoInterface()


# Simulación de datos de doctores
doctors = [
    {'id': 1, 'name': 'Dr. Juan Pérez', 'specialty': 'Cardiología'},
    {'id': 2, 'name': 'Dra. Ana Gómez', 'specialty': 'Pediatría'},
    {'id': 3, 'name': 'Dr. Luis Rodríguez', 'specialty': 'Neurología'},
    {'id': 4, 'name': 'Dr. Sergio Herrera', 'specialty': 'Dermatología'},
    {'id': 5, 'name': 'Dra. Carolina Díaz', 'specialty': 'Psiquiatría'},
    {'id': 6, 'name': 'Dr. Eduardo Sánchez', 'specialty': 'Oftalmología'},
    {'id': 7, 'name': 'Dra. Elena Martínez', 'specialty': 'Ginecología'},
    {'id': 8, 'name': 'Dr. Manuel Ramírez', 'specialty': 'Oncología'},
    {'id': 9, 'name': 'Dra. Isabel Pérez', 'specialty': 'Urología'},
    {'id': 10, 'name': 'Dr. Francisco López', 'specialty': 'Endocrinología'},
    {'id': 11, 'name': 'Dra. Lourdes Fernández', 'specialty': 'Reumatología'},
    {'id': 12, 'name': 'Dr. José Álvarez', 'specialty': 'Neumología'},
    {'id': 13, 'name': 'Dra. Marta Sánchez', 'specialty': 'Oftalmología'},
    {'id': 14, 'name': 'Dr. Carlos González', 'specialty': 'Traumatología'},
    {'id': 15, 'name': 'Dra. Laura Martín', 'specialty': 'Psicología'},
    {'id': 16, 'name': 'Dr. Enrique Torres', 'specialty': 'Cirugía General'},
    {'id': 17, 'name': 'Dra. Patricia López', 'specialty': 'Geriatría'},
    {'id': 18, 'name': 'Dr. Jorge Martínez', 'specialty': 'Inmunología'},
    {'id': 19, 'name': 'Dra. Claudia Morales', 'specialty': 'Pediatría'},
    {'id': 20, 'name': 'Dr. Javier Fernández', 'specialty': 'Neurocirugía'},
    {'id': 21, 'name': 'Dra. María José Martínez', 'specialty': 'Ginecología'},
    {'id': 22, 'name': 'Dr. Alfonso García', 'specialty': 'Dermatología'},
    {'id': 23, 'name': 'Dra. Sandra Ruiz', 'specialty': 'Cardiología'},
    {'id': 24, 'name': 'Dr. Luis Rodríguez', 'specialty': 'Cirugía Plástica'},
    {'id': 25, 'name': 'Dra. Teresa García', 'specialty': 'Odontología'},
]


@app.route('/buscar', methods=['GET', 'POST']) # Endpoint para buscar doctores
def index():
    return render_template('buscador.html')


@app.route('/doctors', methods=['GET', 'POST']) # Endpoint para obtener los doctores
def get_doctors():
    specialty = request.args.get('specialty', '')
    
    if specialty:
        # Filtramos por especialidad si se proporciona
        filtered_doctors = [doctor for doctor in doctors if specialty.lower() in doctor['specialty'].lower()]
    else:
        # Si no se proporciona especialidad, devolvemos todos los doctores
        filtered_doctors = doctors
        
    return jsonify(filtered_doctors)

# @app.route('/reserva?medico=<int:doctor_id>', methods=['GET']) # Endpoint para obtener un doctor específico
@app.route('/reserva?medico', methods=['GET']) # Endpoint para obtener un doctor específico
def doctor_calendar(doctor_id):
    id = request.args.get('id') # Obtener id de medico
    
    doctor = centro_medico.obtener_doctor_por_id(id) # Obtener el doctor por id
    if id is None:
        return jsonify({'error': 'ID inválido'}), 400
    else:
        return render_template("medico.html") # Renderizar la plantilla de doctor


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