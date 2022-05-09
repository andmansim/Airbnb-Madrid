

'''
Sin usar Pandas:

1. Extraer del fichero de alojamientos una lista con todos los alojamientos, 
donde cada alojamiento sea un diccionario que contenga el identificador del alojamiento, 
el identificador del anfitrión, el distrito, el precio y las plazas.
'''
def informacion(): 
    file = open('madrid-airbnb-listings-small.csv') 
    #leer = csv.DictReader(file, delimiter = '\t') #delimiter, para indicar los separadores
    leer = file.readlines()
    file.close()
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



lista = informacion()
for x in range(len(lista)):
    print(lista[x])
    print('\n')

