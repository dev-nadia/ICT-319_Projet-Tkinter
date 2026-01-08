# Nom: I319_Bloc-notes_Tkinter.py
# Auteur: Nadia Abdi Mohamoud
# Date:08.01.2026
# Purpose : Créer un projet Tkinter en utilisant .grid(), .place(), .pack()

#Bibliotèques:
import tkinter as tk
from tkinter import filedialog,messagebox, Menu

#Fonctions Édition:
def copy_text():
	text_area.event_generate ("<<Copy>>")
	messagebox.showinfo("Copié","Texte copié dans le presse-papier!")

def paste_text():
	text_area.event_generate ("<<Paste>>")
def cut_text():
	text_area.event_generate ("<<Cut>>")

# Fonctions Fichier:
def new_file():
    text_area.delete("1.0", tk.END)
def open_file():
    filepath = filedialog.askopenfilename()
    if filepath == "":
        return #si on décide d'annuler
    file = open(filepath, "r")
    contenu= file.read()
    file.close()
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, contenu)
def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath == "":
        return

    text= text_area.get("1.0",tk.END)
    file= open(filepath, "w")
    file.write(text)
    file.close()

def quit():
    messagebox.showinfo(title="Au revoir", message="Merci d'avoir utilisé le bloc-notes !")
    root.quit()

def help_message():
    messagebox.showinfo(title="Aide", message=
    "Ceci est un bloc‑notes.\n" 
    "Utilisez le menu \"Fichier\" pour ouvrir, enregistrer, créer ou quitter.\n" 
    "Utilisez le menu \"Édition\" pour copier, coller ou couper.\n")

#Fenêtre principale

# Création de la fenêtre principale
root = tk.Tk()

# Titre de la fenêtre
root.title("Bloc-notes")
# Définir la taille de la fenêtre (largeur x hauteur)
root.geometry("400x200")

#création de la barre menu
menubar = Menu(root)
root.config(menu=menubar)

#Menu Fichier
#création du menu
file_menu=Menu(menubar,tearoff=False)
#ajouter des éléments au menu (.add_command)
file_menu.add_command(label="Nouveau",command=new_file)
file_menu.add_command(label="Ouvrir",command=open_file)
file_menu.add_command(label="Enregistrer",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Quitter",command=root.quit)
#ajouter le menu fichier à la barre menu et retirer la ligne trait tillés avec tearoff=False
menubar.add_cascade(label="Fichier",menu=file_menu)

#Même chose mais pour le menu Style
edit_menu=Menu(menubar,tearoff=False)
edit_menu.add_command(label="Copier",command=root.quit)
edit_menu.add_command(label="Coller",command=root.quit)
edit_menu.add_command(label="Couper",command=root.quit)
menubar.add_cascade(label="Modifier",menu=edit_menu)

#Zone de texte + Scrollbar un grid dans un frame
frame=tk.Frame(root)
frame.pack(fill="both",expand=True)

text_area=tk.Text(frame, wrap="word")
text_area.grid(row=0,column=0,sticky="nsew")

#la barre de défilement

scrollbar=tk.Scrollbar(frame,command=text_area.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

text_area.configure(yscrollcommand=scrollbar.set)

frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(0, weight=1)

#Bouton Aide ave.place()
btn_help = tk.Button(root, text="?", width=3, command=help_message)
btn_help.place(relx=0,rely=1, anchor="sw")


# Boucle principale de Tkinter : garde la fenêtre ouverte et active
root.mainloop()
