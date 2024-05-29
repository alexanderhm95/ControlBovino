#Utilizado para verificar si un usuario es Admin o User

def es_Admin(user):
    return user.groups.filter(name='Admin').exists()

def es_User(user):
    return user.groups.filter(name='User').exists()
    