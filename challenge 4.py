#Fictious database
database = {
    "user": {"password": "userpass", "role": "user"},
    "admin": {"password": "adminpass", "role": "admin"},
    "super_user": {"password": "superpass", "role": "superuser"}
}

# Function to verify credentials
def authenticate(username, password, required_role):
    if username in database and database[username]["password"] == password:
        if database[username]["role"] == required_role:
            return True
    return False

# Decorator for multi-level authentication
def auth_required(required_role):
    def decorator(function):
        
        def wrapper(username, password):
            if authenticate(username, password, required_role):
                return function(username)
            else:
                return "Acceso no autorizado"
        return wrapper
    return decorator

# Functions protected by authentication levels
@auth_required("user")
def user_function(username):
    return f"¡Hola, usuario {username}!"

@auth_required("admin")
def admin_function(username):
    return f"Bienvenido, administrador {username}."

@auth_required("superuser")
def superuser_function(username):
    return f"Saludos, superusuario {username}!"

# get inputs
username = input("Ingrese su nombre de usuario: ")
password = input("Ingrese su contraseña: ")

if superuser_function(username, password) != "Acceso no autorizado":
    print(superuser_function(username, password))
    
elif admin_function(username, password) != "Acceso no autorizado":
    print(admin_function(username, password) )
    
elif user_function(username, password) != "Acceso no autorizado":
    print(user_function(username, password))
    
else:
    print("Acceso no autorizado en todos los niveles.")
