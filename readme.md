# SCRIPTOR

Scripts utilitaires pour le développement.

## Installation et configuration

- Installer `Python 3`
- Cloner le projet dans un repertoire de votre disque (proche de la racine pour plus de simplicité)
- Dans un terminal, allez dans le repertoire du projet des scripts, puis lancer `update.bat`
> Détails du programme `update.bat` : 
> - Rajoute chaque dossiers dans le PATH des variables d'environnement Windows.
> - Pour le dossier `lib` crée une variable nommée `PYTHONPATH` ayant pour valeur le chemin vers `lib`
>   - Cette variable permets à tout scripts python d'importer des fichiers python situés dans ce répertoire (librairie globale)
> - Associe les fichier `.py` à `python.exe`
- Créer vos propre configurations à partir des fichiers `template` dans le dossier `config`
  -  Ex : Créer le fichier `config/release-conf.json` à partir `config-template/release-conf.json` (dans le même dossier, avec vos propriétés perso)

### Exemple Task Cmder

```sh
run jboss 749debug -new_console:t:"JBoss749X" -new_console:C:"C:\Scriptor\resources\icon\redhat.ico"
```

```sh
angular drp -new_console:t:"Angular DRP" -new_console:C:"C:\Scriptor\resources\icon\angular.ico"
```

```sh
{Postgres SQL}
{JBoss 749x}
{Angular DRP}
```

## Informations

- Le dossier `config` centralise la configuration de différents programmes. Ils sont requis si vous utilisez certaines commandes afin de faire correspondre a votre environnement et vos projets. Ainsi que des icones.
- Le dossier `resources` contient des fichiers utiles pour la configuration du développement
- Le dossier `script` contient les différentes commandes, incluant un dossier `lib` pour les librairies python
- Un dossier `temp` peut être créé dans le repertoire `script` pour des scripts temporaires, ils seront ignorés du repo git. Relancer `update.bat` pour référencer le dossier `temp` dans votre `path` si vous créer ce dossier

## Description des commandes

> ℹ : Pour plus d'informations sur une commande et ses arguments, taper la commande suivi de l'option `-h` ou `--help`

### Alias

`cl` : Clean le terminal

`lsa` : Raccourci pour afficher lister en détail les fichiers et dossier du repertoire courant.

`paths` : Permets d'afficher les différents répertoires proprement du path windows

### Git

`gitalias` : Ajoute des alias dans la configuration global de git. (Voir `.gitconfig` dans le dossier `resources`)

`mgit` : Permets de réaliser des commandes git sur plusieurs projets en même temps pour avoir un état des lieux rapidement et réaliser des procédure simples. Remplir la configuration des différents groupements de projets git sur `mgit-conf.json`

### Maven

`release` : Permet de faire des releases avec maven, réalise le `prepare`, le `perform` ainsi que la montée de `master`. En cas d'erreur, un roll back est réalisé avec un reset git, donc pas de commit ni de fichier temporaire gardé, tout est nettoyé. La config `release-conf.json` est nécessaire pour avoir le nom de l'utilisateur et le mot de passe git qui sera utilisé dans les commandes.

### Serveur

`angular` : Permet de lancer un serveur angular avec la bonne version de node. La config `angular-conf.json` est requise pour indiquer les différents projets angular avec le version de node associé. `Volta` et `Yarn` sont requis.

### Unix

`pathx.sh` : Affiche le path sur un os `Unix`

`bashrc.sh` : Permet d'éditer le fichier `bashrc`

### Utilitaires

`cdw` : Permet de changer rapidement de répertoires pour aller sur un projet d'un workspace. Les workspaces sont à renseigner dans la config associée `cdw-conf.json`. Il est également possible de se déplacer dans un workspace directement et indiquant le nom du workspace.

`clog` : Clean les vieux fichiers datés dans le repetoire de log. Indiquer les fichiers de log dans la configuration `clog-conf.json`

`jvm` : Permet de changer de version de java et maven rapidement (mise à jour des path). Pour un changement de java/maven du systeme (option `-g`), ajouter au préalable `%JAVA_BIN%` et `%M2_BIN%` dans le `PATH` Systeme (admin). Spécifier les associations java/maven dans la configuration `jvm-conf.`

`run` : Permet de créer des alias de commandes simple. Les alias sont à renseigner dans la configuration `run-conf.json`

`scriptor` : Liste toutes les commandes accessibles
