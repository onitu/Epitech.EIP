# Implémentation


## Vue globale

Par nature, Onitu doit gérer beaucoup d'operations en parallèle, pour cela il existe traditionnellement plusieurs solutions classiques. Les trois options principales sont d'utiliser un système événementiel, d'utiliser plusieurs *threads* ou plusieurs processus.

Le système événementiel nous paraît le plus compliqué à mettre en œuvre car il laisse moins de libertés aux différentes parties qui devront obligatoirement respecter une API commune et relativement stricte.
Elle est aussi moins tolérante envers les composants deffectueux qui bloqueraient sans raison, et cela pourait entraîner rapidement une perte de performances ou un arrêt complet du système.

Dans Onitu, nous voudrions que l'utilisateur ait la possibilité d'ajouter des drivers faits par un tiers, ainsi, un système centralisé où tout fonctionnerait parfaitement nous semble utopique.

Il nous reste donc le choix entre l'utilisation de *threads* ou de différents processus. Nous avons pour l'instant choisi d'utiliser des *threads* car l'avantage principal d'avoir plusieurs processus est de pouvoir étendre facilement le système sur plusieurs machines. Cela ne nous interesse que moyenement à ce niveau car nous pourrons déjà le faire en ayant simplement plusieurs instances d'Onitu.
L'autre avantage à utiliser plusieurs processus est de contourner le *Global-Interpreter-Lock* (*GIL*) de Python qui n'autorise en fait qu'une seule opération en parallèle, même dans le cadre du *multi-thread*.
Cependant nous estimons que notre application sera *IO-bounded*, c'est à dire qu'elle sera principalement limitée par les opérations d'entrée/sortie sur le disque et sur le réseau. Ces deux types d'opérations sont implementés de facon à
ne pas causer de blocage sur le *GIL*.

### Messaging

La programation parallèle, *multi-thread* dans notre cas, apporte souvent son lot de problemes. La plus part du temps, il s'agit d'erreurs de gestion de ressources, partagées entre différentes unités d'execution.
Ces ressources partagées se retrouvent utilisées par plusieurs unités en même temps, ce qui cause des conflicts et entraîne dans la majorité des cas une corruption des données.
Il est très compliqué de parvenir à une architecture qui éliminerait ce type de problèmes. C'est pourquoi nous avons décidé de limiter au maximum les données partagées entre *threads*. Cela devrait aussi faciliter un eventuel futur changement vers une architecture *multi-process*.

Pour limiter les données communes, nous utilisons une architecture de type *messaging*.
Il n'y as pas de ressource commune entre les différentes unités d'execution. Néanmoins, les parties du programe pourront communiquer entre-elles au travers de messages en utilisant la bibliothèque *ZeroMQ*.
Un *thread* sera prévenu des événements propres à son *backend* par une implémentation de son choix qui depend grandement de la nature de ce *backend* (*hooks* sur le *filesystem*, *threads* jumeaux qui surveillent une API, etc.).
À l'arrivée d'évènements, il préviendra les autres entités du programe qui souhaitent être en être informés, en leur envoyant des messages.
De la même facon, il va recevra des messages qui seront pour lui des ordres, principalement en provenance du *referee*.

Cette architecture particulière fait que les relations entre les élements d'Onitu sont très simples et se résument souvent à un moyen de démarrer les différentes parties, et à une interface de comunication utilisant *ZeroMQ*.

### Canaux de comunication

Les différents *design patterns* que nous utilisons au niveau du *messaging* sont des surcouches des *sockets* fournies par la bibliothèque *ZeroMQ*. Nous utilisons principalement deux *design patterns*:

* *PUBlisher/SUBscriber*: Il s'agit d'un modèle de publication d'informations, l'émeteur publie un message en utilisant une socket de type PUB et tout les abonés (*subscribers*) le reçoivent. Les messages sont de type *broadcast* et unidirectionels. Il existe cependant la possibilité d'utiliser un filtre sur les messages à recevoir du coté abonné, ce qui rend possible le *multicast*.

* *REQuest/REsPonse*: Ce modèle est relativement standard, il s'agit de celui utilisé par beaucoup de serveurs: un client envoie une requête puis attend une réponse du serveur. Il est obligatoire que la réponse à la requête soit reçue avant de pouvoir en faire une nouvelle.

\clearpage
Voici, avec un exemple, comment communiquent les différentes entités du système:

\HalfWidthFigure{Vue globale}{figures/implementation_vue_globale_fig1.png}

1. Un *driver* (A) prévient d'un changement sur son *backend*, par exemple un nouveau fichier. Le *referee* est abonné à tous les *drivers* et reçoit donc la notification.

2. Le referee décide que le *driver* (B) doit dupliquer ce fichier, il lui envoie une requête le lui demandant et recoit de suite une réponse affirmative signifiant que (B) va essayer la duplication.

3. Le *driver* (B) fait un ensemble de requêtes sur (A) pour récupérer les différents blocs du fichier que (A) lui transmet.

4. Le *driver* (B) prévient le *referee* du succès ou de l'échec de l'opération en publiant un message indiquant le status.

\clearpage

### Séquences type

Lorsqu'un *driver* remarque un changement dans son *backend*, il publie une notification.
Le *referee* met alors à jour sa vision du système et décide des actions à entreprendre.
\FullWidthFigure{Diagramme de séquence}{figures/implementation_vue_globale_seq_fig1.png}

Un *driver* n'est pas nécessairement connecté lorsque le *referee* voudrait lui demander quelque chose. Ces ordres sont alors gardés dans une liste et seront exécutés lorsque le *driver* en question se connectera.
\FullWidthFigure{Diagramme de séquence}{figures/implementation_vue_globale_seq_fig2.png}

Voici un exemple complet, il s'agit du cas où un *driver* détecte un nouveau fichier:
\FullWidthFigure{Diagramme de séquence}{figures/implementation_vue_globale_seq_fig3.png}

Comme nous l'avons vu, les différentes séquences sont très similaires, en fait les seuls changements se font au niveau de l'action qui est effectuée par le *driver*. Voici les séquences pour les trois actions principales. Il s'agit de la duplication, la modification et la suppresion d'un fichier:

\FullWidthFigure{Diagramme de séquence}{figures/implementation_vue_globale_seq_fig4.png}
\FullWidthFigure{Diagramme de séquence}{figures/implementation_vue_globale_seq_fig5.png}
\FullWidthFigure{Diagramme de séquence}{figures/implementation_vue_globale_seq_fig6.png}
\clearpage

## Couches applicatives

Onitu étant un serveur relativement générique gérant des *drivers* pour différents *backends*, son architecture centrale est relativement simple. D'autant plus qu'elle s'appuie sur du *messaging*, ce qui diminue grandement le besoin de beaucoup de methodes et attributs.

<parler du multithread, des hooks, etc. Faire une explication texte d'un dia de seq d'un point de vue driver.>

\FullWidthFigure{Couches applicatives}{figures/implementation_couches_applicatives_fig1.png}
\FullWidthFigure{Couches applicatives}{figures/implementation_couches_applicatives_fig2.png}
