# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
    # tags = re.findall(r'"tag": (.*)', texto) 
    
    # patterns = re.findall(r'"patterns": \[\n      ([^\]]*)', texto)
    # patternsSeparados = re.split('\n', ''.join(patterns))
  
    # responses = re.findall(r'"responses": \[\n      ([^\]]*)',texto)
    # responsesSeparados = re.split('\n', ''.join(responses))

    patterns=re.findall(r'"patterns": \[(.*?)\]', texto, re.DOTALL)
    print(len(patterns))
    print(patterns)
    for i in patterns:
        print(len(patterns(i)))

    ret = []
    # ret.append(str(len(tags)))
    # numPatterns = len(patternsSeparados)-1
    # ret.append(str(numPatterns))
    # numResponses = len(responsesSeparados)-1
    # ret.append(str(numResponses))
    # ret = ' '.join(ret)
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
