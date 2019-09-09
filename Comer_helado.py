
apetece_helado_input = input("¿Te apetece comer un helado?: (SI / NO)").upper()

if apetece_helado_input == "SI":
   apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("Te he dicho que me digas SI o NO, no se que has dicho pero cuento como que no")
    apetece_helado_input == False

tienes_dinero_input = input("¿Tienes dinero para un helado?: (SI / NO)").upper()
esta_el_senor_de_los_helados_input = input("¿Esta el Señor de los helados?: (SI / NO)").upper()
esta_tia_input = input("¿Estas con tu Tia?: (SI / NO)").upper()

apetece_helado = apetece_helado_input == "SI"
tienes_dinero = tienes_dinero_input == "SI"
esta_tu_tia = esta_tia_input == "SI"
puedes_permitirtelo = tienes_dinero or esta_tu_tia
esta_el_senor_de_los_helados = esta_el_senor_de_los_helados_input == "SI"

if apetece_helado and puedes_permitirtelo and esta_el_senor_de_los_helados:
    print("Pues comer un helado")
else:
    print("Pues no puedes comer helado")