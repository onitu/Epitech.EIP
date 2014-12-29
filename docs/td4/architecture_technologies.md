## Technologies utilisées

### Serveur

#### Python

Le projet est développé en python, compatible Python 2.7, Python 3 et versions
ultérieures.

Python est un langage polyvalent et flexible. Il nous permet de développer et
distribuer Onitu très facilement, sans se soucier des plateformes cibles sur
lequel il sera déployé (pas de compilation des sources ou de distribution de
    binaires), étant de plus disponible sur un très grand nombre de systèmes.
Python possède une libraire standard conséquente et est aisé à lire et à
comprendre.

Onitu étant une application limitée majoritairement par les entrées/sorties, la
vitesse d'exécution de Python n'influera pas sur les performances du système: le
temps d'exécution n'est pas dédié à l'interprétation mais au téléchargement de
fichiers et à l'échange d'informations.

#### *ømq*

Onitu déployant divers processus et exétrons, un moyen de communication entre
les composants se révélait nécessaire. *ømq* est une couche haute du protocole
*IP* et des *sockets* *Unix*, qui fournit des patrons de messages. Onitu en
utilise plusieurs, tels les *ROUTER/DEALER*, *PUBLISH/SUBSCRIBE* et
*REQUEST/REPLY*.

*ømq* est très rapide, léger et flexible. Il est disponible sur de nombreuses
plate-formes et possède une implémentation Python, *pyzmq*.

#### *LevelDB* et *plyvel*

Les données stockées par Onitu en base consistent en de simples couples
clef/valeur. C'est pourquoi nous avons opté pour une base de données simple,
  sans schéma, persistante et multi-plateforme. *LevelDB* répondait parfaitement
  à ce besoin, et nous l'avons donc choisi.

Une bibliothèque python, *plyvel* fournit une très bonne abstraction à
*LevelDB*, et est ainsi utilisée au sein d'Onitu pour communiquer avec la base
de données.

#### *Circus*

*Circus* est un programme de gestion et supervision de processus pour lequel
existe une bibliothèque Python.

Onitu dispose de nombreux processus qui doivent être surveillés, de façon à
pouvoir les démarrer/stopper facilement, ou encore les relancer automatiquement
en cas d'erreur critique, c'est pourquoi nous nous sommes orientés vers
*Circus*.

#### *py.test*

*py.test* est une librairie python simplifiant l'écriture et l'exécution de
tests. Elle est utilisée pour tester l'ensemble des composants du projet, et
nous vous invitons à en faire de même pour toutes vos contributions.

#### *Bottle*

*Bottle* est un framework web python. Cette librairie est utilisée pour exposer
un serveur web qui sert notamment à mettre à disposition une API REST.

### Client

Le client reprend les mêmes technologies que le serveur. Peuvent y être ajoutée la bibliothèque ***msgpack*** utilisée pour la sérialisation des données lors des échanges entre clients et serveur.

### Interface web

#### *Javascript*

L'interface web du projet exploite les possibilités offertes par le moteur *Javascript* du navigateur pour offrir un affichage complet et dynamique.

#### *AngularJS*

Le *framework* *AngularJS* est utilisé afin de mieux découper le code *Javascript*, et de disposer d'outils puissants pour la génération dynamique de pages côté client.
