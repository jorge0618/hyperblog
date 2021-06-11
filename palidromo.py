

def palindromo(palabra):
    palabra= palabra.replace(" ","") # quitar los espacios del palindromo
    palabra= palabra.lower() #poner todas las letras en minusculas
    palabra_invertida= palabra[::-1] # invierte el orden de las letras
    if palabra == palabra_invertida:
        return True
    else:
        print(palabra_invertida)
        return False

def run():
    palabra= input("Escribe una palabra: ")
    es_palindromo= palindromo(palabra)
    if es_palindromo== True:
        print("Es palindromo")
    else:
        print("No es palindromo")
        

if __name__ == '__main__':
     run()
