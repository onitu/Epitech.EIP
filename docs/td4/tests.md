# Tests

## Passage et validation

Si vous développez une nouvelle fonctionnalité ou souhaitez simplement tester
votre installation d'Onitu, vous pouvez exécuter les tests fonctionnels.

Les tests fonctionnels peuvent être lancés à l'aide de la commande ```py.test
tests```. Vous pouvez aussi vous aider de ```tox``` afin de générer
automatiquement un environnement propre et fonctionnel pour le lancement des
tests.

Enfin, quelques variables d'environnement que voici peuvent vous être utiles
lors de l'exécution des tests:

* ```ONITU_TEST_TIME_UNIT``` Plusieurs tests se basent sur un délai d'exécution
avant de considérer un transfert en échec. Cette variable contient donc un
nombre de secondes correspondant à l'unité de temps, ```1s``` par défaut.

* ```ONITU_TEST_DRIVER``` La batterie de tests n'est exécutée que pour un pilote
à la fois, cette variable permet de déterminer quel pilote sera testé, et peut
donc prendre des valeurs telles que ```local_storage``` ou ```ssh```.

Des tests automatiques sont lancés par Travis sur tout code intégré à Onitu.
L'historique de ces tests est disponible publiquement. Travis lancera aussi les
tests si vous faites une *pull request*. Vous pouvez consulter la [page Travis
du projet](https://travis-ci.org/onitu/onitu).

Les tests s'exécutent à l'aides des commandes suivantes:

    py.test -v tests/functionnal # Tests avec l'environnement courant
    tox -e py2.7 # Tests avec Python2.7
    tox -e flake8 # Vérification de la syntaxe
    tox -e benchmarks # Tests de performances

## Architecture des tests

## Tests serveur

Onitu est fourni avec une suite de tests conséquente présente dans le répertoire `tests/`. Ces tests sont génériques et conçus pour fonctionner avec tous les *drivers*, comme décrit dans le chapitre 2, ils sont construits à l'aide du framework *py.test*.

Une série d'utilitaires est fournie dans le dossier `tests/utils/` pour vous permettre de développer le plus simplement possible de nouveaux tests.

Ces utilitaires sont décris par les sections suivantes.

#### `driver.py`

Contient des classes permettant de générer des configurations pour divers *drivers* cibles, de façon générique.

#### `launcher.py`

Permet d'exécuter simplement une instance d'Onitu, à l'aide du fichier de configuration donné en paramètre à la classe `Launcher`. Offre en retour la possibilité de réagir aux évènements émis par Onitu, à l'aide des méthodes `launcher.on_nomdelevenement` où `launcher` serait une instance de `Launcher` et `nomdevenement` un nom d'événement valide.

La liste des noms d'événements est présente dans le fichier `logs.py`. Les méthodes de connexion aux événements peuvent aussi prendre des paramètres nommés, visibles eux aussi dans le fichier `logs.py`.

#### `loops.py`

Contient diverses boucles événementielles construites pour être branchées au *launcher*. Les boucles sont lancées à l'aide de leur méthode `run`, et stoppées lorsque l'événement correspondant survient.

La boucle `BooleanLoop` possède une méthode `stop` qu'il suffit de relier à un événement du *launcher* pour être stopée lors de son émission, par exemple: `launcher.on_referee_started(loop.stop)`.

La boucle `CounterLoop` est initialisée avec un nombre *N* et possède une méthode `check`. De la même manière que `BooleanLoop`, elle s'arrêtera une fois que `check` aura été appelée *N* fois.

#### `setup.py`

Les classes `Rule` et `Setup` permettent de générer un fichier de configuration Onitu depuis un script python.


## Tests drivers

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

Les *drivers* peuvent aussi fournir leurs propres fichiers de tests *py.test* en les plaçant dans ce même répertoire.
