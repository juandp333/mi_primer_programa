# Adivina un numero
print("Hola ¿Listos para jugar?")
adivina_numero = int(input("Piensa en un numero entero del 1 al 100 para que tu compañero adivine (Que tu compañero no lo vea):"))

prueba_numero = int(input("Adivina el numero de tu compañero: "))

while prueba_numero != adivina_numero:
    print("{} No es el numero".format(prueba_numero))
    prueba_numero = int(input("Adivina el numero de tu compañero: "))

print("Si es {} en nuemro elegido".format(adivina_numero))