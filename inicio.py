import requests 
from bs4 import BeautifulSoup

print("iniciando futuros")

try: 
    url =  "https://es.investing.com/economic-calendar/"
    response = requests.get(url)
    response.raise_for_status()  # Lanza un error para códigos de estado HTTP incorrectos
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)

    #  Encontrar todos los elementos <p> (parrafos de html)
    # El método find_all() es el más común para buscar todas las ocurrencias de una etiqueta.
    parrafos = soup.find_all('table')
    print(parrafos)

except Exception as e:
        print("ocurrió algo inesperado durante la ejecución")
        #return f"se presentó el siguiente error:\n\n {e}