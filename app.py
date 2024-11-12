from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

doctors = [
    {"name": "Dr. Ana Gonzalez", "specialty": "Cardiología"},
    {"name": "Dr. Juan Perez", "specialty": "Pediatría"},
    {"name": "Dr. Maria Lopez", "specialty": "Neurología"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reserva')
def reserva():
    doctor_name = request.args.get('doctor', 'Médico no seleccionado')
    return render_template('reservar.html', doctor=doctor_name)

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    query = request.args.get('q', '').lower()
    specialty = request.args.get('specialty', '').lower()

    suggestions = [
        {"name": doctor["name"], "specialty": doctor["specialty"]}
        for doctor in doctors
        if query in doctor["name"].lower() and (specialty == '' or specialty in doctor["specialty"].lower())
    ]
    
    return jsonify(suggestions)

if __name__ == '__main__':
    app.run(debug=True)
