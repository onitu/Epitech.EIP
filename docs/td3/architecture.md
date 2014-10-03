# Architecture du projet

#### Glossaire

- **Serveur** — Composé par le *Referee*, le *Majordomo*, *Escalator* et le *Plug*. Entité auprès de laquelle se greffent les drivers.

- **Client** — Programme indépendant permettant d'exécuter des *drivers* à distance.

- **Driver** — Un *driver*, ou pilote, et un programme charqué de la liaison entre Onitu et un service local ou distant (système de fichiers, SSH, Dropbox, etc.).

- **Entrée** — Une entrée est un pilote configuré par l'utilisateur. Il peut s'agir par exemple d'un *driver* Dropbox configuré pour utiliser un compte utilisateur spécifique. Une entréepeut être vue comme l'instanciation d'un *driver*.

- **Règle** — Unité faisant correspondre un ensemble de fichiers à un ensemble d'entrées. Les règles définissent les conditions par lesquelles un fichier serait envoyé à une entrée.

- **Fichier de configuration** — Fichier au format *JSON* décrivant les entrées et les règles d'une exécution d'Onitu.

- **Launcher** —

- **Referee** — Entité chargée de recevoir les événements depuis les entrées et d'appliquer les règles afin de les relayer aux entrées intéressées.

- **Plug** — Composant implémentant les utilitaires nécéssaires à un *driver* pour communiquer avec Onitu.

- **Handler** — Une fonction définie par un *driver* qui sera automatiquement appelée lorsque l'événement correspondant surviendra.


\FullWidthFigure{Architecture globale}{imgs/global_archi.png}

\newpage

#### Arborescence

##### Dépôt `onitu.onitu`

Dépôt principal du projet (serveur).

###### `authorized_keys/`
Dossier contenant les clefs des clients autorisés à se connecter

###### `onitu/`
- `api/` — Module contrôlant l'API d'Onitu
- `drivers/` — Dossier contenant les différents *drivers* installés
    - `local_storage/` — *Driver* gérant le système de fichiers local
        - `manifest.json` — Fichier de description du *driver*
        - `tests/` — Tests spécifiques au *driver*
- `escalator/` — Module consacré à la gestion de la base de données, contenant le serveur est le client
- `plug/` — Module *Plug*
- `referee/` — Module *Referee*

###### `server.key_secret`
Clef secrète du serveur

###### `setup.json`
Fichier de configuration Onitu

###### `tests/`
- `benchmarks/` — Tests des performances du système
- `functional/` — Tests fonctionnels du système
- `utils/` — Module regroupant divers utilitaires pour les tests

##### Dépôt `onitu.client`

Dépôt contenant le client Onitu.

###### `onitu/`
Dossier semblable au `onitu/` du serveur et simulant la même architecture chez le client

###### `keys/`
Dossier regroupant les clefs (publique et secrète) du client et la clef publique du serveur

###### `setup.json`
Fichier de configuration client Onitu
