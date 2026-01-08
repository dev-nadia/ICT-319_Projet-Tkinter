# Nom: I319_Bloc-notes_Tkinter.py
# Auteur: Nadia Abdi Mohamoud
# Date: 08.01.2026
# Purpose : Créer un projet Tkinter en utilisant .grid(), .place(), .pack()

#-------------------------
#       BIBLIOTHEQUES
#-------------------------
import tkinter as tk
from tkinter import filedialog,messagebox, Menu
from tkinter import colorchooser

#-------------------------
#    FONCTIONS 
#-------------------------

#----Fonctions Edition---
def copy_text():
	text_area.event_generate ("<<Copy>>")
	messagebox.showinfo("Copié","Texte copié dans le presse-papier!")

def paste_text():
	text_area.event_generate ("<<Paste>>")
def cut_text():
	text_area.event_generate ("<<Cut>>")

#----Fonctions Fichier---
def new_file():
    text_area.delete("1.0", tk.END)
def open_file():
    filepath = filedialog.askopenfilename()
    if filepath == "":
        return #si on décide d'annuler
    file = open(filepath, "r",encoding="utf-8") #encoding="utf-8" évite qu'il est un problème avec les accents
    contenu= file.read()
    file.close()
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, contenu)
def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath == "":
        return

    text= text_area.get("1.0",tk.END)
    file= open(filepath, "w",encoding="utf-8")
    file.write(text)
    file.close()

def quit():
    messagebox.showinfo(title="Au revoir", message="Merci d'avoir utilisé mon bloc-notes:)")
    root.quit()


#----Fonctions Style----
def bold_text():
     text_area.tag_configure ("bold",font=("TkDefaultFont",12,"bold")) # les tag_configure servetn simplement à définir le style du widget text
     text_area.tag_add("bold","sel.first", "sel.last") # sel.first -->début du texte sélectionné et #sel.last-->fin du texte sélectionné
def italic_text():
    text_area.tag_configure ("italic",font=("TkDefaultFont",12,"italic"))
    text_area.tag_add("italic","sel.first", "sel.last") 
def change_color():
     #Ouvre la palette de couleur
     color=colorchooser.askcolor(title="Palette de couleurs")[1]
     # Si on a choisit une couleur....
     if color:
        #crée un style avec cette couleur
        text_area.tag_configure("color", foreground=color)
        #applique ce style au texte sélectioné
        text_area.tag_add("color","sel.first", "sel.last") 

    #----Fonction bouton d'aide----
def help_message():
    messagebox.showinfo(title="Aide", message=
    "Ceci est un bloc‑notes.\n" 
    "Utilisez le menu \"Fichier\" pour ouvrir, enregistrer, créer un document ou tout simplement quitter.\n" 
    "Utilisez le menu \"Édition\" pour copier, coller ou couper.\n"
    "Utilisez le menu \"Style\" pour mettre en gras, italique ou en couleur.\n")

#-------------------------
#     PROGRAMME PRINCIPAL
#-------------------------

#----Fenêtre principale---
root = tk.Tk()              # création de la fenêtre
root.title("Bloc-notes")     # titre de la fenêtre
root.geometry("800x400")    # Définir la taille de la fenêtre (largeur x hauteur)


#----Barre de menu----
menubar = Menu(root) #création de la barre menu principale
root.config(menu=menubar)

#-------Menu Fichier------
#-------------------------
#Création du menu
file_menu=Menu(menubar,tearoff=False)# création d'un menu déroulant + retire la ligne en points tillé avec "tearoff=False"

#Ajout des éléments au menu "Fichier" (.add_command)
file_menu.add_command(label="Nouveau",command=new_file)
file_menu.add_command(label="Ouvrir",command=open_file)
file_menu.add_command(label="Enregistrer",command=save_file)
file_menu.add_separator() # add_separtor permet de créer une ligne séparant "Quitter" des autres commandes
file_menu.add_command(label="Quitter",command=quit)

# Ajout du menu "Fichier" à la barre menu 
menubar.add_cascade(label="Fichier",menu=file_menu)

#-------Menu Edition------
#-------------------------
#Ajout des éléments au menu "Édition" (.add_command)
edit_menu=Menu(menubar,tearoff=False)# # création d'un menu déroulant + retire la ligne en points tillé avec "tearoff=False"
edit_menu.add_command(label="Copier",command=copy_text)
edit_menu.add_command(label="Coller",command=paste_text)
edit_menu.add_command(label="Couper",command=cut_text)
menubar.add_cascade(label=" Édition",menu=edit_menu)

#-------Menu Style------
#-------------------------
#Ajout des éléments au menu "Édition" (.add_command)
style_menu=Menu(menubar,tearoff=False)# # création d'un menu déroulant + retire la ligne en points tillé avec "tearoff=False"
style_menu.add_command(label="Gras",command=bold_text)
style_menu.add_command(label="Italique",command=italic_text)
style_menu.add_command(label="Couleur",command=change_color)
menubar.add_cascade(label="Style",menu=style_menu)

#----Zone de texte et Scrollbar (un grid dans un frame)--
#--------------------------------------------------------
frame=tk.Frame(root)
frame.pack(fill="both",expand=True) #avec.pack()

text_area=tk.Text(frame, wrap="word") # avec wrap, cela permet un retour automatqiue entre les mots (ne les coupent pas)
text_area.grid(row=0,column=0,sticky="nsew")

#----Scrollbar----

scrollbar=tk.Scrollbar(frame,command=text_area.yview) # avec yview, on peut faire défilier le texte quand on bouge le scroller
scrollbar.grid(row=0, column=1, sticky="ns")

text_area.configure(yscrollcommand=scrollbar.set) #avec scrollbar.set, on déplace la scroll


frame.grid_rowconfigure(0, weight=1) #.grid_rowconfigure permet à une ligne de s'étirer quand la fenêtre s'agrandit 
frame.grid_columnconfigure(0, weight=1)#.grid_columnnconfigure permet à une colonne de s'étirer quand la fenêtre s'agrandit 

#----Bouton Aide---- 
btn_help = tk.Button(root, text="?", bg="yellow", width=3, command=help_message) # avec.place()
btn_help.place(relx=0,rely=1, anchor="sw")



root.mainloop() #boucle principale de Tkinter : garde la fenêtre ouverte et active

