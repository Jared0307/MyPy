import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    password_length = 12  # Cambia la longitud de la contraseña
    
    print("="*70)
    print(" "*15 + "🔐 Generador de Contraseñas Seguras 🔐")
    print("="*70)
    print("Este script genera una contraseña aleatoria y segura.")
    print(f"La contraseña generada es: {generate_password(password_length)}")
    print("="*70)
