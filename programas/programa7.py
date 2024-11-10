# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
    reemplazo1 = r'"tag": "T",'
    simplificarT = re.sub(r'"tag": "(.*)",',reemplazo1, texto)

    reemplazo2 = r'"patterns": [\n      "P"\n   '
    simplificarP = re.sub(r'"patterns": [^\]]*',reemplazo2, simplificarT)

    reemplazo3 = r'"responses": [\n      "R"\n   '
    simplificarR = re.sub(r'"responses": [^\]]*',reemplazo3, simplificarP)

    print(simplificarT)
    print(simplificarP)
    print(simplificarR)
    ret = f"{''.join(simplificarR)}"
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
