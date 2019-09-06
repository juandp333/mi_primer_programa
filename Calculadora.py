# Calculadora debe preguntar al usuario que operacion deseas realizar y dos numeros a calcular

primer_numero = int(input("Hola, ¿Cual es el primer numero a calcular?"))
print("ok sera {}".format(primer_numero))

operacion_realizar = input("¿Que operacion deseas ralizar? (Sumar, Restar, Multiplicacion o Dividir)").upper()
print(operacion_realizar)

segundo_numero = int(input("Cual es el segundo numero a calcular?"))
print("Esta bien {}".format(segundo_numero))

if operacion_realizar == "SUMAR":
    print("El resultado es {}".format(primer_numero + segundo_numero))
elif operacion_realizar == "RESTAR":
    print("El resultado es {}".format(primer_numero - segundo_numero))
elif operacion_realizar == "MULTIPLICAR":
    print("El resultado es {}".format(primer_numero * segundo_numero))
elif operacion_realizar == "DIVIDIR":
    print("El resultado es {}".format(primer_numero / segundo_numero))
