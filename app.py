from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

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


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/doctors', methods=['GET'])
def get_doctors():
    specialty = request.args.get('specialty', '')
    
    if specialty:
        # Filtramos por especialidad si se proporciona
        filtered_doctors = [doctor for doctor in doctors if specialty.lower() in doctor['specialty'].lower()]
    else:
        # Si no se proporciona especialidad, devolvemos todos los doctores
        filtered_doctors = doctors
        
    return jsonify(filtered_doctors)



if __name__ == '__main__':
    app.run(debug=True)
