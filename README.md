# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

*Introducción:*
Creación de una API donde poder visualizar los datos de las librerias y luego alojarlos en un servidor para que puedan ser consultados desde un entorno web.


*Objetivos:*

El objetivo de este proyecto es generar un modelo de recomendación de peliculas basado en el ingreso de un titulo de una filmacion.


*Desarrollo*

A través de la recepción de una base de datos que contenía listas de peliculas para usar como consulta, realicé un proyecto donde se llevaron a cabo una serie de pasos que implicaron la extracción, transformacion y carga de los datos, la configuración de servidores, la instalación del software, la transferencia de datos y la puesta en marcha de la aplicación para que esté en pleno funcionamiento. Esto también incluyó tareas como la configuración de la base de datos, la asignación de recursos, la gestión de permisos y la comprobación de que todo funcione correctamente.


# ETL DE LOS ARCHIVOS
Proceso comentado de ETL en los archivos movies.csv y credits.csv: 
https://github.com/volpo/movies_list_search/tree/main/etl


Se recibieron dos datasets: movies_dataset.csv y credits.csv, los cuales contenían la mayor parte de su informacion anidada en cadenas de texto que 
contenían diccionarios. También contenian muchos valores faltantes en algunas de sus columnas.
se procedió a extraer los diccionarios que estaban anidados y se crearon columnas con esos datos. Para extraer los géneros a los que pertenecían las peliculas se utilizó un sistema similar a one hot encoder. 


# ANÁLISIS EXPLORATORIO DE LOS DATOS 

Análisis exploratorio completo:
https://github.com/volpo/movies_list_search/tree/main/EDA_MOVIES


 <center>Nube de palabras más recurrentes en los titulos de las peliculas
  

<p align="center">
<img src="https://user-images.githubusercontent.com/60153579/249987707-45adbd54-3c8b-4344-b430-360d30539e84.JPG"  height=200>
</p>

<center>Análisis promedio de los votos a los films

<img src="https://user-images.githubusercontent.com/60153579/249987768-1b34d469-8336-4d7f-bb6a-1c27c153c004.JPG"  height=200>

<center>outliers en 'release_year'

<img src="https://user-images.githubusercontent.com/60153579/249987772-78f31880-076e-44f3-b189-7e4c7b6a4810.JPG"  height=200>

<center> IDIOMAS ORIGINALES

<img src="https://user-images.githubusercontent.com/60153579/249987771-07fa9151-f098-4ce4-ac44-5d12a274d28e.JPG"  height=200>



----------------------------------------------------
# MACHINE LEARNING

Para el desarrollo del modelo de recomendación lo que hice fué tomar los géneros que estaban asignados a la pelicula sugerida y con eso filtrar peliculas que coincidieran en al menos dos generos. A su vez, con la libreria NLTK WordNetLemmatizer, tomé los sustantivos y verbos que coincidian en los titulos para filtrar nuevamente la recomendación de las peliculas. 
Luego se retornan las 5 peliculas más similares. 

 <br> 


<br> 
  
### <center>  **Stack Tecnológico**
 Entorno == Python
 API == [FastAPI](https://fastapi.tiangolo.com/) 
 Dashboard ==[Render](https://dashboard.render.com/)
  
EXTRAS:

ETL:Pandas, Numpy, re

 EDA: Ydata-profiling (pandas-profiling package)

 ML:
librerias para python: 
NLTK (Natural Language Toolkit)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

[Video Demostrativo](https://youtu.be/-BmyRvpuGk4)

[Linkedin](https://www.linkedin.com/in/alevolponi/)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''