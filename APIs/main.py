import requests
import json

#Descargar contenido desde url por Python

if __name__ == '__main__':
    url = 'https://kodirecto.com/wp-content/uploads/BJJ-para-reutilizacion.jpg'

    response = requests.get(url, stream=True) #Realiza la solicitud sin descargar
    with open('image.jpg', 'wb') as file:
        for chunk in response.iter_content(): #Descarga el contenido poco a poco
            file.write(chunk)

    response.close()