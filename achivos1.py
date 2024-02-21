
from io import open_code

archivo_text = open('anombres.txt', 'r')

#archivo_text.write('\n datos en el archivo')
#archivo_text.close()

#print(archivo_text.read())

#archivo_text.seek(0)
#print(archivo_text.read())

for lineas in archivo_text.readlines():
    print(lineas.rstrip())

archivo_text.close()