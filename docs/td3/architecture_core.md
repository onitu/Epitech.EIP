## Serveur

Le serveur est le point d'entrée d'Onitu, c'est le programme qui s'occupe des communications avec les différents services, qu'ils soient internes (composants, base de données) ou externes (*drivers*, client).

Onitu est formé de divers composants détaillés dans les sections ci-dessous.

### *Launcher*

Le *Launcher*, ou lanceur, est le programme lancé lorsque la commande `onitu` est entrée.

Il est chargé d'analyser le fichier de configuration et d'initialiser et exécuter à l'aide de *Circus* les autres processus, tels que le *Referee*, la base de données ou les *drivers*.

### *Referee*

Le *Referee*, ou arbitre, est le module chargé de recevoir les événements émis par les services, et de les relayer aux autres services intéressés, suivant les règles de configuration.

La classe `onitu.referee.Referee` est la classe arbitre. Elle est instanciée au démarrage d'Onitu et tourne dans un processus indépendant. Elle écoute sur une socket *ømq* l'arrivée de nouveaux événements et les récupère via la base de données *Escalator*. Chaque événement est attaché à un identifiant de fichier (*fid*), par lequel il a été déclenché.

Les ordres sont ensuite relayés à l'aide d'une publication *ømq* (PUB) identifiée par son port `port:events:referee` en base de données. Le *Plug* de chaque service doit ensuite souscrire à ce flux d'événements via une socket PULL, et s'abonner aux événements débutant par son nom.

Les messages publiés sont constitués de 3 éléments:

- Le nom du canal de communication, ou *addressee*
- Le nom du destinataire (le service cible)
- L'identifiant du fichier émetteur

### *Plug*

Le *Plug* (module `onitu.plug`) est l'interface permettant à un service de communiquer avec Onitu. Chaque service se doit d'instancier un *Plug*.

Une fois le service prêt à recevoir des requêtes, il appelle la méthode `listen` du *Plug* qui bloque jusqu'à la fermeture du programme.

Le plug fait la liaison entre un fichier et ses métadonnées. Les métadonnées sont toutes les informations présentes autour d'un fichier, comme son nom, sa taille, et la liste de ses propriétaires (services sur lesquels le fichier est présent).

Le *Plug* offre aussi la possibilité aux *drivers* de se connecter à des *handlers*.

### *Majordomo*

Le *Majordomo* est l'entité au sein d'Onitu permettant la communication avec des clients distant. Il agit comme un proxy en permettant d'instancier un *driver* sur une machine distante.

Un processus l'instanciant est démarré avec Onitu, qui écoute par défaut sur les ports 20001 et 20003 et attend la connexion de clients. Lorsqu'un client souhaite se connecter, un service de type *remote-driver* (pilote distant) est mise en place, et connecté aux règles établies par le client. Il est par la suite considéré comme un service à part entière, et chaque requête qui lui est faite est relayée au *Majordomo*, puis enfin au client distant.

Chaque client est authentifié par le *Majordomo* à l'aide d'un ensemble de leurs clefs publique et secrète respectives.

### *Escalator*

*Escalator* est le système de gestion de base de données. Il offre une interface réseau à *LevelDB*, permettant ainsi diverses connections simultanées sur la base.

La base de données est utilisée pour tout ce qui est stockage de métadonnées des fichiers, mais aussi pour les règles, options de configuration, et les événements.

Le serveur *Escalator* est initialisé au démarrage d'Onitu, et des clients sont instanciés par chaque composant nécessitant des accès en base.

Le client offre une interface similaire à *plyvel*, et fournit les méthodes suivantes:

- `create`: Créer une base de données.
- `connect`: Se connecter à une base de données, ou à une sous base de donnée (base ne regroupant que les clefs débutant par un certain préfixe)
- `close`: Fermer une base de données ouverte
- `get`: Récuperer la valeur correspondant à une clef
- `exists`: Vérifier l'existence d'une clef
- `put`: Associer une valeur à une clef
- `delete`: Supprimer une clef
- `range`: Récupérer une suite de clefs/valeurs

Le client permet aussi d'instancier des `batch` de base de données, c'est à dire une suite d'opérations qui seront exécutées de façon atomique sur la base.

### Tests

Onitu est fourni avec une suite de tests conséquente présente dans le répertoire `tests/`. Ces tests sont génériques et conçus pour fonctionner avec tous les *drivers*, comme décrit dans le chapitre 2, ils sont construits à l'aide du framework *py.test*.

Une série d'utilitaires est fournie dans le dossier `tests/utils/` pour vous permettre de développer le plus simplement possible de nouveaux tests.

Ces utilitaires sont décris par les sections suivantes.

#### `driver.py`

Contient des classes permettant de générer des configurations pour divers *drivers* cibles, de façon générique.

#### `launcher.py`

Permet d'exécuter simplement une instance d'Onitu, à l'aide du fichier de configuration donné en paramètre à la classe `Launcher`. Offre en retour la possibilité de réagir aux évènements émis par Onitu, à l'aide des méthodes `launcher.on_nomdelevenement` où `launcher` serait une instance de `Launcher` et `nomdevenement` un nom d'événement valide.

La liste des noms d'événements est présente dans le fichier `logs.py`. Les méthodes de connexion aux événements peuvent aussi prendre des paramètres nommés, visibles eux aussi dans le fichier `logs.py`.

#### `loops.py`

Contient diverses boucles événementielles construites pour être branchées au *launcher*. Les boucles sont lancées à l'aide de leur méthode `run`, et stoppées lorsque l'événement correspondant sur vient.

La boucle `BooleanLoop` possède une méthode `stop` qu'il suffit de relier à un événement du *launcher* pour être stopée lors de son émission, par exemple: `launcher.on_referee_started(loop.stop)`.

La boucle `CounterLoop` est initialisée avec un nombre *N* et possède une méthode `check`. De la même manière que `BooleanLoop`, elle s'arrêtera une fois que `check` aura été appelée *N* fois.

#### `setup.py`

Les classes `Rule` et `Setup` permettent de générer un fichier de configuration Onitu depuis un script python.
