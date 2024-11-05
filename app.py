from flask import Flask, redirect, render_template, request, url_for
from funciones_escritura import escribir_a_archivo
import datetime
app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

@app.route('/', methods=['GET', 'POST']) # GET is not secure, POST is secure

def login():

    if request.method == 'POST':
        
        name = request.form['name-input']
        email = request.form['email-input']
        rut = request.form['rut-input']
        fecha = request.form['date-input']
        motivo = request.form['motivo-input']

        fecha = fecha.split("-");
        fecha_cita = datetime.datetime(int(fecha[0]), int(fecha[1]), int(fecha[2]))

        medico_ID = "00001"
        escribir_a_archivo(medico_ID, name, email, fecha_cita, rut, motivo)
        
        return redirect(url_for('user', usr=name))
    else:
        return render_template('login.html')

@app.route('/<usr>')
def user(usr):
    return f'<h1>{usr}</h1>'

if __name__ == '__main__':
    app.run(debug=True)