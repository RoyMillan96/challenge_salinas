# Challenge para grupo Salinas

Este es un challenge debe contener los siguientes criterios con el objetivo de evaluar el diseño, calidad e implementación de un servicio REST, así como el uso de servicios preexistentes

1. Creación, modificación y eliminación de usuarios:
El sistema debe tener una API REST el cual permita la creación, modificación y eliminación de usuarios. A través de esta API, los clientes pueden registrar nuevos usuarios proporcionando información relevante, como el nombre de usuario, la contraseña y otros datos pertinentes. Los usuarios existentes pueden modificar su información utilizando la misma API. Si un usuario ya no necesita el servicio, también debería poder eliminar su cuenta utilizando la API.

2. Autenticación de usuarios:
El sistema debe contar con una funcionalidad para autenticar a los usuarios registrados. La autenticación puede implementarse utilizando JWT, Autenticación básica u otros métodos de autenticación seguros. Una vez que un usuario ha sido autenticado, el sistema debería emitir un token de autenticación que el usuario puede utilizar para acceder a otros servicios del sistema.

3. Consulta a una API externa de clima:
El sistema debe permitir a los usuarios autenticados realizar consultas a una API externa de clima. La funcionalidad solo estará disponible para aquellos usuarios que hayan sido previamente registrados y autenticados. Esta funcionalidad permite a los usuarios obtener información actualizada y relevante sobre las condiciones climáticas en diferentes ubicaciones.

4. Registro de las consultas de clima:
El sistema debe tener una base de datos diseñada para registrar las peticiones de clima hechas al API externa. Esto permite un seguimiento de qué usuarios están utilizando este servicio y cuándo. Esta base de datos debe estar diseñada para almacenar eficientemente la información del usuario y las solicitudes de consulta del clima.

5. Consulta de registros generados por un usuario:
El sistema debe permitir a los usuarios autenticados consultar los registros que han generado. La API debería devolver los registros paginados de acuerdo con parámetros y encabezados, permitiendo a los usuarios filtrar los datos registrados en la base de datos. Esto podría incluir filtros por rango de fecha, ubicación, orden (ascendente o descendente) u otros datos que permitan filtrar la información registrada. Este caso de uso permite a los usuarios tener una visión clara y personalizada de su historial de uso del servicio.

6. Despliegue del servicio con Docker
Se debe permitir iniciar el servicio en un contenedor Docker

7. Una vez terminado el desarrollo de la prueba exponer el servicio para que pueda ser consultado, te recomendamos utilizar NGROK y enviarnos una colección de postman del consumo de tus APIs para que el día de la revisión podamos hacer pruebas, adicional enviarnos un respaldo de tu base de datos.
## Tecnologias utilizadas
- Python
- Django
- Django Rest Framework
- Swagger (Documentación Api)
- Postgresql
- Redis
- doker


## Instalación

1. Clona este repositorio: `git clone https://github.com/RoyMillan96/challenge_salinas.git`
2. Navega al directorio del proyecto: `cd tu-proyecto`
3. Instala docker
4. Configurar las variables de entorno de backend Desde el directorio de backend ejecute: touch .env El comando touch creará el archivo .env en el directorio backend/config. Este comando funciona en Mac y Linux, pero no en Windows. Si es usuario de Windows, en lugar de utilizar la línea de comandos, puede crear el archivo .env manualmente navegando en Visual Studio Code hasta el Explorador, haciendo clic en el directorio config (dentro del directorio backend) y seleccionando la opción Nuevo archivo.
    A continuación, declare las variables de entorno en el archivo .env. Asegúrese de no entrecomillar las cadenas.
    BASE_URL='http://localhost:8000/'
    SECRET_KEY=yoursecretkey
    URL_WEATHER=urlyoursekeyweather
    API_KEY_WEATHER=apileyweather
    API_NAME_WEATHER='challenge_salinas'
    BASE_URL_WEATHER='http://dataservice.accuweather.com/' 
    DATABASE_NAME=yourdb_name
    DATABASE_USER=youruser
    DATABASE_PASS=yourpassword
    DATABASE_HOST=127.0.0.1
    DATABASE_PORT=5432

5.  navega al directorio que contiene el manage.py y ejecuta docker
    docker-compose up
6. Asegúrate de que tus contenedores Docker estén en funcionamiento para correr migraciones. 
9. Realiza las migraciones de la base de datos: 
    ``docker-compose exec web python manage.py migrate`
7. Create an admin user to access the Django Admin interface: 
    `docker-compose exec web python manage.py createsuperuser`
8. Ejecuta el script para poblar la tabla de usuarios 
    abre la shel con el proyecto activado `docker-compose run --rm django python manage.py shell_plus ` y ejecuta lo siguiente:
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


## Customize the application
Instrucciones sobre cómo usar el proyecto.

1. ## API
    contine los endpoints para obtener el token de un usuario asi como su refresh token.
    http://localhost:8000/api/token/
    http://localhost:8000/api/token/

2. ## Login
    contine el endpoint para acceder a los recursos pasando el username y password para iniciar sesión.
    http://localhost:8000/login/

3. ## Logout
    contine el endpoint para cerrar la sesión quedando inaccesibles los recursos.
    http://localhost:8000/logout/

3. ## Users
    contine todos los edpints relacionados al usuario  
    ## List
    http://localhost:8000/users/user/
    ## Create
    http://localhost:8000/users/user/
    ## Get
    http://localhost:8000/users/user/1
    ## Update
    http://localhost:8000/users/user/1
    ## Delete
    http://localhost:8000/users/user/1

3. ## Weather
    contine todos los edpints relacionados al estado del clima actual y por días así como por usuario
    ## Crea y muestra datos del clima por día
    http://localhost:8000/weather/conditions-by-days/
    ## Crea y muestra datos del clima por hora
    http://localhost:8000/weather/conditions-by-hours/
    ## Crea y muestra datos del clima actual 
    http://localhost:8000/weather/current-conditions/
    ## Crea y muestra datos las consultas que hizo el user a las condiciones actuales
    http://localhost:8000/weather/currents-user-detail/
    ## Crea y muestra datos las consultas que hizo el user a las siguientes condiciones de tiempo
    http://localhost:8000/weather/forecast-user-detail/


## Contacto

- Rodrigo Millan Colin
- roymillan96@gmail.com
- https://github.com/RoyMillan96

