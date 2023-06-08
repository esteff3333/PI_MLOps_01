from fastapi import FastAPI
import csv
import sklearn
import pandas as pd
app = FastAPI()


# Cargar el primer dataset
df = pd.read_csv('ruta_del_archivo1.csv')

# Cargar el segundo dataset
df2 = pd.read_csv('ruta_del_archivo2.csv')

# Cargar el primer dataset
merged_df = pd.read_csv('ruta_del_archivo1.csv')



#API 1
@app.get("/filmaciones/{mes}")
def cantidad_filmaciones_mes(mes):
    fechas = pd.to_datetime(df['release_date'], format='%Y-%m-%d')
    nmes = fechas[fechas.dt.month_name(locale='es_CO') == mes.capitalize()]
    respuesta = nmes.shape[0]
    return {'mes': mes, 'cantidad': respuesta}



#API 2
@app.get("/cantidad_filmaciones/{dia}")
def cantidad_filmaciones_dia(dia):
    fechas=pd.to_datetime(df['release_date'],format='%Y-%m-%d')
    ndia=fechas[fechas.dt.day_name(locale='es_CO')==dia.capitalize()]
    respuesta=ndia.shape[0]
    return {'dia':dia, 'cantidad':respuesta}



#API 3
@app.get("/titulo_de_la_filmacion/")
def score_titulo(titulo_de_la_filmacion):
    pelicula = df[df['original_title'] == titulo_de_la_filmacion]

    if len(pelicula) > 0:
        año_estreno = pelicula['release_date'].values[0].split('-')[0]
        popularidad = pelicula['popularity'].values[0]

        return titulo_de_la_filmacion, año_estreno, popularidad
    else:
        return None

# Ejemplo de uso de la función score_titulo
titulo = ''
resultado = score_titulo(titulo)

if resultado:
    titulo, año_estreno, popularidad = resultado
    print(f"Título: {titulo}")
    print(f"Año de estreno: {año_estreno}")
    print(f"Popularidad: {popularidad}")
else:
    print("No se encontró información para el título de la filmación.")




#API 4
@app.get("/votos_promedio_titulo/")
def votos_promedio_titulo(titulo_de_la_filmacion):
    # Filtrar el DataFrame por el título de la filmación
    pelicula = df[df['original_title'] == titulo_de_la_filmacion]

    # Obtener la cantidad de votos y el valor promedio de las votaciones
    votos = pelicula['vote_count'].values[0]
    promedio_votos = pelicula['vote_average'].values[0]

    if votos >= 2000:
        return titulo_de_la_filmacion, votos, promedio_votos
    else:
        return None

# Ejemplo de uso de la función votos_promedio_titulo
titulo = ''
resultado = votos_promedio_titulo(titulo)

if resultado:
    titulo, votos, promedio_votos = resultado
    print(f"Título: {titulo}")
    print(f"Cantidad de votos: {votos}")
    print(f"Valor promedio de las votaciones: {promedio_votos}")
else:
    print("La filmación no cumple con la condición de tener al menos 2000 valoraciones.")







with open('database/books.csv', mode='r') as file:
    reader = csv.DictReader(file)

    conn = engine.connect()
    conn.begin()
    for book in reader:
        conn.execute(books.insert().values(book))
    conn.commit()
    conn.close()
