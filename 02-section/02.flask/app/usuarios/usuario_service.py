from ..custom_exception import CustomException
import bcrypt  # PARTE 2

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
        
    def set_data_login(self, alias=None, password=None):
        self.alias = alias
        self.password = password
        
    def data_usuario(self):
        return {
            "id": self.id,
            "nombre_completo": self.nombre_completo,
            "alias": self.alias,
            "password": self.password
        }
    
    @staticmethod
    def listar_usuarios(conn):
        c = conn.cursor()
        c.execute("SELECT * FROM usuarios")
        usuarios = c.fetchall()
        data = []
        for row in usuarios:
            row_dict = {str(k[0]): v for k, v in zip(c.description, row)}
            data.append(row_dict)
        return data
    
    @staticmethod
    def obtener_alias(conn, alias=None):
        try:
            if alias == None: 
                raise CustomException(400, "Se requiere un alias para buscar.")
            
            c = conn.cursor()
            c.execute("SELECT * FROM usuarios WHERE usuarios.alias = ?;", (alias,))
            usuario = c.fetchone()
            
            if usuario is None:
                raise CustomException(404, f"No se encontró al usuario con alias: {alias}.")
            
            # Convertir el resultado a diccionario
            valores = [description[0] for description in c.description]
            usuario_dict = dict(zip(valores, usuario))
            
            return usuario_dict  # Devolvemos el diccionario directamente
        except CustomException as e:
            raise CustomException(e.code, e.message)
        
    def agregar_usuario(self, conn):
        try:
            # PARTE 2
            password_encrypted = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()) 
        
            # Verificar si el usuario ya existe
            c = conn.cursor()
            c.execute("SELECT * FROM usuarios WHERE nombre_completo = ? AND alias = ?;", (self.nombre_completo, self.alias))
            if c.fetchone():
                raise CustomException(400, "El usuario ya existe.")

            c.execute("INSERT INTO usuarios (nombre_completo, alias, password, fecha_registro) VALUES (?, ?, ?, DATE('now'))",
                    (self.nombre_completo, self.alias, password_encrypted.decode('utf-8')))
            return self.data_usuario()
        except CustomException as e:
            raise CustomException(e.code, e.message)
        
    def modificar_usuario(self, conn):
        # Verificar si el usuario a modificado ya existe
        try:
            
            if self.id == None:
                raise CustomException(400, "Se requiere el Identificador para modificar.")
            
            # PARTE 2
            password_encrypted = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()) 
        
            c = conn.cursor()
            c.execute("SELECT * FROM usuarios WHERE nombre_completo = ? AND alias = ? AND id != ?;", (self.nombre_completo, self.alias, self.id))
            if c.fetchone():
                raise CustomException(400, "Existe otro usuario con los mismos datos.")
            
            c.execute("UPDATE usuarios SET nombre_completo=?, alias=?,  password=? WHERE id=?;", (self.nombre_completo, self.alias, password_encrypted.decode('utf-8'), self.id))
            conn.commit()
            return self.data_usuario()
        except CustomException as e:
            raise CustomException(e.code, e.message)

    def modificar_password(self, conn):
        try:
            if self.id == None:
                raise CustomException(400, "Se requiere el Identificador para modificar.")
            
            if self.password == None:
                raise CustomException(400, "Se requiere el password para modificar.")
            
            if self.password_repeat == None:
                raise CustomException(400, "Se requiere repetir el password para modificar.")
            
            # campos_requeridos = ['id', 'password', 'password_repeat']
            # campos_faltantes = [campo for campo in campos_requeridos if campo not in data]
            # if campos_faltantes:
            #     raise CustomException(400, f"Faltan los campos: {', '.join(campos_faltantes)}")
            
            
            # PARTE 2
            password_encrypted = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()) 
            password_repeat_encrypted = bcrypt.hashpw(self.password_repeat.encode('utf-8'), bcrypt.gensalt()) 
                        
            
            if password_repeat_encrypted != password_encrypted:
                raise CustomException(400, "Los passwords no son iguales.")
            
            c = conn.cursor()
            c.execute("UPDATE usuarios SET password=? WHERE id=?", (password_encrypted.encode('utf-8'), self.id))
            conn.commit()
            print("Password de usuario modificada.")
            return {
                "id": self.id,
                "password": password_encrypted.encode('utf-8')
            }
        except CustomException as e:
            raise CustomException(e.code, e.message)

    def login(self, conn):
        try:
            if self.alias is None: 
                raise CustomException(400, "Se requiere un alias para iniciar sesion.")
            if self.password is None: 
                raise CustomException(400, "Se requiere el password para iniciar sesion.")
            
            # Primero obtenemos el usuario por alias 
            c = conn.cursor()
            c.execute("SELECT * FROM usuarios WHERE usuarios.alias = ?;", (self.alias,))
            usuario = c.fetchone()
            
            if usuario is None:
                raise CustomException(404, f"No se pudo iniciar sesión con alias: {self.alias}.")
            
            # Convertir el resultado a diccionario
            valores = [description[0] for description in c.description]
            usuario_dict = dict(zip(valores, usuario))
            
            # Obtenemos el hash almacenado
            stored_hash = usuario_dict['password'].encode('utf-8')
            
            # Verificamos la contraseña
            if not bcrypt.checkpw(self.password.encode('utf-8'), stored_hash):
                raise CustomException(401, "Credenciales incorrectas")
            
            return usuario_dict
        except CustomException as e:
            raise CustomException(e.code, e.message)
        