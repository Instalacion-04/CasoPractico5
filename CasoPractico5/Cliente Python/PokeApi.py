#Uso de la PokeApi
#Instalamos la libreria con ->pip install requests
import requests
import matplotlib.pyplot as plt
import matplotlib.image as img
from requests.api import request
from requests.models import Response

#Devuelve un pokemon de aucerdo a su nombre
pokemon = input("Introduce el nombre del POKEMON: ")
url = "https://pokeapi.co/api/v2/pokemon/" + pokemon

respuesta= requests.get(url)

if respuesta.status_code !=200 :
    print("Pokemon no encontrado")
    exit()

imagen = img.imread(respuesta.json()['sprites']['front_default'])
plt.title(respuesta.json()['name'])
imgplot=plt.imshow(imagen)
plt.show()
#########################################


#Devuelve una imagen 
if __name__== '__main__':
    url='https://imgur.com/aJjAf4M.jpg'

    response= requests.get(url,stream=True)
    with open('image.jpg', 'wb') as file :
            for chunk in response.iter_content():
                file.write(chunk)

    response.close()
##################################################


#Devuelve un listado de peliculas con informacion
respuesta= requests.get('https://yts.mx/api/v2/list_movies.json')
data=respuesta.json()
result =data['data']
movies=result ['movies']


for movie  in movies:
        titulo =movie['title']
        anio=movie['year'] 
        genero=movie['genres']
        print('Titulo:', titulo)
        print('Genero:', genero)
        print('Año:', anio)
        print("\n")
#####################################################  
