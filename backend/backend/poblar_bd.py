from apps.users.models import User
def create_users():
    users = [
        {
            'username': 'usuario1',
            'email': 'usuario1@example.com',
            'name': 'Nombre1',
            'last_name': 'Apellido1',
        },
        {
            'username': 'usuario2',
            'email': 'usuario2@example.com',
            'name': 'Nombre2',
            'last_name': 'Apellido2',
        },
        {
            'username': 'usuario3',
            'email': 'usuario3@example.com',
            'name': 'Nombre3',
            'last_name': 'Apellido3',
        },
        {
            'username': 'usuario4',
            'email': 'usuario4@example.com',
            'name': 'Nombre4',
            'last_name': 'Apellido4',
        },
        {
            'username': 'usuario5',
            'email': 'usuario5@example.com',
            'name': 'Nombre5',
            'last_name': 'Apellido5',
        },
        {
            'username': 'usuario6',
            'email': 'usuario6@example.com',
            'name': 'Nombre6',
            'last_name': 'Apellido6',
        },
        {
            'username': 'usuario7',
            'email': 'usuario7@example.com',
            'name': 'Nombre7',
            'last_name': 'Apellido7',
        },
        {
            'username': 'usuario8',
            'email': 'usuario8@example.com',
            'name': 'Nombre8',
            'last_name': 'Apellido8',
        },
        {
            'username': 'usuario9',
            'email': 'usuario9@example.com',
            'name': 'Nombre9',
            'last_name': 'Apellido9',
        },
        {
            'username': 'usuario10',
            'email': 'usuario10@example.com',
            'name': 'Nombre10',
            'last_name': 'Apellido10',
        },
        {
            'username': 'usuario11',
            'email': 'usuario11@example.com',
            'name': 'Nombre11',
            'last_name': 'Apellido11',
        },
        {
            'username': 'usuario12',
            'email': 'usuario12@example.com',
            'name': 'Nombre12',
            'last_name': 'Apellido12',
        },
        {
            'username': 'usuario13',
            'email': 'usuario13@example.com',
            'name': 'Nombre13',
            'last_name': 'Apellido13',
        },
        {
            'username': 'usuario14',
            'email': 'usuario14@example.com',
            'name': 'Nombre14',
            'last_name': 'Apellido14',
        },
        {
            'username': 'usuario15',
            'email': 'usuario15@example.com',
            'name': 'Nombre15',
            'last_name': 'Apellido15',
        },
    ]

    for user_data in users:
        user = User(**user_data)
        user.save()

create_users()
