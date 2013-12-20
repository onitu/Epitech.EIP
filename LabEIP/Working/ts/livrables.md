# Livrables

## Cas de tests

Les cas de tests seront divisés en deux principales catégories. Premièrement, les tests liés aux fonctionnalités du système (tels les tests unitaires ou les tests fonctionnels), seront présents sur le dépôt *Git* du projet, dans un répertoire nommé `tests/`. Ce répertoire contiendra ensuite des divisions comprenant chacun des types de tests. Il n'y aura *a priori* pas d'autre liste synthétique de tests effectués que celle fournie en parcourant les répertoires.

Chaque dossier listera des fichiers de tests, qui seront agglomérés et exécutés par *py.test*.

Un second dépôt, `benchmarks`, sera mis en place pour les tests liés aux performances de la solution. Il contiendra les fichiers de configurations spécifiques aux outils *codespeed* et *Travis* qui seront chargés de mesurer ces performances.


## Rapport d'exécution de tests

Ce rapport présente, pour chacun des fichiers de tests présents, ceux dont la validation a échoué, en indiquant les lignes incriminées et les valeurs faisant défaut.

Les rapports du type de ceux produits par *py.test* sont plutôt agréables à lire et très répandus, donc toute personne découvrant le projet sera facilement en mesure de lire les tests et d'en comprendre l'exécution.


## Rapport sur le suivi global de la qualité

De même ici, les outils utilisés, à savoir *codespeed* et *Travis* fournissent des études détaillées des performances, et par extension de la qualité, du système.

Un comparatif des résultats entre les versions est de plus fourni par *codespeed*, permettant de mesurer les évolutions apportées par les nouvelles versions, ou encore, sur une version de développement, de constater une régression.
