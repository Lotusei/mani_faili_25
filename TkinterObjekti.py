# import tkinter as tk
# from tkinter import messagebox

# # Galvenais logs
# root = tk.Tk()
# root.title("Radio Pogas Piemērs")
# root.geometry("300x200")

# # Mainīgais, kas glabās izvēlēto vērtību
# izvele = tk.StringVar(value="Latviešu") # Noklusējuma vērtība

# # Funkcija, kas parāda izvēli
# def paradit_izveli():
#     messagebox.showinfo("Jūsu izvēle", f"Jūs izvēlējāties: {izvele.get()}")

# # Etiķete (Label)
# tk.Label(root, text="Izvēlieties valodu:").pack(pady=5)

# # Radio pogu izveide
# tk.Radiobutton(root, text="Latviešu", variable=izvele, value="Latviešu").pack(anchor='w')
# tk.Radiobutton(root, text="Angļu", variable=izvele, value="Angļu").pack(anchor='w')
# tk.Radiobutton(root, text="Vācu", variable=izvele, value="Vācu").pack(anchor='w')

# # Poga apstiprināšanai
# tk.Button(root, text="Apstiprināt", command=paradit_izveli).pack(pady=20)

# root.mainloop()


# --------------------------------------------------------------------------------------------------------------------------------------------------

# import tkinter as tk
# from tkinter import messagebox

# # Galvenais logs
# root = tk.Tk()
# root.title("Listbox Piemērs")
# root.geometry("300x250")

# # Funkcija, kas parāda atlasīto elementu
# def paradit_izveli():
#     try:
#         # Iegūstam atlasītā elementa indeksu
#         atlasitais_indekss = saraksts.curselection()[0]
#         # Iegūstam pašu elementu pēc indeksa
#         izveleta_pilseta = saraksts.get(atlasitais_indekss)
#         messagebox.showinfo("Jūsu izvēle", f"Jūs izvēlējāties: {izveleta_pilseta}")
#     except IndexError:
#         # Kļūdas apstrāde, ja nekas nav izvēlēts
#         messagebox.showwarning("Kļūda", "Lūdzu, izvēlieties pilsētu no saraksta!")

# # Etiķete
# tk.Label(root, text="Izvēlieties pilsētu:").pack(pady=5)

# # Listbox izveide
# saraksts = tk.Listbox(root, height=5) # Augstums - redzamo rindu skaits
# saraksts.pack(pady=5)

# # Elementu pievienošana sarakstam
# pilsetas = ["Rīga", "Liepāja", "Ventspils", "Daugavpils", "Jelgava"]
# for pilseta in pilsetas:
#     saraksts.insert(tk.END, pilseta) # tk.END nozīmē pievienot beigās

# # Poga apstiprināšanai
# tk.Button(root, text="Apstiprināt", command=paradit_izveli).pack(pady=20)

# root.mainloop()



# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# import tkinter as tk
# from tkinter import messagebox

# # Galvenais logs
# root = tk.Tk()
# root.title("Slider Piemērs")
# root.geometry("300x150")

# # Funkcija, kas parāda slīdņa vērtību
# def paradit_vertibu():
#     vertiba = slidnis.get()
#     messagebox.showinfo("Izvēlētā vērtība", f"Slīdņa vērtība ir: {vertiba}")

# # Etiķete
# tk.Label(root, text="Izvēlieties vērtību (0-100):").pack(pady=10)

# # Slider (Scale) izveide
# slidnis = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
# slidnis.pack(pady=5, padx=20, fill='x')

# # Poga apstiprināšanai
# tk.Button(root, text="Apstiprināt", command=paradit_vertibu).pack(pady=10)

# root.mainloop()
