# Installation

L'installation d'Onitu est très simple, et se contente d'un `pip install onitu` pour mettre en place le programme principal.

Les modules (*drivers*) communiquant avec les différents services s'installent de façon indépendante par une commande similaire:

* `pip install onitu-ssh` pour ajouter le module de communication par *SSH*
* `pip install onitu-dropbox` pour celui communiquant avec les serveurs *Dropbox*

*pip* est un gestionnaire de paquets très répandu dans la sphère Python, qui se charge de la récupération des sources ainsi que de la résolution des dépendances. L'installation par paquets indépendants vous permet de ne pas vous encombrer de dépendances inutiles.

## Lancement

* Lancement à partir d'un programme `onitu` dans le *path*
* A priori, l'installation générera un `setup.json` de base pour pouvoir lancer *Onitu* directement après installation

## Désinstallation

* `pip uninstall onitu`: s'occupe logiquement de la désinstallation des paquets dépendants (drivers)
