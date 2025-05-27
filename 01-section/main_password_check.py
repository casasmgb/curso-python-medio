from fuerza_bruta.password_check import PasswordCheck

def main():
    test_password = "supermariojavith"
    checker = PasswordCheck("supermariojavith")
    
    # Verificar fortaleza
    score, strength_message = checker.check_password_strength()
    print(f"Fortaleza de '{test_password}': Puntuación {score}/100 - {strength_message}")
    
    # Verificar vulneración
    is_pwned, pwned_message = checker.check_pwned_password()
    print(f"Vulneración: {pwned_message}")

if __name__ == "__main__":
    main()
    