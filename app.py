from flask import Flask, redirect, render_template, request, url_for
from funciones import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST']) # GET is not secure, POST is secure
def login():

    if request.method == 'POST':
        name = request.form['name-input']
        email = request.form['email-input']

        escribir_a_archivo(name, email, datetime.datetime.now())
        
        return redirect(url_for('user', usr=name))
    else:
        return render_template('login.html')

@app.route('/<usr>')
def user(usr):
    return f'<h1>{usr}</h1>'

if __name__ == '__main__':
    app.run(debug=True)