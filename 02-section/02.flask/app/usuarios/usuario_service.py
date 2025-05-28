from ..custom_exception import CustomException

class Usuario:
    def __init__(self):
        pass
        
    def set_usuario(self, id=None, nombre_completo=None, alias=None, password=None):
        self.id = id
        self.nombre_completo = nombre_completo
        self.alias = alias
        self.password = password

    def set_data_password(self, id=None, password=None, password_repeat=None):
        self.id = id
        self.password = password
        self.password_repeat = password_repeat
        
    def data_usuario(self):
        return {
            "id": self.id,
            "nombre_completo": self.nombre_completo,
            "alias": self.alias,
            "password": self.password
        }
    
    # TOO CREACR METODO listar_usuarios
    
    # TOO CREACR METODO obtener_alias
        
    # TOO CREACR METODO agregar_usuario
    
    # TOO CREACR METODO modificar_usuario

    # TOO CREACR METODO modificar_password
