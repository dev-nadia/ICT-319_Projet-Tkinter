# Bloc-notes en Tkinter
### Informations générales
- Cours: ICT-319 – Projet Tkinter
- Date de rendu: 08 janvier 2026
- Auteur: Nadia Abdi Mohamoud (SI-CA1a) 

## Description 
Le projet consiste à créer une application de bloc-notes développée en Python avec la bibliothèque Tkinter. Il permet de créer, modifier et enregistrer des fichiers.

à créer une application simple en Python permettant à un utilisateur de jouer à *Feuille, Caillou, Ciseaux* contre l’ordinateur. L’utilisateur entre son choix, l’ordinateur génère le sien aléatoirement, puis le programme affiche le résultat, un message personnalisé en fonction de celui-ci et le score actuel.

## Fonctionnalités 

- Ouverture et enregistrer des fichiers .txt

- Menu simple : Nouveau, Ouvrir, Enregistrer, Quitter 

- Interface minimaliste 

## Fonctions du programme 

- **get_choix_utilisateur()**: affiche les choix de jeu et récupère le choix valide de l'utilisateur grâce à une boucle de contrôle des saisies (*c*, *f*, *s* ou *q*).

- **get_choix_ordinateur()**: génère aléatoirement le choix de l'ordinateur parmi le choix *c*, *f* ou *s*.

- **determine_gagnant(utilisateur, ordinateur)**: compare les choix de l'utilisateur et l'ordinateur puis retourne le résultat de la manche (victoire, défaite ou égalité)

- **jeu()**:la boucle principale qui gère le déroulement complet du jeu.  
  - Elle affiche un message de bienvenue, puis permet à l’utilisateur de jouer plusieurs manches contre l’ordinateur jusqu’à ce qu’il souhaite s'arrêter. 
  - À chaque manche, elle récupère les choix de l’utilisateur et de l’ordinateur, détermine le gagnant, met à jour les scores, et affiche des messages personnalisés en fonction du résultat.

## Niveau de difficulté : 
- Utilisation de boucles `while` pour gérer et contrôler les entrées   utilisateurs
- Boucle principale pour le déroulement du jeu
- Utilisation de structures conditionnelles  (`if`, `else`, `elif`)
- Utilisation d'un dictionnaire pour générer les choix
- Importation et utilisation de bibliothèques standards Python `time` (pauses entre les messages) et `random` (choix aléatoire)
- Utlisation de listes pour stocker et afficher les messages personnalisés
- Suivi et mis à jour du score de l'utilisateur et de l'ordinateur
- Organisation du code en fonctions claires et distinctes 

## Installation 

### Prérequis 

Python 3.12 doit être installé sur votre ordinateur.
Tkinter (interface graphique native)

### Étapes 

**Téléchargez le projet**: 

1. Allez sur le dépôt GitHub (repository).

2. Cliquez sur le bouton vert **Code** puis sélectionnez **Download ZIP**. 

3. Extrayez le fichier ZIP dans un dossier de votre choix. 

4. **Ouvrez le dossier du projet**, par exemple dans un terminal ou via un éditeur de code comme VS Code ou Pycharm. 

5. **Lancez le programme** avec la commande suivante dans le terminal :
```bash
   python Bloc-notes_Tkinter.py.
```
## Utilisation 
Après avoir lancé le programme, un message d’accueil s'affichera et vous invitera à choisir parmi ces quatre options :*feuille*, *caillou*, *ciseaux* ou *quitter*.

Le programme affichera ensuite : 
- Le choix de l’utilisateur (si *quitter*, il affichera un message d’adieu)
- Le choix de l'ordinateur
- Le résultat de la manche 
- Un message personnalisé selon le résultat
- Le score actuel 
- La possibilité de rejouer ou de quitter 

## Bibliothèques utilisées : 

Nous avons utilisé des bibliothèques Tkinter standards tels que : 

- `Tk`:  pour générer des choix aléatoires pour l’ordinateur et choisir les messages personnalisés 
- `Text` : pour ajouter des pauses (laisser le temps de lire à l’utilisateur, simule une réflexion de l’ordinateur et un effet de suspense) 
- `Menu` : pour ajouter des pauses (laisser le temps de lire à l’utilisateur, simule une réflexion de l’ordinateur et un effet de suspense) 
- `Scrollbar` : pour ajouter des pauses (laisser le temps de lire à l’utilisateur, simule une réflexion de l’ordinateur et un effet de suspense) 
- `filedialog` : pour ajouter des pauses (laisser le temps de lire à l’utilisateur, simule une réflexion de l’ordinateur et un effet de suspense) 
- `messagebox` : pour ajouter des pauses (laisser le temps de lire à l’utilisateur, simule une réflexion de l’ordinateur et un effet de suspense) 
Aucun installation n’est normalement nécessaire, Tkinter est inclus avec Python sur Windows, macOs et la plupart des distributions Linux.

## Ajustements du projet et choix réalisés ??
Au départ, nous avions prévu de limiter chaque partie à trois manches maximum. Néanmoins, cela s’est avéré trop rigide au niveau de l’expérience utilisateur. Par la suite, la possibilité de quitter (q) a été implémentée.
De plus, la boucle `while` utilisé pour contrôler les entrées utilisateurs n’est pas représenté dans les diagrammes de flux car elle alourdirait inutilement la structure. Elle n’est pas nécessaire à la compréhension de la logique du programme tout comme les `time.sleep`. On souhaitait également trouver une façon d’éviter que les messages personnalisés d’une liste soient tous utilisées une fois avant de se répéter mais nous n’avons pas eu le temps.  

!!! Souhaiter rajouter des fonctionnalités pour mettre en gras, italique et modifier la couleur du texte : mais manque de temps et difficulté.

## Améliorations possibles
- Possibilité de mettre en gras, couleurs et en italique. 
- ????
  
## Conclusion ??
Ce projet m’a permis de mettre en pratique les notions de base de Python tels que les fonctions, la portée des variables. Grâce à l’utilisation de Tkinter, j’ai appris à créer une interface graphique simple et fonctionnelle et les widgets tel que les menus, la zone de texte, etc. à utiliser GitHub.

## Références ???
Ce projet s'est appuyé sur les ressources suivantes: 
- Documentation python du cours
- Documentation GitHub: https://docs.github.com/fr/get-started/start-your-journey/hello-world  
- Bibliothèques standards de python *time* et *random*
- Camarade de classe: Amin Torrisi
- Enseignants: Claude Rochat (CPNV), Julien Savary (CPNV) et Yassin Kammoun (HEIGVD)
- Microsoft Copilot
- ChatGPT
