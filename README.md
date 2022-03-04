# Lab 3
## Proyecto Lab 3 Django y Google Apis

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Integrantes:
- Marsh Nicolas
- Varela Gaspar

## Apis utilizadas

| Api | Link |
| ------ | ------ |
| Recaptcha | [https://developers.google.com/recaptcha][PlDb] |
| Places API | [https://console.cloud.google.com/apis/library/places-backend.googleapis.com][PlGh] |
| Directions API | [https://console.cloud.google.com/apis/library/directions-backend.googleapis.com][PlGd] |
| Distance Matrix API | [https://console.cloud.google.com/apis/library/distance-matrix-backend.googleapis.com][PlOd] |
| Geocoding API | [https://console.cloud.google.com/apis/library/geocoding-backend.googleapis.com][PlMe] |
| Maps JavaScript API | [https://console.cloud.google.com/apis/library/maps-backend.googleapis.com][PlGa] |

Nuestro Principal objetivo en el trabajo es integrar el framework de python Django con las apis de google, y elegimos
utilizar Google Maps y Recaptcha.

## Vista General
La pagina esta pensada para crearse un usuario y logearse, todo esto esta guardado y protegido por Recaptcha de google
para garantizar que el input es de un humano.
Una vez dentro de la aplicación a la izquierda se ubica un menu en donde se pueden modificar los datos del usuario
haciendo request con la api de google para modificar las direcciones de su hogar.

## Menus
- Ingresar
Este menu se utiliza para iniciar sesión en la pagina.
- Crear Cuenta
Como el nombre lo dice, este menu sirve para crear una cuenta de usuario y almacenarla en la base de datos (sqlite3)
- Cuenta
Este menu sirve para mostrar los detalles generales de la cuenta
- Perfil
Aqui se puede establecer la direccion de la cuenta y posterior se puede actualizar en caso de querer cambiar la dirección
- Ruta
Menu utilizado para generar una ruta entre 4 puntos dados, se utilizan las apis de google para calcular el recorrido
- Mapa
El menu mapa es para que aparezca la ruta visualmente
- Salir
Sirve para deslogearse de la cuenta

## Requisitos

La aplicación requiere [Django](https://www.djangoproject.com/) v3.2.2+ para poder ser ejecutada

Módulos utilizados para la aplicacion.

```sh
asgiref            3.5.0
certifi            2021.10.8
charset-normalizer 2.0.12
Django             3.2.2
humanfriendly      10.0
idna               3.3
pip                22.0.3
pyreadline3        3.4.1
pytz               2021.3
requests           2.27.1
setuptools         60.9.3
sqlparse           0.4.2
tzdata             2021.5
urllib3            1.26.8
wheel              0.37.1
```

Para abrir el servidor en el localhost

```sh
python manage.py runserver
```

## UBP 2022