import csv
import pandas as pd
import matplotlib.pyplot as plt


# Sin pandas
'''
1. Extraer del fichero de alojamientos una lista con todos los alojamientos, 
donde cada alojamiento sea un diccionario que contenga el identificador del alojamiento, 
el identificador del anfitrión, el distrito, el precio y las plazas.
'''
#Abrimos el csv y lo pasamos a diccionario
def informacion():
    lista = []
    with open('madrid-airbnb-listings-small.csv', encoding='UTF-8') as file:
        leer = csv.DictReader(file, delimiter = '\t')
        
        for i in leer:
            lista.append(i)
        return lista

#Renombro y borramos los keys
def modificacion(lista_aloj):
    for a in lista_aloj:
        a['id_aloj'] = a['id']
        a['id_anfi'] = a['host_id']
        a['distrito'] = a['neighbourhood_group_cleansed']
        a['precio'] = a['price']
        a['plazas'] = a['accommodates']   
        nuevos = ['id_anfi', 'id_aloj', 'distrito', 'precio', 'plazas' ]
        borrar = []
        for b in a.keys():
            if b not in nuevos:
                borrar.append(b)
        for c in borrar:        
            del(a[c])
 
    
lista_aloj = informacion()    
modificacion(lista_aloj)   
for x in range(len(lista_aloj)):
    print(lista_aloj[x])
    print('\n')
    
'''
2. Crear una función que reciba la lista de alojamientos y devuelva el número de alojamientos en cada distrito.
'''
def numdistrito(lista_aloj):
    l_d = [] 
  
    for a in lista_aloj:
        distrito = a['distrito']
        l_d.append(distrito)

num = numdistrito(lista_aloj)
print(num)
'''
3. Crear una función que reciba la lista de alojamientos y un número de ocupantes y
devuelva la lista de alojamientos con un número de plazas mayor o igual que el número de ocupantes.
'''


'''
4. Crear una función que reciba la lista de alojamientos un distrito, y 
devuelva los 10 alojamientos más baratos del distrito.
'''

'''
5. Crear una función que reciba la lista de alojamientos y devuelva un diccionario con los anfitriones y 
el número de alojamientos que posee cada uno.
'''


# Con pandas
'''
Preprocesar el fichero de alojamientos para crear un data frame con las variables id, host_id, listing_url, 
room_type, neighbourhood_group_cleansed, price, cleaning_fee, accommodates, minimum_nights, 
minimum_cost, review_scores_rating, latitude, longitude, is_location_exact. 
Eliminar del data frame cualquier fila incompleta. 
Añadir al data frame nuevas variables con el coste mínimo por noche y por persona ç
(que incluya los gastos de limpieza).
'''
df = pd.read_csv('madrid-airbnb-listings-small.csv', encoding='UTF-8', delimiter='\t')
df.rename(columns= {'id': 'id_aloj', 'host_id': 'id_anfi', 'listing_url': 'lista_url', 
'room_type' : 'tipo_hab', 'neighbourhood_group_cleansed': 'distrito', 'price':'precio', 'cleaning_fee':'limpiar', 'accommodates': 'plazas',
'minimum_nights': 'noches_min','minimum_cost': 'cost_min', 'review_scores_rating': 'comprobar_nota', 'latitude': 'latitud',
'longitude': 'longitud', 'is_location_exact': 'localizacion_exact'}, inplace=True)
df1 = df[['id_aloj','id_anfi', 'lista_url', 'tipo_hab', 'distrito', 'precio', 'limpiar', 'plazas', 'noches_min',
          'cost_min', 'comprobar_nota', 'latitud', 'longitud', 'localizacion_exact']]
print(df1)