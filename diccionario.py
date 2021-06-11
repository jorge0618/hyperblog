


mi_diccionario={
    'llave 1': 1,
    'llave 2': 2,
    'llave 3': 3
    
}

poblacion_pais = {
        'colombia':45596087,
        'Argentina': 5653434,
        'Perú': 4546423,
           
}
print(mi_diccionario['llave 1'])


for pais in poblacion_pais.keys():
    print(pais)
    
for pais in poblacion_pais.values():
    print(pais)


for pais, poblacion in poblacion_pais.items():    
    print(pais + ' tiene ' + str(poblacion)+ ' habitantes')    
    
    
    
    
