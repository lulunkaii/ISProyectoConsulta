
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from datetime import datetime, timedelta
from html_interface import CentroMedicoInterface
from conexion_base_datos import ingresar_cita


app = Flask(__name__) # Crear la aplicación Flask
# CORS(app, resources={r"/*": {"origins": "*"}}) # Permitir CORS (Reemplazar con la URL de la aplicación web)
CORS(app)

centro_medico = CentroMedicoInterface()


# Simulación de datos de doctores
@app.route('/')
def home():
    return render_template('main_page.html')

@app.route('/buscar', methods=['GET','POST']) # Endpoint para buscar doctores
def index():
    return render_template('buscador.html')


# Ruta para obtener los filtros disponibles (especialidad, área, convenio)
@app.route('/get_filters', methods=['GET'])
def get_filters():
    # Conectar a la base de datos
    filtros = centro_medico.obtener_campos_filtros() # Obtener los campos de filtro
    return jsonify(filtros) # Devolver los campos de filtro

# Por verificar
@app.route('/obtener_medicos', methods=['GET']) # Endpoint para obtener la lista de médicos
def obtener_medicos():
     # Obtener parámetros de la solicitud GET
    especialidad = request.args.get('especialidad')
    area = request.args.get('area')
    convenio = request.args.get('convenio')
    name = request.args.get('nombre')

    medicos = centro_medico.obtener_medicos(especialidad, area, convenio, name) # Obtener la lista de médicos

    print(medicos)
    return jsonify(medicos) # Devolver la lista de médicos

@app.route('/buscar_medico', methods=['POST']) # Endpoint para obtener la página de reserva
def buscar_medico():
    return jsonify({'status': 'success'}), 200

# @app.route('/reserva?medico=<int:doctor_id>', methods=['GET']) # Endpoint para obtener un doctor específico

@app.route('/reserva', methods=['GET']) # Endpoint para obtener un doctor específico
def agenda_medico():
    # id_medico = request.args.get('id_medico') # Obtener id de medico
    # doctor = centro_medico.obtener_doctor_por_id(id_medico) # Obtener el doctor por id
    

    # if id_medico is None:
        # return jsonify({'error': 'ID inválido'}), 400
    # return jsonify({'error': 'ID inválido'}), 400
  
    return render_template("medico.html") # Renderizar la plantilla de doctor


@app.route('/reserva/mes', methods=['GET']) #  Endpoint para obtener el calendario mensual
def calendario_mensual():
    return render_template("monthly_calendar.html")

@app.route('/reserva/semana', methods=['GET']) # Endpoint para obtener el calendario semanal   
def calendario_semanal():
    return render_template("weekly_calendar.html")


@app.route('/reserva/rellenar-datos', methods=['GET']) # Endpoint para obtener el calendario diario
def rellenar_datos():
    return render_template("form.html")

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


@app.errorhandler(404)
def not_found(error):
    return jsonify({'status': 'error', 'message': 'Ruta no encontrada'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'status': 'error', 'message': 'Error interno del servidor'}), 500




if __name__ == '__main__':
    app.run(debug=True)