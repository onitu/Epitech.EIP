## *API* REST

L'[API REST](https://fr.wikipedia.org/wiki/Representational_State_Transfer) d'Onitu permet à des logiciels externes d'intéragir avec Onitu. Cela offre la possibilité de développer une interface web pour visualiser les photos, surveiller le bon fonctionnement d'Onitu et être averti d'une défaillance ou encore intégrer Onitu à un autre logiciel.

Cette API est développée en utilisant le framework web
[Bottle](http://bottlepy.org/docs/dev/index.html).

### Contrôler Onitu

L'API expose des routes http pour contrôler plusieurs parties d'Onitu : les
fichiers, les *drivers* et les règles de configuration.

#### Les fichiers

Plusieurs routes sont exposées pour manipuler les fichiers gérés par Onitu. Ce
sont les routes qui commencent par ```/api/v1.0/files```.

Pour le moment, ces routes permettent uniquement de la consultation et non
d'envoyer des fichiers sur Onitu. C'est pour cela qu'elles n'acceptent que des
requêtes HTTP GET.

Les routes actuellement en place lisent les fichiers stockés sur Onitu. Elles
permettent de consuler les métadonnées de ces fichiers, pour en déterminer le
propriétaire, la taille ou les *drivers* qui en possèdent une version à jour.

#### Les *drivers*

Une partie importante de l'API est la manipulation des *drivers*. Il est possible
de démarrer et stopper un *driver*, de voir son statut et d'obtenir des
statistique à son sujet.

L'arrêt et le démarrage des *drivers* est notamment utile si vous souhaitez mettre
en *pause* un *driver*, pour par exemple faire une sauvegarde de ses données sans
risquer d'avoir des modifications pendant cette sauvegarde.

Le statut consiste à déterminer l'état de fonctionnement du *driver*, s'il est en
route, à l'arrêt ou en train de changer d'état.

Les statistiques permettent de surveiller qu'un *driver* n'a pas de problème, ne
consomme pas trop de CPU ou de RAM. Mais aussi de savoir depuis combien de temps
il est en route.

Selon les *drivers*, il est aussi possible d'avoir des statistiques
supplémentaires comme l'espace disponible, le nombre de requêtes effectuées sur
le *driver*, …

#### Les règles de configuration

La dernière partie du *driver* travaille sur les règles de configuration entre
*drivers*. Il s'agit de récupérer ces règles, mais aussi de les modifier ou de
lancer une vérification sur l'ensemble des *drivers* pour voir si les fichiers
respèctent bien la dernière version des règles.

### Développer de nouvelles fonctionnalités

Pour ajouter de nouvelles fonctionnalités à l'API REST, il faut ajouter des
routes. l'API utilisant Bottle, il est possible d'utiliser toutes les options de
ce framework.

La création de nouvelles routes doit suivre des règles précises :

- Les routes qui servent à la **consultation** doivent forcément être de type GET.
- Les routes qui servent à la **modification** doivent forcément être de type PUT.
- Les routes qui servent à la **suppression** doivent forcément être de type DELETE.
- Un numéro de version apparaît dans la route. Le fonctionnement d'une route ne
doit pas changer tant que le numéro de version reste le même.
- Toutes les réponses doivent être du JSON valide.
- Le code de réponse HTTP doit être correctement fixé pour correspondre à la
réponse envoyée par l'API. Pas de code 200 quand la route renvoie une erreur.
