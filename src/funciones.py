
import pandas as pd
import numpy as np
import re

def limpiar_type(x):

    if pd.isnull(x):        # si es nulo lo convierte a x
        return x
    elif 'Unprovoked' in x:
        return 'Unprovoked'
    elif 'Provoked' in x:
        return 'Provoked'
    else:
        return 'Unprovoked'
    
def limpiar_sex(x):

    if pd.isnull(x):
        return x
    elif 'M' in x:
        return 'Male'
    elif 'F' in x:
        return 'Female'
    else:
        return 'Unknown'
    
def limpiar_fatal(x):
    x = str(x).lower().strip()     # convertimos todo en str, lo pasamos a minusculas y quitamos los espacios que tengan tanto por der como por izq
    if x == 'y':
        return 'Yes'
    elif x == 'n':
        return 'No'
    else:
        return 'Unknown'
    
def limpiar_year(fecha):
    if pd.isna(fecha):
        return 0
    elif len(str(int(fecha))) == 4:
        return fecha
    else:
        return 0
    
def limpiar_country(pais):
    if re.search(r'\b(OCEAN|SEA|PACIFIC|AFRICA|ASIA|DIEGO|BETWEEN)\b', pais, re.IGNORECASE):
        return 'UNKNOWN'
    else:
        return pais
    
def limpiar_age(edad):
       
    # Reemplazar los NaN por 'Unknown'
    if pd.isna(edad):
        return 'Unknown'
    
    # Si la edad contiene un rango, calcular la edad media del rango
    if 'or' in edad:
        edades = re.findall(r'\d+', edad)
        media = (int(edades[0]) + int(edades[1])) / 2
        return int(media)
    
    # Si la edad contiene un rango, calcular la edad media del rango
    if 'to' in edad:
        edades = re.findall(r'\d+', edad)
        media = (int(edades[0]) + int(edades[1])) / 2
        return int(media)
    
    # Si la edad contiene la palabra "months", convertir a años
    if 'month' in edad:
        meses = re.findall(r'\d+', edad)
        return int(int(meses[0]) / 12)
    
    # Convertir strings completamente en palabras a 'Unknown'
    if not re.match(r'^\d+|\d+\.\d+$', edad):
        return 'Unknown'

    # Reemplazar comillas, signos de interrogación por nada
    edad = re.sub(r'[\'"\?]', '', edad)

    # Reemplazar letras por nada
    edad = re.sub(r'[a-zA-Z]', '', edad)

    return edad

def limpiar_time(hora):
       
    # Reemplazar los NaN por 'Unknown'
    if pd.isna(hora):
        return 'Unknown'
    
    # Eliminar espacios en blanco al final del string y convertir strings completamente en palabras a 'Unknown'
    hora = hora.strip()
    if not re.match(r'^\d+|\d+\.\d+$', hora):
        return 'Unknown'

    # Reemplazar '--' por '/' en el formato 'xxhxx/xxhxx'
    hora = hora.replace('--', '/')

    # Reemplazar ' ' por '/' en el formato 'xxhxx/xxhxx'
    hora = hora.replace('  ', ' / ')

    # Eliminar todo después de un guión o una barra, y convertir a formato 'xxhxx'
    hora = re.sub(r'(-|\/).*', '', hora)
    hora = re.sub(r'\D', '', hora)
    if len(hora) == 3:
        hora = f"{hora[:1]}h{hora[1:]:02}"
    elif len(hora) == 4:
        hora = f"{hora[:2]}h{hora[2:]:02}"
    else:
        hora = 'Unknown'

    return hora
