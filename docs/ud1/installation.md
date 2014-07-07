# Installation

L'installation repose sur *pip*, un gestionnaire de paquets très répandu dans la sphère Python et multi-plateforme, s'utilisant en ligne de commande.

*pip* se charge de la récupération des sources ainsi que de la résolution des dépendances. L'installation par paquets indépendants vous permet de ne pas vous encombrer de dépendances inutiles.

Un installateur sera aussi fourni par la suite afin d'en simplifier l'installation sous Windows.

## Installation

Pour installer le cœur du projet:

* `pip install onitu`

Puis pour chaque module (*driver*), en remplaçant `onitu-nom_du_module` par le nom approprié, par exemple `onitu-ssh` ou `onitu-dropbox`:

* `pip install onitu-nom_du_module`

## Lancement

\begin{figure}[h]
\includegraphics[scale=0.75]{screen_onitu.png}
\caption{Lancement d'\emph{Onitu}}
\end{figure}

Une fois installé, vous pouvez lancer *Onitu* par la simple commande `onitu`, à laquelle vous pouvez joindre le chemin d'un fichier de configuration à l'aide de l'option `--setup` (par défaut est utilisé le fichier `.onitu/setup.json` de votre répertoire utilisateur).

Cela vous permet par exemple de lancer plusieurs instances indépendantes d'*Onitu*, opérant chacune sur une configuration différente, des services différents.

D'autres options sont disponibles au lancement d'*Onitu*:

* Vous pouvez sélectionner la *socket* *ZMQ* à utiliser pour la journalisation grâce à l'option `--log-uri`.
* Vous pouvez obtenir un affichage plus complet (dit de *debug*) à l'aide de l'option `--debug`.
* Enfin, l'option `--help` vous affiche la présente liste d'options disponibles.

## Désinstallation

Si vous êtes amené à désinstaller *Onitu*, il vous suffit d'exécuter `pip uninstall onitu`, qui supprimera *Onitu* ainsi que l'ensemble de ses modules complémentaires (*drivers*), sans oublier les fichiers de configuration locaux qui lui sont propres.
