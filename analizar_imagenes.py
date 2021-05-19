import PIL
from PIL import Image
import os
from os import listdir
import argparse
PIL.Image.MAX_IMAGE_PIXELS = 999999999
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directorio", help="Nombre del directorio")
args = parser.parse_args()
 
if args.directorio:
    print("analizando: ", args.directorio)
from tqdm import tqdm
i = 0
extenciones_validas=['jpg', 'png', 'jpeg', 'gif', 'bmp' ]
for directory, subdirectories, files, in os.walk(args.directorio): 
 for filename in tqdm(files,desc="procesando directorio "+directory):
  
 
        try :
            im =Image.open(os.path.join(directory,filename),)
        except (IOError, SyntaxError) as e: 
            extencion = os.path.splitext(os.path.join(directory,filename))
            if extencion not in extenciones_validas:
                print(os.path.join(directory,filename," no es un tipo de imagen valido"))
            else:
              i = i +1
             
    
              os.rename(os.path.join(directory,filename), os.path.join(directory,"error"+str(i) + extencion[1]))
              print(e,"new name:","error"+str(i) +".png")
            
