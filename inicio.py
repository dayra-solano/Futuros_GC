import requests 
import pandas as pd  
import numpy as np
from bs4 import BeautifulSoup

print("iniciando futuros")

try: 
    url =  "https://es.investing.com/economic-calendar/"
    response = requests.get(url)
    response.raise_for_status()  # Lanza un error para códigos de estado HTTP incorrectos
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)

    #  Encontrar todos los elementos <p> (tabla de html)
    # El método find_all() es el más común para buscar todas las ocurrencias de una etiqueta.
    tabla_id = "economicCalendarData"
    tabla = soup.find('table', {'id': tabla_id})

    #print(tabla)

    if tabla:
          # Obtener todas las filas de la tabla (<tr>) 
          filas = tabla.find('tbody').find_all('tr') 
          print(f"Éxito: Se han encontrado {len(filas)} filas en la tabla.") 
          #print(filas)

          datos= []
          for i, fila in enumerate(filas): 
            #print(f"Fila {i+1}: {fila}")
            datos.append([celda.get_text(strip=True) for celda in fila.find_all('td')])
          
          print(datos)
          
          print(datos[1:])

          data=np.array(datos[1:])    
          print(data)      
          df=pd.DataFrame(data,columns=['hora','pais','na1','evento','actual','prevision','anterior','na2'])
          df.head(5)
          df.to_csv("noticias.csv",index=False)


    else: 
        print(f" Error: No se encontró la tabla con ID: '{tabla_id}'.") 
   

except Exception as e:
        print(f"ocurrió algo inesperado durante la ejecución:\n\n {e}")
        #return f"se presentó el siguiente error:\n\n {e}