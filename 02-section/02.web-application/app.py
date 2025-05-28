from flask import Flask, render_template, request, redirect, url_for, session, flash
import requests
from functools import wraps

app = Flask(__name__)
app.secret_key = 'clave_temporal'  # Se usara el password cifrado del usuario despues

# Configuración del servicio web
HOST = "http://localhost:8000"  

# Decorador para verificar sesión
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            flash('Por favor inicie sesión primero', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@login_required
def index():
    return render_template('welcome.html', user=session['user'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = {
            "alias": request.form['alias'],
            "password": request.form['password']
        }
        
        try:
            response = requests.post(f"{HOST}/login", json=data)
            response_data = response.json()
            
            if response.status_code == 200 and response_data.get('code') == 0:
                # Actualizar la clave secreta con el password cifrado
                app.secret_key = response_data['data']['password']
                
                # Guardar datos del usuario en sesión
                session['logged_in'] = True
                session['user'] = response_data['data']
                return redirect(url_for('index'))
            else:
                error_msg = response_data.get('message', 'Credenciales incorrectas')
                flash(error_msg, 'danger')
        except Exception as e:
            flash(f"Error al conectar con el servicio: {str(e)}", 'danger')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Has cerrado sesión correctamente', 'info')
    return redirect(url_for('login'))

@app.route('/usuarios')
@login_required
def listar_usuarios():
    try:
        response = requests.get(f"{HOST}/usuarios")
        response_data = response.json()
        
        if response.status_code == 200 and response_data.get('code') == 0:
            usuarios = response_data['data']
        else:
            usuarios = []
            flash(response_data.get('message', 'Error al obtener usuarios'), 'danger')
    except Exception as e:
        usuarios = []
        flash(f"Error al conectar con el servicio: {str(e)}", 'danger')
    
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/registrar', methods=['GET', 'POST'])
@login_required
def registrar_usuario():
    if request.method == 'POST':
        data = {
            "nombre_completo": request.form['nombre_completo'],
            "alias": request.form['alias'],
            "password": request.form['password']
        }
        
        try:
            response = requests.post(f"{HOST}/usuarios", json=data)
            response_data = response.json()
            
            if response.status_code == 200 and response_data.get('code') == 0:
                flash('Usuario registrado exitosamente', 'success')
                return redirect(url_for('listar_usuarios'))
            else:
                error_msg = response_data.get('message', 'Error al registrar usuario')
                flash(error_msg, 'danger')
        except Exception as e:
            flash(f"Error al conectar con el servicio: {str(e)}", 'danger')
    
    return render_template('registrar.html')

if __name__ == '__main__':
    app.run(debug=True)