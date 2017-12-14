import pandas as pd

nombretabla = 'C:\\Users\\seven\\Python\\projectone\\projectone\\tablas\\'
primero = str(int(raw_input('Anio inicial\n >')))
ultimo = str(int(raw_input('Anio final\n >')))
paisA = raw_input('Pais A\n >')
paisB = raw_input('Pais B:\n >')
inicio = pd.read_excel(nombretabla + primero + '.xlsx')
final = pd.read_excel(nombretabla + ultimo + '.xlsx')
indiceinicio = inicio.set_index("country")
indicefinal = final.set_index("country")
celdaAinicio = indiceinicio.loc[paisA,"gdp"]
celdaBinicio = indiceinicio.loc[paisB, "gdp"]
celdaAfinal = indicefinal.loc[paisA, "gdp"]
celdaBfinal = indicefinal.loc[paisB, "gdp"]


if celdaAinicio > celdaBinicio:
    if celdaAfinal > celdaBfinal:
        print '%s sigue siendo mas rico que %s.' % (paisA, paisB)
    else:
        print '%s supero a %s.' % (paisB, paisA)
elif celdaBinicio > celdaAinicio:
    if celdaBfinal > celdaAfinal:
        print '%s sigue siendo mas rico que %s.' % (paisB, paisA)
    else:
        print '%s supero a %s' % (paisA, paisB)
