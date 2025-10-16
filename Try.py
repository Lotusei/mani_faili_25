# import tkinter as tk

# from tkinter import messagebox


# logs = tk.Tk ()
# logs.title("Mans logs")
# logs.geometry("300x400")

# def saskaiti_skatlus():
#     try: 
#         a = float(ievade.get())
#         b = float(ievade2.get())
            
#         rezultats = a + b

#         label_rezultats.config(text=f"Summa: {rezultats}")
#     except ValueError: 
#         messagebox.showerror("Kļūda!","Kļūdas ziņojums šeit!")

# tk.Label(logs, text = "Pirmais skaitlis:").pack()

# ievade = tk.Entry(logs)
# ievade.pack()


# tk.Label(logs, text = "Otrais skaitlis:").pack()

# ievade2 = tk.Entry(logs)
# ievade2.pack()

# poga = tk.Button(logs, text = "Aprēķināt",
#                 command = saskaiti_skatlus)
# poga.pack()

# label_rezultats = tk.Label(logs, text = "")
# label_rezultats.pack()


# logs.mainloop()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------


# import tkinter as tk

# from tkinter import messagebox


# logs = tk.Tk ()
# logs.title("Kalkulātors")
# logs.geometry("300x400")

# tk.Label(logs, text="Ievadi skaitļus!").pack(pady=3)

# def saskaiti_skatlus():
#     try: 
#         a = float(ievade.get())
#         b = float(ievade2.get())
            
#         rezultats = a / b

#         label_rezultats.config(text=f"Summa: {rezultats}")
#         messagebox.showerror("Rezultāts!",f"Atbilde: {rezultats}!")

#     except ValueError: 
#         messagebox.showerror("Kļūda!","Kļūdas ziņojums šeit!")
#     except ZeroDivisionError: 
#         messagebox.showerror("Kļūda!","Ar nulli nevar dalīt!")

# tk.Label(logs, text = "Dalāmais:").pack()

# ievade = tk.Entry(logs)
# ievade.pack()


# tk.Label(logs, text = "Dalītājs:").pack()

# ievade2 = tk.Entry(logs)
# ievade2.pack()

# poga = tk.Button(logs, text = "Aprēķināt",
#                 command = saskaiti_skatlus)
# poga.pack()

# label_rezultats = tk.Label(logs, text = "")
# label_rezultats.pack()

# attels_objekts = tk.PhotoImage(file='zvaigzne.png')
# attela_konteineris = tk.Label(logs, image=attels_objekts)
# attela_konteineris.image = attels_objekts
# attela_konteineris.pack(pady=20)

# logs.mainloop()