## Interface web

L'interface web est construite de façon assez simple: ses fonctionnalités sont basées sur l'*API REST* à laquelle elle offre une interface graphique pour une utilisation grand public. Ainsi, elle consiste simplement en des appels vers l'*API* et le formattage des réponses.

L'interface présente ainsi différentes routes, décrites dans le fichier `js/app.js` pour la gestion des fichiers et des services.

#### Fichiers

Le contrôleur `filesListCtrl` est chargé de lister les fichiers présents sur le système. En plus de la liste des services possesseurs du fichier, une icône est aussi présente pour décrire la nature du fichier (en fonction de son type *MIME*).

Le contrôleur `filesDetailsCtrl` récupère les informations détaillées d'un fichier particulier, et permet la recherche par nom de fichier.

#### Services

Un premier contrôleur, `driverListCtrl`, permet de lister les services actuellement présent dans l'isntance courante d'Onitu, et d'accéder aux contrôleurs suivants.

`driverInfoCtrl` indique à l'utilisateur les informations détaillées du service: son état, sa consommation mémoire, sa consommation *CPU*, son temps d'activité, et ses paramètres. Il permet en outre de démarrer/stopper le service.

Les paramètres d'un service peuvent être modifiés à l'aide du contrôleur `driverEditCtrl`, ces changements seront directement pris en compte par Onitu.

Un dernier contrôleur, `driverAddCtrl`, permet d'ajouter et de connecter à chaud un service au système.
