from fastapi import FastAPI
app = FastAPI()

import pandas as pd


movies_final = pd.read_csv('movies_final.csv',low_memory=False)
casting_final = pd.read_csv('casting_final.csv', sep=',',  low_memory=False)
director_final = pd.read_csv('directores_final.csv', sep=',',  low_memory=False)


@app.get("/")
def index():

    '''
    "Para saber la cantidad de peliculas que se estrenaron ese mes historicamente /cantidad_filmaciones_mes/{mes}   
    "Para retornar la cantidad de peliculas que se estrenaron ese dia historicamente /cantidad_filmaciones_dia/{dia} 
    "Ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score /score_titulo/{titulo}
    "Ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones /votos_titulo/{titulo}
    "Ingresa nombre de director para devolver el éxito del mismo medido a través del retorno, nombre de sus películas,"
    "Con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma. /get_director{nombre_director} 
    'Ingresas un nombre de pelicula y te recomienda las similares en una lista. /recomendacion/{titulo}'

    '''

    q1 = ["Para saber la cantidad de peliculas que se estrenaron ese mes historicamente /cantidad_filmaciones_mes/{mes}     "]
    q2 = ["Para retornar la cantidad de peliculas que se estrenaron ese dia historicamente /cantidad_filmaciones_dia/{dia}    "]
    q3 = ["Ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score /score_titulo/{titulo}    "]
    q4 = ["Ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones /votos_titulo/{titulo}    "]
    q5 = ["Ingresa nombre de actor para devolver el éxito a través del retorno y cantidad de películas que participó y el promedio de retorno /get_actor/{nombre_actor}   "]  
    q6 = ["Ingresa nombre de director para devolver el éxito del mismo medido a través del retorno, nombre de sus películas,"
         "Con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma. /get_director{nombre_director}   "]
    q8 = ['Ingresas un nombre de pelicula y te recomienda las similares en una lista. /recomendacion/{titulo}']

    indice = q1+q2+q3+q4+q5+q6+q8
    return indice

#----------------------------------------------------------------------------------------------------------------------------------------

@app.get('/cantidad_filmaciones_mes/{mes}')
def cantidad_filmaciones_mes(mes:str):
    ''' Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset'''
    qmes=mes.capitalize()
    meses = {
        "Enero": 1,
        "Febrero": 2,
        "Marzo": 3,
        "Abril": 4,
        "Mayo": 5,
        "Junio": 6,
        "Julio": 7,
        "Agosto": 8,
        "Setiembre": 9,
        "Octubre": 10,
        "Noviembre": 11,
        "Diciembre": 12
    }

    #Convertir el tipo de la columna 'release_date' al tipo datetime
    movies_final['release_date'] = pd.to_datetime(movies_final['release_date'])
    # Filtrar el dataframe para obtener las peliculas estrenadas en ese mes
    peliculas_mes = movies_final[movies_final['release_date'].dt.month == meses.get(qmes)]
    respuesta = len(peliculas_mes)
    return {'mes':mes, 'cantidad':respuesta}


@app.get('/cantidad_filmaciones_dia/{dia}')
def cantidad_filmaciones_dia(dia:str):
    '''Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrenaron ese dia historicamente'''
    qdia=dia.capitalize()
    dias = {
        "Lunes": 0,
        "Martes": 1,
        "Miercoles": 2,
        "Jueves": 3,
        "Viernes": 4,
        "Sabado": 5,
        "Domingo": 6
    }    

    #Convertir el tipo de la columna 'release_date' al tipo datetime
    movies_final['release_date'] = pd.to_datetime(movies_final['release_date'])
    # Filtrar el dataframe para obtener las peliculas estrenadas en ese dia
    peliculas_dia = movies_final[movies_final['release_date'].dt.day_of_week == dias.get(qdia)]
    respuesta = len(peliculas_dia)
    
    return {'dia':dia, 'cantidad':respuesta}

@app.get('/score_titulo/{titulo}')
def score_titulo(titulo:str):
    '''Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score'''
    titulo = titulo.lower()
    movies_final["title"] = movies_final["title"].str.lower()
    df_query = movies_final[movies_final["title"].str.contains(titulo)]
    tot_sel=df_query['title'].count()
    if tot_sel == 0:
        return {'No se encontraron películas similares al título ingresado'}
    
    titulo=df_query['title'].iloc[0]
    titulo=titulo.title()
    anio = df_query['release_year'].astype('str').iloc[0]
    popularidad = df_query['popularity'].iloc[0]
    
    return {'titulo':titulo, 'anio':anio, 'popularidad':popularidad}

@app.get('/votos_titulo/{titulo}')
def votos_titulo(titulo: str):
    '''Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. 
    La misma variable deberá de contar con al menos 2000 valoraciones, 
    caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningún valor.'''
    titulo = titulo.lower()
    # Filtrar el dataframe para obtener las peliculas con el título ingresado
    movies_final["title"] = movies_final["title"].str.lower()
    peliculas_filtradas = movies_final[movies_final['title'] == titulo]
    
    if len(peliculas_filtradas) > 0:
        # Seleccionar la primera fila del dataframe
        pelicula_seleccionada = peliculas_filtradas.iloc[0] 
        voto_total = int(pelicula_seleccionada['vote_count'])
        voto_promedio = pelicula_seleccionada['vote_average']
        
        if voto_total >= 2000:
            return {'titulo': titulo, 'voto_total': voto_total, 'voto_promedio': voto_promedio}
        else:
            return {"mensaje": f"La cantidad de votos de la película {titulo} no supera los 2000 votos, por ende no se devuelve ningún valor"}
    else:
        return {"mensaje": f"No se encontró ninguna película con el título {titulo}"}


