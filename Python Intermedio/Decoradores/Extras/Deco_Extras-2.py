user_logged_in = False

def requires_login(func):
    def wrapper(*args, **kwargs):
        if not user_logged_in:
            raise Exception("Usuario no autenticado")
        return func(*args, **kwargs)
    return wrapper

@requires_login
def view_profile():
    print("Mostrando perfil del usuario")




print("── Case 1: without login ──")
try:
    view_profile()
except Exception as e:
    print(f"Error: {e}")


print("\n── Case 2: with login ──")
user_logged_in = True
view_profile()