# Challenge para grupo Salinas

Este proyecto es una implementación de un servicio Rest que obtiene las condiciones actuales 
dada una localidad, condiciones por día y hora obtenidos en la app de accuWeather.com, dicha 
implementación requiere que el usuario este autenticado mediante token proporcionados por JWT,
cada consulta a la aplicación de weather será almacenada en la base de datos para posteriormente
ser consultada en los endpoints creados para obtener las consultas hechas por usuario.
## Tecnologias utilizadas
- Python
- Django
- Django Rest Framework
- Swagger (Documentación Api)
- Postgresql
- Redis
- doker
- Redis


## Instalación
1. Instalar Docker
    Puedes instalar Docker en Ubuntu 22.04 directamente desde la terminal sin tener que usar más que un par de comandos básicos.

    Paso 1. Preparar el sistema
        El primer paso es actualizar tu sistema operativo a la versión más reciente, algo que se consigue rápidamente con dos comandos:
        sudo apt-get update
        sudo apt-get upgrade

    Paso 2. Eliminar cualquier rastro de Docker.
        Si ya has usado alguna versión beta de Docker o has instalado una previsualización de este software de virtualización, tendrás que eliminarlas antes de poder instalar Docker. Si no, es posible que se produzcan efectos secundarios no deseados.

        sudo apt remove docker-desktop
        rm -r $HOME/.docker/desktop
        sudo rm /usr/local/bin/com.docker.cli
        sudo apt purge docker-desktop

    Paso 3. Descargar repositorio de Docker.
    Docker usa en su instalación un repositorio que debes almacenar en tu sistema. Para poder trabajar con este repositorio, debes primero instalar los siguientes paquetes:

        sudo apt-get install \
            ca-certificates \
            curl \
            gnupg \
            lsb-release

        A continuación, puedes añadir a tu sistema la clave GPG de Docker:

        sudo mkdir -p /etc/apt/keyrings
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
        El repositorio de Docker también se configura en la línea de comandos. Para ello, también basta con aplicar el comando de terminal adecuado:

        echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

    Paso 4. Instalar el motor de Docker.
        En Ubuntu 22.04 también puedes descargar el motor de Docker directamente desde la terminal. Los comandos concretos que necesitas para hacerlo dependen de si quieres descargarte una versión concreta de Docker o si prefieres optar por la versión más reciente.

        Para descargarte una versión en concreto de Docker puedes usar el siguiente comando para ver una lista de todas las versiones disponibles:

        apt-cache madison docker-ce | awk '{ print $3 }'
        Puedes elegir una de las versiones que aparecen en la lista. Indica cuál quieres con el string de la versión. Luego, instálala con lo siguiente:

        VERSION_STRING=5:20.10.13~3-0~ubuntu-jammy
        sudo apt-get install docker-ce=$VERSION_STRING docker-ce-cli=$VERSION_STRING containerd.io docker-compose-plugin
        Instalar la versión actual de Docker es incluso más sencillo:

        apt-cache madison docker-ce | awk '{ print $3 }'

    Paso 5. Comprobar la instalación.
        Para comprobar si el programa se ha instalado correctamente, Docker te permite iniciar un Docker container de “Hello World”. Hazlo con el siguiente comando del terminal:

        sudo docker run hello-world
        Si todo ha ido bien, te aparecerá la siguiente pantalla en tu línea de comandos:

        Salida de la terminal tras ejecutar “sudo docker run hello-world”
        Tras ejecutar el comando “docker run hello-world”, Docker te dará la bienvenida explicándote cómo se configuran los contenedores.

    Opcional: Paso 6. Ejecutar Docker como usuario no root.
        Como has visto con los comandos de terminal, actualmente necesitas derechos root para ejecutar Docker, ya que todos los comandos deben empezar con “sudo”. Si quieres ejecutar Docker como usuario sin derechos root, puedes hacerlo creando un grupo Docker.

    Paso 6.1. Crear grupo llamado “Docker”.
        Puedes crear un grupo llamado “Docker” y asignarle usuarios con el siguiente comando:
        sudo groupadd docker

    Paso 6.2. Añadir usuarios.
        Con un simple comando de la línea de comandos puedes añadir a tu grupo Docker todos los usuarios que podrán ejecutar Docker sin derechos root:

        sudo usermod -aG docker $USER
        $USER es un marcador de posición que debe reemplazarse por el nombre del usuario deseado. Para que puedan reconocerse y darse seguimiento a los cambios de tu sistema, debes cerrar y volver a iniciar sesión. Después, podrás acceder a Docker como usuario registrado en el grupo y no tener que recurrir a sudo.

2. Install dependencias.

        $ git clone https://github.com/RoyMillan96/challenge_salinas.git
        $ cd backend


3. Configurar las variables de entorno.

    crear un .env que contendra datos sencibles que no deben ser expuestos.

        touch .env

    si esta en windows crear el archivo manualmente en la raiz del proyecto.

    A continuación, declare las variables de entorno en el archivo .env. Asegúrese de no entrecomillar las cadenas puede ver el archivo de ejemplo .env. que se encuentra en la raiz del proyecto.

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

4. correr la aplicación.

    docker compose up

5. En una nueva instancia  corre las migraciones de la aplicacion.

    docker compose exec django python manage.py migrate

6. ve a la aplicación en tu navegador.

     http://localhost:8000/

7. Crea un admin user para acceder a la interfaz de admin de django colocando los datos requeridos.

    docker-compose exec web python manage.py createsuperuser

8. en una nueva instancia de docker abre la shell de python para crear users.

    docker-compose run --rm django python manage.py shell_plus

    ejecuta lo siguiente:
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

