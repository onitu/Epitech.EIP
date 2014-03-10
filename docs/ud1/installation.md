# Installation

L'installation d'Onitu est très simple, et se contente d'un `pip install onitu` pour mettre en place le programme principal.

Les modules (*drivers*) communiquant avec les différents services s'installent de façon indépendante par une commande similaire:

* `pip install onitu-ssh` pour ajouter le module de communication par *SSH*
* `pip install onitu-dropbox` pour celui communiquant avec les serveurs *Dropbox*

*pip* est un gestionnaire de paquets très répandu dans la sphère Python, qui se charge de la récupération des sources ainsi que de la résolution des dépendances. L'installation par paquets indépendants vous permet de ne pas vous encombrer de dépendances inutiles.

## Lancement

Une fois installé, vous pouvez lancer *Onitu* par la simple commande `onitu`, à laquelle vous pouvez joindre le chemin d'un fichier de configuration (par défaut est utilisé le fichier `.onitu/setup.json` de votre répertoire utilisateur).

Cela vous permet par exemple de lancer plusieurs instances indépendantes d'*Onitu*, opérant chacune sur une configuration différentes, des services différents.

## Désinstallation

Si vous êtes amené à désinstaller *Onitu*, il vous suffit d'exécuter `pip uninstall onitu`, qui supprimera *Onitu* ainsi que l'ensemble de ses modules complémentaires (*drivers*), sans oublier les fichiers de configuration locaux qui lui sont propres.
