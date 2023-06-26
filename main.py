from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def index():
    q1 = ["Para retornar la cantidad de peliculas que se estrenaron ese mes historicamente /cantidad_filmaciones_mes/{mes}     "]
    q2 = ["Para retornar la cantidad de peliculas que se estrenaron ese dia historicamente /cantidad_filmaciones_dia{dia}    "]
    q3 = ["Ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score /score_titulo/{titulo}    "]
    q4 = ["Ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones /votos_titulo/{titulo}    "]
    q5 = ["Ingresa nombre de actor para devolver el éxito a través del retorno y cantidad de películas que participó y el promedio de retorno /get_actor/{nombre_actor   "]  
    q6 = ["Ingresa nombre de director para devolver el éxito del mismo medido a través del retorno, nombre de sus películas,     "]
    q7 = q6 + ["Con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma. /get_director(nombre_director)   "]
    q8 = ['Ingresas un nombre de pelicula y te recomienda las similares en una lista. /recomendacion/{titulo}']

    indice = q1+q2+q3+q4+q5+q6+q7+q8
    return indice

@app.get('/cantidad_filmaciones_mes/{mes}')
def cantidad_filmaciones_mes(mes:str):
    '''Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes historicamente'''
    return {'mes':mes, 'cantidad':'respuesta'}

@app.get('/cantidad_filmaciones_dia{dia}')
def cantidad_filmaciones_dia(dia:str):
    '''Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrebaron ese dia historicamente'''
    return {'dia':dia, 'cantidad':'respuesta'}

@app.get('/score_titulo/{titulo}')
def score_titulo(titulo:str):
    '''Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score'''
    return {'titulo':titulo, 'anio':'respuesta', 'popularidad':'respuesta'}

@app.get('/votos_titulo/{titulo}')
def votos_titulo(titulo:str):
    '''Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. 
    La misma variable deberá de contar con al menos 2000 valoraciones, 
    caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.'''
    return {'titulo':titulo, 'anio':'respuesta', 'voto_total':'respuesta', 'voto_promedio':'respuesta'}

@app.get('/get_actor/{nombre_actor}')
def get_actor(nombre_actor:str):
    '''Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
    Además, la cantidad de películas que en las que ha participado y el promedio de retorno'''
    return {'actor':nombre_actor, 'cantidad_filmaciones':'respuesta', 'retorno_total':'respuesta', 'retorno_promedio':'respuesta'}

@app.get('/get_director/{nombre_director}')
def get_director(nombre_director:str):
    ''' Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
    Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.'''
    return {'director':nombre_director, 'retorno_total_director':'respuesta', 
    'peliculas':respuesta, 'anio':'respuesta', 'retorno_pelicula':'respuesta', 
    'budget_pelicula':respuesta, 'revenue_pelicula':'respuesta'}