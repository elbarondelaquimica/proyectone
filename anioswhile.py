import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

original = pd.read_excel('C:\Users\seven\Python\ElBueno.xls')
archivonuevo = 'C:\Users\seven\Desktop\shit\Project\\'

for anio in range (1950,2015):
    print "Creando tabla para %d" % anio
    si = original[original['year'] == anio] #muestra solamente aquellas filas en las que year es igual a 1950
    writer = ExcelWriter(archivonuevo + str(anio) + '.xlsx') #defino una variable que toma un archivo Excel y permite escribirlo
    si.to_excel(writer)
    writer.save()
