import pandas as pd 
import matplotlib.pyplot as plt

# Con pandas
'''
Preprocesar el fichero de alojamientos para crear un data frame con las variables id, host_id, listing_url, 
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

