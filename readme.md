# SCRIPTOR

Scripts utilitaires pour le développement.

## Installation et configuration

- Installer `Python 3`
- Cloner le projet dans un repertoire de votre disque (proche de la racine pour plus de simplicité)
- Dans un terminal, allez dans le repertoire du projet des scripts, puis lancer `install.bat`
> Détails du programme `install.bat` : 
> - Rajoute chaque dossiers dans le PATH des variables d'environnement Windows.
> - Pour le dossier `pyLib` crée une variable nommée `PYTHONPATH` ayant pour valeur le chemin vers `pyLib`
>   - Cette variable permets à tout scripts python d'importer des fichiers python situés dans ce répertoire (librairie globale)
> - Associe les fichier `.py` à `python.exe`
- Créer vos propre configurations à partir des fichiers `template` dans le dossier `config`
  -  Ex : Créer le fichier `config/release-conf.json` à partir `config/release-conf.template.json` (dans le même dossier, avec vos propriétés perso)

## Informations

- Le dossier `resources` contient des fichiers utiles pour la configuration du développement
- Un dossier `temp` peut être créé pour des fichiers temporaires, ils seront ignorés du repo git