import csv

def istabu_skaits():
    while True:
        majas = []

# komandas atrod un atlasa mājas ar izvēlēto skaitu guļamistabu
        with open('Maju_cenas.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # izlaižam virsrakstus
            
            for rinda in reader:
                if len(rinda) != 0:           # ja rinda nav tukša
                    majas.append(rinda)

            # Ja nav datu
            if len(majas) == 0:
                print("Failā nav prasīto guļamistabu skaits")
                break
                
            
            mekle_maja = input("\nCik guļamistabas vēlaties? (piem. 2 - 5): ").strip().upper()

            atrastie = []
            for maja in majas:
                if maja[2] == mekle_maja:
                    atrastie.append(maja)

            if len(atrastie) > 0:
                print(f"\nMājas ar {mekle_maja} guļamistabām: \ncena  kubikmetri")
        #         print (atrastie)
                for s in atrastie:
                    print(f"• {s[0]} {s[1]}")
                    
            break

#  mājas ar izvēlēto skaitu guļamistabu tiek eksportētas uz atsevišķu failu
    # Eksportējam uz atsevišķu failu
    faila_nosaukums = mekle_maja + "_istabu_cenas.csv"
    with open(faila_nosaukums, 'w', newline='', encoding='utf-8') as eks:
        writer = csv.writer(eks)
        writer.writerow(['cena','kubikmetri','guļamistabas','vannasistabas','sāvi','pie galvenāceļa','viesistabas','pagrabs','apkures katls','gaisa kondicionieris','parkošanās','prefarea','mēbeles'])
        for s in atrastie:
            writer.writerow(s)

        print(f"\nSaglabāts failā: {faila_nosaukums}")

# komandas atrod un atlasa mājas ar izvēlēto skaitu vannasistabu
    while True:
        majas = []

        with open( faila_nosaukums , 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # izlaižam virsrakstus
            
            for rinda in reader:
                if len(rinda) != 0:           # ja rinda nav tukša
                    majas.append(rinda)

            # Ja nav datu
            if len(majas) == 0:
                print("Failā nav prasīto vannasistabu skaits")
                break
                
            
            mekle_maja2 = input("\nCik vannasistabas vēlaties? (piem. 1 - 4): ").strip().upper()

            atrastie = []
            for maja in majas:
                if maja[3] == mekle_maja2:
                    atrastie.append(maja)

            if len(atrastie) > 0:
                print(f"\nMājas ar {mekle_maja} guļamistabām un {mekle_maja2} vannasistabām: \ncena  kubikmetri")
        #         print (atrastie)
                for s in atrastie:
                    print(f"• {s[0]} {s[1]}")
                    
            break

#  mājas ar izvēlēto skaitu vannasistabām tiek eksportētas uz atsevišķu failu
    # Eksportējam uz atsevišķu failu
    faila_nosaukums2 = mekle_maja + "+" + mekle_maja2 + "_istabu_cenas.csv"
    with open(faila_nosaukums2, 'w', newline='', encoding='utf-8') as eks:
        writer = csv.writer(eks)
        writer.writerow(['cena','kubikmetri','guļamistabas','vannasistabas','sāvi','pie galvenāceļa','viesistabas','pagrabs','apkures katls','gaisa kondicionieris','parkošanās','prefarea','mēbeles'])
        for s in atrastie:
            writer.writerow(s)

        print(f"\nSaglabāts failā: {faila_nosaukums2}")

# komandas atrod un atlasa mājas ar/bez viesistabas
    while True:
        majas = []

        with open( faila_nosaukums2 , 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # izlaižam virsrakstus
            
            for rinda in reader:
                if len(rinda) != 0:           # ja rinda nav tukša
                    majas.append(rinda)

            # Ja nav datu
            if len(majas) == 0:
                print("Failā nav prasītais")
                break
                
            
            mekle_maja3 = input("\nVai vēlaties viesistabu? (piem. yes/no): ").strip()

            atrastie = []
            for maja in majas:
                if maja[6] == mekle_maja3:
                    atrastie.append(maja)

            if len(atrastie) > 0:

                print(f"\nMājas ar {mekle_maja} guļamistabām, {mekle_maja2} vannasistabām un {mekle_maja3} viesistabām: \ncena  kubikmetri")
        #         print (atrastie)
                for s in atrastie:
                    print(f"• {s[0]} {s[1]}")
                    
            break

#  mājas ar/bez viesistabas tiek eksportētas uz atsevišķu failu
    # Eksportējam uz atsevišķu failu


    faila_nosaukums3 = mekle_maja + "+" + mekle_maja2 + "+" + mekle_maja3 +"_istabu_cenas.csv"
    with open(faila_nosaukums3, 'w', newline='', encoding='utf-8') as eks:
        writer = csv.writer(eks)
        writer.writerow(['cena','kubikmetri','guļamistabas','vannasistabas','sāvi','pie galvenā ceļa','viesistabas','pagrabs','apkures katls','gaisa kondicionieris','parkošanās','prefarea','mēbeles'])
        for s in atrastie:
            writer.writerow(s)

        print(f"\nSaglabāts failā: {faila_nosaukums3}")

def stavu_skaits():
    while True:
        majas = []
# komandas atrod un atlasa mājas ar izvēlēto stāvu skaitu
        with open( 'Maju_cenas.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # izlaižam virsrakstus
                
            for rinda in reader:
                if len(rinda) != 0:           # ja rinda nav tukša
                    majas.append(rinda)

                # Ja nav datu
            if len(majas) == 0:
                print("Failā nav prasīto stāvu skaits")
                break
                    
                
            mekle_maja = input("\nCik stāvus vēlaties? (piem. 1 - 4): ").strip().upper()

            atrastie = []
            for maja in majas:
                if maja[4] == mekle_maja:
                    atrastie.append(maja)

            if len(atrastie) > 0:
                print(f"\nMājas ar {mekle_maja} stāviem \ncena  kubikmetri")
            #print (atrastie)
                for s in atrastie:
                    print(f"• {s[0]} {s[1]}")
                        
            break
#  mājas ar izvēlēto stāvu skaitu tiek eksportētas uz atsevišķu failu
        # Eksportējam uz atsevišķu failu
    faila_nosaukums = mekle_maja + "_stāviem_cenas.csv"
    with open(faila_nosaukums, 'w', newline='', encoding='utf-8') as eks:
        writer = csv.writer(eks)
        writer.writerow(['cena','kubikmetri','guļamistabas','vannasistabas','sāvi','pie galvenāceļa','viesistabas','pagrabs','apkures katls','gaisa kondicionieris','parkošanās','prefarea','mēbeles'])
        for s in atrastie:
            writer.writerow(s)

        print(f"\nSaglabāts failā: {faila_nosaukums}")


    while True:
        majas = []
# komandas atrod un atlasa mājas ar/bez pagraba
        with open( faila_nosaukums , 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # izlaižam virsrakstus
                
            for rinda in reader:
                if len(rinda) != 0:           # ja rinda nav tukša
                    majas.append(rinda)

                # Ja nav datu
            if len(majas) == 0:
                print("Failā nav prasītais")
                break
                    
                
            mekle_maja2 = input("\nVai vēlaties pagrabu? (piem. yes/no): ").strip()

            atrastie = []
            for maja in majas:
                if maja[7] == mekle_maja2:
                    atrastie.append(maja)

            if len(atrastie) > 0:
                print(f"\nMājas ar {mekle_maja2} stāviem \ncena  kubikmetri")
            #print (atrastie)
                for s in atrastie:
                    print(f"• {s[0]} {s[1]}")
                        
            break

#  mājas ar/bez pagraba tiek eksportētas uz atsevišķu failu
        # Eksportējam uz atsevišķu failu
    faila_nosaukums2 = mekle_maja + "+" + mekle_maja2 + "_stāviem_cenas.csv"
    with open(faila_nosaukums2, 'w', newline='', encoding='utf-8') as eks:
        writer = csv.writer(eks)
        writer.writerow(['cena','kubikmetri','guļamistabas','vannasistabas','sāvi','pie galvenāceļa','viesistabas','pagrabs','apkures katls','gaisa kondicionieris','parkošanās','prefarea','mēbeles'])
        for s in atrastie:
            writer.writerow(s)

        print(f"\nSaglabāts failā: {faila_nosaukums2}")

def iekartojums():
    while True:
        majas = []
# komandas atrod un atlasa mājas ar/pa pusei/bez mēbelēm 

        with open( 'Maju_cenas.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # izlaižam virsrakstus
                
            for rinda in reader:
                if len(rinda) != 0:           # ja rinda nav tukša
                    majas.append(rinda)

                # Ja nav datu
            if len(majas) == 0:
                print("Failā nav prasītais")
                break
                    
                
            mekle_maja = input("\nCik iekārtotu māju jūs vēlaties? (piem. furnished/ semi-furnished/ unfurnished): ").strip()

            atrastie = []
            for maja in majas:
                if maja[12] == mekle_maja:
                    atrastie.append(maja)

            if len(atrastie) > 0:
                print(f"\nMājas ar {mekle_maja} stāviem \ncena  kubikmetri")
            #print (atrastie)
                for s in atrastie:
                    print(f"• {s[0]} {s[1]}")
                        
            break

#  mājas ar/pa pusei/bez mēbelēm tiek eksportētas uz atsevišķu failu
        # Eksportējam uz atsevišķu failu
    faila_nosaukums = mekle_maja + "_iekartojums_cenas.csv"
    with open(faila_nosaukums, 'w', newline='', encoding='utf-8') as eks:
        writer = csv.writer(eks)
        writer.writerow(['cena','kubikmetri','guļamistabas','vannasistabas','sāvi','pie galvenāceļa','viesistabas','pagrabs','apkures katls','gaisa kondicionieris','parkošanās','prefarea','mēbeles'])
        for s in atrastie:
            writer.writerow(s)

        print(f"\nSaglabāts failā: {faila_nosaukums}")


    while True:
        majas = []
# komandas atrod un atlasa mājas ar/bez apkures katla
        with open( faila_nosaukums, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # izlaižam virsrakstus
                
            for rinda in reader:
                if len(rinda) != 0:           # ja rinda nav tukša
                    majas.append(rinda)

                # Ja nav datu
            if len(majas) == 0:
                print("Failā nav prasītais")
                break
                    
                
            mekle_maja2 = input("\nVai jūs vēlaties apkures katlu? (piem. yes/ no): ").strip()

            atrastie = []
            for maja in majas:
                if maja[8] == mekle_maja2:
                    atrastie.append(maja)

            if len(atrastie) > 0:
                print(f"\nMājas ar {mekle_maja2} stāviem \ncena  kubikmetri")
            #print (atrastie)
                for s in atrastie:
                    print(f"• {s[0]} {s[1]}")
                        
            break

#  mājas ar/bez apkures katla tiek eksportētas uz atsevišķu failu
        # Eksportējam uz atsevišķu failu
    faila_nosaukums2 = mekle_maja2 + "+" + mekle_maja + "_iekartojums_cenas.csv"
    with open(faila_nosaukums2, 'w', newline='', encoding='utf-8') as eks:
        writer = csv.writer(eks)
        writer.writerow(['cena','kubikmetri','guļamistabas','vannasistabas','sāvi','pie galvenāceļa','viesistabas','pagrabs','apkures katls','gaisa kondicionieris','parkošanās','prefarea','mēbeles'])
        for s in atrastie:
            writer.writerow(s)

        print(f"\nSaglabāts failā: {faila_nosaukums2}")

    while True:
        majas = []
# komandas atrod un atlasa mājas ar/bez kondicioniera
        with open( faila_nosaukums2, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # izlaižam virsrakstus
                
            for rinda in reader:
                if len(rinda) != 0:           # ja rinda nav tukša
                    majas.append(rinda)

                # Ja nav datu
            if len(majas) == 0:
                print("Failā nav prasītais")
                break
                    
                
            mekle_maja3 = input("\nVai jūs vēlaties gaisa kondicionieri? (piem. yes/ no): ").strip()

            atrastie = []
            for maja in majas:
                if maja[9] == mekle_maja3:
                    atrastie.append(maja)

            if len(atrastie) > 0:
                print(f"\nMājas ar {mekle_maja3} stāviem \ncena  kubikmetri")
            #print (atrastie)
                for s in atrastie:
                    print(f"• {s[0]} {s[1]}")
                        
            break

#  mājas ar/bez kondicioniera tiek eksportētas uz atsevišķu failu
        # Eksportējam uz atsevišķu failu
    faila_nosaukums3 = mekle_maja3 + "+" + mekle_maja2 + "+" + mekle_maja + "_iekartojums_cenas.csv"
    with open(faila_nosaukums3, 'w', newline='', encoding='utf-8') as eks:
        writer = csv.writer(eks)
        writer.writerow(['cena','kubikmetri','guļamistabas','vannasistabas','sāvi','pie galvenāceļa','viesistabas','pagrabs','apkures katls','gaisa kondicionieris','parkošanās','prefarea','mēbeles'])
        for s in atrastie:
            writer.writerow(s)

        print(f"\nSaglabāts failā: {faila_nosaukums3}")

while True:
  print("Izvēlne:")
  print("1. Atrast māju pēc istabām")
  print("2. Atrast māju pēc stāviem")
  print("3. Atrast māju pēc iekārtojuma")
  print("4. Iziet")

  izvēle = input("Ievadiet savu izvēli (1-4): ")

  if izvēle == '1':
    istabu_skaits()
  elif izvēle == '2':
    stavu_skaits()
  elif izvēle == '3':
    iekartojums()
  elif izvēle == '4':
    print("Paldies par programmas izmantošanu!")
    break
  else:
    print("Nepareiza izvēle. Lūdzu, ievadiet skaitli no 1 līdz 4.")