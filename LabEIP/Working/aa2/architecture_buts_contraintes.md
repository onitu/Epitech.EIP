# Architecture, buts et contraintes


## Objectifs spécifiques ayant un impact sur l'architecture

La réflexion sur l'architecture du projet passe d'abord par la définition d'objectifs clairs, que voici énoncés.

Le premier objectif est d'offrir une alternative libre au serveur *Ubuntu One*, et donc d'être entièrement compatible avec ce dernier.

Un autre est d'offrir à l'utilisateur un contrôle total sur ses données, il lui revient de choisir où ses fichiers seront stockés.

Aussi, pour une meilleure expérience utilisateur, cette solution se devra d'être facilement déployable.

Un des objectifs est aussi de permettre de stocker les données sur des services externes, tels *Dropbox*, par l'intermédiaire de *drivers*. C'est principalement autour de cet objectif que se forme l'architecture du projet.


## Contraintes fonctionnelles

Différentes contraintes permettent aussi de diriger les choix techniques. Premièrement, les contraintes fonctionnelles, qui décrivent les caractéristiques du système.

Il a été décidé que les différents *drivers* communiqueraient entre-eux à l'aide de queues de messages. Ainsi, le programme disposera d'un *core* très basique, ne s'occupant que de la transmission des messages.

Une autre contrainte et la volonté de pouvoir assurer une réplication des données sur différents services. Par l'intermédiaire des *drivers*, préalablement configurés, qui écouteront les modifications d'un ensemble de fichiers pour les reproduire à l'identique sur leur espace de stockage.

L'ensemble des modules devront pouvoir être configurés de façon centralisée à l'aide d'un *DSL*, permettant une configuration plus souple qu'un simple système clef-valeur.


## Contraintes non fonctionnelles

Les autres contraintes, non fonctionnelles, régissant les choix architecturaux sont les suivantes.

Onitu devra être conforme au protocole définit par *Ubuntu One*, puisque compatible avec le client officiel.

L'utilisation de certaines bibliothèques, telles que *Twisted*, non portée en Python3, contraint à l'utilisation d'une version antérieure.

Dans un soucis de simplicité, le *DSL* proposé devra être facilement compréhensible par l'utilisateur, ne devra pas le rebuter. Ce dernier devrait sans problème pouvoir bénéficier d'une configuration fine de son système.

C'est principalement dans un soucis de protection et contrôle des données que la solution Onitu sera utilisée, c'est pourquoi sa sécurité doit être maximale.
