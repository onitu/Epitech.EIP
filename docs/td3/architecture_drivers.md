## *Drivers*

Les *drivers* sont les éléments clefs d'Onitu. Ils forment une interface entre le cœur d'Onitu et les services distant.

Un *driver* est spécifique à un service, en cela il implémente l'API propre à chaque service. Certaines API ne fournissent pas toutes les fonctionnalités que nous pourrions espérer (téléchargement par blocs) et peuvent donc impliquer des *drivers* plus limités.

### *Handlers*

Les *handlers* sont les méthodes par lequel le *Plug* effectue des requêtes auprès d'une entrée.

Ils se définissent dans le module du *driver* à l'aide de décorateurs python englobant les méthodes voulues.

Les *handlers* disponibles sont les suivants.

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

???

### Exceptions

### Installation

### Tests
