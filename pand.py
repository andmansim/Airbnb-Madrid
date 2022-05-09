import pandas as pd 
import matplotlib.pyplot as plt

# Con pandas
'''
Preprocesar el fichero de alojamientos para crear un data frame con las variables id, host_id, listing_url, 
room_type, neighbourhood_group_cleansed, price, cleaning_fee, accommodates, minimum_nights, 
minimum_cost, review_scores_rating, latitude, longitude, is_location_exact. 
Eliminar del data frame cualquier fila incompleta. 
Añadir al data frame nuevas variables con el coste mínimo por noche y por persona ç
(que incluya los gastos de limpieza).
'''



df = pd.read_csv('madrid.csv', delimiter ='\t', encoding = 'UTF-8')
print (df)

'''df.rename(columns= {'id': 'id_aloj', 'host_id': 'id_anfi', 'listing_url': 'lista_url', 
'room_type' : 'tipo_hab', 'neighbourhood_group_cleansed': 'distrito', 'price':'precio', 'cleaning_fee':'limpiar', 'accommodates': 'plazas',
'minimum_nights': 'noches_min','minimum_cost': 'cost_min', 'review_scores_rating': 'comprobar_nota', 'latitude': 'latitud',
'longitude': 'longitud', 'is_location_exact': 'localizacion_exact'}, inplace=True)
df1 = df[['id_aloj','id_anfi', 'lista_url', 'tipo_hab', 'distrito', 'precio', 'limpiar', 'plazas', 'noches_min',
          'cost_min', 'comprobar_nota', 'latitud', 'longitud', 'localizacion_exact']]
print(df1)'''
