# Architecture du projet

EXPLICATION + SCHÉMA

## Glossaire

- **Driver** — Un *driver*, ou pilote, et un programme charqué de la liaison entre Onitu et un service local ou distant (système de fichiers, SSH, Dropbox, etc.).

- **Entrée** — Une entrée est un pilote configuré par l'utilisateur. Il peut s'agir par exemple d'un *driver* Dropbox configuré pour utiliser un compte utilisateur spécifique. Une entréepeut être vue comme l'instanciation d'un *driver*.

- **Règle** — Unité faisant correspondre un ensemble de fichiers à un ensemble d'entrées. Les règles définissent les conditions par lesquelles un fichier serait envoyé à une entrée.

- **Fichier de configuration** — Fichier au format *JSON* décrivant les entrées et les règles d'une exécution d'Onitu.

- **Referee** — Entité chargée de recevoir les événements depuis les entrées et d'appliquer les règles afin de les relayer aux entrées intéressées.

- **Plug** — Composant implémentant les utilitaires nécéssaires à un *driver* pour communiquer avec Onitu.

- **Handler** — Une fonction définie par un *driver* qui sera automatiquement appelée lorsque l'événement correspondant surviendra.
