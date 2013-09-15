# Vue logique de l'application


## Vue globale

Structurellement, l'application Onitu est divisée en plusieurs modules séparés selon leur rôle.
Tout d'abord le *Core*, nœud central de l'application. Puis le *Referee* (ou aiguilleur), qui a pour mission de rediriger correctement les fichiers à synchroniser, et enfin les *drivers*, des briques logicielles créées sur mesure pour chaque protocole voulu, chargées de relayer les communications entre le *Core* et l'application cible de chacune d'entre elles. Les *drivers* sont des instances de ce qu'on appelle un *Plug*.

Étant une application résolument orientée réseau, Onitu a par conséquent besoin d'outils performants pour gérer un nombre de connexions ainsi que des transferts de fichiers qui peuvent potentiellement être conséquents. Pour cela, nous nous basons sur *Circus*, un manager de processus et de sockets, avec lequel nous interagissons grâce au daemon *circusd* pour le lancement d'Onitu, mais également au travers de son API Python à l'intérieur de notre programme.

*Circus* utilise *ZeroMQ*, une surcouche très performante aux systèmes de sockets classiques et bénéficiant de nombreuses améliorations (systèmes de *publisher*/*subscriber*, *divide-and-conquer*, etc.).

Pour encore plus de rapidité, nous utilisons également *Redis*, un SGBD clé-valeur en mémoire, permettant d'excellentes performances en minimisant les accès disques. Il est lui aussi géré par *Circus*.

\begin{landscape}
\FullWidthFigure{Vue logique de l'application}{figures/vue_logique_fig1.png}
\end{landscape}

\clearpage


## Composants principaux

\label{composants_principaux}

Dans cette partie, nous allons décrire plus en détails les principaux composants de notre application.

- Le *Core*: Il s'agit du nœud central, celui destiné à tourner sur le serveur et héberger toutes les informations du système et des fichiers qui y sont synchronisés (métadonnées, etc.). Il devra être configurable, soit au moyen d'un fichier de configuration, soit via une interface web.

- Le *Referee*: Aussi appelé aiguilleur, il est l'nterlocuteur direct du Core. Lorsqu'une modification sur le système est détectée (ajout, suppression, modification de fichier...), c'est l'entité qui est chargée de décider, à partir de règles établies au préalable (dans la configuration par exemple), avec quels drivers faut-il synchroniser l'information ou commencer un transfert.

- Le *Plug*: C'est l'entité générique qui se connecte (d'où son nom) au *Referee* pour récupérer et envoyer des données à un *driver* spécifique.

- Les *drivers*: Les *drivers* sont des programmes interagissant chacun avec un *Plug* (au moyen de décorateurs) afin de faire la transition entre le système Onitu et l'application cible (Dropbox, Ubuntu One...) dans le protocole de cette application.

- *Redis*: Système de gestion de base de données clé-valeur stockant entièrement les données en mémoire. Ce procédé permet d'excellentes performances tout en minimisant de coûteux accès disque. Un de ses avantages est qu'il gère plusieurs types de valeurs autres que des *strings*. Nous l'utilisons conjointement avec *Circus* afin d'être plus performant qu'avec un système de base de données classique.

- *Circus*: Système de gestion de processus et de sockets basé sur *ZeroMQ*, destiné à contrôler plus finement l'exécution des processus surveillés et permet notamment de mettre en commun des sockets entre ces processus. *Circus* comprend également une API Python, proposant par exemple un *wrapper* et un *manager* de processus. Nous utilisons *Circus* notamment pour gérer notre application ainsi que la base de données *Redis*.

- *ZeroMQ*: Système de gestion de messages permettant la communication entre les différents organes de l'application. *ZeroMQ* est une bibliothèque réalisée en C mais offrant des *bindings* pour ne nombreux langages tels que Python.
