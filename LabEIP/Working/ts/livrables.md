# Livrables

## Cas de tests

Les cas de tests seront divisés en deux principales catégories. Premièrement, les tests liés aux fonctionnalités du système (tels les tests unitaires ou les tests fonctionnels), seront présents sur le dépôt *Git* du projet, dans un répertoire nommé `tests/`. Ce répertoire contiendra ensuite des divisions comprenant chacun des types de tests. Il n'y aura *a priori* pas d'autre liste synthétique de tests effectués que celle fournie en parcourant les répertoires.

Chaque dossier listera des fichiers de tests, qui seront agrégés et exécutés par *py.test*.

Un second dépôt, `benchmarks`, sera mis en place pour les tests liés aux performances de la solution. Il contiendra les fichiers de configurations spécifiques aux outils *codespeed* et *Travis* qui seront chargés de mesurer ces performances.

Les deux dépôts seront disponibles sur le site web *Github*, à l'adresse suivante : [http://github.com/onitu](https://github.com/onitu).


## Rapport d'exécution de tests

Ce rapport présente, pour chacun des fichiers de tests présents, ceux dont la validation a échoué, en indiquant les lignes incriminées et les valeurs faisant défaut.

Les rapports sont produits par l'outil *py.test*, qui est un format soigné et très répandu dans la communauté Python. Cela permet à une personne extérieure au projet de pouvoir facilement lire les tests et d'en comprendre l'exécution.

Les rapports d'exécutions des tests fonctionnels et unitaires sont disponibles via le site *Travis-ci*, qui présente la sortie de *py.test*. Les benchmarks, eux, seront présentés via l'outil *Codespeed*.


## Rapport sur le suivi global de la qualité

Les deux outils permettant d'afficher les rapports d'exécution des tests permettent de comparer les résultats selon les différentes versions. *Codespeed* affiche un diagramme pour chaque version permettant d'évaluer les évolutions d'une version à l'autre, et ainsi de constater les régressions.
