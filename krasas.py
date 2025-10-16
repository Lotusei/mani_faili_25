# import tkinter as tk

# logs = tk.Tk ()
# logs.title("Mans logs")
# logs.geometry("300x400")

# def maini_fonu():
#     krasa = ievade.get()

#     logs.config(bg = krasa)

# tk.Label(logs, text = "Ieraksti krāsu angļu valodā:").pack()

# ievade = tk.Entry(logs)
# ievade.pack()



# poga = tk.Button(logs, text = "Krāsot!",
#                 command = maini_fonu)
# poga.pack()


# logs.mainloop()


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox

# Galvenais logs
root = tk.Tk()
root.title("Slider Piemērs")
root.geometry("300x450")

# Funkcija, kas parāda slīdņa vērtību
def paradit_vertibu():
    sarkans = red.get()
    zils = blue.get()
    dzeltens = yellow.get()
    messagebox.showinfo("RGB vērtība", f"Sarkanā vērtība ir: {sarkans}. \nZilā vērtība ir: {zils}. \nDzeltenā vērtība ir: {dzeltens}.")

def krasu_maina(event):
    try: 
        sarkans = red.get()
        zils = blue.get()
        dzeltens = yellow.get()

        hex_kods = f"#{sarkans:02x}{zils:02x}{dzeltens:02x}"

        krasas_paraugs.config(bg = hex_kods)

    except Exception as e:
        print(f"Notikusi kļūda: {e}")


# Etiķete
tk.Label(root, text="Izvēlieties katras krāsas vērtību (0-255):").pack(pady=10)

# Slider (Scale) izveide

red = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL)
red.pack(pady=0, padx=20, fill='x')
tk.Label(root, text="Sarkans").pack(pady=2)


blue = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL)
blue.pack(pady=5, padx=20, fill='x')
tk.Label(root, text="Zils").pack(pady=2)

yellow = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL)
yellow.pack(pady=5, padx=20, fill='x')
tk.Label(root, text="Dzeltens").pack(pady=2)


krasas_paraugs= tk.Label(root, width= 30, height= 10, bg = "black").pack(pady=10)

# Poga apstiprināšanai
tk.Button(root, text="Apstiprināt", command=paradit_vertibu).pack(pady=10)

root.mainloop()