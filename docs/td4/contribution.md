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

    onitu

#### Client

Le client se trouve hébergé sur un dépôt séparé, mais son installation est semblable à celle du serveur:

    git clone git@github.com:onitu/client.git
    cd client
    pip install -r requirements.txt

Quant à l'utilisation:

    python -m onitu

#### Interface web (facet)

L'interface web est disponible sur un troisième dépôt, et est fournie clefs en main.

    git clone git@github.com:onitu/facet.git
    cd facet

Il suffit ensuite de servir statiquement le répertoire, avec Python 2 par exemple:

    python -m SimpleHttpServer

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

### Cœur du projet

Si vous cherchez à contribuer au cœur du projet, pensez initialement à consulter les *issues* *Github* pour être informé des besoins actuels. Ces *issues* regroupent les rapports de bogues et les demandes de nouvelles fonctionnalités.

Pour le développement d'une nouvelle fonctionnalité, n'hésitez pas à en discuter sur les *issues* ou à venir rencontrer l'équipe sur notre chan IRC.

Le cœur du projet est diffusé sous licence *MIT*, vous êtes donc libre de copier, modifier et redistribuer les sources, sous les termes énoncés par la licence. En outre, les contributions au sein du dépôt officiel devront s'inscrire sous cette même licence.

#### *API*

Pour ajouter de nouvelles fonctionnalités à l'*API REST*, il vous faut ajouter de
nouvelles routes. l'*API* utilisant *Bottle*, il est possible d'utiliser toutes les options de
ce *cadriciel*.

La création de nouvelles routes doit suivre des règles précises :

- Les routes qui servent à la **consultation** doivent forcément être de type *GET*.
- Les routes qui servent à la **modification** doivent forcément être de type *PUT*.
- Les routes qui servent à la **suppression** doivent forcément être de type *DELETE*.
- Un numéro de version apparaît dans la route. Le fonctionnement d'une route ne
doit pas changer tant que le numéro de version reste le même.
- Toutes les réponses doivent être du *JSON* valide.
- Le code de réponse *HTTP* doit être correctement fixé pour correspondre à la
réponse envoyée par l'*API*. Pas de code 200 quand la route renvoie une erreur.

### Développement de drivers

Les *drivers* sont l'essence du projet, et les services externes en continuelle expansion. Le développement de nouveaux *drivers* permet donc au projet de se maintenir à jour et d'avoir de l'intérêt.

Un *driver* est constitué d'un paquet installable via *pip*, respecant l'arborescence décrite au chapitre \ref{arborescence} **[Arborescence]**.

Le fichier `LICENSE` doit contenir la licence sous laquelle le *driver* est distribué. Le code source doit se trouver dans le *sous-package* `onitu_nom_du_driver`, contenant un fichier `__init__.py` exportant un objet `plug` et une fonction `start`. Les fichiers `manifest.json` et `setup.py` seront décrits dans les sections qui suivent.

Enfin, le *driver* doit implémenter les classes de tests décrites au chapitre \ref{tests_drivers} **[Tests *drivers*]**.

#### Configuration

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

Ce script se doit d'installer toutes les dépendances requises par le *driver* (`install_requires`), et d'installer dans `onitu.drivers` le paquet `onitu_nom_du_driver` et `onitu_nom_du_driver.tests` dans `onitu.tests`.

Un `setup.py` d'exemple est fourni en figure \ref{setup.py}.

\begin{figure}[h]
\begin{lstlisting}[language=python]
from setuptools import setup, find_packages

setup(
    name="onitu-nom-du-driver",
    version="1.2.3",
    url="http://site.du.driver.com",
    description="Description courte du driver",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    package_data={'': ['manifest.json']},
    entry_points={
        'onitu.drivers': [
            'nom_du_driver = onitu_nom_du_driver'
        ],
        'onitu.tests': [
            'nom_du_driver = onitu_nom_du_driver.tests'
        ]
    }
)
\end{lstlisting}
\caption{\label{setup.py} setup.py}
\end{figure}


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

Pour chaque nouvelle fonctionnalité que vous développez, vous devez vous assurer que le projet est toujours fonctionnel, en passant la suite de tests comme indiqué au chapitre \ref{tests} **[Tests]**.

De plus, vous devrez implémenter vos propres tests vérifiant la stabilité de votre nouvelle fonctionnalité.

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
