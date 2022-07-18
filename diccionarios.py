def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # print(mi_diccionario)
    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])
    
    # for llaves in mi_diccionario.keys():
    #     print(llaves)

    # for valores in mi_diccionario.values():
    #     print(valores)

    for llaves, valores in mi_diccionario.items():
        print(f"{llaves} {valores}")

if __name__ == '__main__':
    run()
