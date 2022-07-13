def imprimir_potencia(base, potencia, final):
    pass


def run():
    LIMITE = 1000
    contador = 0
    potencia_2 = 2**contador
    while(potencia_2 < 1000000):
        print(f"2 elevado a {contador} es igual a: {2**contador}")
        contador += 1
        potencia_2 = 2**contador

if __name__ == '__main__':
    run()

