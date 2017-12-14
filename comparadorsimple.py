import pandas as pd

nombretabla = 'C:\\Users\\seven\\Python\\projectone\\projectone\\tablas\\'
inicial = str(int(raw_input('Anio\n >')))
paisA = raw_input('Pais A\n >')
paisB = raw_input('Pais B:\n >')
original = pd.read_excel(nombretabla + inicial + '.xlsx')
indice = original.set_index("country")
celdaA = indice.loc[paisA,"gdp"]
celdaB = indice.loc[paisB, "gdp"]

if celdaA > celdaB:
    print 'En %s %s era mas rica que %s.' % (inicial, paisA, paisB)
else:
    print 'En %s %s era mas rica que %s.' % (inicial, paisB, paisA)
