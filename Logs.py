import tkinter as tk

logs = tk.Tk ()
logs.title("Mans logs")
logs.geometry("300x400")

def paradi_ievadi():
    teksts.config(text = "Tu ierakstīji: " + ievade.get())

tk.Label(logs, text = "Ieraksti kaut ko:").pack()

ievade = tk.Entry(logs)
ievade.pack()

poga = tk.Button(logs, text = "Parādīt tekstu",
                command = paradi_ievadi)
poga.pack()

teksts = tk.Label(logs, text = "")
teksts.pack()

logs.mainloop()