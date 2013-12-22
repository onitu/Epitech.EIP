# Types de tests et périmètre

Notre stratégie de tests se divise en trois axes principaux : Les tests unitaires, les tests fonctionnels, et les test de performance (ou *benchmarks*).

## Les tests Fonctionnels
Les tests fonctionnels seront les premiers tests écrits. Ces tests sont là pour assurer que les fonctionnalités d'*Onitu* sont respectées et qu'aucune régression n'est introduite.

Les tests vont être répartis par fonctionnalité (échange de fichier entre deux différents *drivers*, reprise des transferts, *etc.*) et chaque test assurera qu'*Onitu* adopte le bon comportement dans une situation bien précise.

## Les tests de Performance
Les tests de performance, ou *benchmarks*, permettent d'évaluer les performances d'*Onitu* au fil du temps. Ces tests permettent de chiffrer toute progression et d'éviter les régressions.

Plusieurs scénarios seront définis et seront lancés sur diverses itérations, avec les différentes versions d'*Onitu*. Ils seront toujours exécutés sur la même machine, et dans un état le plus constant possible.

## Les tests Unitaires
Les tests unitaires seront introduits dans un second temps. Lorsque nous considérerons que le code du cœur d'*Onitu* est suffisamment mature et sujet à moins de ré-écritures, les tests unitaires seront écrits et permettront d'éviter toute régression, même mineure. Pour le moment, il serait vain de les écrire étant donné que le cœur subit de profonds changements réguliers.

Ces tests seront beaucoup plus précis que les tests fonctionnels. Chaque test se focalisera sur le comportement de quelques lignes dans un cas bien particulier, et sera décorrelé de l'état des autres composants.
