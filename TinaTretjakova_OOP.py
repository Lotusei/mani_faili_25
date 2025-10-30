#Pievieno tkinter kā tk
import tkinter as tk

# Pievieno noteiktu funkciju no tkinter
from tkinter import messagebox



# Izveido un definē logu
logs = tk.Tk ()
logs.title("Kalkulātors")
logs.geometry("400x400")

# Izveido un definē virsrakstu
tk.Label(logs, text='''Izrēķini bumbiņas kinētisko enerģiju (J)!''',
         font = ('Arial',10 , 'bold'),
         fg = "Red"
         ).pack( pady=3 )

# Definē aprēķina funkciju
def saskaiti_skatlus():

# Mēģina šo ceļu
    try: 

    # Izsauc ievadītos skaitļus
        v = float(ievade.get())
        m = float(ievade2.get())
            
    #Ievieto izsauktos skaitļus funkcijā
        KE = (1/2)*m*v**2\
            
    # izmet kļūdu, ja kāds skaitlis ir negatīvs nr.1 error
        if m < 0 or v < 0:
            messagebox.showerror("Kļūda!","Skaitļiem ir jābūt pozitīviem!")
    
    # Izmet rezultātu, ja visi skaitļi ir ierakstīti pareizi
        else:
            label_rezultats.config(text=f"Summa: {KE}")
            messagebox.showerror("Rezultāts!",f"Atbilde: Bumbiņas kinētiskā enerģija ir {KE} J!")

        
    # Izmet kļūdu, ja vismaz viens ievades logs ir atstāts tukšs nr.2 error
    except ValueError: 
        messagebox.showerror("Kļūda!","Lūdzu ievadiet skaitļus!")

        
# Izveido un definē atsevišķu rezultātu logu
label_rezultats = tk.Label(logs, text = "")
label_rezultats.pack()

# Nosaka, kas jāraksta pirmajā ievades logā
tk.Label(logs, text = "Ievadi bumbiņas lidojuma ātrumu (m/s):").pack()

# Izveido ātruma ievades lodziņu
ievade = tk.Entry(logs)
ievade.pack()

#Nosaka, kas ir jāraksta otrajā ievades logā
tk.Label(logs, text = "Ievadi bumbiņas svaru (kg):").pack()

# Izveido laika ievades lodziņu
ievade2 = tk.Entry(logs)
ievade2.pack()

#Izveido pogu, kuru uzspiežot izvet rezultātu vai kļūdas
poga = tk.Button(logs, text = '''Aprēķināt''',
                font = ('Arial',10 , 'bold'),
                fg = "Red"
                command = saskaiti_skatlus)
poga.pack()

#Ievieto attēlu
attels_objekts = tk.PhotoImage(file='Kinetika.png')
attela_konteineris = tk.Label(logs, image=attels_objekts)
attela_konteineris.image = attels_objekts
attela_konteineris.pack(pady=20)

# Noslēdz logu
logs.mainloop()