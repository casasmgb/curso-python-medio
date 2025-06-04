from flask import Blueprint, request, jsonify, current_app
from .usuario_service import Usuario
from ..custom_exception import CustomException
from ..utils import format_response
from .usuario_table import SQLiteTable

usuario_controller = Blueprint('usuario_controller', __name__)

@usuario_controller.route('/usuarios', methods=['GET'])
def listar_usuarios():
    with SQLiteTable(current_app.config['DB']) as conn:
        try:
            usuariosResults = []
            usuariosResults = Usuario.listar_usuarios(conn)
            response = format_response(usuariosResults, 'DATOS OBTENIDOS DE MANERA CORRECTA')
            return jsonify(response)
        except CustomException as e:
            raise CustomException(e.code, e.message)

@usuario_controller.route('/usuarios-alias', methods=['GET'])
def obtener_alias():
    alias = request.args.get('alias')
    with SQLiteTable(current_app.config['DB']) as conn:
        try:
            usuariosResults = []
            usuariosResults = Usuario.obtener_alias(conn, alias)
            response = format_response(usuariosResults, 'DATOS OBTENIDOS DE MANERA CORRECTA')
            return jsonify(response)
        except CustomException as e:
            raise CustomException(e.code, e.message)

@usuario_controller.route('/usuarios', methods=['POST'])
def crear_usuario():
    with SQLiteTable(current_app.config['DB']) as conn:
        try:
            nuevo_usuario = request.json
            
            usuario = Usuario()
            usuario.set_usuario(
                        nombre_completo = nuevo_usuario['nombre_completo'], 
                        alias = nuevo_usuario['alias'], 
                        password = nuevo_usuario['password']
                    )
            
            result = usuario.agregar_usuario(conn)
            response = format_response(result, 'SE REALIZO EL REGISTRO')
            conn.commit()
            return jsonify(response), 201
        except CustomException as e:
            conn.rollback()
            raise CustomException(e.code, e.message)
    
@usuario_controller.route('/usuarios', methods=['PUT'])
def modificar_usuario():
    with SQLiteTable(current_app.config['DB']) as conn:
        try:
            data = request.json
            
            usuario = Usuario()
            usuario.set_usuario(
                        id = data['id'], 
                        nombre_completo = data['nombre_completo'], 
                        alias = data['alias'], 
                        password = data['password']
                    )
            
            result = usuario.modificar_usuario(conn)
            response = format_response(result, 'SE REALIZO LA MODIFICACION')
            conn.commit()
            return jsonify(response), 200
        except CustomException as e:
            conn.rollback()
            raise CustomException(e.code, e.message)
    
@usuario_controller.route('/login', methods=['POST'])
def login():
    with SQLiteTable(current_app.config['DB']) as conn:
        try:
            data = request.json
            
            usuario = Usuario()
            usuario.set_data_login(
                        alias = data['alias'], 
                        password = data['password'],
                    )
            
            result = usuario.login(conn)
            response = format_response(result, 'SE REALIZO LA MODIFICACION DE PASSWORD')
            conn.commit()
            return jsonify(response), 200
        except CustomException as e:
            conn.rollback()
            raise CustomException(e.code, e.message)
