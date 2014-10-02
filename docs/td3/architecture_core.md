## Serveur

Le serveur est le point d'entrée d'Onitu, c'est le programme qui s'occupe des communications avec les différents services, qu'ils soient internes (composants, base de données) ou externes (*drivers*, client).

Onitu est formé des composants suivants:

### *Referee*

Le *Referee*, ou arbitre, est le module chargé de recevoir les événements émis par les entrées, et de les relayer aux autres entrées intéressées, suivant les règles de configuration.

La classe `onitu.referee.Referee` est la classe arbitre. Elle est instanciée au démarrage d'Onitu et tourne dans un processus indépendant. Elle écoute sur une socket `ømq` l'arrivée de nouveaux événements et les récupère via la base de données *Escalator*. Chaque événement est attaché à un identifiant de fichier (*fid*), par lequel il a été déclenché.

Les ordres sont ensuite relayés à l'aide d'une publication `ømq` (PUB) identifiée par son port `port:events:referee` en base de données. Le *Plug* de chaque entrée doit ensuite souscrire à ce flux d'événements via une socket PULL, et s'abonner aux événements débutant par son nom.

Les messages publiés sont constitués de 3 éléments:
- Le nom du canal de communication, ou *addressee*
- Le nom du destinataire (l'entrée cible)
- L'identifiant du fichier émetteur

### *Plug*

Le *Plug* (module `onitu.plug`) est l'interface permettant à une entrée de communiquer avec Onitu. Chaque entrée se doit d'instancier un *Plug* et de l'initialiser à l'aide de la méthode `initialize`.

Une fois l'entrée prête à recevoir des requêtes, elle appelle la méthode `listen` du *Plug* qui bloque jusqu'à la fermeture du programme.

Le plug fait la liaison entre un fichier et ses métadonnées. Les métadonnées sont toutes les informations présentes autour d'un fichier, comme son nom, sa taille, et la liste de ses propriétaires (entrées sur lesquelles le fichier est présent).

### *Majordomo*

Le *Majordomo* est l'entité au sein d'Onitu permettant la communication au sein des clients. Il agit comme un proxy en permettant d'instancier un *driver* sur une machine distante.

Un processus l'instanciant est démarré avec Onitu, qui écoute par défaut sur les ports 20001 et 20003 et attend la connexion de clients. Lorsqu'un client souhaite se connecter, une entrée de type *remote-driver* (pilote distant) est mise en place, et connectée aux règles établies par le client. Elle est par la suite considérée comme une entrée à part entière, et chaque requête qui lui est faite est relayée au *Majordomo*, puis enfin au client distant.

### *Escalator*

*Escalator* est le système de gestion de base de données. Il offre une interface réseau à *LevelDB*, permettant ainsi diverses connections simultanées sur la base.

La base de données est utilisée pour tout ce qui est stockage de métadonnées des fichiers, mais aussi pour les règles, options de configuration, et les événements.

Le serveur *Escalator* est initialisé au démarrage d'Onitu, et des clients sont instanciés par chaque composant nécessitant des accès en base.

Le client offre une interface similaire à *plyvel*, et fournit les méthodes suivantes:

- `create`: Créer une base de données.
- `connect`: Se connecter à une base de données, ou à une sous base de donnée (base ne regroupant que les clefs débutant par un certain préfixe).
- `close`: Fermer une base de données ouverte
- `get`: Récuperer la valeur correspondant à une clef
- `exists`: Vérifier l'existence d'une clef
- `put`: Associer une valeur à une clef
- `delete`: Supprimer une clef
- `range`: Récupérer une suite de clefs/valeurs

Le client permet aussi d'instancier des `batch` de base de données, c'est à dire une suite d'opérations qui seront exécutées de façon atomique sur la base.
