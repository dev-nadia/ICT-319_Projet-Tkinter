# Nom: I319_Bloc-notes_Tkinter.py
# Auteur: Nadia Abdi Mohamoud
# Date:15.12.20205
# Purpose : Créer un projet Tkinter en utilisant .grid(), .place(), .pack()


# On importe le module tkinter et on le renomme en 'tk' pour simplifier son utilisation
import tkinter as tk
from tkinter import Menu
from tkinter import filedialog

#les fonctions

#def open
   # file=filedialog.askopenfilename()
  #  if file:
      #  with

#def save

#def save as

#def copy

#def paste

#def cut


#def bold

#def italic

#def color
#









# Création de la fenêtre principale
root = tk.Tk()

# Titre de la fenêtre
root.title("Bloc-notes")

# Définir la taille de la fenêtre (largeur x hauteur)
root.geometry("400x200")

#ferme la fenêtre principale
def quit():
    root.quit()

#création de la barre menu
menubar= Menu(root)
root.config(menu=menubar)
#craétion du menu
file_menu=Menu(menubar,tearoff=False)

#ajouter des éléments au menu (.add_command)

file_menu.add_command(label="Nouveau",command=root.quit)
file_menu.add_command(label="Ouvrir",command=root.quit)
file_menu.add_command(label="Enregistrer",command=root.quit)
file_menu.add_command(label="Enregistrer sous",command=root.quit)
file_menu.add_separator()
file_menu.add_command(label="Quitter",command=root.quit)
#ajouter le menu fichier à la barre menu et retirer la ligne trait tillés avec tearoff=False
menubar.add_cascade(label="Fichier",menu=file_menu)


#Menu édition
edit_menu=Menu(menubar,tearoff=False)
edit_menu.add_command(label="Gras",command=root.quit)
edit_menu.add_command(label="Italique",command=root.quit)
edit_menu.add_command(label="Couleur",command=root.quit)
menubar.add_cascade(label="Édition",menu=edit_menu)#alt+144


#Même chose mais pour le menu Style
style_menu=Menu(menubar,tearoff=False)
style_menu.add_command(label="Copier",command=root.quit)
style_menu.add_command(label="Coller",command=root.quit)
style_menu.add_command(label="Couper",command=root.quit)
menubar.add_cascade(label="Modifier",menu=style_menu)

#Boutons style:
toolbar=tk.Frame(root)
toolbar.pack(side="top", fill="x")

#messagebox.showinfo("Bloc-notes", f"Voulez-vous enregistrer les modifications : {move_count}\nCouleurs : {color_count}")


#zone de text avec Text et .grid
#text=tk.Frame(root,wrap="word")
#text.pack(fill="both", expand=True)

text=tk.Text(text,wrap="word")
text.grid(row=0, column=0)

#la barre de défilement
scrollbar=tk.Scrollbar(root, orient="vertical",command=text.yview())
scrollbar.grid(row=0, column=1, sticky="ns")

text.configure(yscrollcommand=scrollbar.set)

root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

# Boucle principale de Tkinter : garde la fenêtre ouverte et active
root.mainloop()