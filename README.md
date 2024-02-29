# Proyecto 6
## Ares Miguel Rodriguez Pajita, 7to grupo, Sprint 6

Proyecto 6 del Curso de QA Engineer pide automatizar la comprobación del campo name en la solicitud de creación de un kit de productos en la aplicación Urban Grocers.

## Características

- Automatiza tanto pruebas positivas como negativas.
- Se crean pruebas para el campo name según la lista de comprobación.
- Comprueba las pruebas con las respuestas del servidor.

## Configuración

Para configurar el proyecto, es necesario arrancar el servidor de Urban Grocers y copiar la dirección en la variable URL_SERVICE del archivo configuration.py.

## Ejecución

Para poder ejecutar las pruebas, se tiene que seguir los siguientes pasos:
- Asegurar que pytest esté instalado. Si no es así se puede usar el comando en tu entorno de desarrollo:
<pre>pip install pytest</pre>
- Dirigete donde se ubica el archivo create_kit_name_kit_test.py usando el comando:
<pre>cd 'dirección del proycto'</pre>
- Usa el siguiente comando para poder ejecutar las pruebas:
<pre>pytest create_kit_name_kit_test.py</pre>
- En la terminal, se debe de mostrar la información del progreso de las pruebas.

## Tecnologías

El proyecto usa varias tecnologías de código abierto:

- [Python](https://www.python.org) - Lenguaje de programación usado en este proyecto.
- [Requests](https://pypi.org/project/requests/) - Librería que permite enviar pedidos HTTP/1.1.
- [Git](https://git-scm.com) - Software de control de versiones de proyectos.

## Instalación

El proyecto necesita un editor de código como PyCharm para poder leerlo y/o editarlo.

Para clonar el proyecto es necesario seguir la siguiente dirección https://github.com/AresRdrgz/qa-project-06-es.git.

## Plugins

Se usaron los siguientes plugins en el desarrollo del proyecto:

- [PyCharm](https://www.jetbrains.com/es-es/pycharm/) - Entorno de desarrollo integrado en programación en Python.
- [GitHub](https://github.com) - Forja para alojar proyectos utilizando el control de versiones Git.

