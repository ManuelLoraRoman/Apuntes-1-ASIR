#Web scraping es una técnica utilizada mediante programas de software para extraer información de sitios web.
#Por ejemplo, con el siguiente código podemos leer el HTML de una página web.
    #from urllib.request import urlopen
    #response = urlopen('http://tiempoytemperatura.es/espana/sevilla/dos-hermanas.html')
    #lineas=response.readlines()
#En el ejemplo anterior, la página nos da información meteorológica de Dos Hermanas.
#Haz un programa que te muestre la temperatura, presión y humedad actual de Dos Hermanas.


from urllib.request import urlopen

response = urlopen('http://tiempoytemperatura.es/espana/sevilla/dos-hermanas.html')
lineas = response.readlines()
for i in lineas:
    if "<li>" in str(i) and "Dos Hermanas" in str(i):
        print(str(i).replace("b'                <li>","").replace("\\xc2\\xbaC","ºC").replace("\\xc3\\xad","í").replace("\\xc3\\xa1","á")
        .replace("</li>\\n'","").replace("\\xc3\\xb3","ó").replace("\\xc3\\xa9","é").replace("\\xc3\\xa1","á").replace("\\n'",""))
