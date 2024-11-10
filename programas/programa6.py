# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
    x = re.findall(r'"tag": "(.*)",',texto) #Todos los tags
    tags = re.findall(r'"tag": .*',texto)


    for i in range(0,len(x)):
#Patterns
        pattern = tags[i] + r'[^\]]*'
        textoPorTagHastaPatterns = ''.join(re.findall((pattern),texto))

        loQueDejoPat = r'"patterns": [\n      [^\"]*\"[^\"]*"'
        primerPat = ''.join(re.findall(loQueDejoPat,textoPorTagHastaPatterns))

        primPat = re.split(": \[\n      ",primerPat)

        pat1Patt = r'"patterns": \[\n      '+primPat[1]+'[^\]]*'
        pat2Patt = primerPat+'\n   '
        texto = re.sub(pat1Patt, pat2Patt, texto)

#Responses
        patron2 = tags[i]+ r'[^\]]*\][^\]]*'
        textoPorTag =  ''.join(re.findall((patron2),texto))

        loQueDejoRes = r'"responses": [\n      [^\"]*\"[^\"]*"'
        primerResp = ''.join(re.findall(loQueDejoRes,textoPorTag))
        #print(primerResp)
        primRes = re.split(": \[\n      ",primerResp)
        #print(prim[1])
        
        pat1Response= r'"responses": \[\n      '+primRes[1]+'[^\]]*'
        pat2Response= primerResp+'\n   '
        texto = re.sub(pat1Response,pat2Response,texto)  
    #OBSERVACION
    #no toma las entradas 1 porquee tiene un ( del ":(" y no ejecuta porque no está cerrado, no sé si lo consideraría un error
    return texto



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
