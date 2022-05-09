import csv
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
        a['id_anfi'] = a['id']
        a['id_aloj'] = a['host_id']
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
    cont = 0
    for a in range(len(lista_aloj)):
        distrito = a.get('distrito')
        l_d.append(distrito)
    for c in range(len(l_d)):
        if l_d[c] == l_d[c + 1]:
            cont = cont + 1

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
