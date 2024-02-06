# Nombre de proyecto: AppMendezDahiana 
# Alumno/a: Mendez Dahiana
# Versión: pre-entregable 3

# Aplicación que permite la funcionalidad de una Estetica.

- Los modelos que presenta esta aplicación son:
 -Tratamiento
 -Personal
 -Cliente

-Las funcionalidades de la página y la forma de actuar es la siguiente:

Clona este repositorio en tu máquina local.
Abrí una terminal y navega hasta la raíz del proyecto
Activa el entorno virtual.
Instala las dependencias del proyecto: pip install -r requirements.txt.
En la terminal, navega hasta la carpeta del proyecto con cd App3raEntrega.
Ejecuta las migraciones de Django con el comando: python manage.py migrate.
Ejecuta el servidor con el comando: python manage.py runserver.

Abre un navegador y navega hasta http://127.0.0.1:8000/App3raEntrega para ver la página principal.
Para acceder a la vista de los tratamientos en la db, hace click en la navbar en "Tratamientos" o accede a http://127.0.0.1:8000/App3raEntrega/tratamientos.
En está misma página, se encuentra el boton "Agregar tratamiento", haciendo click en este te llevara a la vista Agregar tratamiento. En está 
se encuentra un formulario que te permirira agregar un nuevo tratamiento haciendo click en "Agregar". Tambien podras acceder al formulario
desde http://127.0.0.1:8000/App3raEntrega/tratamiento_formulario.

Para acceder a la vista del personal en la db, hace click en la navbar en "Personal" o accede a http://127.0.0.1:8000/App3raEntrega/personal.
En está misma página, se encuentra el boton "Agregar personal", haciendo click en este te llevara a la vista Agregar personal. En está 
se encuentra un formulario que te permirira agregar nuevo personal, haciendo click en "Agregar". Tambien podras acceder al formulario
desde http://127.0.0.1:8000/App3raEntrega/personal_formulario.

Para acceder a la vista de los clientes en la db, hace click en la navbar en "Clientes" o accede a http://127.0.0.1:8000/App3raEntrega/clientes.
En está misma página, se encuentra el boton "Agregar cliente", haciendo click en este te llevara a la vista Agregar cliente. En está 
se encuentra un formulario que te permirira agregar un nuevo cliente haciendo click en "Agregar". Tambien podras acceder al formulario
desde http://127.0.0.1:8000/App3raEntrega/cliente_formulario.
Para buscar tratamientos entre todas las que hay guardadas, hace click en la navbar en "Buscar" o accede al formulario en http://127.0.0.1:8000/App3raEntrega/buscar.

Para acceder al administrador de la página, dirigirse a http://127.0.0.1:8000/admin y tipear el usuario: "admin" y la contraseña: "12345".

Esas son todas las funcionalidades de la página web con 3 modelos distintos, formularios para cada uno y formulario de busqueda que consiste
en poder visualizar los tratamientos por un patron en el nombre.
