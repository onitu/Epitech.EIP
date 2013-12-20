# Outils

## Dépôt de tests

La majeure partie des tests sera présente sur le dépôt des sources du projet, à savoir [onitu](https://github.com/onitu/onitu). Sera présent à la racine de ce dépôt un répertoire `tests`, subdivisé de façon à contenir les tests unitaires, les tests système et les tests fonctionnels du projet.

Les tests d'acceptance quant à eux — et plus généralement les outils de mesures liés aux performances d'*Onitu* — seront hébergés sur un dépôt différent, [benchmarks](https://github.com/onitu/benchmarks).


## Outils d’automatisation des tests

De façon à être le plus simple possible, en offrant à chacun la possibilité d'exécuter les tests, mais aussi à s'assurer que le projet sera régulièrement testé, divers outils d'automatisation seront mis en place.

### py.test

*py.test* sera à la fois utile pour les tests fonctionnels et unitaires. Il s'agit un framework de tests facile d'accès, et répondant parfaitement à nos besoins en termes de fonctionnalités.

L'utilitaire se charge de trouver l'ensemble des fichiers et fonctions de tests à partir d'un répertoire donné. Il génère ainsi des rapports d'exécution détaillés plus haut dans la partie *Livrables*.

Cet outil utilisant des fichiers de tests rédigés en Python, nous profitions de toutes les fonctionnalités du langage dans l'écriture des tests. Il offre de plus des méthodes pour pré-charger divers éléments avant le lancement des tests.

[http://pytest.org/latest/getting-started.html](http://pytest.org/latest/getting-started.html)

### tox

*tox* est un outil permettant de tester la portabilité du projet, à savoir s'il est compatible avec différents environnements Python: *py2k*, *py3k* ou encore *pypy*.

[http://tox.readthedocs.org/en/latest/](http://tox.readthedocs.org/en/latest/)

### Travis-ci

*Travis-ci* est un service d'intégration continue. Détectant un nouveau *commit* sur le projet, il lance ainsi automatiquement une batterie de tests pré-établie, dont le rapport est ensuite consultable directement sur le site de *Travis-ci*.

[https://travis-ci.org/](https://travis-ci.org/)


## Outils pour les tests de performance

### Codespeed

*Codespeed* est une application permettant l'évaluation des performances du projet. Elle offre entre autres des outils de calculs de temps d'exécutions, mais aussi permet des comparaisons entre différentes versions du projet, générant ainsi un aperçu simple de l'évolution globale des performances.

[https://github.com/tobami/codespeed/](https://github.com/tobami/codespeed/)
