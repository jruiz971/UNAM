Author: *Juan Luis Ruiz Vanegas*
email: *juanluisruiz971@gmail.com*

#------- Descripcion -------# 
Los datos de los que vamos a hacer las peticiones json y xml se encuentran en la pagina 

xml -> http://interaksys.com.mx/curso/peliculas.php?type=xml;
json -> http://interaksys.com.mx/curso/peliculas.php?type=json

Las listas de peliculas son mostradsa de diez elementos.

Los datos de las peliculas son procesados y exportados a en un archivo .txt y se van a mostrar de la siguiente manera: 
´´´
Pelicula: 1
Titulo: IN-ACTIVIDAD PARNORMAL
Genero: COMEDIA
Año: 2014
Duracion: 86
Productora: WAYANS BROS ENTERTAINMENT
Director: MICHAEL TIDDES
´´´
#------- Requerimientos -------#

Es necesario usar python3; asi como sus librerias:

- json
- requests
- urllib.request
- BeautifulSoup

Tambien contar con un parser.
    Si no lo tiene, ejecutar:
    
    - sudo pip3 install lxml

    
#------- Para correr el programa -------#

Es necesario estar en el directorio en el que se tienen los archivos Json2Txt.py y Xml2Txt.py

- python3 Json2Txt.py 
- python3 Xml2Txt.py
