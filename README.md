# Ollivanders-Flask

![ollivander_flask](./doc/olivanders.jpg)


## Índice de contenido

- [**Introducción**](#introducción)
- [**Tareas a realizar**](#tareas-a-realizar)
    - [**Lógica**](#lógica)
    - [**Base de datos**](#base-de-datos)
    - [**App web**](#app-web)
- [**Requisitos**](#requisitos)
    - [**Docker**](#docker)
    - [**MySQL**](#mysql)
    - [**Opcional**](#opcional)
        - [**HeidiSQL**](#heidisql)
        - [**Xampp**](#xampp)
- [**Instalación**](#instalación)
    - [**Entorno**](#entorno)
    - [**Base de Datos**](#base-de-datos-1)
    - [**Docker**](#docker-1)
- [**Uso**](#uso)
- [**Testing**](#testing)
    - [**Pytest**](#pytest)



## Introducción

El famoso negocio de Ollivander ha crecido.

Como la demanda de productos mágicos no para de crecer, la expansión del negocio es inevitable para sobrevivir a Amazon.

Ollivander había contratado a Dobbie -a través del programa de FP Dual DAW de Hogwarts colegio concertado- para que le hiciese una app que gestionase el inventario, pero tras los tristes aoontecimientos en los que se vió -desgraciadamente- envuelto el pobrecico elfo, no tiene a nadie que pueda modificar el código para incluir nuevos productos.

Ollivander ha contratado los servicios de la consultora en la que trabajas para que adecúe la aplicación a las nuevas necesidades del inventario, por lo que te envían "a cliente" -a la tienda- a lidiar con él y, lo que es peor, con el código spagheti que manufacturó Dobby en sus momentos de langidez infinita.

Por si no fuera suficiente, tu compañero de empresa al que enviaron a cliente antes que a ti, a acaba de irse de España porque en el extranjero le pagan por trabajar, y ha dejado tiritando el código de los casos test que intentó añadir en un día de desesperación absoluta.


## Tareas a realizar


### Lógica

1. Refactoriza el código de la lógica para que sea fácil de entender, barato de modificar y no cambie el comportamiento observable del código existente.

2. El código existente pasa los casos test. Asegúrate de que el tuyo también, sin modificarlos.

3. Haz un evolutivo del sistema para que sea posible añadir al inventario un nuevo tipo de item llamado "Conjured". Los “Conjured” items degradan su calidad el doble de rápido que un item normal. Añade esta lógica al sistema así como los casos test que necesites.

**WARNING**
No alteres la clase Item o las propiedades de Items porque el colegio profesional de goblings no cree en la propiedad compartida del código y suele enviar inquisidores por la tienda de vez en cuando para chequear no dos sino tres, digo tres cosas sino cuatro, no cuatro sino cinco cosas, oh f*ck! que han de respetar su certificación de gobbling inside.


### Base de datos

1. Crea una base de datos SQL que permita realizar CRUD sobre el inventario.

2. El inventario inicial es el que especifica el primer caso test, el existente en el "día 0". Recuerda realizar un esquema que permita ampliarlo con el nuevo tipo de ítem "Conjured":

```
name, sellIn, quality
+5 Dexterity Vest, 10, 20
Aged Brie, 2, 0
Elixir of the Mongoose, 5, 7
Sulfuras, Hand of Ragnaros, 0, 80
Sulfuras, Hand of Ragnaros, -1, 80
Backstage passes to a TAFKAL80ETC concert, 15, 20
Backstage passes to a TAFKAL80ETC concert, 10, 49
Backstage passes to a TAFKAL80ETC concert, 5, 49
Conjured Mana Cake, 3, 6
```

### App web

Como quieres modernizar un poco el sistema de gestión de la tienda de Ollivander, decides desarrollar una app web que permita visualizar el estado del inventario, actualizar la calidad de los items y realizar operaciones básicas CRUD.

Esto supone tres capas en tu aplicación.

1. Capa de presentación y frontend.
    * Utilizando HTML, CSS y JS construye un pequeño sitio web para la intranet, con una interfaz de usuario/a que permita a Ollivander realizar las operaciones de la lógica.

2. Capa de lógica y backend
    * En el back encapsularás la lógica del negocio que has programado. Utilizarás un microframework llamado Flask para:
        * Atender y responder las peticiones que lleguen a través de un navegador web con las consulas de a la base de datos.
        * Construir una API REST que con al menos dos end points: un recurso devuelve el inventario y el otro la actualización del inventario. Si implementas el resto de operaciones CRUD, tendrás que añadir los end points correspondientes.

3. Acceso a datos (backend)
    * Mediante Flask, escribe el código necesario de la capa de acceso a datos, que conecte las peticiones web con la base de datos, para realizar las operaciones de la lógica. Recuerda que la lógica de la aplicación ha de ser agnóstica respecto a la base de datos utilizada.

4. Base de datos: reutiliza tus conocimientos de Mongo Atlas del primer trimestre, o aprovecha para implementar una base de datos relacional con MySQL.

5. Pensando en introducir un flujo de trabajo de Integración Continua y Entrega Continua (CI /CD) prepararás un contenedor [Docker](https://www.docker.com/) de desarrollo y pruebas y otro contenedor docker para despliegue. De momento, con Python es suficiente [tox](https://tox.wiki/en/latest/).




# Requisitos

Para poder ejecutar la aplicación correctamente, es necesario tener instalado las siguientes herramientas/aplicaciones:


## [Docker](https://www.docker.com/products/docker-desktop/)

Necesitaremos tener Docker instalado y en funcionamiento, dado que será donde tengamos nuestro contenedor ejecutando la aplicación.

## [MySQL](https://www.mysql.com/downloads/)

Para este proyecto utilizó la base de datos de MySQL, por lo tanto, para poder usar la base de datos es necesario tener instalado y configurado MySQL.

## Opcional

También para poder visualizar mejor el proyecto utilizo HeidiSQL y Xampp dado que me permiten interactuar mejor con la base de datos.

### [HeidiSQL](https://www.heidisql.com/download.php)

### [Xampp](https://www.apachefriends.org/es/download.html)



# Instalación

Una vez tengas instalado y configurado todos los requisitos, tendremos que seguir estos pasos para poder hacer uso de nuestra aplicación:


## Entorno

Primero de todo tenemos que tener nuestro entorno preparado con sus respectivas carpetas y archivos, para ello tendremos que hacer lo siguiente:

1. Crear un directorio/carpeta
```
mkdir .\ollivanders_shop
cd ollivanders_shop
```

2. Clonar repositorio
```
git clone https://github.com/Adrianlm17/ollivanders-Flask.git
```

3. Entorno virtual
```
python -m venv venv
```

4. Activar entorno
```
.\venv\Scripts\activate
```

5. Instalar Requirements.txt
```
pip install -r requirements.txt
```


## Base de Datos

1. Una vez tenemos el entorno preparado vamos a preparar nuestra base de datos, para ello haremos uso de MySQL (o HeidiSQL), nos tendremos que registrar y acceder a una consulta.

2. Una vez tenemos la consulta preparada, ejecutaremos el script que se proporciona [**"ollivanders-database.sql"**](./database/ollivanders-database.sql) y lo ejecutaremos.



## Docker

Por ultimo pero no menos importante, es necesario tener un contenedor donde se ecjutara nuestra aplicación, en este repositorio se proporciona un archivo llamado **"Dockerfile"** que nos permitira crear una imagen de Docker y posteriormente crear el contenedor necesario.

1. Imagen Docker
```
docker build -t ollivanders-shop .
```

![Imagen_Docker](./doc/docker_imagen.png)


2. Contenedor Docker
```
docker run --name=ollivanders_shop -p 5000:5000 -d ollivanders-shop:latest
```



# Uso

Para poder hacer uso de nuestra aplicación, tendremos que seguir los siguientes pasos:

1. Asegurate de estar en lar tura adecuada:
```
.\ollivanders-Flask>
```

2. Ejecuta el comando de arrancado:
```
flask --debug run
```

![flask_run](./doc/flask_run.png)

3. Si nos dirigimos a la ruta que nos indica en consola (http://127.0.0.1:5000), nos mostrara nuestra aplicación creada!

![app_ollivanders](./doc/ollivanders_web.png)



# Testing

## Pytest

Pytest es una biblioteca de pruebas de Python que se utiliza para escribir y ejecutar pruebas unitarias y de integración de forma eficiente.
Para poder hacer uso de dicha biblioteca, ejecuta el siguiente comando:

```
pytest
```

![Pytest](./doc/pytest.png)

