# Contribuer au projet

## Environnement de développement

### Github

### Bugtracker

Quand vous rencontrez des problèmes avec Onitu, nous aimons en être informés.
Non pas que nous aimions que des bogues surviennent dans Onitu, mais il est
préférable de les corriger que de les laisser en place.

Si vous êtes amené à faire un rapport de bogue, pensez à inclure toutes les
informations que vous avez en votre possession, voici quelques conseils pour
avoir un rapport le plus pertinent possible:

* Si le problème est reproductible, relancez Onitu en mode de débogage.
* Onitu journalise son exécution sur la sortie, cette sortie nous est très utile
pour la compréhension du problème.
* Tentez de simplifier le problème en ne gardant que l'ensemble minimal
d'actions permettant de le reproduire.

### Pull requests

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

## Technologies utilisées

#### Python

Le projet est développé en python, compatible toute version ultérieure à Python 2.7.

Python est un langage polyvalent est flexible. Il nous permet de développer et distribuer Onitu très facilement, sans se soucier des plateformes cibles sur lequel il sera déployé (pas de compilation des sources ou de distribution de binaires), étant de plus disponible sur un très grand nombre de systèmes. Python possède une libraire standard conséquente et est aisé à lire et à comprendre.

Onitu étant une application limitée majoritairement par les entrées/sorties, la vitesse d'exécution de Python n'influera pas sur les performances du système: le temps d'exécution n'est pas dédié à l'interprétation mais au téléchargement de fichiers et à l'échange d'informations.

#### *ømq*

Onitu déployant divers processus et exétrons, un moyen de communication entre les composants se révélait nécessaire. *ømq* est une couche haute du protocole *IP* et des *sockets* *Unix*, qui fournit des patrons de messages. Onitu en utilise plusieurs, tels les *ROUTER/DEALER*, *PUBLISH/SUBSCRIBE* et *REQUEST/REPLY*.

*ømq* est très rapide, léger et flexible. Il est disponible sur de nombreuses plate-formes et possède une implémentation Python.

#### *LevelDB* et *plyvel*

Les données stockées par Onitu en base consistent en de simples couples clef/valeur. C'est pourquoi nousavons opté pour une base de données simple, sans schéma, persistante et multi-plateforme. *LevelDB* répondait parfaitement à ce besoin, et nous l'avons donc choisi.

Une bibliothèque python, *plyvel* fournit une très bonne abstraction à *LevelDB*, et est ainsi utilisée au sein d'Onitu pour communiquer avec la base de données.

## Normes

Vos contributions au projet doivent respecter les règles définies par la
[PEP 008](http://www.python.org/dev/peps/pep-0008), vous pouvez utiliser un outil
tel que flake8 pour vérifier que votre code est en accord avec ces règles.

Dans le cas où vous vous poseriez la question, l'indentation utilisée est de
quatre espaces.

Merci de prendre en considération ces quelques règles, qui assurent au projet de
rester propre. Chaque demande de ```pull request``` sera étudiée afin de
regarder en premier lieu si le code fourni les respecte.

## Tests

Si vous développez une nouvelle fonctionnalité ou souhaitez simplement tester
votre installation d'Onitu, vous pouvez exécuter les tests unitaires.

Pour cela, vous devrez installer les dépendances nécessaires au dispositif de
tests, ce qui peut facilement être réalisé par la commande ```pip install -r
requirements_dev.txt```.

Les tests unitaires peuvent être lancés à l'aide de la commande ```py.test
tests```. Vous pouvez aussi vous aider de ```tox``` afin de générer
automatiquement un environnement propre et fonctionnel pour le lancement des
tests.

Enfin, quelques variables d'environnement que voici peuvent vous être utiles
lors de l'exécution des tests:

* ```ONITU_TEST_TIME_UNIT``` Plusieurs tests se basent sur un délai d'exécution
avant de considérer un transfert en échec. Cette variable contient donc un
nombre de secondes correspondant à l'unité de temps, ```1s``` par défaut.

* ```ONITU_TEST_DRIVER``` La batterie de tests n'est exécutée que pour un pilote
à la fois, cette variable permet de déterminer quel pilote sera testé, et peut
donc prendre des valeurs telles que ```local_storage``` ou ```ssh```.

Des tests automatiques sont lancés par Travis sur tout code intégré à Onitu.
L'historique de ces tests est disponible publiquement. Travis lancera aussi les
tests si vous faites une pull request. Vous pouvez consulter la [page Travis du
projet](https://travis-ci.org/onitu/onitu).
