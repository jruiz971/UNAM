import json 
import requests


def LlenarDatos(indice):
    #----Obtener el archivo json para trabajar----#
    response = requests.get("http://interaksys.com.mx/curso/peliculas.php?type=json") #Servidor
    data = response.json()
    keys = data.keys() # ['catalogo']

    #----Obtenemos el catalogo de la forma [{}]----#
    catalogo = data.get('catalogo')
    #print (len(catalogo)) # 10 Registros

    #----Ejemplo de Registros----#
    """{'compania_productora': 'WARNER', 'anio_estreno': '2014',
        'titulo': 'ANNABELLE', 'duracion': '109', 'genero': 'TERROR',
        'director': 'JOHN R. LEONETTI'}"""

    #----Guardar los datos del catalogo en los vectores----#
    N = len(catalogo)

    for i in range (N):
        
        if indice == 0:
            pelicula.append((i+1)) #Mas 1 porque i inicia en 0
        else:
            pelicula.append((indice*10)+(i+1)) #Mas 1 porque i inicia en 0
        productora.append(catalogo[i].get('compania_productora'))
        anio.append(catalogo[i].get('anio_estreno'))
        titulo.append(catalogo[i].get('titulo'))
        duracion.append(catalogo[i].get('duracion'))
        genero.append(catalogo[i].get('genero'))
        director.append(catalogo[i].get('director'))
    return N

def ExportarATxt():
    file_name = "Catalogo(json).txt"
    with open(file_name,'w') as txt_file:
        for i in range (len(pelicula)):
            txt_file.write("Pelicula: "+str(pelicula[i])+"\n")
            txt_file.write("Titulo: "+str(titulo[i])+"\n")
            txt_file.write("Genero: "+str(genero[i])+"\n")
            txt_file.write("Año: "+str(anio[i])+"\n")
            txt_file.write("Duracion: "+str(duracion[i])+"\n")
            txt_file.write("Productora: "+str(productora[i])+"\n")
            txt_file.write("Director: "+str(director[i])+"\n\n")




if __name__=='__main__':
    indice = 0
    
    
    #----Arrays donde se van a guardar los datos----#
    pelicula = [] #numero id de pelicula (debe ser 50)
    titulo = []
    genero = []
    anio = []
    duracion = []
    productora = []
    director = []
    
    while len(pelicula)<50:
        LlenarDatos(indice)
        indice +=1
        ExportarATxt()
   
