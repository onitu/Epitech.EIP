# Contribuer au projet

## Environnement de développement

### Dépôt Git

Onitu est un projet libre dont les sources sont hébergées sur Github. Github, en plus de nous fournir des dépôts *Git*, nous permet de gérer tout le travail autour du projet.

Nous avons sur le site une organisation Onitu à laquelle sont membres toutes les personnes de l'équipe du projet, et contenant plusieurs dépôts.

Github nous offre un système d'*issues* par lequel nous gérons le *bugtracking* (voir plus bas) mais aussi le développement des fonctionnalités courantes. Enfin, les *pull requests* nous permettent de gérer au mieux les collaborations externes.

### Installation et dépendances

La première étape à réaliser est le téléchargement des sources depuis Github:

    git clone git@github.com:onitu/onitu.git
    cd onitu

L'environnement de développement se configure ensuite à l'aide d'un *virtualenv* (ce n'est pas obligatoire mais fortement conseillé, afin de garder l'installation des dépendances locale à votre répertoire de travail).

    virtualenv env
    source env/bin/activate

Cette dernière commande est à exécuter chaque fois que vous entrez dans le répertoire de travail.

Il ne vous reste ensuite qu'à installer les dépendances requises par Onitu:

    pip install -r requirements.txt

Le projet est maintenant fonctionnel, vous pouvez le lancer à l'aide de la commande suivante:

    onitu --debug

### *Bugtracker*

Quand vous rencontrez des problèmes avec Onitu, nous aimons en être informés.
Non pas que nous aimions que des bogues surviennent dans Onitu, mais il nous est
préférable de les corriger que de les laisser en place.

Si vous êtes amené à faire un rapport de bogue, pensez à inclure toutes les
informations que vous avez en votre possession, voici quelques conseils pour
avoir un rapport le plus pertinent possible:

* Si le problème est reproductible, relancez Onitu en mode de débogage.
* Onitu journalise son exécution sur la sortie, cette sortie nous est très utile
pour la compréhension du problème.
* Tentez de simplifier le problème en ne gardant que l'ensemble minimal
d'actions permettant de le reproduire.

Les rapports de bogues se font au moyen des *issues* Github du projet.

## Contribution

### Coeur du projet

### Développement de drivers

#### Configuration

Le dossier du *driver* doit respecter l'arborescence décrite plus haut, en intégrant un fichier `manifest.json` et un fichier `LICENSE`.

Chaque *driver* est fourni avec un fichier `manifest.json` qui permet de définir et de valider la structure de ses options de configuration.

Ce fichier est décrit dans la figure suivante.

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
{
  "name": "Nom du driver",
  "description": "Description du driver",
  "options": {
    "root": {
      "name": "Nom de l'option root",
      "description": "Description de l'option",
      "type": "Type de l'option"
    }
  }
}
\end{lstlisting}
\caption{manifest.json}
\end{figure}

Les champs `name` et `description` servent simplement à informer les futurs utilisateurs et développeurs de l'utilité du *driver*, ainsi que d'afficher des noms clairs dans les interfaces de configuration.

Le champ `options` contient les options disponibles pour ce *driver* dans le fichier de configuration. La clef correspond au nom d'option à utiliser dans la configuration.

Le champ `type` contient le type de l'option: sont disponibles `string` (chaîne de caractères), `int` (nombre entier), `float` (nombre à virgule), `boolean` (booléen), et `enumerate` (choix parmi une liste de valeurs précisées dans le champ `values` de l'option).

#### Installation

Un *driver* doit être fourni avec un script python `setup.py`, construit à l'aide des *setuptools* python et permettant l'installation du *driver* au sein d'Onitu.

Ce script est simplement chargé de copier les fichiers du *driver* dans le répertoire `drivers/` d'Onitu (client ou serveur).

## Validation

### Validation du code

Vos contributions au projet doivent respecter les règles définies par la [PEP
008](http://www.python.org/dev/peps/pep-0008), vous pouvez utiliser un outil tel
que `flake8` pour vérifier que votre code est en accord avec ces règles.

Dans le cas où vous vous poseriez la question, l'indentation utilisée est de
quatre espaces.

Merci de prendre en considération ces quelques règles, qui assurent au projet de
rester propre. Chaque demande de ```pull request``` sera étudiée afin de
regarder en premier lieu si le code fourni les respecte.

### Passage des tests

### *Pull requests*

Afin de maintenir le projet tout en intégrant les contributions externes, nous
avons besoin de mettre en place certaines règles. Ceci est d'autant plus vrai au
regard de l'utilisation de Git.

Chaque développement de nouvelle fonctionnalité doit être fait dans une branche
qui lui est propre. Une fois la fonctionnalité prête à être intégrée, la branche
doit être rebasée sur l'état actuel de la branche ```develop```, avant de faire
une demande de ```pull request```.

Les mainteneurs de la branche ```develop``` pourront ensuite intégrer la
fonctionnalité au moment venu. Ils pourraient auparavant vous demander
d'effectuer quelques changements sur votre travail.

Vous ne devez jamais fusionner la branche ```master``` sur votre branche de
développement, préférez à la place rebaser votre branche.
