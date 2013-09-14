# Vue logique de l'application


## Vue globale

Structurellement, l'application Onitu est divisée en plusieurs modules séparés selon leur rôle.
Tout d'abord le Core, nœud central de l'application. Puis le referee (ou aiguilleur), qui a pour mission de rediriger correctement les fichiers à synchroniser, et enfin les drivers, des briques logicielles créées sur mesure pour chaque protocole voulu, chargées de relayer les communications entre le Core et l'application cible de chacune d'entre elles. Les drivers sont des instances de ce qu'on appelle un Plug.

Étant une application résolument orientée réseau, Onitu a par conséquent besoin d'outils performants pour gérer un nombre de connexions ainsi que des transferts de fichiers qui peuvent potentiellement être conséquents. Pour cela, nous nous basons sur Circus, un manager de processus et de sockets, avec lequel nous interagissons avec son daemon circusd pour le lancement d'Onitu, mais également au travers de son API Python à l'intérieur de notre programme.

Circus utilise ZeroMQ, une surcouche très performante aux systèmes de sockets classiques et bénéficiant de nombreuses améliorations (systèmes de publisher/subscriber, divide-and-conquer, etc.).

Pour encore plus de rapidité, nous utilisons également Redis, un SGBD clé-valeur en mémoire, permettant d'excellentes performances en minimisant les accès disques. Il est lui aussi géré par Circus.

\FullHeightRotatedFigure{Vue logique de l'application}{figures/vue_logique_fig1.png}


## Composants principaux

