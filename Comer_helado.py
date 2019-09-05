apetece_helado = input("¿Te apetece comer un helado?: (SI / NO)" ).upper()
tienes_dinero = input("¿Tienes dinero para un helado?: (SI / NO)").upper()
esta_el_senor_de_los_helados = input("¿Esta el Señor de los helados?: (SI / NO)").upper()
esta_tia = input("¿Estas con tu Tia?: (SI / NO)").upper()

if apetece_helado == "SI" and (tienes_dinero == "SI" or esta_tia == "SI") and esta_el_senor_de_los_helados == "SI":
    print("Pues comer un helado")
else:
    print("Pues no puedes comer helado")