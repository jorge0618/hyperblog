import math

#def potencia():

#LIMITE =1000
#contador=0
#potencia_2 =2**contador

#while potencia_2 < LIMITE:
    #print(potencia_2, contador)
    #contador=contador+1
    #potencia_2= 2**contador 
    
def raiz_cuadrada(numero):
    raiz_cua = math.sqrt(numero)
    print(raiz_cua)


def run():
    numero =int(input("ingrese el número para sacar raiz: "))
    raiz=raiz_cuadrada(numero)
    
if __name__=='__main__':
    run()
