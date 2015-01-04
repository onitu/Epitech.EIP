## Fonctionnement

En s'appuyant sur la figure \ref{use_cases} de la présentation, nous voyons Onitu configuré pour partager les documents textes avec *Hubic* et *Amazon S3*, les photos avec *Flickr*, les vidéos avec *Dropbox*, la musique avec *Google drive*, et enfin tous types de documents avec le client.

Nous imaginons un utilisateur créant un document texte sur **Hubic** (figure \ref{use_case_1}).

\HalfWidthFigure{\label{use_case_1}Création d'un document par l'utilisateur}{imgs/sequence_schema_1.png}

Ce document est par la suite détecté par le *driver* **Hubic**, et reconnu comme répondant à la règle «document texte», il est donc transféré via son *Plug* vers le **serveur Onitu** (figure \ref{use_case_2}).

\HalfWidthFigure{\label{use_case_2}Détection du fichier par le service et transfert vers Onitu}{imgs/sequence_schema_2.png}

Enfin, après consultation des règles, le fichier est fourni aux services **Amazon S3** (configuré pour les documents texte) et **client Onitu** (configuré pour tous types de fichiers), et sont maintenant accessibles à l'utilisateur depuis ces services (figure \ref{use_case_3}).

\HalfWidthFigure{\label{use_case_3}Détection par Onitu et partage vers les services concernés}{imgs/sequence_schema_3.png}
