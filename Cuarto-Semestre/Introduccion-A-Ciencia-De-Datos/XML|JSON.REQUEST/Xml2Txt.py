import requests
import urllib.request
from bs4 import BeautifulSoup
#----Obtener el archivo xml para trabajar----#
#https://sdbrett.com/BrettsITBlog/2017/03/python-parsing-api-xml-response-data/

url = 'http://interaksys.com.mx/curso/peliculas.php?type=xml'
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html,'lxml')
#print(soup.prettify)
"""
<?xml version="1.0" encoding="UTF-8"?>
<html>
 <body>
  <catalogo>
   <pelicula>
    <titulo>
     EL NIÑO CON LA PIJAMA DE RAYAS
    </titulo>
    <director>
     MARK HERMAN
    </director>
    <compania_productora>
     HEYDAY FILMS
    </compania_productora>
    <genero>
     DRAMA
    </genero>
    <anio_estreno>
     2008
    </anio_estreno>
    <duracion>
     94
    </duracion>
   </pelicula>
   ...
  </catalogo>
 </body>
</html>

"""

#----Arrays donde se van a guardar los datos----#
pelicula = [] #numero id de pelicula (debe ser 50)
titulo = []
genero = []
anio = []
duracion = []
productora = []
director = []


peliculas = soup.findAll('pelicula')
#peliculas es una lsita
#print (peliculas[5])

#----Agregar las peliculas a los arrays----#
peliculaIndex = 1
while len(pelicula)<50:
    for item in peliculas:
        pelicula.append(peliculaIndex)
        titulo.append(item.titulo.string)
        genero.append(item.genero.string)
        anio.append(item.anio_estreno.string)
        duracion.append(item.duracion.string)
        productora.append(item.compania_productora.string)
        director.append(item.director.string)
        peliculaIndex +=1

#----Guardar lso vectores a un documeto txt----#
file_name = "Catalogo(xml).txt"
with open(file_name,'w') as txt_file:
    for i in range (len(pelicula)):
        txt_file.write("Pelicula: "+str(pelicula[i])+"\n")
        txt_file.write("Titulo: "+str(titulo[i])+"\n")
        txt_file.write("Genero: "+str(genero[i])+"\n")
        txt_file.write("Año: "+str(anio[i])+"\n")
        txt_file.write("Duracion: "+str(duracion[i])+"\n")
        txt_file.write("Productora: "+str(productora[i])+"\n")
        txt_file.write("Director: "+str(director[i])+"\n\n")
