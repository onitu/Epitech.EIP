## *Drivers*

Les *drivers*, ou pilotes, sont les éléments clefs d'Onitu. Ils forment une interface entre le cœur d'Onitu et les services distant.

Un *driver* est spécifique à un service, en cela il implémente l'API propre à ce service. Certaines API ne fournissent pas toutes les fonctionnalités que nous pourrions espérer (téléchargement par blocs par exemple) et peuvent donc impliquer des *drivers* plus limités.

Un *driver* consiste simplement en un module python. Chaque *driver* doit comporter une méthode `start`, son point d'entrée, qui sera appelée pour son initialisation.

### *Plug* et *handlers*

Un *driver* est amené à demander des informations auprès d'un *Plug* qu'il aura préalablement instancié, il peut ainsi utiliser les méthodes vues précédemment pour communiquer avec Onitu, mais aussi connecter des *handlers*.

Les *handlers* sont les méthodes par lesquelles le *Plug* effectue des requêtes auprès d'un service.

Ils se définissent dans le module du *driver* à l'aide d'un décorateur `plug.handler()` englobant les méthodes voulues.

Les *handlers* disponibles sont les suivants:

#### `start_upload`

Informe le *driver* du commencement d'un transfert de fichier vers ce *driver*.
Un paramètre `metadata` permet de lire les métadonnées de ce futur fichier.

#### `end_upload`

Informe le *driver* de la fin de transfert d'un fichier, lorsque le transfert s'est bien déroulé.
Les métadonnées du fichier sont données en paramètre.

#### `abort_upload`

Informe le *driver* de l'abandon d'un transfert de fichier.
Les métadonnées du fichier sont données en paramètre.

#### `upload_chunk`

Transfère au *driver* une portion d'un fichier.
Les 3 paramètres (`metadata`, `offset`, `chunk`) contiennent respectivement les métadonnées du fichier, la position dans le fichier à partir de laquelle débuter l'écriture, et le contenu à écrire.

#### `upload_file`

Transfère au *driver* un fichier entier. Sont donnés en paramètres les métadonnées du fichier et le contenu de celui-ci.

#### `get_chunk`

Demande au *driver* de récupérer un bloc d'un fichier.
Les 3 paramètres (`metadata`, `offset`, `size`) contiennent respectivement les métadonnées du fichier, la position dans le fichier à partir de laquelle débuter la lecture, et la taille du bloc à lire.
Le *handler* doit retourner le contenu lu.

#### `get_file`

Demande au *driver* d'envoyer un fichier en un coup. Les métadonnées du fichier sont données en paramètre.
Le *handler* doit retourner le contenu entier du fichier.

#### `delete_file`

Demande au *driver* la suppression d'un fichier. Les métadonnés du fichier sont données en paramètre.

#### `move_file`

Demande au *driver* de déplacer un fichier vers un nouvel emplacement. Les métadonnées de l'ancien et du nouveau fichier sont données en paramètres.

#### `set_chunk_size`

Permet de négocier la taille des blocs entre le *Referee* et le *driver*. Le *handler* prend en paramètre la taille proposée par le *Referee*, et retourne `None` si cette valeur lui convient, ou une autre taille dans le cas contraire.

### Exceptions

Différentes exceptions sont mises à disposition des *drivers* pour avertir Onitu de l'apparition d'une erreur.

#### `ServiceError`

Cette exception doit être levée si une opération ne peut aboutir, en raison d'un problème hors de portée du *driver*.

#### `DriverError`

Cette exception doit être levée pour tout autre problème survenant au niveau du *driver* empêchant de mener à bien une opération.
