import csv
import operator

lista = []
def informacion(lista): 
    file = open('madrid-airbnb-listings-small.csv') 
    #leer = csv.DictReader(file, delimiter = '\t') #delimiter, para indicar los separadores
    leer = file.readlines()
    file.close()
    datos = ['id', 'host_id', 'neighbourhood_group_cleansed', 'accommodates', 'price']
    traduccion = {'id': 'id_aloj', 'host_id': 'id_anfi', 'neighbourhood_group_cleansed': 'distrito', 
                    'price': 'precio', 'accommodates': 'plazas'}
    
    columnas = leer[0].split('\t')
    for i in leer[1:]:
        aloj = {}
        a = i.split('\t')
        for j in range(len(columnas)):
            if columnas[j] in datos:
                aloj[traduccion[columnas[j]]] = a[j]
        lista.append(lista)
    
    return lista


informacion(lista)
for x in range(len(lista)):
    print(lista[x])
    print('\n')

