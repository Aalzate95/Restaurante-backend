# Restaurante

Proyecto desarrollador con el objetivo de servir como API Rest framework para el front-end de un sistema de reservas de un restaurante local.

Integrantes:
- Alexander Alzate
- Angie Tuarez
- Cesar Carlier


### Guia de ejecución
---
Para ejecutar este proyecto podemos hacerlo de dos maneras: con Docker o directamente con python.

Docker:

1. Instalación : En la raíz del repositorio encontrará un documento guía de uso para principiantes. (Solo nos interesa la instalación.)
2. Clonar el repositorio desde github.
3. Abrir con VScode u otro de su preferencia.
4. En la raíz del proyecto ejecutar: `docker-compose up`
5. Se creará la base de datos y las conexiones, cuando tengamos la conexión exitosa damos CTRL+C y volvemos a ejecutar `docker-compose up`

*Nota: En caso de tener problemas revisar puede ser por no tener instalado:[ WSL 2](https://docs.docker.com/desktop/windows/wsl/)*

Python:
1. Crear un env. con la versión 3 de Python.
    1. 1 Guia para creación de environments [link](https://www.programaenpython.com/miscelanea/crear-entornos-virtuales-en-python/)
    1. 2 Crear un environment con Anaconda (recomendado) [link](https://www.anaconda.com/products/individual)

2. Una vez creado y ejecutado el environment de Python ejecutar en la raíz del proyecto `python manage.py runserver`


Si todo está funcionando todo de forma correcta, la aplicación de Django estará ejecutandose en el puerto 8000, ir a `http://localhost:8000` en su navegador web preferido.

#### Notas
---
Por motivos de ser un proyecto en desarrollo tenemos:
`ALLOWED_HOSTS = ['*']` (Este valor no es seguro para un proyecto en producción.)

Para ejecutar comandos de Django como por ejemplo el `migrate` debe hacerse de la siguiente manera:

    `docker-compose run web [comando Django]`

P. ej.

    `docker-compose run web python manage.py migrate`