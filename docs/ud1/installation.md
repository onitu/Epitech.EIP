# Installation

L'installation repose sur *pip*, un gestionnaire de paquets très répandu dans la sphère Python, s'utilisant en ligne de commande.

*pip* se charge de la récupération des sources ainsi que de la résolution des dépendances. L'installation par paquets indépendants vous permet de ne pas vous encombrer de dépendances inutiles.

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

Une fois installé, vous pouvez lancer *Onitu* par la simple commande `onitu`, à laquelle vous pouvez joindre le chemin d'un fichier de configuration (par défaut est utilisé le fichier `.onitu/setup.json` de votre répertoire utilisateur).

Cela vous permet par exemple de lancer plusieurs instances indépendantes d'*Onitu*, opérant chacune sur une configuration différente, des services différents.

## Désinstallation

Si vous êtes amené à désinstaller *Onitu*, il vous suffit d'exécuter `pip uninstall onitu`, qui supprimera *Onitu* ainsi que l'ensemble de ses modules complémentaires (*drivers*), sans oublier les fichiers de configuration locaux qui lui sont propres.
