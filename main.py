from fastapi import FastAPI
import pandas as pd
import locale


df = pd.read_csv('data/df_movies.csv')
df['release_date'] = pd.to_datetime(df['release_date'])

app = FastAPI()


#API 1
@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes: str):
    df["release_date"] = pd.to_datetime(df["release_date"], errors='coerce')
    meses = {"enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6, "julio": 7,
             "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12}
    
    mes_numero = meses.get(mes.lower())
    contador = 0 
    
    for fecha in df["release_date"]:
        if pd.notnull(fecha) and fecha.month == mes_numero:
            contador += 1

    return {'mes': mes, 'cantidad': contador}


#API 2
@app.get("/cantidad_filmaciones_dia/{dia}")
def cantidad_filmaciones_dia(dia:str):
    df["release_date"] = pd.to_datetime(df["release_date"])
    dias_semana = {
    'lunes': 0, 
    'martes' : 1,
    'miercoles' : 2,
    'jueves' : 3,
    'viernes' : 4,
    'sabado' : 5,
    'domingo' :6}
    
    dia_numero = dias_semana.get(dia.lower())
    contador = 0 
    
    for fecha in df["release_date"]:
        if fecha.weekday() == dia_numero:
            contador += 1
    return {'dia':dia, 'cantidad':contador}


#API 3
@app.get("/score_titulo/")
def score_titulo(titulo_de_la_filmacion):
    # Filtrar el DataFrame por el título de la filmación
    pelicula = df[df['title'] == titulo_de_la_filmacion]
    if len(pelicula) > 0:
        # Obtener el año de estreno y la popularidad
        año_estreno = pelicula['release_year'].values[0]
        popularidad = pelicula['popularity'].values[0]

        return {'titulo': titulo_de_la_filmacion, 'anio':año_estreno, 'popularidad': popularidad}
    else:
        return {'titulo': None, 'anio':None, 'popularidad': None}


#API 4
@app.get("/votos_titulo/")
def votos_promedio_titulo(titulo_de_la_filmacion):
    # Filtrar el DataFrame por el título de la filmación
    pelicula = df[df['title'] == titulo_de_la_filmacion]

    # Obtener la cantidad de votos y el valor promedio de las votaciones
    votos = pelicula['vote_count'].values[0]
    promedio_votos = pelicula['vote_average'].values[0]
    año_estreno = pelicula['release_year'].values[0]
    
    if votos >= 2000:
        return {'titulo': titulo_de_la_filmacion, 'anio':año_estreno, 'voto_total': votos, 'voto_promedio': promedio_votos}
    else:
        return {'titulo': None, 'anio':None, 'voto_total': None, 'voto_promedio': None }


#API 5
@app.get("/get_actor/")
def get_actor(nombre_actor: str):
    actor_films = df[df['cast'].apply(lambda x: nombre_actor in x)]
    if actor_films.empty:
        return {"mensaje": "El actor no fue encontrado en ninguna filmación."} 
    
    cantidad_films = actor_films.shape[0]
    retorno_total = actor_films['return'].sum()
    promedio_retorno = actor_films['return'].mean()
    
    return {"actor": nombre_actor, "cantidad_films": cantidad_films, "retorno_total": retorno_total, "promedio_retorno": promedio_retorno}


#API 6
@app.get("/get_director/")
def get_director(nombre_director: str):
    director_data = df[df['crew'].apply(lambda x: nombre_director in x)]
    if director_data.empty:
        return {"mensaje": "Director no encontrado"}
    
    peliculas = []
    retorno_maximo = 0
    exito = None
    
    for _, row in director_data.iterrows():
        pelicula = {
            "titulo": row['title'],
            "fecha_lanzamiento": row['release_date'],
            "retorno": row['return'],
            "costo": row['budget'],
            "ganancia": row['revenue']
        }
        peliculas.append(pelicula)
        
        if row['return'] > retorno_maximo:
            retorno_maximo = row['return']
            exito = row['title']
    
    return {
        "director": nombre_director,
        "exito": exito,
        "peliculas": peliculas}
    
    
    
    
