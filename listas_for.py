mi_lista = []
input_usuario = input("¿Que necesitas compar? (Escribe FIN para salir): ").upper()

while input_usuario != "FIN":
    mi_lista.append(input_usuario)
    input_usuario = input("¿Que necesitas compar? (Escribe FIN para salir): ").upper()

largo_lista = len(mi_lista)
indice_actual = 0

#esto es cuando se usa WHILE pero cuando se reemplaza por FOR se usa como esta debajo
# while indice_actual < largo_lista:
 #   print("Tengo que conprar {}".format(mi_lista[indice_actual]))
  #  indice_actual += 1

for cosas in mi_lista:
    print("Tengo que comprar {}".format(cosas))

print("Esta es la lista a comprar")