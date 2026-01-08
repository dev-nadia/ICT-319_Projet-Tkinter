# Bloc-notes en Tkinter
### Informations générales
- Cours: ICT-319 – Projet Tkinter
- Nom du fichier: Bloc-notes_Tkinter.py
- Date de rendu: 08 janvier 2026
- Auteur: Nadia Abdi Mohamoud (SI-CA1a) 

## Description
Le projet consiste à créer une petite application de type bloc-notes, développée en Python avec la bibliothèque Tkinter. Il permet de créer, modifier et enregistrer des fichiers. L’objectif est d’apprendre à utiliser les gestionnaires de layout `.pack()`, `.grid()`, `.place()`.

## Fonctionnalités

### Menu Fichier
- **Nouveau** : efface le texte  
- **Ouvrir** : charge un fichier `.txt`  
- **Enregistrer** : sauvegarde le fichier  
- **Quitter** : ferme l’application  

### Menu Édition
- Copier  
- Coller  
- Couper  

### Menu Style
- **Gras**  
- **Italique**  
- **Couleur de texte**  

### Aide
- Bouton « ? » : affiche un message explicatif  

## Fonctions du programme
- **new_file()** : efface tout le contenu de la zone de texte  
- **open_file()** : ouvre un fichier texte et affiche son contenu  
- **save_file()** : enregistre le contenu de la zone de texte dans un fichier  
- **quit()** : ferme la fenêtre principale  
- **copy_text()**, **paste_text()** et **cut_text()**  
- **bold_text()**, **italic_text()** : applique des styles au texte sélectionné  
- **change_color()** : ouvre une palette de couleurs et applique la couleur choisie  
- **help_message()** : affiche une fenêtre d’aide  

## Niveau de difficulté
Ce projet a un niveau de difficulté de débutant à intermédiaire.

- **Niveau facile** :
  - Importation et utilisation de Tkinter
  - Création de la fenêtre Tkinter
  - Ajout d’un widget `Text`
  - Ajout d’un bouton
  - Utilisation de `.pack()`, `.grid()`, `.place()`
  - Affichage de `messagebox.showinfo()`
  - Utilisation des structures conditionnelles (`if`, `return`)
  - Organisation du code en fonctions claires

- **Niveau intermédiaire** :
  - Manipulation des fichiers
  - Utilisation de menus (`Menu`, `add_command`, `add_cascade`)
  - Utilisation de tags (`tag_configure`, `tag_add`)
  - Ajout d’une barre de défilement fonctionnelle (scrollbar)  

## Installation

### Prérequis
Python 3.12 doit être installé sur votre ordinateur.  
### Étapes

**Téléchargez le projet :**

1. Allez sur le dépôt GitHub (repository).  
2. Cliquez sur le bouton vert **Code**, puis sélectionnez **Download ZIP**.  
3. Extrayez le fichier ZIP dans un dossier de votre choix.  
4. **Ouvrez le dossier du projet**, par exemple dans un terminal ou via un éditeur de code comme VS Code ou PyCharm.  
5. **Lancez le programme** avec la commande suivante dans le terminal :

```bash
python Bloc-notes_Tkinter.py

```
## Utilisation 
Après avoir lancé le programme, l’utilisateur peut commencer à écrire du texte dans la zone principale. Le  menu *Fichier* permet de créer un nouveau document,  d’ouvrir un fichier texte déjà présent sur l’ordinateur  ou d’enregistrer le contenu présent dans la zone de texte. Le menu *Édition* permet de copier, coller et couper. Le menu *Style* permet de mettre en gras, en italique ou de modifier la couleur du texte sélectionné. Pour terminer, le bouton « ?» affiche une petite fenêtre d’aide expliquant le fonction générale du bloc-notes. 

## Bibliothèques utilisées
Le programme utilise uniquement des modules de la bibliothèque standard Python tels que : 
- Tkinter : bibliothèque standard pour la création de l’interface graphique
  - `Tk`: fenêtre principale
  - `Text` : zone de texte
  - `Menu` : création de la barre de menus
  - `Scrollbar` : barre de défilement verticale 
  - `filedialog` : ouverture et enregistrement des fichiers
  - `messagebox` : affiche les messages
  - `colorchooser` :sélectionne une couleur pour le texte
  
Aucun installation n’est normalement nécessaire, Tkinter est inclus avec Python sur Windows, macOs et la plupart des distributions Linux.

## Ajustements du projet et choix réalisés 
Au départ, j’avais prévu de faire des boutons pour la mise en forme du texte. Après un essai, j’ai réalisé que cela chargeait visuellement le bloc-notes. J’ai donc opté pour un menu déroulant, c’est plus discret.

## Améliorations possibles
- Gestion d’erreur (par exemple, s’il est impossible d’ouvrir le fichier)
- Raccourcis clavier
- Fonctionnalités avancées
  
## Conclusion 
Ce projet m’a permis de mettre en pratique les notions de base de Python tels que les fonctions et les structurelles conditionnelles. Grâce à l’utilisation de Tkinter, j’ai appris à créer une interface graphique simple et fonctionnelle et manipuler les différents widgets comme les menus, la zone de texte, la barre de défilement. Ce travail m’a aussi permis de revisiter GitHub et de revoir son utilisation.

## Références
Ce projet s'est appuyé sur les ressources suivantes: 
### Support de cours
- Cookbook d’introduction python sur Moodle
- Cookbook Introduction TK  sur Moodle
- Book 1 intro tk sur Moodle
### Tutoriels et articles consultés
- Menus Tkinter : Simplifiez vos interfaces
https://blog.alphorm.com/ajouter-menu-tkinter-interface-python
- Dialogues de fichiers avec Tkinter
https://blog.alphorm.com/dialogues-fichiers-tkinter
- Modifier Police et Taille des Widgets Tkinter — CodeSpace
https://wikiform.fr/codespace/modifier-police-et-taille-des-widgets-tkinter/
- Comment fermer une fenêtre Tkinter avec un bouton — DelftStack https://www.delftstack.com/fr/howto/python-tkinter/how-to-close-a-tkinter-window-with-a-button/
- Tkinter Scrollbar
https://www.tutorialspoint.com/python/tk_scrollbar.htm
- How To Create Message Boxes With Python Tkinter? https://www.pythontutorial.net/tkinter/tkinter-messagebox/
- Tkinter Menu 
https://www.pythontutorial.net/tkinter/tkinter-menu/
- Tkinter Text
https://www.pythontutorial.net/tkinter/tkinter-text/
- How to Wrap Text in Label in Tkinter Python 
https://www.delftstack.com/howto/python-tkinter/how-to-wrap-text-in-label-in-tkinter/
- Python | place() method in Tkinter — GeeksforGeeks https://www.geeksforgeeks.org/python-place-method-in-tkinter/
- Change the color of certain words in the Tkinter Text widget —GeeksforGeeks
https://www.geeksforgeeks.org/python/change-the-color-of-certain-words-in-the-tkinter-text-widget/
- Python Tkinter – Choose Color Dialog — GeeksforGeeks https://www.geeksforgeeks.org/python/python-tkinter-choose-color-dialog/
- Tkinter: Using tags to style text — python.19633.com
https://python.19633.com/fr/GUI/Tkinter/1001036224.html
### Outils utilisés
- Microsoft Copilot
- ChatGPT

