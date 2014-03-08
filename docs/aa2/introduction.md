# Introduction


## Rappel de l'EIP

Epitech, école d'expertise informatique en cinq ans, offre aux étudiants l'opportunité de réaliser un projet de fin d'études sur trois ans, l'EIP (pour *Epitech Innovative Project*).

À ce titre, les élèves doivent s'organiser en un groupe d'au moins cinq personnes et choisir un sujet porteur de nouveautés ou améliorant un ancien sujet. L'EIP est un passage obligatoire et unique dans la scolarité de l'étudiant, de par son envergure (18 mois) et la préparation requise. Le but est, à la fin du temps imparti, d'obtenir un projet commercialisable.


## Contexte et périmètre du projet

Onitu est un projet visant à proposer une alternative libre et *open-source* au serveur d’Ubuntu One.

Ubuntu One est un service de Canonical (sponsor officiel d'Ubuntu) permettant de disposer d’un espace de stockage en ligne, synchronisé entre différents ordinateurs et périphériques compatibles via un logiciel client. Le client et le protocole d’Ubuntu One sont disponibles sous licence libre. Néanmoins, le serveur est propriétaire et n’a pas été publié.

L'objectif d'Onitu est de proposer un équivalent libre à ce serveur, afin de profiter des fonctionnalités d’Ubuntu One tout en maîtrisant le stockage des données et des informations.

Les fichiers gérés par Onitu pourront être stockés sur un serveur administré par son utilisateur, ou bien sûr des services tiers tels que Dropbox, Amazon S3, ou Google Drive. L'innovation d'Onitu réside dans un paramétrage fin de façon à ce que l'utilisateur puisse choisir sur quels services seront stockés quels fichiers.

La cible première d'Onitu est l'utilisateur averti, soucieux des problématiques de centralisation des données, et son entourage, à qui il fera profiter le serveur mis en place. Il n'est pas forcément technicien mais assez curieux, le profil même de l'utilisateur Ubuntu.
Onitu vise aussi à être utilisé au sein d'entreprises ayant la volonté de maîtriser facilement le stockage de leur données.


## Définitions, acronymes et abréviations

- *SGDB*: Système de Gestion de Base de Données.

- *Core*, *Referee*, *Plug*, *drivers*: Organes spécifiques de notre applications, détaillés en partie \ref{composants_principaux}.

- *Redis*, *Circus*, *ZeroMQ* (ou *Zmq*, *0mq*): Différentes bibliothèques utilisées au sein de notre programme, elles aussi détaillées dans la section \ref{composants_principaux}.
