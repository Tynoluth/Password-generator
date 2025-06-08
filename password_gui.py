import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        use_digits = digits_var.get()
        use_symbols = symbols_var.get()

        characters = string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation
        characters += string.ascii_uppercase

        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=f"{password}")
        copy_button["state"] = "normal"  # Active le bouton "Copier"
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre valide pour la longueur.")

def copy_to_clipboard():
    password = result_label.cget("text").replace("🔐 ", "")
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()
    messagebox.showinfo("Copié", "Le mot de passe a été copié dans le presse-papier !")

# Fenêtre principale
root = tk.Tk()
root.title("Générateur de mot de passe")
root.geometry("400x300")
root.resizable(False, False)

# Champ longueur
tk.Label(root, text="Longueur du mot de passe :").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.insert(0, "12")
length_entry.pack()

# Options
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Inclure des chiffres", variable=digits_var).pack()
tk.Checkbutton(root, text="Inclure des symboles", variable=symbols_var).pack()

# Bouton de génération
tk.Button(root, text="Générer", command=generate_password).pack(pady=10)

# Affichage du mot de passe
result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=5)

# Bouton Copier désactivé par défaut, activé après génération
copy_button = tk.Button(root, text="Copier dans le presse-papier", command=copy_to_clipboard, state="disabled")
copy_button.pack(pady=5)

# Boucle principale
root.mainloop()
