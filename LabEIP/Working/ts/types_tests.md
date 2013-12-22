# Types de tests

Ce chapitre présente en détails les types de tests qui seront implémentés au sein de notre stratégie.

## Tests unitaires

### Couverture
La couverture des tests unitaires ne sera pas totale. Seuls les composants du cœur d'*Onitu* (*Referee* et *Plug*) seront testés de manière unitaire.

### Environnement et conditions de réalisation
Ces tests seront réalisés via l'outil *py.test*. Un bibliothèque permettant de faire du *mocking* (simulation d'objets) sera éventuellement utilisée. Aucun environnement particulier n'est requis.

### Configurations particulières
Aucune configuration particulière ne sera nécessaire pour lancer les tests unitaires. Les tests seront lancés sur plusieurs configurations de *Python* grâce à l'outil *tox*.

### Planning et charge
Les tests unitaires arriveront lorsque le cœur d'*Onitu* sera jugé mature et moins prompt à de gros changements. Cela devrait arriver aux alentours de la version `0.5`. Ils devraient être développés, au moins en partie, avant la première version grand public.

### Critère de démarrage des tests
Les tests seront lancés automatiquement de manière régulière par le serveur d'intégration continue (*Travis-ci*). Ils pourront aussi être lancés dans les mêmes conditions en développement sur n'importe quelle machine.

### Critères de passage/échec
Chaque test unitaire devrait faire une seule et unique assertion. Le test est validé si et seulement si cette assertion est juste.

## Tests fonctionnels

### Couverture
Les tests fonctionnels sont nos tests privilégiés. Ils doivent couvrir toutes les fonctionnalités d'*Onitu*, dans un maximum de situations possibles. Cependant, toutes les situations ne sont ni prévisibles, ni reproductibles. Des compromis devront être choisis avec précaution.

### Environnement et conditions de réalisation
Une série d'utilitaires est développée afin de permettre des opérations basiques sur Onitu (le configurer, le démarrer, l'arrêter, *etc.*). Ces utilitaires seront utilisés par les tests afin d'éviter une duplication inutile du code.

Beaucoup de tests auront besoin d'avoir accès à des composants externes (disque local, serveur *Dropbox*, serveur *SSH*, *etc.*). Une liste des composants externes disponibles sera tenue à jour et accessible lors de l'écriture des tests. Par exemple, un test pourra facilement demander l'accès à un compte *Dropbox* de test.

Cela peut potentiellement poser de gros problèmes, par exemple si deux tests sont lancés en même temps et utilisent le même compte de test. Des mesures particulières devront être prises dans ces cas là.

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
Les tests de performance vont mesurer les performances d'*Onitu* dans plusieurs situations. La couverture de ces tests sera le nombre de situations mesurées. Il n'est pas possible de tester toutes les situations possibles, donc seuls plusieurs types de situations seront testés. Voici quelques exemples envisagés :

- Montée en charge lors du transfert de centaines de petits fichiers
- Temps de transfert de gros fichiers (plusieurs giga-octets) entre différents drivers
- Temps de lancement d'*Onitu*
- Utilisation mémoire lors des transferts
- Indexation d'un gros répertoire
- Détection des changements sur les différents drivers

### Environnement et conditions de réalisation
L'environnement des tests de performance doit être préparé avec beaucoup d'attention. L'intérêt de ces tests est de pouvoir comparer les évolutions entre les différentes versions, il est donc très important qu'ils aient été lancés dans des conditions les plus similaires possibles.

### Configurations particulières
Ces tests seront lancés sur une plateforme dédiée. Ils pourront aussi être lancés de manière locale par les développeurs, mais les résultats officiels seront ceux de la plateforme. La configuration de la plateforme ne doit pas changer, ou alors tous les tests doivent être relancés pour toutes les versions d'*Onitu*.

Les tests seront lancés avec plusieurs configurations de *Python* (*Python 2.x*, *Python 3.x* et *Pypy*) afin de comparer l'incidence de ces configurations sur les performances.

### Planning et charge
Pour le moment, une personne s'occupe des tests de performance. Ces tests représentent un travail conséquent, et il est prévu que nous continuions à y dédier une personne pour les prochains mois.

L'essentiel des tests devrait être écrit avant la première version grand public, même si des ajouts jugés pertinents ou testant de nouvelles fonctionnalités pourront être effectués par la suite.

### Critère de démarrage des tests
Ces tests peuvent être très longs et demander diverses interventions. De ce fait, ils ne seront pas déclenchés automatiquement mais manuellement.
La suite de *benchmarks* pourra être lancée à tout moment par un développeur voulant mesurer les différences liées à un ajout en cours de développement, sans nécessairement publier les résultats.

### Critères de passage/échec
Ces tests n'ont pas de critères précis de passage ou d'échec, mais des variations par rapport aux versions précédentes.
