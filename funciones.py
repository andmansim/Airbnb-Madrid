import csv
# Sin pandas
'''
1. Extraer del fichero de alojamientos una lista con todos los alojamientos, 
donde cada alojamiento sea un diccionario que contenga el identificador del alojamiento, 
el identificador del anfitrión, el distrito, el precio y las plazas.
'''
'''def informacion(): 
    file = open('madrid-airbnb-listings-small.csv', encoding='UTF-8') 
    leer = csv.DictReader(file, delimiter = '\t') #delimiter, para indicar los separadores
    leer = file.readlines()
    
    columnas = leer[0].split('\t')
    datos = ['id', 'host_id', 'neighbourhood_group_cleansed', 'accommodates', 'price']
    traduccion = {'id': 'id_aloj', 'host_id': 'id_anfi', 'neighbourhood_group_cleansed': 'distrito', 
                    'price': 'precio', 'accommodates': 'plazas'}
    
    lista = []
    for line in leer[1:]:
        aloj = {}
        a = line.split('\t')
        for j in range(len(columnas)):
            if columnas[j] in datos:
                aloj[traduccion[columnas[j]]] = a[j]
        lista.append(lista)
    
    return lista
'''
def informacion():
    lista = []
    with open('madrid-airbnb-listings-small.csv', encoding='UTF-8') as file:
        leer = csv.DictReader(file, delimiter = '\t')
        
    for i in leer:
        lista.append(i)

lista_aloj = informacion()
def modificacion(lista_aloj):
    for a in lista_aloj:
        a['id_anfi'] = a['id']
        a['id_aloj'] = a['host_id']
        a['distrito'] = a['neighbourhood_group_cleansed']
        a['precio'] = a['price']
        a['plazas'] = a['accommodates']   
        nuevos = ['id_anfi', 'id_aloj', 'distrito', 'precio', 'plazas' ]
        if a.keys not in nuevos:
            del(a.keys)

    print(lista_aloj)
    return lista_aloj
    
lista_aloj1 = modificacion(lista_aloj)   
print(lista_aloj)
'''for x in range(len(lista_aloj)):
    print(lista_aloj[x])
    print('\n')'''
    
'''
2. Crear una función que reciba la lista de alojamientos y devuelva el número de alojamientos en cada distrito.
'''
def numdistrito(lista_aloj):
    l_d = []
    for a in range(len(lista_aloj)):
        distrito = a.get('distrito')
        l_d.append(distrito)
        
