from flask import Flask, request, jsonify, render_template_string
import time

app = Flask(__name__)
correct_user = "admin"
correct_password = "supermariojavith"

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = data.get('user')
    password = data.get('password')
    time.sleep(0.1)  # Pequeña pausa para no saturar
    if user == correct_user and password == correct_password:
        return jsonify({"token": "QpwL5tke4Pnpja7X4QpwL5tke4Pnpja7X4"}), 200
    return jsonify({"status": "failed", "message": "Usuario o contraseña incorrectos"}), 401

@app.route('/', methods=['GET'])
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login Seguro</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-100 flex items-center justify-center h-screen">
        <div class="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
            <h1 class="text-2xl font-bold mb-6 text-center">Iniciar Sesión</h1>
            <div id="message" class="mb-4 text-center"></div>
            <form id="loginForm" class="space-y-4">
                <div>
                    <label for="user" class="block text-sm font-medium text-gray-700">Usuario</label>
                    <input type="text" id="user" name="user" class="mt-1 block w-full p-2 border border-gray-300 rounded-md" required>
                </div>
                <div>
                    <label for="password" class="block text-sm font-medium text-gray-700">Contraseña</label>
                    <input type="password" id="password" name="password" class="mt-1 block w-full p-2 border border-gray-300 rounded-md" required>
                </div>
                <button type="submit" class="w-full bg-blue-500 text-white p-2 rounded-md hover:bg-blue-600">Iniciar Sesión</button>
            </form>
        </div>
        <script>
            document.getElementById('loginForm').addEventListener('submit', async (e) => {
                e.preventDefault();
                const user = document.getElementById('user').value;
                const password = document.getElementById('password').value;
                const messageDiv = document.getElementById('message');
                
                try {
                    const response = await fetch('/login', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ user, password })
                    });
                    const data = await response.json();
                    
                    if (response.status === 200) {
                        messageDiv.innerHTML = `<p class="text-green-600">¡Login exitoso! Token: ${data.token}</p>`;
                    } else {
                        messageDiv.innerHTML = `<p class="text-red-600">${data.message}</p>`;
                    }
                } catch (error) {
                    messageDiv.innerHTML = '<p class="text-red-600">Error en la solicitud</p>';
                }
            });
        </script>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)