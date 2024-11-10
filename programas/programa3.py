# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
    
    x = re.findall(r'"tag": "(.*)",',texto) #Todos los tags

    ret = []
    tags = re.findall(r'"tag": .*',texto)

    for i in range(0,len(x)):
        patron = tags[i] + '\n   "patterns": \[\n' + r'([^\]]*)'
        patterns =re.findall(patron,texto, flags=re.MULTILINE)
        patternsPlusSalto = re.split("\n",''.join(patterns)) #Me va a dar todos los elementos separados por coma, le sobra 1 para ser el num elems de patterns
        numPatterns = (len(patternsPlusSalto)-1)
        ret.append(x[i])
        ret.append(' ' + str(numPatterns))
        ret.append('\n')


    ret = ''.join(ret)
    return ret

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    f = open(entrada, 'r') # abrir archivo entrada
    datos = f.read()       # leer archivo entrada
    f.close()              # cerrar archivo entrada
    
    ret = prog(datos)      # ejecutar er
    
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
