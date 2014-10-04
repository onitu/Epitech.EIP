## *Drivers*

Les *drivers*, ou pilotes, sont les éléments clefs d'Onitu. Ils forment une interface entre le cœur d'Onitu et les services distant.

Un *driver* est spécifique à un service, en cela il implémente l'API propre à chaque service. Certaines API ne fournissent pas toutes les fonctionnalités que nous pourrions espérer (téléchargement par blocs par exemple) et peuvent donc impliquer des *drivers* plus limités.

Un *driver* consiste simplement en un module python. Chaque *driver* doit comporter une méthode `start`, son point d'entrée, qui sera appelée pour son initialisation.

### *Handlers*

Les *handlers* sont les méthodes par lequel le *Plug* effectue des requêtes auprès d'une entrée.

Ils se définissent dans le module du *driver* à l'aide d'un décorateur `plug.handler()` englobant les méthodes voulues.

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

Permet de négocier la taille des blocs entre le *Referee* et le *driver*. Le *handler* prend en paramètre la taille proposée par le *Referee*, et retourne `None` si cette valeur lui convient, ou une autre taille dans le cas contraire.

### Plug

Un *driver* est de plus amené à demander des informations auprès du *Plug*, il peut le faire à l'aide des méthodes suivantes.

#### `get_metadata`

Permet de récupérer les métadonnées d'un fichier. Prend le chemin du fichier en paramètre et retourne un object `Metadata` (object contenant le nom, la taille, le type *MIME* et les propriétaires du fichier).

#### `update_file`

Indique au *Plug* qu'un fichier a été mis à jour. Transmet les métadonnées du fichier en paramètre.

#### `delete_file`

Notifie le *Plug* de la suppression d'un fichier, en précisant les métadonnés du fichier en paramètre.

#### `move_file`

Notifie le *Plug* du déplacement d'un fichier, en indiquant en paramètre les métadonnées du fichier et le nouvel emplacement.

### Exceptions

Différentes exceptions sont mises à disposition des *drivers* pour relayer à Onitu l'apparition d'un erreur.

#### `ServiceError`

Cette exception doit être levée si une opération ne peut aboutir, en raison d'un problème hors de portée du *driver*.

#### `DriverError`

Cette exception doit être levée pour tout autre problème survenant au niveau du *driver* empêchant de mener à bien une opération.

### Déploiement

#### Configuration

Chaque driver est fourni avec un fichier `manifest.json` qui permet de définir et de valider la structure de ses options de configuration.

Ce fichier est décrit dans la figure suivante.

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
{
  "name": "Nom du driver",
  "description": "Description du driver",
  "options": {
    "root": {
      "name": "Nom de l'option root",
      "description": "Description de l'option",
      "type": "Type de l'option"
    }
  }
}
\end{lstlisting}
\caption{manifest.json}
\end{figure}

Les champs `name` et `description` servent simplement à informer les futurs utilisateurs et développeurs de l'utilité du *driver*, ainsi que d'afficher des noms clairs dans les interfaces de configuration.

Le champ `options` contient les options disponibles pour ce *driver* dans le fichier de configuration. La clef correspond au nom d'option à utiliser dans la configuration.

Le champ `type` contient le type de l'option: sont disponibles `string` (chaîne de caractères), `int` (nombre entier), `float` (nombre à virgule), `boolean` (booléen), et `enumerate` (choix parmi une liste de valeurs précisées dans le champ `values` de l'option).

#### Installation

Un *driver* doit être fourni avec un script python `setup.py`, construit à l'aide des *setuptools* python et permettant l'installation du *driver* au sein d'Onitu.

Ce script est simplement chargé de copier les fichiers du *driver* dans le répertoire `onitu/drivers/` d'Onitu (client ou serveur).

### Tests

Afin de pouvoir être éligible aux tests génériques prévus par Onitu, chaque driver doit être fourni avec un module `driver.py` dans un sous-répertoire `tests`.

Ce module contient une classe `Driver` héritant de `tests.utils.testdriver.TestDriver` fournissant un ensemble d'opérations élémentaires pour communiquer avec le service cible lors des tests.

Ces opérations sont les suivantes:

- **mkdir** — Crée sur le service le ou les répertoires indiqués par le chemin donné en paramètre
- **rmdir** — Supprime le répertoire correspondant au chemin donné
- **write** — Écrit dans le fichier donné en premier paramètre le contenu donné en second paramètre
- **generate** — Génère un fichier aléatoire de taille fixe. Le premier paramètre contient le nom du fichier et le second la taille des données à générer
- **exists** — Vérifie l'existence d'un fichier sur le service, par son chemin donné en paramètre. Retourne vrai si le fichier existe et faux dans le cas contraire
- **unlink** — Supprime le fichier pointé par le chemin
- **rename** — Renomme un fichier, le premier paramètre contient le chemin actuel, et le second contient le nouveau
- **checksum** — Retourne la somme *MD5* du fichier pointé par le chemin donné en paramètre
- **close** — Permet la coupure de la connexion auprès du service

Les drivers peuvent aussi fournir leurs propres fichiers de tests *py.test* en les plaçant dans ce même répertoire.
