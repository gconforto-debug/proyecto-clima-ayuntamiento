import csv
import os
import hashlib
import sys
import getpass

# Configuración de persistencia (Librerías estándar de Python)
ARCHIVO_USUARIOS = "usuarios.csv"
COLUMNAS = ["usuario", "password_hash"]

def _hash_password(password):
    """Encripta la contraseña de forma segura (SHA-256)."""
    return hashlib.sha256(password.encode()).hexdigest()

def _cargar_usuarios():
    """Lee los usuarios guardados en el CSV."""
    usuarios = {}
    if not os.path.exists(ARCHIVO_USUARIOS):
        return usuarios
    try:
        with open(ARCHIVO_USUARIOS, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                usuarios[fila["usuario"]] = fila["password_hash"]
    except Exception: 
        pass 
    return usuarios

def registrar_usuario():
    print("\n--- 👤 REGISTRO DE USUARIO ---")
    usuarios_db = _cargar_usuarios()
    
    # Bucle para asegurar que el usuario se introduce correctamente
    while True:
        nuevo_user = input("Elige un nombre de usuario: ").strip().lower()
        
        if not nuevo_user:
            print("❌ El usuario no puede estar vacío. Inténtalo de nuevo.")
            continue
            
        if nuevo_user in usuarios_db:
            print("❌ Este usuario ya existe.")
            return  # Lo devolvemos al menú si el usuario ya existe
            
        break # Si el usuario es válido y nuevo, salimos del bucle

    # Bucle para asegurar que la contraseña cumple los requisitos
    while True:
        pw = getpass.getpass("Elige una contraseña (mínimo 4 caracteres): ")
        
        # Usamos strip() para evitar contraseñas hechas solo de espacios
        if len(pw.strip()) < 4:
            print("❌ Contraseña demasiado corta o inválida. Inténtalo de nuevo.")
            continue
            
        break # Si la contraseña es válida, salimos del bucle

    archivo_nuevo = not os.path.exists(ARCHIVO_USUARIOS)
    try:
        with open(ARCHIVO_USUARIOS, "a", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=COLUMNAS)
            if archivo_nuevo: 
                escritor.writeheader()
            escritor.writerow({"usuario": nuevo_user, "password_hash": _hash_password(pw)})
        print(f"✅ Usuario '{nuevo_user}' creado con éxito.")
    except Exception as e:
        print(f"❌ Fallo al guardar: {e}")

def login_tradicional():
    print("\n--- 🔐 INICIO DE SESIÓN ---")
    usuarios_db = _cargar_usuarios()
    user = input("Usuario: ").strip().lower()
    pw = getpass.getpass("Contraseña: ")
    
    if usuarios_db.get(user) == _hash_password(pw):
        print(f"✅ Bienvenido, {user}.")
        return True
    print("❌ Usuario o contraseña incorrectos.")
    return False

def login_google():
    """Simulación simple de OAuth."""
    print("\n[G] Conectando con Google...")
    print("✅ Acceso concedido vía Google.")
    return True

def solicitar_acceso():
    """Punto de entrada para main.py"""
    while True:
        print("\n" + "="*30)
        print("  🔑 CONTROL DE ACCESO")
        print("="*30)
        print("1. Iniciar Sesión")
        print("2. Acceder con Google")
        print("3. Registrarse")
        print("4. Salir")

        opc = input("\nOpción: ")
        if opc == "1": 
            if login_tradicional(): return True
        elif opc == "2": 
            if login_google(): return True
        elif opc == "3": 
            registrar_usuario()
        elif opc == "4": 
            print("\nCerrando sistema...")
            sys.exit()
        else: 
            print("⚠️ Opción no válida.")