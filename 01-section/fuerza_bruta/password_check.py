import requests
import hashlib
import re

class PasswordCheck:
    def __init__(self, password):
        self.password = password

    def check_password_strength(self):
        """
        Verifica la fortaleza de una contraseña usando la API de PasswordUtility.
        Retorna una tupla con la puntuación (1-100) y un mensaje descriptivo.
        """
        # Reglas locales basadas en NIST
        score = 0
        messages = []

        # Longitud
        length = len(self.password)
        if length >= 12:
            score += 40
        elif length >= 8:
            score += 20
        else:
            messages.append("Longitud menor a 8 caracteres")

        # Variedad de caracteres
        if re.search(r"[a-z]", self.password):
            score += 15
        else:
            messages.append("Faltan minúsculas")
        if re.search(r"[A-Z]", self.password):
            score += 15
        else:
            messages.append("Faltan mayúsculas")
        if re.search(r"[0-9]", self.password):
            score += 15
        else:
            messages.append("Faltan números")
        if re.search(r"[^a-zA-Z0-9]", self.password):
            score += 15
        else:
            messages.append("Faltan símbolos")

        # Penalización por patrones comunes
        if re.search(r"(.)\1\1", self.password):  # Repetición de 3+ caracteres
            score -= 20
            messages.append("Evita repeticiones (e.g., aaa)")
        if re.search(r"123|abc|qwe", self.password, re.IGNORECASE):
            score -= 20
            messages.append("Evita secuencias comunes (e.g., 123, abc)")

        # Asegurar puntaje entre 0 y 100
        score = max(0, min(100, score))
        # Generar mensaje
        if score >= 80:
            message = "Fuerte: Contraseña muy segura"
        elif score >= 60:
            message = "Moderada: Contraseña aceptable, pero podría mejorarse"
        else:
            message = "Débil: Contraseña vulnerable, considera más caracteres y variedad"
        if messages:
            message += f" ({', '.join(messages)})"
        return score, message

    def check_pwned_password(self):
        """
        Verifica si una contraseña ha sido vulnerada usando la API de HaveIBeenPwned.
        Retorna True si la contraseña está comprometida, False si no, o un mensaje de error.
        """
        try:
            # Generar hash SHA-1 de la contraseña
            sha1 = hashlib.sha1(self.password.encode()).hexdigest().upper()
            prefix, suffix = sha1[:5], sha1[5:]
            
            # Consultar la API con el prefijo del hash
            url = f"https://api.pwnedpasswords.com/range/{prefix}"
            response = requests.get(url)
            response.raise_for_status()
            
            # Buscar el sufijo en la respuesta
            for line in response.text.splitlines():
                hash_suffix, count = line.split(':')
                if hash_suffix == suffix:
                    return True, f"¡Advertencia! Contraseña encontrada en {count} brechas"
            
            return False, "Contraseña no encontrada en brechas conocidas"
        except requests.RequestException as e:
            return False, f"Error al consultar HaveIBeenPwned: {str(e)}"

