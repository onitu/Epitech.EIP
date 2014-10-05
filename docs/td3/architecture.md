# Architecture du projet

## Architecture générale

### Glossaire

- **Serveur** — Composé par le *Referee*, le *Majordomo*, *Escalator* et le *Plug*. Entité auprès de laquelle se greffent les pilotes.

- **Client** — Programme indépendant permettant d'exécuter des *drivers* à distance en se connectant au serveur.

- **Driver** — Un *driver*, ou pilote, est un programme chargé de la liaison entre Onitu et un service local ou distant (système de fichiers local, SSH, Dropbox, etc.).

- **Service** — Un service est un pilote configuré par l'utilisateur. Il peut s'agir par exemple d'un pilote Dropbox configuré pour utiliser un compte utilisateur spécifique. Un service peut être vu comme l'instanciation d'un pilote.

- **Règle** — Unité faisant correspondre un ensemble de fichiers à un ensemble de services. Les règles définissent les conditions par lesquelles un fichier serait envoyé à un service.

- **Fichier de configuration** — Fichier au format *JSON* décrivant les services et les règles d'une exécution d'Onitu.

- **Launcher** — Le *Launcher* est le composant appelé au démarrage d'Onitu, et qui s'occupe de lancer les autres processus.

- **Referee** — Entité chargée de recevoir les événements depuis les services et d'appliquer les règles afin de les relayer aux services intéressés.

- **Plug** — Composant implémentant les utilitaires nécéssaires à un pilote pour communiquer avec Onitu.

- **Handler** — Une fonction définie par un pilote qui sera automatiquement appelée lorsque l'événement correspondant surviendra.

- **API** — Interface permettant le contrôle du serveur (ajout de pilotes, modification des règles), épaulée par une interface web.


\FullWidthFigure{Architecture globale}{imgs/global_archi.png}

\newpage

### Arborescence

##### Dépôt `onitu.onitu`

Dépôt principal du projet (serveur).

###### `authorized_keys/`
Dossier contenant les clefs des clients autorisés à se connecter

###### `drivers/`
Dossier contenant les différents *drivers* installés

- `local_storage/` — *Driver* gérant le système de fichiers local
    - `LICENSE` — Fichier précisant la licence sous laquelle est distribuée le *driver*
    - `manifest.json` — Fichier de description du *driver*
    - `onitu_local_storage/` — Module de *driver*
        - `tests/` — Tests spécifiques au *driver*
    - `setup.py` — Script *setuptools* d'installation

###### `onitu/`
- `api/` — Module contrôlant l'API REST d'Onitu
- `drivers/` — Module chargé du chargement des *drivers*
- `escalator/` — Module consacré à la gestion de la base de données, contenant le serveur et le client
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

###### `drivers/`
Dossier où sont installés les *drivers* client

###### `onitu/`
Dossier semblable au `onitu/` du serveur et simulant la même architecture chez le client

###### `keys/`
Dossier regroupant les clefs (publique et secrète) du client et la clef publique du serveur

###### `setup.json`
Fichier de configuration client Onitu
