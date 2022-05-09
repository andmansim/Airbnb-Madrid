from locale import normalize
import pandas as pd 
import matplotlib.pyplot as plt

# Con pandas
'''
1. Preprocesar el fichero de alojamientos para crear un data frame con las variables id, host_id, listing_url, 
room_type, neighbourhood_group_cleansed, price, cleaning_fee, accommodates, minimum_nights, 
minimum_cost, review_scores_rating, latitude, longitude, is_location_exact. 
Eliminar del data frame cualquier fila incompleta. 
Añadir al data frame nuevas variables con el coste mínimo por noche y por persona 
(que incluya los gastos de limpieza).
'''
df = pd.read_csv('madrid.csv', delimiter ='\t', encoding = 'UTF-8')

df.rename(columns= {'id': 'id_aloj', 'host_id': 'id_anfi', 'listing_url': 'url', 
'room_type' : 'tipo_hab', 'neighbourhood_group_cleansed': 'distrito', 'price':'precio', 'cleaning_fee':'limpiar', 'accommodates': 'plazas',
'minimum_nights': 'noches_min', 'review_scores_rating': 'puntuacion', 'latitude': 'latitud',
'longitude': 'longitud', 'is_location_exact': 'localizacion_exact'}, inplace=True)
df1 = df[['id_aloj','id_anfi', 'url', 'tipo_hab', 'distrito', 'precio', 'limpiar', 'plazas', 'noches_min', 'puntuacion']]
#eliminar
df1= df1.dropna()
#reemplazar

df1['precio'] = df1.precio.str.replace(',', '.')
df1['precio'] = df1.precio.str.replace('$', '')
print(df['precio']) # Da error mirar pq
df1['limpiar'] = df1.limpiar.str[1:].astype('float')
print(df1['limpiar'])

df1['precio_per'] = (df1['noches_min'] * df1['precio'] + df1['limpiar'])/(df1['noches_min'] + df1['plazas'])
print('El precio por persona es:')
print(df1['precio_oer'])

'''
2. Crear una función que reciba una lista de distritos y 
devuelva un diccionario con los tipos de alojamiento en ese distrito y
el porcentaje de alojamientos de ese tipo.
'''
#Mirar y hacer
def porcentaje(df, distritos):
    if distritos in df['distrito']:
        for i in distritos:
            df[i].tipo_hab.value_counts(normalize=True) * 100
            
porcentaje(df, ['Centro', 'Salamanca'])
'''
3. Crear una función que reciba una lista de distritos y 
devuelva un diccionario con el número de alojamientos que cada anfitrión ofrece en esos distrito, 
ordenado de más a menos alojamientos.
'''

'''
4. Crear una función que reciba devuelva un diccionario con el número medio de alojamientos por anfitrión de 
cada distrito.
'''

'''
5. Crear una función que reciba una lista de distritos y dibuje un diagrama de sectores con los porcentajes 
de tipos de alojamientos en esos distritos.
'''

'''
6. Crear una función que dibuje un diagrama de barras con el número de alojamientos por distritos.
'''

'''
7. Crear una función que dibuje un diagrama de barras con los porcentajes acumulados de tipos de alojamientos 
por distritos.
'''
'''
8. Crear una función reciba una lista de distritos y una lista de tipos de alojamientos, y dibuje un diagrama 
de sectores con la distribución del número de alojamientos de ese tipo por anfitrión.
'''

'''
9. Crear una función que dibuje un diagrama de barras con los precios medios por persona y día de cada 
distrito.
'''

'''
10. Crear una función que reciba una lista de distritos y dibuje un gráfico de dispersión con el coste mínimo 
por noche y persona y la puntuación en esos distritos.
'''

'''
11. Crear una función que reciba una lista de distritos y dibuje dos histogramas con la distribución de 
precios por persona y día, uno para los alojamientos con título en inglés y otro para los alojamientos con 
títulos en español. Si la distribución es muy asimétrica, aplicar una transformación logarítmica. 
¿Hay diferencias entre los precios de los alojamientos en inglés y el español? Nota: Para identificar el 
idioma puede usare el módulo langdetect.
'''