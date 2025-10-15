# import tkinter as tk

# # 1. Izveido galveno logu
# logs = tk.Tk()
# logs.title("Vienkāršs attēls")
# logs.geometry("400x300")

# # 2. Ielādē GIF attēlu
# # Pārliecinieties, ka fails "bilde.gif" atrodas skripta mapē!
# attels_objekts = tk.PhotoImage(file='zvaigzne.png')

# # 3. Izveido "konteineri" (Label) attēlam un ievieto to
# attela_konteineris = tk.Label(logs, image=attels_objekts)

# # 4. Svarīgi! Saglabā saiti uz attēlu, lai tas nepazustu
# attela_konteineris.image = attels_objekts

# # 5. Parāda attēlu logā
# attela_konteineris.pack(pady=20)

# # 6. Palaiž programmu
# logs.mainloop()