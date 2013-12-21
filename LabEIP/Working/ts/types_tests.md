# Types de tests

Dans ce chapitre vous décrirez en détail les types de tests que vous allez effectuer avec la même cinématique

## Tests unitaires

### Couverture
La couverture des tests unitaires ne sera pas totale. Seuls les composants du cœur d'Onitu (Referee et Plug) seront testés de manière unitaire.

### Environnement et conditions de réalisation
Ces tests seront réalisé via l'outil `py.test`. Un bibliothèque permettant de faire du `mocking` (simulation d'objet) sera éventuellement utilisée. Aucun environnement particulier n'est requis.

### Configurations particulières
Aucune configuration particulière ne sera nécessaire pour lancer les tests unitaires. Les tests seront lancés sur plusieurs configurations de *Python* grâce à l'outil *tox*.

### Planning et charge
Les tests unitaires arrivont lorsque le cœur d'Onitu sera jugé mature et moins prompt à de gros changements. Cela devrait arriver aux alentours de la version `0.5`. Ils devraient être développés, au moins en partie, avant la première version grand publique.

### Critère de démarrage des tests
Les tests seront lancés automatiquement de manière régulière par le serveur d'intégration continue (*Travis-ci*). Ils pourront aussi être lancés dans les mêmes conditions en développement sur n'importe quelle machine.

### Critères de passage/échec
Chaque test unitaire devrait faire une seule et unique assertion. Le test est validé que si cette assertion est juste.

## Tests fonctionnels

### Couverture
Les tests fonctionnels sont les tests privilégiés. Ils doivent couvrir toutes les fonctionnalités d'Onitu, dans un maximum de situations possibles. Cependant, toutes les situations ne sont ni prévisibles, ni reproductibles. Des compromis devront être choisis avec précaution.

### Environnement et conditions de réalisation
Une série d'utilitaires est développée afin de permettre des opérations basiques sur Onitu (le configurer, le démarrer, l'arrêter, etc…). Ces utilitaires seront utilisés par les tests afin d'éviter une duplication inutile du code.

Beaucoup de tests auront besoin d'avoir accès à des composants externes (disque local, serveur Dropbox, serveur SSH, etc…). Une liste des composants externes disponibles sera tenue à jour et sera accessible lors de l'écriture des tests. Par exemple, un test pourra facilement demander l'accès à un compte Dropbox de test.
Cela peut potentiellement poser de gros problèmes, par exemple si deux tests sont lancés en même temps et utilisent le même compte Dropbox de tests. Des mesures particulières devront être prise dans ces cas là.

### Configurations particulières
Tout comme les tests unitaires, l'outil *tox* sera utilisé afin de lancer les tests avec différentes configurations de *Python*.

### Planning et charge
Les premiers tests fonctionnels sont écrits dès la première version d'Onitu. Pour le moment, un membre du groupe travaille essentiellement à leur élaboration. Cette situation est temporaire, par la suite les tests devraient être écrits de manière systématique par tous les contributeurs.

La charge de travail de l'écriture des tests est estimée à un tiers du temps de développement.

### Critère de démarrage des tests
De la même manière que les tests unitaires, les tests fonctionnels seront démarrés automatiquement par le serveur d'intégration continue. Un serveur dédié sera accessible, mais les développeurs devraient pouvoir lancer les tests sur leur propre machine.

### Critères de passage/échec
Chaque test fonctionnel peut faire une ou plusieurs assertions. Le test échoue à la première assertion invalide, et passe si toutes sont valides.

## Tests de performance

### Couverture

### Environnement et conditions de réalisation

### Configurations particulières

### Planning et charge

### Critère de démarrage des tests

### Critères de passage/échec
