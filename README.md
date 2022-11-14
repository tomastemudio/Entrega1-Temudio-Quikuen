# Set-up
1. Copiar el url del codigo desde github.  
2. En Visual Studio Code abriremos una nueva terminal y escribimos lo siguiente: `git copy + url previamente copiado`
    Ejemplo: `git copy https://github.com/tomastemudio/Entrega1-Temudio-Quikuen`
3. Para comenzar a utilizar la pagina podemos crear un entorno virtual o instalar las versiones de los paquetes incluidos en el archivo 'requirements.txt' , para instalar estos archivos debemos escribir en la terminal lo siguente: `pip install -r + el archivo donde estan las versiones normalmente llamado requirements.txt.` 
    Ejemplo: `pip install -r requirements.txt`
4. En este programa necesitamos un base de datos por esta razon debemos inicializarla. En la terminal escribimos `python manage.py migrate`
5. Una vez hecho todo lo anterior se debe inciar el servidor de Django desde la terminal con el comando `python manage.py runserver`. Una vez hecho esto la terminal arrojara un link desde el cual se puede comenzar a utilizar la pagina e interactuar con ella.

# Uso de la pagina
El funcionamiento de la pagina es simple. El objetivo principal de esta es la creacion y visualizacion de jugadores de fubtol.
La pagina continen 3 secciones principales. Estas son un 'sobre nosotros' que posee informacion sobre los creadores de la pagina, otra seccion para la creacion de jugadores y una ultima seccion para la visualizacion, edicion y eliminacion de los jugadores creados.

Para crear un jugador es necesario ingresar 4 campos de informacion. Estos son: nombre, apellido, nacionalidad y liga en donde juega el jugador. Una vez hecho esto, la informacion va a aparecer en la seccion de visualizacion en forma de lista. Desde aqui se pueden editar o borrar los jugadores creados.
Este es el funcionamiento principal de la pagina.