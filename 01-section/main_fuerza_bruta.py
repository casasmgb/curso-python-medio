from fuerza_bruta.http_bruteforcer import HTTPBruteForcer

def main():
    attacker = HTTPBruteForcer(
        login_url="http://localhost:5000/login",
        username="eve.holt@reqres.in",
        wordlist_path="passwords.txt"  # Archivo con contraseñas de prueba
    )
    attacker.brute_force()

if __name__ == "__main__":
    main()
    