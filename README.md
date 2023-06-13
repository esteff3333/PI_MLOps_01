### PROYECTO INDIVIDUAL Nº1 (MACHINE LEARNING)

[<img src= "https://www.iberdrola.com/documents/20125/40921/machine_learning_746x419.jpg/15ff7571-4cfc-d9f0-5ef4-9c2e9306ad88?t=1627968463400" width=150><br><sub>esteff3333</sub>](https://github.com/esteff3333)


Autora: Estefania Serna 



## Indice
<!-- TABLA DE CONTENIDO -->
<details>
  <summary>Tabla de contenido </summary>
  <ol>
    <li><a href="#Indice">Indice</a></li>
    <li><a href="#Introduccion">Introduccion</a></li>
    <li><a href="#Objetivos">Objectivos</a></li>
    <li><a href="#ETL">ETL</a></li>
    <li><a href="#Desarrollo de la API">Desarrollo de la API</a></li>
    <li><a href="#Deployment">Deployment</a></li>
    <li><a href="#Video explicativo">Video explicativo</a></li>
  </ol>
</details>



## Introduccion 
A continuacion les presento mi primer proyecto de trabajo en Henry, una API de recomendacion de peliculas.

En el contexto del proyecto de recomendacion de películas, se aplicó el proceso de ETL a dos datasets de películas que no estaban normalizados. Antes de poder abordar el objetivo principal del proyecto, era necesario realizar una serie de cambios y ajustes en los conjuntos de datos.

Durante la etapa de Extracción, se obtuvieron los conjuntos de datos de películas, los cuales podían contener valores nulos, columnas innecesarias o estructuras de datos complicadas como diccionarios dentro de las columnas.

Estas acciones permiten transformar los datos crudos en información útil y preparada para su posterior análisis y utilización en el desarrollo de las APIs y otros componentes del proyecto.

En la fase posterior se pedia el desarrollo de 6 API, para hacer consultas acerca de las peliculas, actores, directores, el exito y el promedio de cada una de ellas y hacer un deployment para subir nuestra API en la web.


## Objetivos

- (ETL) Proceso de transformacion y limpieza de datos.
- Realizacion de endpoints para la API
- Crear la API en la libreria FastAPI
- Hacer el deploy de la API en Render


## ETL

El proceso (ETL) es una parte fundamental en el ámbito del análisis de datos y la preparación de datos para su posterior procesamiento. En este proceso, se realizan una serie de pasos para obtener datos de diferentes fuentes, transformarlos según las necesidades del análisis.

Luego, en la etapa de Transformación, se llevaron a cabo una serie de tareas para limpiar y preparar los datos. Esto implicó eliminar los valores nulos, eliminar columnas que no eran relevantes para el procesamiento de los datos y desanidar estructuras de datos complejas para facilitar el acceso a la información requerida.

Finalmente, en la etapa de Carga, los datos transformados y preparados se cargaron en un destino final, posiblemente una base de datos o un sistema de almacenamiento adecuado. Estos datos limpios y estructurados ahora están listos para su uso en el desarrollo de las APIs y otras tareas de análisis y procesamiento de datos.

Es importante destacar que el proceso de ETL puede ser tedioso, pero también es fundamental para garantizar la calidad de los datos y obtener resultados precisos en los análisis posteriores. Los datos procesados en el proceso de ETL sentarán las bases para el éxito de las API desarrolladas y para alcanzar los objetivos esperados en el proyecto.


## Desarrollo de la API
Durante el desarrollo de las APIs, se implementaron diversas funciones utilizando FastAPI para acceder y exponer los datos de manera eficiente. Estas APIs permiten realizar consultas sobre películas, actores y directores, brindando información valiosa y facilitando el análisis de datos en el ámbito cinematográfico.

Se crearon 6 funciones con decoradores específicos para cada endpoint. Estas funciones incluyen consultas como la cantidad de filmaciones en un mes o día específico, el puntaje y la popularidad de una película según su título, la cantidad de votos y el promedio de votaciones de una película, la información de éxito de un actor en términos de participación en filmaciones y el retorno promedio obtenido, así como el éxito de un director junto con los detalles de cada película dirigida, como la fecha de lanzamiento, el retorno individual, el costo y la ganancia.

Estas APIs ofrecen una forma sencilla y eficiente de acceder a información crucial sobre películas, actores y directores, permitiendo realizar análisis y tomar decisiones informadas en el ámbito cinematográfico.



## Deployment
Para realizar el despliegue de las APIs y crear la página web, se siguieron varios pasos. En primer lugar, se configuró el proyecto creando un archivo .gitignore para excluir archivos innecesarios y sensibles, y un archivo requirements.txt para enumerar las dependencias del proyecto. Estos archivos son fundamentales para asegurar la correcta instalación de las bibliotecas requeridas.

Luego, se procedió a crear una cuenta en Render, una plataforma que facilita el alojamiento de aplicaciones web. Mediante Render, se configuró la aplicación para desplegarla automáticamente. Se conectó el repositorio de Git donde se encontraba el código fuente y se especificó el entorno virtual para instalar las dependencias.

Finalmente, Render realizó el despliegue automático de la aplicación, instalando las dependencias y poniendo en funcionamiento las APIs. Se generó una URL pública para acceder a la página web, que ofrecía una interfaz intuitiva para interactuar con las APIs. Los usuarios podían realizar consultas sobre películas, actores y directores, ingresando parámetros como el mes o día de estreno de una película, el título de una película, o el nombre de un actor o director.

En resumen, el proceso de despliegue en Render y creación de la página web implicó la configuración del proyecto mediante los archivos .gitignore y requirements.txt, seguido de la utilización de Render para el despliegue automático. Esto permitió disponibilizar las APIs y brindar una interfaz web amigable para interactuar con ellas de manera rápida y sencilla.


## Video explicatico 

https://drive.google.com/file/d/1fFspyW31i9jP9S-RJijWPeHjCbKm2dHj/view?usp=drive_link

- Github: esteff3333
LinkedIN: https://www.linkedin.com/in/estefania-serna-961944196/

