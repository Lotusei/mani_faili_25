try:
    with open("dati.txt", "r") as fails:
# A. Lasīt visu saturu kā vienu virkni
        viss_saturs = fails.read()
        print("\n--- A. Viss Saturs ---")
        print(viss_saturs)

except FileNotFoundError:
    print("Fails 'dati.txt' nav atrasts. Lūdzu, izveidojiet to.")