def conversor(tipo_pesos, valor_dolar):
    pesos = float(input("¿Cuántos pesos" + tipo_pesos + "tienes?: "))
    dolares = str(round(pesos / valor_dolar,2))
    if pesos / valor_dolar > 1:
        print("Usted Tiene $" + dolares + " dólares")
    else:
        print("Usted Tiene $" + dolares + " dólar")

menu = """ 
Conversor de monedas
1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos",3875)
elif opcion == 2:
    conversor("argentinos",65)
elif opcion == 3:
    conversor("méxicanos",20.79)
else:
    print("Ingresa una opción correcta por favor")