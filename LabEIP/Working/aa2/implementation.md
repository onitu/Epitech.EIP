# Implémentation


## Vue globale

Par nature Onitu doit gérer beaucoup d'operations en paralelle, pour cela il existe traditionelement
plusieurs solutions clasique. Les trois options principales sont d'utiliser un systeme evenementiel,
utiliser plusieurs threads ou utiliser plusieurs process.

Le systeme evenementiel nous parait le plus compliquer à mettre en place car il laisse moins de
libertés aux differentes parties qui devront obligatoirement respecter une API commune et relativement
stricte. Elle est aussi moins tolérante envers les composants qui bloquent alors qu'ils ne devraient
pas et cela pourait entrainer rapidement une perte de performance ou un arrêt complet du systeme.

Dans Onitu nous voudrions que l'utilisateur ai la possibilité d'ajouter des drivers fait par un tier,
donc un système centralisé où tout doit obligatoirement fonctionner parfaitement nous semble utopique.

Il nous reste donc le choix entre l'utilisation de threads ou de différents process, pour l'instant nous
avons choisis d'utiliser des threads car l'avantage principal d'avoir plusieurs process est de pouvoir
étendre facilement le système sur plusieurs machines. Cela ne nous interesse que moyenement à ce niveau
car nous pourront déjà le faire en aillant simplement plusieurs instances d'Onitu. L'autre avantage
d'avoir plusieurs process est de contourner la Global-Interpreter-Lock (GIL) de Python qui n'autorise en
fait qu'une seule opération en paralèlle même dans le cadre du multithread. Cependant nous estimons que
notre application sera IO-bounded, c'est a dire qu'elle sera principalement limitée par les opération
d'entrée/sortie sur le disque et sur le réseaux. Ces deux types d'opération sont implementés de facon à
ne pas causer de blocage sur la GIL.

### Messaging

La programation paralèlle, multi-thread dans notre cas, apporte souvent des problemes. La plus part du
temps il s'agit d'erreurs de gestion des ressources qui sont partagées entre différentes unitées
d'execution. Ces ressources partagés ce retrouvent utilisées par plusieurs unitées en meme temps ce qui
cause des conflicts et entraine souvent une corruption des données. Il est très compliqué de réussir à
avoir une architecture qui élimine ces problemes. C'est pourquoi nous avons décidé de limiter au maximum
les données partagées entre différents threads. Cela devrais aussi faciliter un changement eventuel en
faveur du multi-process.

Pour limiter les donnes commune nous utilisont une architecture de type messaging. Il n'y as pas de
ressources commune entre les différentes unitées d'execution. Les différentes parties du programe vont
néamoins pouvoir communiquer au travers de messages en utilisant la librairie 0mq. Un thread va être
prévenu des évenements propre à son backend par une implémentation de son choix qui depend grandement
de la nature du backend. (hooks sur le filesystem, thread-jumaux qui surveille une API, ...) Quand il
y a des évènements il va prévenir les autres parties du programe qui en ont besoin de cette information
en envoyant des messages. De la même facon il va recevoir des message qui seront pour lui des ordres,
principalement en provenance du referee.

Cette architecture particuliere fait que les relations entre les diferents élements d'Onitu sont très
simple et ce resument souvent à un moyen de démarer les diferentes parties et d'interface de comunication
utilisatn 0mq.

### Canaux de comunication

Les differents design pattern que nous utilisont au niveau du messagin sont des surcouche des sockets
fournis par la librairie 0mq. Nous utilisons deux design pattern differents:

* PUBlisher/SUBscriber: Il s'agit d'un modele de publication d'information, l'émeteur publie un
message en utilisant une socket de type PUB et tout les abonées (subscribers) le recevront. Les
messages sont broadcast et unidirectionel. Il y'as cependant la possibilité d'utiliser un filtre
sur les messages à recevoir du coté abonnée ce qui rend possible du multicast.

* REQuest/REsPonse: Ce modele est relativement standart, il s'agit de celui utilisé par beaucoup
de serveurs, un client envoie une requette puis lit une réponse du serveur. Il est obligatoire
que la réponse de la requette soit recu avant de pouvoir en faire une nouvelle.


Voici, avec un exemple, comment communiquent les différentes parties du projet:

\FullWidthFigure{Vue globale}{figures/implementation_vue_globale_fig1.png}
\clearpage

1. Un driver (A) préviens d'un changement sur son backend, par exemple un nouveau fichier.
Le referee est abonné à tout les drivers et recoit donc la notification.

2. Le referee décide que le driver (B) doit dupliquer ce fichier, il lui envoie une requete
le lui demandant et recoit tout de suite une réponse affirmative signifiant que (B) va
essayer la duplication.

3. Le driver (B) fait un ensemble de requetes sur (A) pour récupérer les différentes parties
du fichier que (A) lui renvoie.

4. Le driver (B) préviens le referee du succes ou de l'echec de l'opération en publiant un
message indiquant le status.


### Séquences type

Lorsque un driver remarque un changement dans son backend il va publier une notification.
Le referee va alors mettre à jour ca vision du système et décider des actions à entreprendre.
\FullWidthFigure{Diagramme de séquence}{figures/implementation_vue_globale_seq_fig1.png}

Un driver n'est pas forcement connécté lorsque le referee voudrais lui faire faire quelque
chose. Ces ordres sont gardés dans une liste et seront émis lorsque le driver se connectera.
\FullWidthFigure{Diagramme de séquence}{figures/implementation_vue_globale_seq_fig2.png}

Voici un exemple complet, il s'agit du cas ou un driver detecte un nouveau fichier:
\FullWidthFigure{Diagramme de séquence}{figures/implementation_vue_globale_seq_fig3.png}

Comme nous l'avons vu les différentes séquences sont très similaires, en fait les seuls
changement sont au niveau de l'action qui est effectué par le driver. Voici les séquences
pour les trois actions principales. Il s'agit de la duplication, la modification et la
suppresion d'un fichier:

\FullWidthFigure{Diagramme de séquence}{figures/implementation_vue_globale_seq_fig4.png}
\FullWidthFigure{Diagramme de séquence}{figures/implementation_vue_globale_seq_fig5.png}
\FullWidthFigure{Diagramme de séquence}{figures/implementation_vue_globale_seq_fig6.png}
\clearpage

## Couches applicatives

Onitu etant un serveur relativement generique gerant des drivers pour les differents backends,
son architecture centrale est relativement simple. D'autant plus que l'architecture s'appuie
sur du messaging ce qui diminue grandement le besoin de beaucoups de methodes et attributs.

<parler du multithread, des hooks, etc. Faire une explication texte d'un dia de seq d'un point de vue driver.>

\FullHeightRotatedFigure{Couches applicatives}{figures/implementation_couches_applicatives_fig1.png}
\FullHeightRotatedFigure{Couches applicatives}{figures/implementation_couches_applicatives_fig2.png}