@app.get('/get_actor/{nombre_actor}')
def get_actor(nombre_actor:str):
    '''Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
    Además, la cantidad de películas que en las que ha participado y el promedio de retorno'''
    nombre_actor = nombre_actor.lower() #convierto en minuscula la variables
    casting_final["name_actor"] = casting_final["name_actor"].str.lower() #convierto en minuscula la columna
    df_total=pd.merge(movies_final, casting_final, on = 'id', how = 'inner')
    df_query = df_total[df_total["name_actor"].str.contains(nombre_actor)]
    tot_sel=df_query['name_actor'].count()
    
    if tot_sel == 0:
        return {'No se encontraron películas para el nombre de actor ingresado'}
    
    nombre_actor = nombre_actor.title()
    retorno_total = df_query['return'].sum()
    retorno_promedio = df_query['return'].mean()
    return {'actor':nombre_actor, 'cantidad_filmaciones':str(tot_sel), 'retorno_total':str(retorno_total), 'retorno_promedio':str(retorno_promedio)}
    
# ------------------------------------------------------------------------------------------------------------------    

@app.get('/get_director/{nombre_director}')
def get_director(nombre_director:str):
    ''' Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
    Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.'''
     # Convertir a minúsculas la variable
    nombre_director = nombre_director.lower()

    # Convertir a minúsculas la columna 'nombre_director'
    director_final["nombre_director"] = director_final["nombre_director"].str.lower()

    # Merge de los dos DataFrames
    df_total = pd.merge(movies_final, director_final, on='id', how='inner')

    # Obtener el éxito total del director (retorno_total_director)
    retorno_total_director = df_total[df_total['nombre_director'] == nombre_director]

    # Sumar los valores de la columna 'return' en las filas coincidentes
    suma_retorno = retorno_total_director['return'].sum()

    # Obtener información de cada película del director
    peliculas = df_total[df_total['nombre_director'] == nombre_director]

    # Convertir el DataFrame en una lista de diccionarios
    peliculas = peliculas.to_dict(orient='records')

    # Crear una lista para almacenar la información de cada película
    peliculas_info = []

    # Obtener información de cada película (nombre, año, retorno, presupuesto y ganancias)
    for pelicula in peliculas:
        nombre_pelicula = pelicula['title']
        anio_lanzamiento = pelicula['release_year']
        retorno_pelicula = pelicula['return']
        budget_pelicula = pelicula['budget']
        revenue_pelicula = pelicula['revenue']

        # Agregar la información de la película a la lista
        peliculas_info.append({
            'pelicula': nombre_pelicula,
            'anio': anio_lanzamiento,
            'retorno_pelicula': retorno_pelicula,
            'budget_pelicula': budget_pelicula,
            'revenue_pelicula': revenue_pelicula
        })
        # Crear y retornar el diccionario con la información del director y sus películas
    return {
        'director': nombre_director,
        'retorno_total_director': suma_retorno,
        'peliculas': peliculas_info
    }

# --------------------------------------------------------------------------------------------------    

# ML
@app.get('/recomendacion/{titulo}')
def recomendacion(titulo:str):
    '''Ingresas un nombre de pelicula y te recomienda las peliculas similares tomando como variable su popularidad y su género. devuelve una lista'''
    # Convertir a minúsculas la variable
    titulo = titulo.lower()

    # Convertir a minúsculas la columna 'title'
    movies_final["title"] = movies_final["title"].str.lower()

    # Obtener las puntuaciones de la película dada
    puntuaciones = movies_final[movies_final['title'] == titulo][['title', 'popularity']]
    if puntuaciones.empty:
        return []  # La película no se encuentra en el dataset
    
    # Eliminar duplicados de títulos y mantener solo la película de mayor popularidad
    puntuaciones = puntuaciones.drop_duplicates(subset='title', keep='first')
    
    # Filtrar las películas que coinciden en al menos dos géneros
    peliculas_coincidentes = movies_final[movies_final.apply(lambda row: row['title'] != titulo and sum(row[genre] == 1 for genre in ['Animation', 'Comedy', 'Family', 'Adventure', 'Fantasy', 'Romance', 'Drama', 'Action', 'Crime', 'Thriller', 'Horror', 'History', 'Science Fiction', 'Mystery', 'War', 'Foreign', 'Music', 'Documentary', 'Western', 'TV Movie']) == 3, axis=1)].copy()
    
    # Calcular la similitud de puntuación entre esa película y el resto
    peliculas_coincidentes['similarity'] = peliculas_coincidentes['popularity'].apply(lambda x: abs(x - puntuaciones['popularity'].iloc[0]))
    
    # Ordenar las películas según el score de similitud
    peliculas_ordenadas = peliculas_coincidentes.sort_values(by='similarity')
    
    # Obtener las 5 películas más similares
    peliculas_recomendadas = peliculas_ordenadas.head(5)['title'].tolist()
            
    return {'lista recomendada': peliculas_recomendadas}

# -----------------------------------------------------------------------

# Ejecutar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)