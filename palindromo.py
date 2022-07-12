def es_palindromo(frase):
    frase = frase.lower().replace(" ","")
    if (frase == frase[::-1]):
        return True
    else:
        return False


def run():
    print("*** Programa verifica si la frase que ingresaste es un palíndromo ***")
    
    frase = input("Escribe una frase: ")
    
    if (es_palindromo(frase)):
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")


if __name__ == '__main__':
    run()
