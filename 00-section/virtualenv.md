## Manejo de Virtualenvs e Instalación de Paquetes en Python (Windows)

Los entornos virtuales permiten mantener tus proyectos Python organizados y libres de conflictos.

### 📌 1. Verificación 
revisar la instalación en la terminal (CMD o PowerShell):

```
python --version
pip --version
```

### 🔧 2. Instalación de virtualenv
Ejecuta en la terminal:

```
pip install virtualenv
```

### 🚀 3. Creación y Activación de Entornos Virtuales

**Crear un entorno virtual:**
Navega a la carpeta de tu proyecto 
```
cd C:\ruta\al\proyecto
```
una vez adentro ejecuta la creacion del entorno virtual,
usa el nombre **.venv** para el nombre del entorno (puede ser cualquier nombre)

```
virtualenv .venv
```
Activa el entorno

```
.\.venv\Scripts\activate
```

Desactiva el entorno

```
deactivate
```

### 📦 4. Instalación de Paquetes con pip

Instalar paquetes (con el entorno activado):
```
pip install numpy
pip install flask
pip install pillow
```

Listar paquetes instalados:
```
pip list
```

Guardar los paquetes instaldos en requirements.txt:
```
pip freeze > requirements.txt
```

Instalar múltiples paquetes (desde un archivo requirements.txt):
```
pip install -r requirements.txt
```
### 💡 5. Recomendaciones Avanzadas

#### Alternativa Nativa
De forma alternativa puedes usar este comando para crear el entorno virtual

```
python -m venv .venv
```

#### Integra VSCode + Entornos Virtuales:
**Paso 1.** Abre tu proyecto en VSCode.

**Paso 2.** Selecciona el intérprete Python del entorno virtual:

**Ctrl + Shift + P** > **Python: Select Interpreter** > Elige **.\\.venv\Scripts\python.exe.**



