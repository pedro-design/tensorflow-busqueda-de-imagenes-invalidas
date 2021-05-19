# tensorflow-busqueda-de-imagenes-invalidas
busca y detecta problemas en directorios con imagenes, como por ejemplo archivos corruptos o archivos invalidos
* caracteristicas:
 * marca los directorios de manera individual 
 * marca los archivos por directorio
 * devuelve el nombre del archivo invalido 
 * los archivos corruptos los renombra a corrupto y en terminal marca que esta mal con ellos


# guia:dispositivos con python

* este programa requiere de las librerias:
 * PIL 
 * OS
 * TQDM

para correr el analizador solo escribe: pyhton analizar_imagenes.py -d "y aqui va la ruta de la carpeta entre comillas"
              

# guia:dispositivos con windows

en este caso ya se da un archivo comprimido para windows si no se tiene instalado python 
abre una ventana de cmd y cambia al directorio donde se encuentra el ejecutable (con cd /d "y la ruta del directorio")
despues para correr el analizador solo escribe: analizar_imagenes.exe -d "y aqui va la ruta de la carpeta entre comillas"
