menu = """ 
Conversor de monedas
1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = float(input("¿Cuántos pesos colombianos tienes?: "))
    valor_dolar = 3875
    dolares = str(round(pesos / valor_dolar,2))

    if pesos / valor_dolar > 1:
        print("Usted Tiene $" + dolares + " dólares")
    else:
        print("Usted Tiene $" + dolares + " dólar")
elif opcion == 2:
    pesos = float(input("¿Cuántos pesos argentinos tienes?: "))
    valor_dolar = 65
    dolares = str(round(pesos / valor_dolar,2))

    if pesos / valor_dolar > 1:
        print("Usted Tiene $" + dolares + " dólares")
    else:
        print("Usted Tiene $" + dolares + " dólar")
elif opcion == 3:
    pesos = float(input("¿Cuántos pesos méxicanos tienes?: "))
    valor_dolar = 20.79
    dolares = str(round(pesos / valor_dolar,2))

    if pesos / valor_dolar > 1:
        print("Usted Tiene $" + dolares + " dólares")
    else:
        print("Usted Tiene $" + dolares + " dólar")

else:
    print("Ingresa una opción correcta por favor")