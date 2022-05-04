from flask import Flask , render_template, url_for 
import requests
app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template ("inicio.html")  

@app.route("/contacto")
def contacto():
    APPI_KEY ="62ead433"
# CRRAMOS PARAMETROS 
    Titulo ="Avatar"
    # SE CREA UNA URL DE CONSULTA 
    URL = "https://www.omdbapi.com/?apikey="+APPI_KEY+"&t="+Titulo
    print(URL)
    datos_de_pelicula = requests.get(URL)
    print(datos_de_pelicula)
    datos_de_pelicula = datos_de_pelicula.json()
    Titlo_de_pelicula = datos_de_pelicula["Title"]
    directo_de_pelicula = datos_de_pelicula["Director"]
    datos_filtadros={"titulo": Titlo_de_pelicula , "director" : directo_de_pelicula}
    return render_template("contacto.html",datos_de_pelicula = datos_filtadros)




if __name__ == "__main__":
    app.run(debug=True)
