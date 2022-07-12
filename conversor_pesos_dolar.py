
print("*** Programa que convierte los pesos Méxicanos a Dólares. ***")
pesos = float(input("¿Cuántos pesos Méxicanos tienes?: "))
valor_dolar = 20.79
dolares = str(round(pesos / valor_dolar,2))

if pesos / valor_dolar > 1:
    print("Usted Tiene $" + dolares + " dólares")
else:
    print("Usted Tiene $" + dolares + " dólar")