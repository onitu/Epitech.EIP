# Tests

\label{tests}

## Passage et validation

Les tests peuvent être lancés à l'aide de la commande ```py.test
tests```. Vous pouvez aussi vous aider de ```tox``` afin de générer
automatiquement un environnement propre et fonctionnel pour le lancement des
tests.

Quelques variables d'environnement que voici peuvent vous être utiles
lors de l'exécution des tests:

* ```ONITU_TEST_TIME_UNIT``` Plusieurs tests se basent sur un délai d'exécution
avant de considérer un transfert en échec. Cette variable contient donc un
nombre de secondes correspondant à l'unité de temps, ```1s``` par défaut.

* ```ONITU_TEST_DRIVER``` La batterie de tests n'est exécutée que pour un pilote
à la fois, cette variable permet de déterminer quel pilote sera testé, et peut
donc prendre des valeurs telles que ```local_storage``` ou ```ssh```.

#### Intégration continue

Des tests automatiques sont lancés par Travis sur tout code intégré à Onitu.
L'historique de ces tests est disponible publiquement. Travis lancera aussi les
tests si vous faites une *pull request*. Vous pouvez consulter la [page Travis
du projet](https://travis-ci.org/onitu/onitu).

#### Lancement des tests

Les tests s'exécutent à l'aides des commandes suivantes:

    py.test -v tests # Tests avec l'environnement courant
    tox -e py2.7 # Tests avec Python2.7
    tox -e flake8 # Vérification de la syntaxe
    tox -e benchmarks # Tests de performances

## Architecture des tests

Onitu est fourni avec une suite de tests conséquente présente dans le répertoire `tests/`. Ces tests sont génériques et conçus pour fonctionner avec tous les *drivers*, comme décrit au chapitre **[Technologies utilisées]**, ils sont construits à l'aide du cadriciel *py.test*.

Une série d'utilitaires est fournie dans le dossier `tests/utils/` pour vous permettre de développer le plus simplement possible de nouveaux tests.

Ces utilitaires sont décris par les sections suivantes.

#### `launcher.py`

Permet d'exécuter simplement une instance d'Onitu, à l'aide du fichier de configuration donné en paramètre à la classe `Launcher`. Offre en retour la possibilité de réagir aux évènements émis par Onitu, à l'aide des méthodes `launcher.on_nomdelevenement` où `launcher` serait une instance de `Launcher` et `nomdelevenement` un nom d'événement valide.

La liste des noms d'événements est présente dans le fichier `logs.py`. Les méthodes de connexion aux événements peuvent aussi prendre des paramètres nommés, visibles eux aussi dans le fichier `logs.py`.

#### `loops.py`

Contient diverses boucles événementielles construites pour être branchées au *launcher*. Les boucles sont lancées à l'aide de leur méthode `run`, et stoppées lorsque l'événement correspondant survient.

La boucle `BooleanLoop` possède une méthode `stop` qu'il suffit de relier à un événement du *launcher* pour être stopée lors de son émission, par exemple: `launcher.on_referee_started(loop.stop)`.

La boucle `CounterLoop` est initialisée avec un nombre *N* et possède une méthode `check`. De la même manière que `BooleanLoop`, elle s'arrêtera une fois que `check` aura été appelée *N* fois.

#### `setup.py`

La classe `Setup` permet de générer un fichier de configuration Onitu depuis un script python.

#### `driver.py`

Contient des classes représentant un *driver* et ses fonctionnalités au sein des tests. Ce sont ces classes qui devront être spécialisées par les *drivers* pour les rendre éligibles aux tests.

#### `targetdriver.py`

Ce module est chargé d'instancier le *driver* courant, pointé par `ONITU_TEST_DRIVER`, et ainsi de le contrôler. Le *helper* `if_features` permet de plus de vérifier que le *driver* supporte une certaine fonctionnalité.

#### `test_driver` et `testdriver.py`

Ce *package* présente un *driver* spécialement conçu pour les tests. Il présente une interface semblable aux autres *drivers*, et permet de tester le cœur d'Onitu sans se baser sur un *driver* particulier potentiellement biaisé.

Le module `testdriver.py` permet de plus d'instancier directement ce *driver* dans les tests.

#### `fixtures.py`

Les tests se basent beaucoup sur les *fixtures py.test*. Cette fonctionnalité permet en effet d'instancier automatiquement des objets pour le lancement de chaque test. Les *fixtures* utilisées par Onitu sont présentes dans ce module, et concernent la génération d'un `Setup` et d'un `Launcher` fonctionnels.

## Tests serveur

Les tests serveur sont regroupés dans les répertoires `tests/unit` et `tests/functional/core`. Le premier, comme son nom l'indique, contient les tests unitaires du système.

Les tests fonctionnels sont présents dans le second répertoire. La suite de tests est la suivante:

#### `test_api.py`

Tests concernant l'*API REST*: vérifie le bon fonctionnement de toutes les routes, ainsi que la supervision des services (démarrage, arrêt).

#### `test_changes.py`

Tests vérifiant les transferts lors de modifications sur des fichiers.

#### `test_copy.py`

Tests vérifiant les transferts lors de créations de nouveaux fichiers.

#### `test_corruption.py`

Tests s'assurant de la fiabilité du système si un fichier se trouve être modifié simultanément par deux services.

#### `test_crash.py`

Tests s'assurant de la bonne reprise du système si celui-ci se trouve être stoppé en plein transfert.

#### `test_deletion.py`

Tests vérifiant les transferts lors de suppressions de fichiers.

#### `test_folders.py`

Tests vérifiant le bon respect des règles définies par les *folders*.

#### `test_move.py`

Tests vérifiant les transferts lors de déplacements de fichiers.

#### `test_multipass_copy.py`

Tests vérifiant les transferts lors de créations de fichiers en plusieurs passes (plusieurs *chunks*).

#### `test_startup.py`

Tests s'assurant du bon comportement d'Onitu en fonction du fichier de configuration.

## Tests *drivers*

\label{tests_drivers}

Afin de pouvoir être éligible aux tests génériques prévus par Onitu, chaque driver doit être fourni avec un module ou *package* `tests`.

Ce module contient une classe `Driver` héritant de `tests.utils.driver.Driver` fournissant un ensemble d'opérations élémentaires pour communiquer avec le service cible lors des tests. Une classe `DriverFeatures`, héritant de `tests.utils.driver.DriverFeatures`, doit aussi être présente pour énoncer les fonctionnalités supportées par le *driver*.

\ 

Les opérations élémentaires sont les suivantes:

- **mkdir** — Crée sur le service le ou les répertoires indiqués par le chemin donné en paramètre
- **rmdir** — Supprime le répertoire correspondant au chemin donné
- **write** — Écrit dans le fichier donné en premier paramètre le contenu donné en second paramètre
- **generate** — Génère un fichier aléatoire de taille fixe. Le premier paramètre contient le nom du fichier et le second la taille des données à générer
- **exists** — Vérifie l'existence d'un fichier sur le service, par son chemin donné en paramètre. Retourne vrai si le fichier existe et faux dans le cas contraire
- **unlink** — Supprime le fichier pointé par le chemin
- **rename** — Renomme un fichier, le premier paramètre contient le chemin actuel, et le second contient le nouveau
- **checksum** — Retourne la somme *MD5* du fichier pointé par le chemin donné en paramètre
- **close** — Permet la coupure de la connexion auprès du service

\ 

Les *drivers* peuvent aussi fournir leurs propres fichiers de tests *py.test* en les plaçant dans un module `driver_tests` de ce même *package* `tests`.

\ 

La suite de tests passées pour le *driver* est ensuite définie dans le répertoire `tests/functional/driver` d'Onitu:

#### `test_driver_copy.py`

Tests vérifiant les créations de fichier (semblable à `core/tests_copy.py`).

#### `test_driver_del.py`

Tests vérifiant les suppressions de fichier (semblable à `core/tests_deletion.py`).

#### `test_driver_move.py`

Tests vérifiant les déplacements de fichier (semblable à `core/tests_move.py`).

#### `test_unicode.py`

Tests s'assurant de la compatibilité unicode du *driver*.

#### `test_specific.py`

Lancement de la suite de tests spécifique au *driver* (`tests.driver_tests`).
